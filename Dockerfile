FROM python:3.12.3-alpine

WORKDIR /app

COPY requirements.lock /app
COPY requirements-dev.lock /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.lock

RUN pip install pytest

COPY src/  /app

COPY tests /app

CMD [ "python", "app.py" ]