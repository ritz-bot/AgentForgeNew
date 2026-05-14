# Interview Positioning for BIT Capital

This file is a role-focused prep note for presenting this repository in an interview for an `AI Engineering Intern` role at BIT Capital.

## 1. How to position this project

Do not present this as just "a chatbot."

Present it as:

`A configurable AI-agent application that combines LLM reasoning, optional external search, API-based service design, and production-minded deployment.`

That framing matches the BIT Capital role because they want:

- LLM-powered internal tools
- API integration
- external data integration
- engineering ownership
- practical tooling that improves workflows

## 2. The best angle for this role

BIT Capital is not hiring for a generic prompt-engineering intern. They are hiring for someone who can build useful AI systems for research workflows.

So your angle should be:

`This project shows that I can build an end-to-end AI application: UI, backend API, LLM integration, tool use, deployment pipeline, and an architecture that can be extended into internal research tooling.`

## 3. One-minute version

Use this if they say, "Walk me through one project you built."

`This project is a configurable AI-agent application built in Python. I created a Streamlit frontend where a user can define the agent behavior through a system prompt, choose the model, and decide whether the agent can use live web search. That request goes to a FastAPI backend, which validates the input and calls a LangGraph-based agent layer. The agent uses Groq-hosted models, and when search is enabled it can use Tavily to fetch current information before generating a response. I also containerized the application with Docker and added a Jenkins pipeline that runs SonarQube analysis, builds the image, pushes it to ECR, and deploys it to ECS Fargate.`

## 4. Two-minute version

Use this if they want more detail.

`I built this as a modular AI application rather than a notebook-style prototype. The frontend is in Streamlit and keeps the interaction simple for end users. The backend is a FastAPI service that exposes a `/chat` endpoint, validates the selected model, and separates application logic from presentation. In the core layer, I use LangGraph's ReAct agent pattern with ChatGroq, and I conditionally attach Tavily as a search tool when the user wants up-to-date information.`

`What I like about this structure is that it creates a clean boundary between interface, API, and agent logic. That matters if you later want to turn the same core capability into an internal analyst tool, a Slack bot, or a research workflow service. I also added Docker and a Jenkins-based CI/CD pipeline with SonarQube and AWS deployment, because I wanted to treat it as something that could move beyond a local demo.`

## 5. How this maps to the BIT Capital job description

### LLM-powered tools

This project directly shows:

- LLM integration with `Groq`
- prompt-controlled agent behavior
- tool-augmented generation using live search
- a user-facing workflow rather than just an isolated script

How to say it:

`The main thing I wanted to demonstrate was not just calling an LLM API, but wrapping that capability into a reusable tool with a clear interface and backend service layer.`

### APIs and external data

This project directly shows:

- API design with `FastAPI`
- external service integration with `Groq` and `Tavily`
- request/response flow between frontend and backend

How to say it:

`This repo reflects the kind of engineering work where the LLM is only one component. The useful part is integrating model APIs and external data into a system that users can actually interact with.`

### Internal tooling mindset

This project is relevant because:

- it is structured like an internal tool
- it separates UI from service logic
- it can be repurposed for domain-specific workflows

How to say it:

`The architecture is intentionally simple but extensible. I wanted a foundation that could later support domain-specific assistants, internal dashboards, or task-specific research agents.`

### Ownership and shipping

This project helps you demonstrate:

- full-stack ownership in Python
- basic packaging
- Dockerization
- CI/CD thinking
- logging and exception handling

How to say it:

`I built the project end-to-end myself, including the interface, API layer, agent logic, and deployment pipeline, so it reflects how I think about shipping a working system rather than just experimenting with models.`

## 6. What not to overclaim

Be careful on these points.

### "Multi-agent"

Current reality:

- the project is closer to a configurable single-agent system
- it creates one tool-using agent per request
- it does not orchestrate multiple specialized agents

Safe wording:

`Right now it is a configurable agent platform and a foundation for multi-agent workflows. The next step would be splitting responsibilities across specialized agents such as researcher, synthesizer, and critic.`

### "Production-ready"

Current reality:

- good demo architecture
- production-minded components
- not yet fully production-hardened

Safe wording:

`I designed it with production-style components like API separation, Docker, logging, and CI/CD, but there are still hardening steps I would take before calling it fully production-ready.`

