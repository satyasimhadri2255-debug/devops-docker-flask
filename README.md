# DevOps Docker Flask Application

A production-style DevOps project demonstrating Docker, CI/CD, automated testing, Docker Hub publishing, and Kubernetes deployment.

---

## 🚀 Project Overview

This project demonstrates a complete DevOps workflow:

1. Build a Flask application
2. Containerize using Docker
3. Automate CI with GitHub Actions
4. Add smoke tests and automated tests
5. Publish Docker image to Docker Hub (CI/CD)
6. Deploy to Kubernetes with health checks

---

## 🛠 Tech Stack

- Python (Flask)
- Docker
- Docker Compose
- Git & GitHub
- GitHub Actions (CI/CD)
- Docker Hub
- Kubernetes (Docker Desktop)
- Pytest

---

## 📂 Project Structure


devops-project/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
│
└── .github/
└── workflows/
└── ci.yml


---

## 🧩 Application Endpoints

| Endpoint | Purpose |
|---------|---------|
| `/` | Returns welcome message |
| `/health` | Health check endpoint (used by CI + Kubernetes) |

---

## ▶️ Run Locally (Without Docker)

```bash
pip install -r requirements.txt
python app.py

Open:

http://localhost:5000
🐳 Run With Docker
Build Image
docker build -t my-first-devops-app .
Run Container
docker run -p 5000:5000 my-first-devops-app
🐳 Run With Docker Compose
docker compose up --build

Stop:

docker compose down
🔄 CI/CD Pipeline (GitHub Actions)

On every push to main, GitHub Actions:

Builds Docker image

Runs container

Performs smoke test (curl /)

Checks health endpoint (curl /health)

Runs pytest tests

Stops container

Logs into Docker Hub

Tags and pushes image automatically

✔ Successful run = Green check in Actions tab

📦 Docker Hub Image

Image is automatically published to:

docker.io/satyasimhadri2255/my-first-devops-app:latest

Pull it:

docker pull satyasimhadri2255/my-first-devops-app:latest

Run it:

docker run -p 5000:5000 satyasimhadri2255/my-first-devops-app:latest
☸ Kubernetes Deployment

Deploy:

kubectl apply -f k8s/

Port forward:

kubectl port-forward service/flask-service 8080:80

Open:

http://localhost:8080
📘 Key DevOps Concepts Implemented

Docker containerization

CI automation

Smoke testing in pipeline

Automated unit testing (pytest)

CI/CD publishing to Docker Hub

Kubernetes Deployment & Service

Liveness/Readiness health probes

Logs and troubleshooting

🧠 Interview Summary

“I built a containerized Flask application and implemented a full CI/CD pipeline using GitHub Actions. The pipeline builds, tests, runs smoke checks, publishes the image to Docker Hub, and deploys it to Kubernetes with health probes configured.”

👤 Author

Sri Satya Simhadri Thota
DevOps Engineer – Hands-on Project