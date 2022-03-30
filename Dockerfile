# syntax=docker/dockerfile:1
FROM python:3.8.0-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends make

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app/app_files

CMD ["python", "app.py"]
runtime: custom
env: flex

manual_scaling:
  instances: 1
resources:
  cpu: 1
  memory_gb: 0.5
  disk_size_gb: 10
