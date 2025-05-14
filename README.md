
# DevOps Assignment 1

This project is part of a DevOps assignment. It demonstrates the use of GitHub, Docker, Docker Compose, Redis, and Flask to build and deploy a simple web service with persistent storage and version control best practices.

---

## 📌 Project Overview

This project contains:
- A Python Flask-based web service.
- Redis as a backend storage service.
- Docker and Docker Compose for container orchestration.
- Persistent Redis storage using Docker volumes.
- GitHub workflow with protected main branch and pull request requirements.

---

## 🔧 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/ElizabethNikol/DevOps-Assignment-1.git
cd DevOps-Assignment-1
```

### 2. Build and Start the Containers

```bash
docker-compose up --build
```

The web service will be accessible at: [http://localhost:5080](http://localhost:5080)

---

## 🧠 Project Components

### Web Service (Flask)

- Python-based application located in `app.py`.
- Renders a basic HTML page and interacts with Redis.

### Redis

- In-memory key-value database used to store data.
- Configured via Docker Compose with data persisted to `./data/redis`.

### Docker

- `Dockerfile`: Builds the Flask web service image.
- `docker-compose.yml`: Orchestrates Flask + Redis containers.

---

## 💾 Persistent Data

Redis data is stored persistently on the host machine using Docker volumes.  
The data is saved under:

```
./data/redis
```



