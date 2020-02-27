# docker build 

FROM python:3.7-alpine

LABEL maintainer='viktor.medyankin@mail.ru'

#RUN apk update && apk upgrade && apk add bash

WORKDIR /app

#COPY requirements.txt /bin/

COPY . /app 

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["main.py"]

#CMD ["python", "/app/main.py"]



