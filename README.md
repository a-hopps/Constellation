# Constellation

<p align="center">
  <strong>Personal Network CRM & Relationship Mapping Platform</strong>
</p>

---

## 📌 Overview

**Constellation** is a full-stack personal CRM designed to help anyone manage, visualize, and query their network connections. Beyond a standard address book, Constellation transforms contact records into an interactive 2D graph, maps real-world geographical locations, and provides an AI assistant powered by Retrieval-Augmented Generation (RAG) to query interaction history using natural language.

---

## 🛠️ Tech Stack

- **Frontend:** Next.js 14 (App Router), TypeScript, Tailwind CSS
- **Visualizations:** `react-force-graph-2d` (D3.js), `react-leaflet` (Leaflet.js / OpenStreetMap)
- **Backend:** FastAPI (Python 3.11+), Pydantic, SQLAlchemy 2.0 (Async)
- **Database:** PostgreSQL + `pgvector` (Relational data & vector embeddings)
- **AI / RAG:** OpenAI API (`text-embedding-3-small`, `gpt-4o-mini`), LangChain
- **DevOps:** Docker Compose, GitHub Actions, Vercel / Render

---

## 📐 Architecture & Project Structure

```text
constellation/
├── client/              # Next.js TypeScript Frontend
│   ├── src/
│   │   ├── app/         # App Router Pages (Contacts, Graph, Map, AI)
│   │   ├── components/  # Reusable UI, Graph, & Map Components
│   │   ├── lib/         # API Clients & Fetchers
│   │   └── types/       # TypeScript Interfaces
│   └── package.json
│
├── server/              # FastAPI Python Backend
│   ├── app/
│   │   ├── api/         # Endpoint Routers (Contacts, Interactions, RAG)
│   │   ├── core/        # Database & Environment Config
│   │   ├── models/      # SQLAlchemy Database Models
│   │   └── schemas/     # Pydantic Schemas
│   ├── alembic/         # Database Migrations
│   └── requirements.txt
│
└── docker-compose.yml   # Local PostgreSQL + pgvector Setup