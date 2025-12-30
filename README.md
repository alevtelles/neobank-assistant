# Neobank Assistant
Generative AI Architecture for Financial Use Cases

This project is an end-to-end **Generative AI assistant architecture** designed for financial and neobank scenarios, focusing on **structured knowledge retrieval, explainability and production readiness**.

It demonstrates how to combine **LLMs, Retrieval-Augmented Generation (RAG) and backend APIs** to build reliable AI-driven systems for regulated environments.

---

## 🎯 Problem Context

Financial institutions deal with large volumes of internal documentation, policies and structured knowledge.  
Traditional chatbots struggle with:
- hallucinations
- lack of explainability
- poor control over data sources

This project addresses these challenges by using a **RAG-based architecture** that grounds responses on trusted documents while keeping the system modular and extensible.

---

## 🏗️ Architecture Overview

The solution is organized as a modular pipeline:

1. **Document Ingestion**
   - Structured ingestion of financial documents
   - Text normalization and chunking
   - Embedding generation

2. **Semantic Indexing**
   - Vector-based storage for efficient retrieval
   - Decoupled indexing layer to allow different vector DB providers

3. **Retrieval Layer**
   - Contextual search based on user queries
   - Top-K document selection with relevance filtering

4. **Generation Layer**
   - LLM-based answer generation
   - Responses grounded exclusively on retrieved context

5. **API & Orchestration**
   - FastAPI backend exposing inference endpoints
   - Clear separation between orchestration and model logic

---

## 🔍 Design Decisions

- **RAG instead of fine-tuning:** improves explainability and reduces operational cost
- **Backend-first approach:** enables reuse across web, mobile or internal systems
- **Provider-agnostic design:** allows swapping LLMs or vector databases
- **Explicit separation of concerns:** simplifies maintenance and scaling

---

## ⚠️ Known Limitations

- This project focuses on architecture and orchestration, not UI/UX
- Authentication and authorization are intentionally minimal
- Monitoring and tracing are simplified for clarity

These aspects are expected to be extended in a production environment.

---

## 🚀 Possible Extensions

- Role-based access control (RBAC)
- Prompt versioning and evaluation
- Caching and latency optimization
- Observability (logs, metrics, traces)
- Frontend integration (dashboard or chat UI)

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **AI:** LLMs, embeddings, RAG
- **Data:** Vector databases
- **Language:** Python
- **Infra:** Container-ready architecture

---

## ▶️ Running the Project

```bash
# clone repository
git clone https://github.com/alevtelles/neobank-assistant
cd neobank-assistant

# install dependencies
pip install -r requirements.txt

# run API
uvicorn app.main:app --reload
