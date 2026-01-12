
# website/views.py (Modificado)
from django.shortcuts import render

def index(request):
    # Ahora especificamos la ruta COMPLETA: 'nombre_de_la_app/nombre_del_archivo.html'
    return render(request, 'website/index.html')
# Puedes agregar más vistas aquí, por ejemplo, para la página "Nosotros"
def nosotros(request):
    """
    Renderiza la página "Nosotros".
    """
    # Usamos la ruta anidada
    return render(request, 'website/nosotros.html')

def acceso(request):
    """
    Renderiza la página de Acceso para administradores.
    """
    # Usamos la ruta anidada
    return render(request, 'website/acceso.html')

def habitaciones(request):
    """
    Renderiza la página de listado de habitaciones.
    """
    # Usamos la ruta anidada
    return render(request, 'website/habitaciones.html')

def reserva(request):
    """
    Renderiza el formulario de reserva de habitaciones.
    """
    return render(request, 'website/reserva_habitaciones.html')

def eventos(request):
    """
    Renderiza la página de salones y eventos.
    """
    return render(request, 'website/eventos.html') 

def reserva_eventos(request):
    """
    Renderiza el formulario de cotización/reserva de eventos.
    (Pendiente de HTML)
    """
    # Usaremos una plantilla simple de "en construcción" por ahora si no tienes el HTML
    return render(request, 'website/reserva_salon.html')

def detalle_habitacion(request, habitacion_id):
    """
    Renderiza la página de detalle de una habitación específica.
    En un proyecto real, se usaría habitacion_id para buscar datos.
    """
    # El ID se usa en el backend para buscar, pero lo pasamos aquí
    context = {'habitacion_id': habitacion_id} 
    return render(request, 'website/detalle_habitacion.html', context)


def servicios(request):
    """
    Renderiza la página de Servicios y Servicios Adicionales.
    Corresponde a la tabla servicio_adicional en la DB.
    """
    return render(request, 'website/servicios.html')

def reserva_restaurante(request):
    """
    Renderiza el formulario de reserva de restaurante.
    """
    # Apunta a la plantilla de reserva de mesa
    return render(request, 'website/reservar_mesa.html') 

def restaurante(request):
    """
    Renderiza la página principal del restaurante (o redirige a la reserva).
    """
    # Podemos hacer que la URL principal del restaurante cargue directamente la reserva, 
    # o si tienes una plantilla de menú, puedes apuntar a ella.
    return render(request, 'website/reservar_mesa.html') 

# Opcional: Si tienes una URL para el menú, asegúrate de que esta exista
def restaurante_menu(request):
    """
    Renderiza la página del menú del restaurante (placeholder).
    """
    return render(request, 'website/menu.html')

def galeria(request):
    return render(request, 'website/galeria.html')

def contacto(request):
    """Renderiza la página de contacto."""
    return render(request, 'website/contacto.html')

def admin_panel_base(request):
    """
    Renderiza la plantilla base del panel de administración.
    La plantilla se encuentra en website/templates/website/admin/admin_base.html
    """
    # Importante: La ruta incluye la subcarpeta 'admin/'
    return render(request, 'website/admin/admin_base.html')

def empleo(request):
    """
    Renderiza la página de 'Trabaja con Nosotros'.
    """
    return render(request, 'website/empleo.html')