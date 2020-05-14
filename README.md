# AC Labs 2020 - Lab 7

This repo will contain:
 - Docker file for python 3.7
 - A Django project containing a ToDo model

## How to run project

Build image:

`docker build . --tag lab7`

Run image:

`docker run -it -v "$(pwd)":/app -p 8000:8000 --rm lab7`
