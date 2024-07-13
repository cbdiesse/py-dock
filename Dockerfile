FROM python:3.12.3-alpine

WORKDIR /app

COPY requirements.lock /app
COPY requirements-dev.lock /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pytest

RUN mkdir -p /app/tests

COPY src/  /app
COPY tests/ /app/tests

CMD [ "python", "app.py" ]