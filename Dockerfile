# syntax=docker/dockerfile:1
FROM python:3.8.0-slim-buster
FROM gcr.io/cloud-builders/gcloud
COPY notice.sh /usr/bin
ENTRYPOINT ["/usr/bin/notice.sh"]

RUN apt-get update && apt-get install -y --no-install-recommends make

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
