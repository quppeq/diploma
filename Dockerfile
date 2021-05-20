FROM python:3.9.4-alpine
RUN apk add --update python3 py-pip python3-dev postgresql-dev gcc musl-dev patch git tzdata build-base

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN python3 -m pip install -r requirements.txt

ADD . /app
EXPOSE 5000