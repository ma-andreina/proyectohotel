from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from reserva_habitacion.models import ReservaHabitacion
from django.conf import settings
import time

logger = get_task_logger(__name__)

@shared_task(bind=True)
def enviar_email_confirmacion(self, id_reserva):
    """
    Tarea asíncrona que gestiona el proceso de envío de email de confirmación.
    Incluye lógica de reintentos y manejo de errores detallado.
    """
    logger.info(f"--- [CELERY] Iniciando envío de email para reserva ID: {id_reserva} ---")
    
    # Pausa de seguridad para asegurar que la transacción de la DB se haya completado
    time.sleep(1)
    
    try:
        # 1. Obtener la reserva con datos relacionados (usuario y habitación)
        reserva = ReservaHabitacion.objects.select_related('usuario', 'habitacion').get(pk=id_reserva)
        
        # 2. Validar que el usuario tenga un correo configurado
        email_cliente = reserva.usuario.email if (reserva.usuario and reserva.usuario.email) else None
        
        if not email_cliente:
            logger.warning(f"El usuario {reserva.usuario.username if reserva.usuario else 'Desconocido'} no tiene un email configurado.")
            return f"Fallo: Usuario sin email en reserva {id_reserva}"

        # 3. Preparar los datos del mensaje
        # Usamos el nombre de pila si está disponible, sino el nombre de usuario
        nombre_persona = reserva.usuario.first_name if reserva.usuario.first_name else reserva.usuario.username
        num_habitacion = reserva.habitacion.numero_habitacion if reserva.habitacion else "N/A"
        
        asunto = f"Confirmación de Reserva #{reserva.codigo_confirmacion} - Hotel Indigo"
        
        mensaje = (
            f"Hola {nombre_persona},\n\n"
            f"Tu reserva en Hotel Indigo ha sido confirmada con éxito.\n\n"
            f"Detalles de la Reserva:\n"
            f"  - Código de Confirmación: {reserva.codigo_confirmacion}\n"
            f"  - Habitación: {num_habitacion}\n"
            f"  - Fecha Check-In: {reserva.fecha_checkin}\n"
            f"  - Fecha Check-Out: {reserva.fecha_checkout}\n"
            f"  - Huéspedes: {reserva.huespedes}\n"
            f"  - Total a Pagar: ${reserva.total}\n\n"
            f"Gracias por elegirnos. ¡Te esperamos!"
        )

        # 4. Enviar el correo electrónico
        send_mail(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [email_cliente],
            fail_silently=False,
        )

        logger.info(f"--- [CELERY] Email enviado exitosamente a {email_cliente} ---")
        return f"Éxito: Email de reserva {reserva.codigo_confirmacion} enviado."

    except ReservaHabitacion.DoesNotExist:
        logger.error(f"Error Crítico: La reserva {id_reserva} no existe en la base de datos.")
        return f"Error: Reserva {id_reserva} no encontrada."
    
    except Exception as exc:
        logger.error(f"Error al enviar email para reserva {id_reserva}: {exc}")
        # En caso de error de conexión, reintentamos la tarea
        # countdown=60 espera 1 minuto antes de reintentar, máximo 3 veces.
        raise self.retry(exc=exc, countdown=60, max_retries=3)