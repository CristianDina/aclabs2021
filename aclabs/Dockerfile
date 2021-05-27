FROM python:3.7

RUN apt update
RUN apt-get install nginx -y
RUN apt-get install libmariadb-dev -y

RUN pip install Django==2.2.12
RUN pip install graphene_django==2.8.2

RUN pip install gunicorn

RUN pip install mysqlclient

COPY configuration/aclabs /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/aclabs /etc/nginx/sites-enabled

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV DB_ENGINE=django.db.backends.mysql
ENV DB_NAME=<your-db-name-here>
ENV DB_USER=<your-user-here>
ENV DB_PASSWORD=<your-password-here>
ENV DB_HOST=<your.host.here.com>
ENV DB_PORT=3306

CMD [ "configuration/entrypoint.sh" ]

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput --settings=aclabs.settings