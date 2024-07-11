FROM python:3.12.3-alpine

WORKDIR /kaspy_app

COPY requirements.lock .
COPY requirements-dev.lock .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pytest

COPY app/ .

COPY tests/ app/tests/

CMD [ "python", "app.py" ]