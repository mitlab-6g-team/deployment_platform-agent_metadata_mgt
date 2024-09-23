FROM python:3.8.10

WORKDIR /app/agent_metadata_mgt

COPY . .

RUN apt-get update \
    && pip install -r /app/agent_metadata_mgt/requirements/local.txt