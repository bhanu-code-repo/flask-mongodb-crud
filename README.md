# Flask MongoDB CRUD Application

This is a simple Flask web application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database. The application is containerized using Docker, allowing easy deployment and scalability.

## Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Clone the Repository

```
git clone https://github.com/bhanu-code-repo/flask-mongodb-crud.git
cd flask-mongodb-crud
```

### Build and Run Docker Containers

```
docker-compose build
docker-compose up
```

## Usage

### Add a User

```
curl -X POST -H "Content-Type: application/json" -d '{"name":"John", "age":25}' http://localhost:5000/add
```

### Get All Users

```
curl http://localhost:5000/get
```

### Update a User

```
curl -X PUT -H "Content-Type: application/json" -d '{"age":30}' http://localhost:5000/update/John
```

### Delete a User

```
curl -X DELETE http://localhost:5000/delete/John
```
