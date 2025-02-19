# Aplicación Django de Prueba

Para poner en marcha la aplicación, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local.
2. Crea un entorno virtual con `python -m venv .venv`.
3. Activa el entorno virtual con `source .venv/bin/activate` en Linux o `.venv\Scripts\activate` en Windows.
4. Instala las dependencias con `pip install -r requirements.txt`.
5. Copia el fichero de configuración de muestra `config_example.ini` a `config.ini` y modifica los valores según tus necesidades.
6. Realiza las migraciones con `python manage.py migrate`.
7. Pon en marcha con `python manage.py runserver`.
