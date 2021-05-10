FROM python:3.9.4-alpine
ADD requirements.txt /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

ADD . /app
EXPOSE 5000