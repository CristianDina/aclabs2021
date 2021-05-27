# AC Labs 2021 - Lab 9

This repo will contain:
 - A Django project containing a ToDo model
 - A React client to serve the django backend
 - A `docker-compose.yml` file to run both services

## How to run project

Use `docker-compose up` to launch both services.

Use `docker-compose up backend` to only launch the backend container.
Use `docker-compose up frontend` to only launch the frontend container.

## Accessing the frontend

The frontend can be served by either the Django backend, on `localhost:8000`, or the React app on `localhost:3000`.
Only the `backend` container is needed for the former option, while the latter will require both.

## How to run from single docker container

```docker build . --tag aclabs``` 

```docker run -it -v $(pwd):/app -p 8000:8000 --rm aclabs```

