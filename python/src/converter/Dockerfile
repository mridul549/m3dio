# Each query creates a new layer in the image on top of the previous one.\
# This means that the order of the commands in the Dockerfile is important.\
# building our application on top of the base image, this means using a system where python is already installed
FROM python:3.11.8-slim-bullseye

# The RUN command is used to execute a command during the build process of the Docker image.\
# Keeping all the RUN commands in a single command reduces the number of layers created in the image.\
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential ffmpeg \
    && pip install --no-cache-dir --upgrade pip

# Application src directory
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

# The CMD command is used to specify the command that will run when the container starts.\
CMD ["python3", "consumer.py"]