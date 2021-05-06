FROM python:3.9-alpine

COPY ./requirments.txt /requirments.txt
COPY ./app /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install -r /requirments.txt && \
    adduser --disabled-pasword --no-create-home django-user

ENV PATH="/py/bin:$PATH"

USER django-user