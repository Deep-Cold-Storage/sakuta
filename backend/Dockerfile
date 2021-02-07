FROM python:3.8.2

RUN apt update
RUN apt install -y curl

# Copy requirements.
ADD requirements.txt /requirements.txt

# Install requirements.
RUN pip3 install -r requirements.txt

# Copy files.
ADD / /backend

EXPOSE 8000

# Healthcheck
HEALTHCHECK CMD curl --fail http://127.0.0.1:8000/health || exit 1  

# Run app server.
CMD uvicorn --host 0.0.0.0 --port 8000  --root-path /api backend.main:app 