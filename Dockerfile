# syntax=docker/dockerfile:1


ARG PYTHON_VERSION=3.11.8
FROM python:${PYTHON_VERSION}-slim as base


ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


USER root
RUN chown -R root:root /app
COPY . .

EXPOSE 8000
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT [ "bash", "/app/entrypoint.sh" ]
# Run the application.
# CMD gunicorn 'journaling_project.wsgi' --bind=0.0.0.0:8000
