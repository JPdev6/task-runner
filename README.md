
![CI](https://github.com/JPdev6/myapp/actions/workflows/ci.yml/badge.svg)

# 🚀 MyApp

A modern Python FastAPI starter app, with Docker, Poetry, GitHub Actions CI, linting, and test automation — built as part of the **120-Day Junior Python Developer Sprint**.

---

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework  
- [Poetry](https://python-poetry.org/) — Dependency and package manager  
- [Docker](https://www.docker.com/) — Containerization  
- [GitHub Actions](https://github.com/features/actions) — CI/CD pipeline  
- [pytest](https://docs.pytest.org/) — Testing framework  
- [pre-commit](https://pre-commit.com/) — Code linting automation  

---

## 📦 Installation

Install project dependencies and run the app locally with hot reload:

```bash
poetry install
poetry run uvicorn myapp.main:app --reload
```

---

## 🧪 Run Tests

```bash
poetry run pytest
```

---

## 🧹 Format & Lint (pre-commit)

Set up and run pre-commit hooks:

```bash
poetry run pre-commit install
poetry run pre-commit run --all-files
```

---

## 🐳 Docker Usage

Build and run the app with Docker:

```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
```

---

## ✅ Continuous Integration

This project uses GitHub Actions to automatically run tests and lint checks on every push:

![CI](https://github.com/JPdev6/myapp/actions/workflows/ci.yml/badge.svg)

---

## 📁 Project Structure

```
myapp/
├── myapp/                  # Application package
│   └── main.py             # FastAPI app
├── tests/                  # Pytest tests
│   └── test_smoke.py
├── pyproject.toml          # Poetry config
├── .pre-commit-config.yaml # Linting hooks
├── .github/workflows/ci.yml# GitHub Actions workflow
├── Dockerfile              # Docker image definition
├── README.md               # Project documentation
└── .gitignore
```

---