## 7. The biggest gap relative to BIT Capital

The BIT Capital role explicitly mentions:

- databases
- SQL
- data pipelines
- investment research workflows

This repo does not yet demonstrate those strongly.

Do not ignore that. Address it directly.

Use this answer:

`The current version is strongest on LLM integration, APIs, and application structure. If I were extending it for this role, the first thing I would add is a proper research data layer: for example a Postgres database for company metadata and cached outputs, scheduled ingestion of external market data, and a retrieval layer so the agent can reason over internal structured and unstructured sources rather than only live web search.`

That answer shows maturity.

## 8. Best "how I would adapt this for investment research" answer

If they ask how this project could be useful at BIT Capital, say:

`I would evolve it from a general-purpose agent into a research workflow assistant. For example, one agent could gather company updates from external APIs or news sources, another could summarize the information in an analyst-friendly format, and a third could check whether the output matches a specific investment template. I would also add a database layer for storing company-level context, cached summaries, and evaluation data, so the system becomes more consistent and useful over time.`

## 9. Concrete finance-focused extensions you can propose

These are good follow-up ideas if they ask what you would build next.

### Extension 1: Earnings and news summarizer

- ingest company news and earnings updates
- summarize them into analyst-readable notes
- tag items by topic such as guidance, margins, product launches, or management changes

### Extension 2: Company research copilot

- attach internal notes, transcripts, and market data
- let analysts ask company-specific questions
- return answers with source-backed context

### Extension 3: Market monitoring agent

- watch selected tickers or themes
- trigger alerts when certain events occur
- produce daily or weekly summaries

### Extension 4: Sales and PM support tool

- convert research into short client-facing talking points
- maintain different answer styles for analysts, PMs, and sales teams

## 10. What parts of the code to mention if they ask for implementation details

### Frontend

File:
- `app/frontend/ui.py`

What it does:
- collects the system prompt
- lets the user choose the model
- optionally enables web search
- sends the request to the backend API

### Backend

File:
- `app/backend/api.py`

What it does:
- defines the request schema
- validates allowed model names
- calls the agent layer
- returns the response

### Agent logic

File:
- `app/core/ai_agent.py`

What it does:
- creates a `ChatGroq` model instance
- optionally attaches `TavilySearchResults`
- creates a ReAct agent using `LangGraph`

### App orchestration

File:
- `app/main.py`

What it does:
- starts the backend service
- launches the Streamlit frontend

### Infra

Files:
- `Dockerfile`
- `Jenkinsfile`
- `custom_jenkins/Dockerfile`

What they show:
- containerization
- static analysis with SonarQube
- image build and push
- AWS deployment flow

## 11. Questions they may ask and strong answers

### Why did you use FastAPI instead of putting everything in Streamlit?

`I wanted a clean API boundary. That makes the agent logic reusable and lets me swap the frontend later without rewriting the core application logic.`

### Why did you use LangGraph?

`Because I wanted an agent-oriented abstraction rather than a raw API call. It gives me a cleaner path to add tool use, workflow logic, and eventually multi-agent coordination.`

### What is the value of the Tavily integration?

`It addresses a practical limitation of LLMs: stale knowledge. With optional live search, the agent can answer questions that depend on more recent information.`

### What would you improve first?

`I would add a database layer, remove hardcoded config, add tests, pin dependencies, and convert the current single-agent flow into a true multi-agent research workflow.`

### How is this relevant to investment research?

`The core pattern is highly relevant: take unstructured user questions, combine LLM reasoning with external data, and return structured outputs. The domain-specific step would be connecting that pattern to company data, research notes, and market workflows.`

## 12. Honest weaknesses you should mention if pressed

You do not need to volunteer every flaw, but if they probe deeper, these are honest and acceptable:

- no test suite yet
- no database layer yet
- not a true multi-agent orchestration system yet
- frontend/backend coupling through a hardcoded local URL
- some cleanup still needed in dependency management and repo hygiene

Good way to frame it:

`I treated this as a strong end-to-end prototype with deployable structure, and I can clearly see the next engineering steps needed to turn it into a more robust internal platform.`

## 13. The exact message to leave them with

If you want one final sentence that fits this role, use this:

`This project shows that I can move beyond simple LLM demos and build AI tools as real software systems, with APIs, tool use, deployment, and a clear path toward research-focused workflows.`
