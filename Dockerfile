# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./requirements/ ./requirements/
RUN pip install -r requirements/local.txt


# add app
COPY . .
