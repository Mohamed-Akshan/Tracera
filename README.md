# Tracera

### Agentic AI for Production Incident Investigation

Tracera is an AI-powered production incident investigation application that helps engineers analyze logs, identify recurring failures, investigate potential root causes, and produce evidence-backed findings.

The system uses **multi-agent orchestration, Corrective RAG, and human-in-the-loop verification** to support reliable incident investigations.

## Tech Stack

- **Frontend:** React, Vite, CSS
- **Backend:** Python, FastAPI
- **Database:** PostgreSQL, SQLAlchemy
- **Vector Database:** Pinecone
- **LLM:** Google Gemini (primary), Groq (fallback)
- **Embeddings:** Google Gemini
- **AI Frameworks:** LangChain, LangGraph
- **Tracing:** LangSmith

## Planned Features

- ChatGPT-style AI Investigation Workspace
- Automated incident investigation
- Multi-agent orchestration using LangGraph
- Corrective RAG for evidence retrieval
- Production log and document analysis
- Agent investigation trace
- Evidence-backed findings dashboard
- Human review and verification
- Structured investigation reports
- Guardrails and evaluation pipeline

## System Architecture

React Frontend → FastAPI Backend → LangGraph Agents → Corrective RAG → Gemini / Groq

PostgreSQL stores investigation metadata and results. Pinecone will support semantic evidence retrieval.

## Project Status

**In active development**

Completed foundations:
- Backend configuration and LLM setup
- PostgreSQL database models
- FastAPI application and health endpoints
- React frontend foundation
- Frontend/backend connection checks
- Investigation CRUD operations

Upcoming:
- Evidence file uploads and processing
- Pinecone vector storage
- Corrective RAG pipeline
- Multi-agent investigation workflow
- Guardrails, evaluations, and reports

## Local Setup

### Backend

Create and activate a Python virtual environment inside `backend`, then run:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure the required credentials.

Start FastAPI:

```bash
python -m uvicorn app.main:app --reload
```

### Frontend

Inside `frontend`, run:

```bash
npm install
npm run dev
```

Frontend: http://localhost:5173

Backend API documentation: http://127.0.0.1:8000/docs

## Purpose

Tracera is a portfolio project demonstrating practical AI engineering, retrieval-augmented generation, multi-agent systems, backend development, and evidence-grounded AI workflows.

*Note: Features listed as planned are not yet implemented.*