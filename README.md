# Equipo de Desarrollo Inteligente de Software: EDIS

Equipo de desarollo para Ingeniería de Software. 

## 50 Amigos
Hay dos métodos para ejecutar el sistema en una máquina local con fines de prueba y desarrollo:
  * En un contenedor de <a href="https://www.docker.com/" target="_blank">Docker</a>
  * En un entorno virtual con <a href="https://docs.conda.io/en/latest/" target="_blank">Conda</a>

### Prerrequisitos
* Tener <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git" target="_blank"> Git instalado</a>


Para ejecutar el sistema en una máquina local con Conda:
* Tener <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html" target="_blank"> Conda instalado</a>

Para ejecutar el sistema en una máquina local con Docker:
* Tener <a href="https://docs.docker.com/desktop/" target="_blank"> Docker instalado</a>


### Instalación

Clonar el repositorio en la computadora local:

```
$ git clone https://github.com/Veppam2/EDIS.git
$ cd EDIS/djangoProject/proyecto
```
#### Utilizando un entorno virtual con Conda
Creamos el entorno virtual en el que va a correr el sistema:
```
$ conda env create -f environment.yml
```
Activamos el entorno virtual _cincuentaAmigosEnviro_
```
$ conda activate cincuentaAmigosEnviro
```
#### Utilizando un entorno virtual con Docker

Creamos el contenedor en el que va a correr el sistema:
```
$ sudo docker build -t python-django-edis .
```
## Uso
#### Utilizando un entorno virtual con Conda
Después de haber creado el entorno virtual, podemos ejecutar el sistema con:
```
$ python manage.py runserver
```
Donde se desplegará en la terminal el siguiente mensaje:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 30, 2023 - 00:09:35
Django version 4.1.6, using settings 'proyecto.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Después redirigirse a http://0.0.0.0:8000/

#### Utilizando un contenedor de Docker
Después de haber creado el contenedor, podemos ejecutar el sistema con:
```
$ sudo docker run -it -p 8000:8000 python-django-edis
```
Donde se desplegará en la terminal el siguiente mensaje:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 30, 2023 - 00:12:55
Django version 4.1.6, using settings 'proyecto.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```
En ambos casos nos redirigimos a la url que nos despliega la terminal
## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...
