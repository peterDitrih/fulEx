FROM python:3.10

ENV PYTHONPATH=/fulex_api

COPY requirements.txt /

RUN apt update && \
 apt install -y libpq-dev python3-dev&& \
 pip install -r /requirements.txt && \
 rm /requirements.txt && \
 mkdir -p /fulex_api/src/api

COPY src /fulex_api/src

ENTRYPOINT ["/bin/bash","-c","uvicorn src.api:app --host 0.0.0.0 --port 5000"]