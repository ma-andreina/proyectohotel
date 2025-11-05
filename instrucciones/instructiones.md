## Resumen rápido del proyecto

Proyecto: sitio web estático del Hotel Indigo. Carpeta principal del frontend: `frontend/`.

- HTML principales: `frontend/index.html`, `frontend/nosotros.html`.
- CSS: `frontend/css/base.css` (base y variables) y `frontend/css/custom.css` (overrides y páginas).
- JS: `frontend/js/app.js` (comportamiento cliente). Imágenes en `frontend/images/`.


## Comandos importantes

- Ejecutar linters (arreglos automáticos):

  - `npm run lint:css` — ejecuta `stylelint css/base.css css/custom.css --fix`.
  - `npm run lint:js` — ejecuta `eslint js/ --fix`.

## Convenciones específicas del proyecto

- Nombres de clases: mezcla de guiones y guiones_bajos (ej.: `.header_principal`, `.item-nav`, `.boton_principal`). NO renombres clases existentes sin actualizar los HTML/JS simultáneamente.
- CSS: variables CSS están definidas en `:root` dentro de `frontend/css/base.css` (ej.: `--color-acento`, `--espaciado-medium`). Reutiliza estas variables.
- Notación de color: en este repo hemos estandarizado a la notación moderna `rgb(r g b / 10%)` para sombras y bordes (muchas reglas stylelint lo exigen).
- Media queries: el código contiene la forma `@media (width <= 900px)`; la configuración de stylelint en el repo se relajó para aceptar esa convención.


## Archivos clave a revisar antes de editar

- `frontend/css/base.css` — variables, layout y componentes base.
- `frontend/css/custom.css` — estilos por página y overrides; aquí es común encontrar reglas específicas de la Home y Nosotros.
- `.stylelintrc.json` — reglas de stylelint (modificadas para este repo). Cambios en estas reglas afectan qué correcciones son necesarias.
- `package.json` — scripts útiles (`lint:css`, `lint:js`).

Si algo en estas instrucciones no está claro o quieres que adapte la configuración (por ejemplo, restaurar reglas estrictas de stylelint y convertir todas las clases a una convención), dime cuál prefieres y lo implemento en el siguiente paso.

## Estándares de Código (resumen rápido)

- Nomenclatura:
  - Python (backend Django): PEP8 — snake_case para funciones/variables, PascalCase para clases, CONSTANTES en MAYÚSCULAS.
  - JavaScript (frontend): usar snake_case consistente para variables/funciones; constantes en MAYÚSCULAS.
  - Base de datos: nombres de tablas/columnas en snake_case (ej.: `reserva_habitacion`, `fecha_checkin`).
- Estructura de proyecto esperada:
  - Backend Django: `hotel_indigo/`, `apps/` (reservas, habitaciones, usuarios, pagos), `templates/`, `static/`.
  - Frontend: `frontend/css/`, `frontend/js/`, `frontend/images/`, `frontend/index.html`.
- Linters / Scripts (recomendado):
  - `npm run lint:js` — ESLint sobre `frontend/js/` (con --fix).
  - `npm run lint:css` — Stylelint sobre `frontend/css/**` (con --fix).
  - `npm run lint` — ejecuta ambos (agregado al `package.json`).
- Revisión de PRs: usar checklist mínima (nomenclatura, nombres significativos, comentarios que expliquen el "por qué", manejo de errores, no duplicación).

Acciones opcionales que puedo aplicar ahora:
- Añadir `CONTRIBUTING.md` con estas reglas y la checklist de revisión.
- Crear un `pre-commit` que ejecute linters antes del commit (husky + lint-staged).
- Forzar reglas más estrictas en `.stylelintrc.json` y añadir un script para normalizar CSS.

