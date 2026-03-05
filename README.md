# DevOps Docker Flask Application

A production-style DevOps project demonstrating Docker, CI/CD, automated testing, Docker Hub publishing, and Kubernetes deployment with Ingress routing and autoscaling.

---

## 🚀 Project Overview

This project demonstrates a complete DevOps workflow:

1. Build a Flask application  
2. Containerize using Docker  
3. Automate CI with GitHub Actions  
4. Add smoke tests and automated tests  
5. Publish Docker image to Docker Hub (CI/CD)  
6. Deploy to Kubernetes with health checks  
7. Expose application using Kubernetes Ingress  
8. Implement autoscaling using Kubernetes HPA  

---

## 🛠 Tech Stack

- Python (Flask)
- Docker
- Docker Compose
- Git & GitHub
- GitHub Actions (CI/CD)
- Docker Hub
- Kubernetes (Docker Desktop)
- NGINX Ingress Controller
- Pytest
- Horizontal Pod Autoscaler (HPA)

---

## 📂 Project Structure


devops-project/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── ingress.yaml
│ └── hpa.yaml
│
└── .github/
└── workflows/
└── ci.yml


---

## 🧩 Application Endpoints

| Endpoint | Purpose |
|--------|--------|
| `/` | Returns welcome message |
| `/health` | Health check endpoint (used by CI + Kubernetes) |

---

# ▶️ Run Locally (Without Docker)

Install dependencies:

```bash
pip install -r requirements.txt

Run the application:

python app.py

Open browser:

http://localhost:5000
🐳 Run With Docker

Build Docker image:

docker build -t my-first-devops-app .

Run container:

docker run -p 5000:5000 my-first-devops-app

Open browser:

http://localhost:5000
🐳 Run With Docker Compose

Start application:

docker compose up --build

Stop application:

docker compose down
🔄 CI/CD Pipeline (GitHub Actions)

On every push to the main branch, GitHub Actions automatically:

Builds the Docker image

Runs the container

Performs smoke test (curl /)

Checks health endpoint (curl /health)

Runs pytest unit tests

Stops and removes container

Logs into Docker Hub

Tags and pushes Docker image automatically

Successful pipeline runs show a green check mark in the Actions tab.

📦 Docker Hub Image

Image is automatically published to Docker Hub:

docker.io/satyasimhadri2255/my-first-devops-app:latest

Pull the image:

docker pull satyasimhadri2255/my-first-devops-app:latest

Run the image:

docker run -p 5000:5000 satyasimhadri2255/my-first-devops-app:latest
☸ Kubernetes Deployment

Deploy resources:

kubectl apply -f k8s/

Check running pods:

kubectl get pods
Access Using Port Forward (Optional)
kubectl port-forward service/flask-service 8080:80

Open:

http://localhost:8080
🌐 Kubernetes Ingress (No Port Forward Required)

After installing the NGINX Ingress Controller:

kubectl apply -f k8s/ingress.yaml

Access application directly:

http://localhost/
http://localhost/health

Traffic flow:

Browser → Ingress Controller → Service → Pod
📈 Kubernetes Autoscaling (HPA)

Horizontal Pod Autoscaler automatically scales the Flask application based on CPU usage.

Configuration:

Minimum pods: 1

Maximum pods: 3

Target CPU utilization: 50%

Apply HPA:

kubectl apply -f k8s/hpa.yaml

Check autoscaler:

kubectl get hpa

Watch scaling:

kubectl get pods -w
📘 Key DevOps Concepts Implemented

Docker containerization

CI automation with GitHub Actions

Smoke testing in CI pipeline

Automated unit testing (pytest)

CI/CD publishing to Docker Hub

Kubernetes Deployment & Service

Liveness and Readiness probes

NGINX Ingress routing

Horizontal Pod Autoscaler (HPA)

Logs and troubleshooting

Debugging pipeline and Kubernetes issues

🧠 Interview Summary

"I built a containerized Flask application and implemented a complete CI/CD pipeline using GitHub Actions. The pipeline automatically builds, tests, and pushes Docker images to Docker Hub. The application is deployed to Kubernetes with health probes, Ingress routing, and Horizontal Pod Autoscaling configured."

👤 Author

Sri Satya Simhadri Thota
DevOps Engineer – Hands-on Project


---

