# DevOps Docker Flask Application

This is a beginner-friendly DevOps project where a simple Python Flask web application is containerized using Docker and automated using GitHub Actions CI.

---

## 🚀 Project Overview

The goal of this project is to understand the complete DevOps flow:
- Build a simple application
- Containerize it using Docker
- Run it locally using Docker
- Version control using Git & GitHub
- Automatically build the Docker image using GitHub Actions (CI)

---

## 🛠 Tech Stack

- **Python** (Flask)
- **Docker**
- **Git & GitHub**
- **GitHub Actions (CI)**

---

## 📂 Project Structure

```

devops-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
│
└── .github/
└── workflows/
└── ci.yml

```

---

## 🧩 Application Details

- The Flask app exposes a single endpoint `/`
- When accessed, it returns a simple message:
```

Hello! My first DevOps Docker app is working 🚀

````

---

## ▶️ Run Application Without Docker

```bash
python -m pip install flask
python app.py
````

Open browser:

```
http://localhost:5000
```

---

## 🐳 Run Application Using Docker

### Build Docker Image

```bash
docker build -t my-first-devops-app .
```

### Run Docker Container

```bash
docker run -p 5000:5000 my-first-devops-app
```

Open browser:

```
http://localhost:5000
```

---

## 🔄 CI Pipeline (GitHub Actions)

This project includes a GitHub Actions CI workflow that:

* Runs on every push to the `main` branch
* Checks out the code
* Builds the Docker image automatically

A successful pipeline run is indicated by a **green check mark ✔** in the GitHub Actions tab.

---

## 📘 What I Learned

* How to build a Flask application
* How Docker images and containers work
* How to write a Dockerfile
* How to run applications inside containers
* How GitHub Actions automates Docker builds
* How to debug real Docker and Windows issues

---

## 🧠 Interview Summary

> “I built and Dockerized a Flask application, pushed it to GitHub, and implemented a CI pipeline using GitHub Actions that automatically builds the Docker image on every commit.”

---

## 👤 Author

**Sri Satya Simhadri Thota**
DevOps Engineer (Sample Project)
