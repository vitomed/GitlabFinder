# docker build 
FROM ubuntu:16.04

FROM python:3.7

RUN apt-get update

EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY maint.py /app

CMD python main.py



