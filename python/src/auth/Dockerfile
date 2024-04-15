# Each query creates a new layer in the image on top of the previous one.\
# This means that the order of the commands in the Dockerfile is important.\
# building our application on top of the base image, this means using a system where python is already installed
FROM --platform=linux/amd64 python:3.11.8-slim-bullseye as build

# The RUN command is used to execute a command during the build process of the Docker image.\
# Keeping all the RUN commands in a single command reduces the number of layers created in the image.\
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev pkg-config libssl-dev \
    && pip install --no-cache-dir --upgrade pip

# Application src directory
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

EXPOSE 5000

# The CMD command is used to specify the command that will run when the container starts.\
CMD ["python3", "server.py"]