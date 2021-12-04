FROM python:3.8
RUN mkdir /usr/src/server2/
WORKDIR /usr/src/server2/

ADD app.py app.py

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 82