# Architecture Decisions

This document records major technical decisions made during development.

---

## Decision 1 — Google Gemini as the LLM

**Decision**

Use Google Gemini as the primary Large Language Model.

**Reason**

* Strong reasoning capabilities
* Good support for enterprise-style applications
* Simple API integration
* Suitable free tier for development
* Fast response times

**Alternatives Considered**

* OpenAI GPT
* Open-source LLMs (Llama, Mistral)

---

## Decision 2 — LangChain

**Decision**

Use LangChain for orchestrating prompts, retrieval, and LLM interactions.

**Reason**

* Mature ecosystem
* Excellent RAG support
* Easy integration with Gemini
* Flexible architecture

---

## Decision 3 — FAISS

**Decision**

Use FAISS as the vector database.

**Reason**

* Local execution
* No cloud dependency
* Fast similarity search
* Simple setup for demonstrations

**Production Alternative**

* Pinecone
* Azure AI Search
* Weaviate

---

## Decision 4 — Streamlit

**Decision**

Use Streamlit for the user interface.

**Reason**

* Rapid development
* Interactive UI components
* Ideal for AI demos
* Minimal frontend overhead

---

## Decision 5 — PyMuPDF

**Decision**

Use PyMuPDF for PDF processing.

**Reason**

* Fast text extraction
* Reliable PDF handling
* Easy integration into ingestion pipelines

---

## Decision 6 — python-dotenv

**Decision**

Store API keys using environment variables.

**Reason**

* Keeps secrets out of source code
* Standard development practice
* Easy local configuration

---

## Version 1.0 Scope

Included

* RAG pipeline
* Gemini integration
* FAISS vector search
* Streamlit UI
* Executive summaries
* Risk analysis

Deferred

* LangGraph agents
* Docker
* Kubernetes
* Cloud deployment
* Monitoring
* Authentication
* OCR
* Fine-tuning
