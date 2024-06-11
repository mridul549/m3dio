# M3DIO: MP4 to MP3 Converter Application

## Introduction

This repository contains the source code for an MP4 to MP3 converter application. The project follows a microservices architecture and leverages various technologies to provide a robust and scalable solution. The application is designed to convert MP4 video files to MP3 audio files, utilizing a combination of Python, Kubernetes, RabbitMQ, MongoDB, and MySQL.

## Tech Stack

- **Python**: Primary programming language for developing the microservices.
- **Kubernetes**: Container orchestration platform to manage and deploy the microservices.
- **RabbitMQ**: Message broker for handling asynchronous communication between services.
- **MongoDB**: NoSQL database for storing metadata and other data related to the media files.
- **MySQL**: Relational database for handling user authentication and other structured data.

## System Design
![M3DIO](https://github.com/mridul549/m3dio/assets/94969636/8dbf7edd-d92a-4d43-8bfe-ea1065d4d9c7)

The system is designed with multiple microservices, each responsible for a specific functionality of the application. Below is an overview of the key components and their interactions:

1. **Auth Service**:
   - Handles user authentication using JWTs.
   - Stores user credentials and sessions in MySQL.
   - Provides secure access to the other services.

2. **Gateway Service**:
   - Acts as a reverse proxy and routes requests to appropriate services.
   - Manages API requests and load balancing.
   - Deployed using Kubernetes Ingress.

3. **Converter Service**:
   - Performs the actual conversion of MP4 files to MP3 format.
   - Uses Python libraries for media processing.
   - Scales according to the workload using Kubernetes StatefulSet.

4. **Notification Service**:
   - Sends notifications to users about the status of their conversion tasks.
   - Integrates with RabbitMQ for asynchronous messaging.
   - Can send emails, push notifications, or other forms of alerts.

5. **Database Layer**:
   - **MongoDB**: Stores media files and metadata using GridFS.
   - **MySQL**: Manages user data, authentication information, and other structured data.

6. **Message Broker**:
   - RabbitMQ facilitates communication between microservices.
   - Ensures asynchronous processing and decoupling of services.

7. **Kubernetes**:
   - Manages the deployment, scaling, and operations of containerized applications.
   - Uses Kubernetes Ingress for routing and Kubernetes StatefulSet for managing RabbitMQ.

