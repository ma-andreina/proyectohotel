/*
    ==============================================
    ANIMATIONS.JS
    ==============================================
*/

document.addEventListener('DOMContentLoaded', () => {
    // --- Animación de entrada para secciones ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Seleccionamos elementos que queremos animar
    const elementsToAnimate = document.querySelectorAll('.habitacion_tarjeta, .seccion_busqueda, .contenedor_detalle > *, .subtitulo, .seccion_servicios, .seccion_barinas');

    elementsToAnimate.forEach(el => {
        // Establecemos un estado inicial para la animación
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });

    // --- Efecto de brillo en hover para botones ---
    // 👇 CAMBIO INTEGRADO AQUÍ: Se añade '.btn-details' a la selección de botones.
    const buttons = document.querySelectorAll('.boton_principal, .boton_fullwidth, .btn-details');

    buttons.forEach(button => {
        button.addEventListener('mouseenter', (e) => {
            // Creamos el elemento span para el brillo
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');

            const rect = button.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = `${size}px`;
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;

            // Añadimos el ripple y lo eliminamos después de la animación
            button.appendChild(ripple);
            setTimeout(() => {
                ripple.remove();
            }, 600); // Coincide con la duración de la animación en CSS
        });
    });

    // --- Añadimos el CSS necesario para el efecto ripple ---
    const style = document.createElement('style');
    style.innerHTML = `
        /* 👇 CAMBIO INTEGRADO AQUÍ: Se añade '.btn-details' a los estilos. */
        .boton_principal, .boton_fullwidth, .btn-details {
            position: relative;
            overflow: hidden;
        }

        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.4);
            transform: scale(0);
            animation: ripple-effect 0.6s linear;
        }

        @keyframes ripple-effect {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);


    // ==============================================
    // LÓGICA DE MENÚ HAMBURGUESA (MÓVIL) CON ANIMACIÓN DE BAJADA/SUBIDA
    // ==============================================
    const menuToggle = document.querySelector('.menu-toggle');
    const navWrapper = document.querySelector('.nav-wrapper');
    const dropdownTriggers = document.querySelectorAll('.dropdown-trigger');

    // Ajuste: offset (en px) para bajar el menú un poquito cuando esté abierto en modo 'fixed/absolute'
    // Modifica este valor si quieres mayor/menor separación.
    const OPEN_OFFSET = 12; // <- cambia este número (px) para ajustar la altura
    const SLIDE_AMOUNT = 10; // px que se desliza hacia abajo/arriba al abrir/cerrar

    if (menuToggle && navWrapper) {
        // Guardamos la posición original por si está en fixed (para restaurarla al cerrar)
        const initialPosition = getComputedStyle(navWrapper).position;
        const wasFixed = initialPosition === 'fixed';

        function updateNavMaxHeight() {
            // Limpiamos maxHeight momentáneamente para medir el contenido real
            navWrapper.style.maxHeight = '';
            const rect = navWrapper.getBoundingClientRect();
            // Espacio disponible desde la parte superior del nav (ya considera OPEN_OFFSET si se aplicó) hasta el bottom del viewport (dejamos 20px de margen)
            const availableHeight = Math.max(0, window.innerHeight - rect.top - 20);
            // Usamos el menor entre el contenido real y el espacio disponible
            const desired = Math.min(navWrapper.scrollHeight, availableHeight);
            navWrapper.style.maxHeight = desired + 'px';

            // Si el contenido supera el espacio disponible, permitimos scroll interno
            if (navWrapper.scrollHeight > availableHeight) {
                navWrapper.style.overflowY = 'auto';
                navWrapper.style.overscrollBehavior = 'contain';
            } else {
                navWrapper.style.overflowY = '';
                navWrapper.style.overscrollBehavior = '';
            }
        }

        function openCleanupListeners() {
            window.addEventListener('resize', updateNavMaxHeight);
            window.addEventListener('orientationchange', updateNavMaxHeight);
        }
        function closeCleanupListeners() {
            window.removeEventListener('resize', updateNavMaxHeight);
            window.removeEventListener('orientationchange', updateNavMaxHeight);
        }

        menuToggle.addEventListener('click', () => {
            const isOpen = navWrapper.classList.toggle('is-open');
            menuToggle.setAttribute('aria-expanded', String(isOpen));

            // Cambiar icono de hamburguesa a X
            const icon = menuToggle.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-times');
            }

            if (isOpen) {
                // Si el nav estaba en 'fixed', lo convertimos temporalmente a 'absolute'
                // para que no quede "fijo" por encima de todo cuando se hace scroll.
                // Restauraremos la posición al cerrar.
                if (wasFixed) {
                    const rect = navWrapper.getBoundingClientRect();
                    navWrapper.style.position = 'absolute';
                    // Colocamos el nav donde estaba visualmente (relativo al documento) y lo bajamos OPEN_OFFSET px
                    navWrapper.style.top = (window.scrollY + rect.top + OPEN_OFFSET) + 'px';
                    // Aseguramos que se mantenga el ancho visual
                    navWrapper.style.left = rect.left + 'px';
                    navWrapper.style.right = '';
                    navWrapper.style.width = rect.width + 'px';
                }

                // Ajustar altura para que no supere el viewport y permitir scroll al contenido debajo
                updateNavMaxHeight();

                // PREPARAR Y EJECUTAR LA ANIMACIÓN: bajada desde -SLIDE_AMOUNT -> 0
                navWrapper.style.transition = 'transform 0.28s cubic-bezier(0.2,0,0,1), max-height 0.28s ease';
                // Posicion inicial ligeramente elevada
                navWrapper.style.transform = `translateY(-${SLIDE_AMOUNT}px)`;
                // Forzar reflow para asegurar que la transición se aplique
                requestAnimationFrame(() => {
                    navWrapper.style.transform = 'translateY(0)';
                });

                openCleanupListeners();
            } else {
                // Cerrar: animar subida (0 -> -SLIDE_AMOUNT) y al terminar cerrar por completo
                // Nos aseguramos de que exista una transición definida
                navWrapper.style.transition = 'transform 0.22s cubic-bezier(0.2,0,0,1), max-height 0.22s ease';
                // Iniciar la animación hacia arriba
                // (dejamos maxHeight tal cual para que el contenido se mantenga hasta que termine la animación)
                requestAnimationFrame(() => {
                    navWrapper.style.transform = `translateY(-${SLIDE_AMOUNT}px)`;
                });

                // Una vez termine la animación de transform, hacemos el resto del cierre (colapsar altura, restaurar estilos, reset submenús)
                const onTransitionEnd = (e) => {
                    if (e.propertyName !== 'transform') return;
                    navWrapper.removeEventListener('transitionend', onTransitionEnd);

                    // Colapsar el menú y limpiar estilos
                    navWrapper.style.maxHeight = '0';
                    navWrapper.style.overflowY = '';
                    navWrapper.style.overscrollBehavior = '';
                    if (wasFixed) {
                        navWrapper.style.position = '';
                        navWrapper.style.top = '';
                        navWrapper.style.left = '';
                        navWrapper.style.width = '';
                    }
                    // Resetear transform y transition inline (para volver al estado "cerrado" inicial)
                    navWrapper.style.transition = '';
                    navWrapper.style.transform = '';

                    closeCleanupListeners();

                    // Resetear todos los submenús cuando se cierra el menú principal
                    dropdownTriggers.forEach(trigger => {
                        const parent = trigger.closest('.menu_dropdown');
                        if (parent) {
                            parent.classList.remove('is-open');
                            const submenu = parent.querySelector('.dropdown_menu');
                            if (submenu) submenu.style.height = "0";
                        }
                    });
                };

                navWrapper.addEventListener('transitionend', onTransitionEnd, { passive: true, once: false });
            }
        });
    }

    // 2. Alternar la visibilidad de los submenús (Servicios / Sobre Nosotros)
    dropdownTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.preventDefault(); // Evita que el enlace padre navegue

            const parentLi = trigger.closest('.menu_dropdown');
            parentLi.classList.toggle('is-open');

            // Lógica para que el JS calcule la altura para la animación CSS
            const submenu = parentLi.querySelector('.dropdown_menu');
            if (parentLi.classList.contains('is-open')) {
                 // Establecer la altura del submenu para que la transición CSS funcione
                 submenu.style.height = submenu.scrollHeight + "px";
            } else {
                 submenu.style.height = "0";
            }
        });
    });

    // ==============================================
    // LÓGICA FORMULARIO MULTI-PASO (Reserva de Habitación)
    // ==============================================
    const stepIndicators = document.querySelectorAll('.paso_item');
    const formSteps = document.querySelectorAll('.paso_formulario');
    const nextButtons = document.querySelectorAll('.boton_siguiente');
    const prevButtons = document.querySelectorAll('.boton_anterior');

    function updateFormStep(targetStep) {
        // Ocultar todos los pasos y desmarcar indicadores
        formSteps.forEach(step => {
            step.classList.remove('activo');
        });
        stepIndicators.forEach(indicator => {
            indicator.classList.remove('activo');
        });

        // Mostrar el paso objetivo y marcar el indicador
        const targetForm = document.querySelector(`.paso_formulario[data-step="${targetStep}"]`);
        const targetIndicator = document.querySelector(`.paso_item[data-step="${targetStep}"]`);

        if (targetForm) {
            targetForm.classList.add('activo');
        }
        if (targetIndicator) {
            targetIndicator.classList.add('activo');
        }
    }

    nextButtons.forEach(button => {
        button.addEventListener('click', () => {
            const nextStep = button.getAttribute('data-step-target');
            // Aquí puedes añadir validación de formulario antes de avanzar
            updateFormStep(nextStep);
        });
    });

    prevButtons.forEach(button => {
        button.addEventListener('click', () => {
            const prevStep = button.getAttribute('data-step-target');
            updateFormStep(prevStep);
        });
    });

    // Asegurar que solo el paso 1 esté activo al cargar
    updateFormStep(1);
});

document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.carousel');
    const slides = document.querySelectorAll('.carousel-slide');
    const totalSlides = slides.length;
    let currentSlide = 0;
    const slideDuration = 5000; // 5000ms = 5 segundos

    function nextSlide() {
        // Incrementa el índice de la diapositiva
        currentSlide = (currentSlide + 1) % totalSlides; 
        
        // Calcula cuánto debe moverse el carrusel. Cada diapositiva es 100% de ancho.
        const offset = -currentSlide * 100;
        
        // Aplica el desplazamiento suave (gracias a la propiedad 'transition' en el CSS)
        carousel.style.transform = `translateX(${offset}%)`;
    }

    // Inicia el carrusel para que se mueva automáticamente cada 5 segundos
    setInterval(nextSlide, slideDuration);
});