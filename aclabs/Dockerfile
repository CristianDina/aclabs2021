FROM python:3.7

RUN apt-get update

RUN mkdir /app
ADD . /app
WORKDIR /app/aclabs

EXPOSE 8000

RUN pip install Django==3.1
RUN pip install graphene_django==2.8.2

CMD ["/app/entrypoint.sh"]
