FROM python:2.7.7-onbuild

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt
