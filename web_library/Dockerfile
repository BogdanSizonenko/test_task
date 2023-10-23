FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ADD . /web_library

WORKDIR /web_library

RUN pip install -r requirements.txt