FROM python:3.8
RUN mkdir /usr/src/server3/
WORKDIR /usr/src/server3/

ADD app.py app.py

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 83