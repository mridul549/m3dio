# M3DIO

M3DIO is a robust microservices-based application designed to demonstrate a scalable and efficient way of managing authentication, data storage, and interservice communication. This project leverages cutting-edge technologies such as Kubernetes, RabbitMQ, Docker, and MongoDB.

## Features

- **Authentication Service**: Manages user authentication and session management.
- **Gateway Service**: Acts as a central point for routing requests to various services.
- **Notification Service**: Handles sending notifications to users.
- **Converter Service**: Provides data format conversion functionalities.

## Tech Stack

- **Flask**: For building fast and scalable server-side applications.
- **MongoDB**: A NoSQL database used for high-volume data storage.
- **RabbitMQ**: Handles asynchronous interservice communication.
- **Docker**: For containerizing the application and its services.
- **Kubernetes**: Used for automating deployment, scaling, and operations of application containers across clusters.
- **GitHub Actions**: Implements CI/CD pipelines for automated integrations and deployments.

## System Design
<img width="910" alt="Screenshot 2024-04-22 at 9 35 04 PM" src="https://github.com/mridul549/m3dio/assets/94969636/32fd56b9-90f1-43aa-a9d4-a3da872cf365">

## Working
The main objective of the project is to convert a video file to audio file. The project utilizes various services in order to achieve this functionality.

- The user first logs into the system by calling the gateway service which in turn calls the authentication service. The authentication validates the credentials and generates the respective token and sends back to the client via the gateway.
- Then the user uploads the file via using the gateway service. The service then uploads the video to the primary database (MongoDB), and then adds the request onto rabbitmq. The converter service picks up the message from the queue, pulls the video from the MongoDB and converts the video to audio file. After this the converter uploads the file again onto MongoDB and informs the queue.
- The notification picks up the uploaded mp3 message from the queue and informs the user via email of the same.
- The notified user then requests the gateway to download the converted audio file from the database.


