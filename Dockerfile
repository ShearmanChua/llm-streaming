FROM python:3.8.15-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1


ADD requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN pip install "uvicorn[standard]"

WORKDIR /src