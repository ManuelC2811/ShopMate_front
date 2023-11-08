# Guía para Abrir el Proyecto Shopmate Front

Este repositorio contiene el código fuente del proyecto "Shopmate Front" que incluye la aplicación "Base". A continuación, se proporcionan instrucciones para abrir y ejecutar el proyecto en tu entorno de desarrollo.

## Requisitos Previos

Asegúrate de tener instalados los siguientes requisitos antes de comenzar:

- Python (preferiblemente Python 3.x)
- Django (puedes instalarlo usando `pip install Django`)
- Git (opcional, pero recomendado para clonar el repositorio)

## Pasos para Abrir el Proyecto

1. **Clona el Repositorio** (si no tienes Git, también puedes descargar el proyecto como un archivo ZIP):

   ```bash
   git clone https://github.com/tuusuario/shopmate_front.git
   ```

2. **Configura un Entorno Virtual (recomendado)**

Para evitar conflictos con las dependencias de otros proyectos, puedes crear un entorno virtual (asegurate de instalar Django en el)

```bash
python -m venv venv
```
Luego, activa el entorno virtual

En Windows:
```bash
    venv\Scripts\activate
```

En macOS y Linux:
```bash
    source venv/bin/activate
```

3. **Aplica las migraciones**
Ejecuta las migraciones para configurar la base de datos

```bash
python manage.py migrate
```

4. **Ejecuta el servidor de desarrollo**
Ejecuta el siguiente comando para iniciar el servidor de desarrollo

```bash
python manage.py runserver
```