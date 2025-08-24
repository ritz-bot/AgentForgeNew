# Multi-AI Agent System for Customizable Query Handling (AgentForge)


A production-grade, customizable multi-AI agent application that allows users to create specialized agents (e.g., financial, medical, study) for real-time query responses. Combines LLMs with internet search to provide up-to-date answers, overcoming LLM data cutoff limitations.

---

### Objective
Build a customizable, production-grade multi-AI agent system that integrates LLMs with real-time search for accurate, domain-specific query responses, while ensuring scalability through containerization, code quality checks, and automated CI/CD deployment.

---

### Business Case
Develop a versatile AI application enabling users to create specialized agents (e.g., financial, medical, study) for real-time, informed decision-making, reducing reliance on outdated LLM data and improving efficiency in business, healthcare, or education scenarios.

---

### Problem Statement
Address LLM limitations like outdated training data (e.g., cutoff at 2021) by integrating real-time internet search, while ensuring the system is deployable, maintainable, and high-quality through automated pipelines to handle dynamic queries across domains.

---

## Features
- User-defined agent types with specific behaviors.
- Real-time internet search integration for current information.
- End-to-end workflow: AI logic, backend, frontend, containerization, code quality checks, and CI/CD deployment.
- Scalable and maintainable with automated pipelines.

---

## Key Technologies and Roles
1. **Grok (LLM via Grok Cloud)** – Free LLM API, supports Llama 3 models.
2. **Tavily** – Free API for real-time search.
3. **LangChain** – Framework for LLM integration and tool chaining.
4. **LangGraph** – Workflow management for agentic AI.
5. **FastAPI** – Backend service.
6. **Streamlit** – Lightweight, interactive UI.
7. **Docker** – Containerization for consistent deployment.
8. **SonarQube** – Automated code quality analysis.
9. **Jenkins** – CI/CD pipelines for automated build, test, and deploy.
10. **AWS (ECR + ECS Fargate)** – Cloud deployment with scalability.

---

## Detailed Concepts
- **Tavily + LLM Integration**: Ensures real-time, accurate responses by combining historical LLM data with live search.
- **SonarQube**: Detects code smells, bugs, and duplication for maintainability.
- **Jenkins Pipeline**: Automates workflows from GitHub push to AWS deployment.

---

## Step-by-Step Setup
1. **Project Setup**
   - Create a virtual environment and install dependencies from `requirements.txt`.
   - Structure the project with `app/backend`, `app/frontend`, `app/core`, and `app/common`.

2. **API and Keys**
   - Sign up for **Grok** and **Tavily** APIs.
   - Store credentials in a `.env` file.

3. **Backend**
   - Build APIs using FastAPI to handle agent logic and LLM queries.

4. **Frontend**
   - Use Streamlit for an interactive web UI.

5. **Dockerization**
   - Create a Dockerfile and containerize the app for deployment.

6. **CI/CD with Jenkins**
   - Automate builds, testing, and deployment to AWS ECS Fargate.
