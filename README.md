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
Step-by-Step Setup Guide for Multi-AI Agent System:

1. **Project Setup**: Create "multi AI agent" folder; open in VS Code. Set virtual env (`python -m venv env`; activate). Add requirements.txt (listed libs); copy/modify setup.py; install `pip install -e .`. Structure app/ subfolders; add main.py, __init__.py; re-install. Common: Add __init__.py, logger.py, custom_exception.py; re-install. .env: Add API keys (Groq/Tavily). Install WSL/Ubuntu; Docker Engine on Ubuntu; verify.

2. **API Setup**: Get/sign up for Groq/Tavily keys; store in .env.

3. **Config (settings.py)**: Add __init__.py. Imports: load_dotenv, os. Load .env. Settings class: API keys via getenv. Allowed models list (e.g., Llama variants). Instantiate settings.

4. **Core (ai_agent.py)**: Add __init__.py; install. Imports as listed. Function: Init LM (ChatGroq); tools (Tavily if allowed); create agent; state with query; invoke; extract/filter AI messages; return latest.

5. **Backend (api.py)**: Add __init__.py; install. Imports as listed. Logger init. FastAPI app. RequestState class. POST /chat: Log/validate model; try get response, return JSON; except error.

6. **Frontend (ui.py)**: Add __init__.py; install. Imports as listed. Logger. Page config/title. Inputs: system prompt, model select, search checkbox, query. API URL. Button: Payload; POST request; display response or error.

7. **Main (main.py)**: Imports as listed. Load env. Logger. run_backend: Subprocess Uvicorn. run_frontend: Subprocess Streamlit. Main: Thread backend; sleep 2; frontend.

8. **Code Versioning**: .gitignore exclusions. Create GitHub repo. Install Git. Commands: init, branch main, remote add, add ., commit, push.

9. **Dockerfile**: Copy code: FROM Python 3.11-slim; ENV vars; WORKDIR /app; RUN deps; COPY . .; RUN install -e .; EXPOSE ports; CMD python main.py.

10. **Jenkins**: Custom folder/Dockerfile (DinD). Build/run container. Get password/logs. Access IP:8080; unlock/setup user. Install Python in container; restart.

11. **GitHub Integration**: Generate token (repo/hook); add Jenkins cred. New pipeline: SCM Git, URL/cred/branch/Jenkinsfile. Jenkinsfile: Copy/comment stages; add checkout. Push; build; verify workspace.

12. **SonarQube**: Run Docker commands (sonarqube-did). Access IP:9000; login/update. Jenkins plugins. Create project/token; add cred/server/tools. Update Jenkinsfile (env/stage/creds/projectKey). Network: Create/connect containers. Build; verify report.

13. **Build/Push**: Jenkins AWS plugins. Install AWS CLI in container; restart. IAM user/access key; add cred. Create ECR repo. Update Jenkinsfile (stage/env/region/repo/tag/cred). Push; build; verify ECR image.

14. **Deployment**: ECS cluster (Fargate). Task def: CPU/mem/container URI/ports/env vars. Service: Public IP. Security: Inbound ports. Update Jenkinsfile (deployment/cluster/service). Add IAM ECS policy. Build; verify app at IP:8501; changes auto-deploy.
