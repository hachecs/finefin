# FineFin

Foobar is a Python library for dealing with word pluralization.

## Requerimientos
Asegurate de tener instalado lo siguiente:
* Python 3.x
* pip
* virtualenv o pipenv

## Instalación 
```
# clonar proyecto
git clone https://github.com/hachecs/finefin.git
```
```
# Instalación de pip
$ sudo easy_install pip
# instalacion de virtualenv
$ sudo apt-get install virtualenv
# Crear entorno virtual
$ virtualenv venv
# Instalar el archivo requirements que está dentro del proyecto
$ pip install -r requirements.txt

# Una vez instaladas las librerías
# ejecutar las migraciones dentro del proyecto, donde esta
python manage.py makemigrations
python manage.py migrate

Renombrar el archivo _.env por .env y poner las credenciales de un correo
para el envio de emails (Probar con un correo de Gmail)

#Ejecutar el proyeto
$ python manage.py runserver

```

## License
[MIT](https://choosealicense.com/licenses/mit/)