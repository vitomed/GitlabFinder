# docker build 

FROM python:3.7-alpine

WORKDIR /app

RUN pip install -r requiremens.txt

ADD main.py ./

EXPOSE 5000

CMD ['python3', 'main.py']



