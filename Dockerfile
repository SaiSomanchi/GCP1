# syntax=docker/dockerfile:1
FROM python:3.6-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends make

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
ENV PORT=8080

CMD ["python", "app.py"]
