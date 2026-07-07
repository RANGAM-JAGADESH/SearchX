# 🚀 SearchX

<div align="center">

### A Production-Ready Search Engine Backend

Built with **FastAPI • Elasticsearch • PostgreSQL • Redis • Docker**

Lightning-fast product search, autocomplete, intelligent recommendations, analytics, caching, and monitoring inspired by modern e-commerce platforms.

---

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-Search-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Redis](https://img.shields.io/badge/Redis-Cache-red)

</div>

---

# 📖 Overview

SearchX is a production-style backend search engine developed to simulate how modern e-commerce companies like Amazon, Flipkart, and Shopify manage millions of searchable products while maintaining low response times and high availability.

Instead of relying solely on relational database queries, SearchX combines Elasticsearch for full-text search, PostgreSQL for persistent storage, Redis for high-speed caching, and FastAPI for REST APIs.

The project follows a modular architecture, making it easy to extend and maintain while demonstrating industry-standard backend engineering concepts.

---

# ❗ Problem Statement

Traditional SQL databases work well for storing data but become inefficient for advanced product searches involving:

- Large product catalogs
- Keyword matching
- Search relevance
- Typo tolerance
- Autocomplete
- Recommendation systems
- High request traffic

Executing every search directly against PostgreSQL increases response time and database load.

SearchX solves these problems using a dedicated search architecture.

---

# 🎯 Project Objectives

- Build a scalable search backend
- Implement full-text product search
- Provide autocomplete suggestions
- Cache frequently searched queries
- Support recommendation engines
- Monitor system health
- Log search analytics
- Containerize the complete application
- Follow production-ready backend architecture

---

# ✨ Features

## 🔍 Intelligent Product Search

- Full-text search
- Multi-field searching
- Ranked search results
- Relevance scoring
- Price sorting
- Query normalization
- PostgreSQL fallback when Elasticsearch is unavailable

---

## ⚡ Elasticsearch Integration

- Dedicated search index
- Fast inverted indexing
- BM25 ranking
- Optimized search queries
- High-speed retrieval

---

## 🗄 PostgreSQL Integration

- Product storage
- Search logging
- Persistent data
- SQLAlchemy ORM

---

## ⚡ Redis Cache

- Query result caching
- Faster repeated searches
- Cache statistics
- Cache invalidation
- Cache clearing endpoint

---

## 💡 Autocomplete Engine

- Prefix matching
- Instant suggestions
- Improved user experience

---

## 🎯 Recommendation Engine

- Popular products
- Trending products
- Recently viewed products
- Recommendation APIs

---

## 📊 Analytics

- Search logs
- Search statistics
- Cache usage
- System metrics
- Dashboard APIs

---

## ❤️ Health Monitoring

Health API monitors

- FastAPI
- PostgreSQL
- Elasticsearch
- Redis

Returns overall application status with response time.

---

## 🐳 Dockerized Architecture

Entire application runs inside Docker containers.

Services include

- FastAPI
- PostgreSQL
- Redis
- Elasticsearch

Managed through Docker Compose.

---

# 🏗 System Architecture

```text
                          +----------------------+
                          |      Client/API      |
                          +----------+-----------+
                                     |
                                     |
                              FastAPI Backend
                                     |
           +-------------------------+-------------------------+
           |                         |                         |
           |                         |                         |
           ▼                         ▼                         ▼
     Elasticsearch               Redis Cache             PostgreSQL
   Full Text Search           Frequently Used Data       Primary Database
           |                         |                         |
           +-------------------------+-------------------------+
                                     |
                                     ▼
                              Search Results
```

---

# 🔍 Search Workflow

```text
                User Search Request
                        │
                        ▼
              Query Normalization
                        │
                        ▼
               Check Redis Cache
                        │
          ┌─────────────┴─────────────┐
          │                           │
      Cache Hit                  Cache Miss
          │                           │
          ▼                           ▼
 Return Cached Result         Elasticsearch Search
                                      │
                         ┌────────────┴────────────┐
                         │                         │
                    Results Found             No Results
                         │                         │
                         ▼                         ▼
                  Return Results         PostgreSQL Fallback
                         │                         │
                         └────────────┬────────────┘
                                      ▼
                              Store in Redis
                                      │
                                      ▼
                                Return Response
```

---

# 📂 Project Structure

```
SearchX
│
├── app
│   ├── analytics
│   ├── api
│   ├── cache
│   ├── core
│   ├── db
│   ├── metrics
│   ├── models
│   ├── recommendations
│   ├── schemas
│   ├── search
│   ├── services
│   └── utils
│
├── datasets
│
├── scripts
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙ Technology Stack

| Category | Technology |
|------------|------------|
| Language | Python |
| Backend Framework | FastAPI |
| Search Engine | Elasticsearch |
| Database | PostgreSQL |
| Cache | Redis |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| API Docs | Swagger UI |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Dataset | CSV |

---

# 📡 REST APIs

## Search APIs

```
GET    /search
GET    /autocomplete
GET    /recommendations
```

---

## Monitoring APIs

```
GET    /health
GET    /metrics
GET    /analytics
```

---

## Cache APIs

```
GET       /cache/stats
DELETE    /cache/clear
```

---

# 🚀 Performance Optimizations

- Elasticsearch Full-Text Search
- Redis Query Caching
- PostgreSQL Fallback
- Query Normalization
- Dockerized Services
- Health Monitoring
- Modular Architecture

---

# 📊 Search Pipeline

```text
CSV Dataset
      │
      ▼
PostgreSQL Database
      │
      ▼
 Synchronization Scripts
      │
      ▼
 Elasticsearch Index
      │
      ▼
 FastAPI Search APIs
      │
      ▼
 Redis Cache
      │
      ▼
 Client Response
```

---

# 🧠 Engineering Challenges Solved

| Challenge | Solution |
|------------|----------|
| Slow SQL searching | Elasticsearch Full-Text Search |
| Repeated database queries | Redis Cache |
| Search engine downtime | PostgreSQL Fallback |
| Product discovery | Recommendation Engine |
| Search suggestions | Autocomplete |
| Monitoring | Health APIs |
| Search Analytics | Logging & Metrics |
| Multi-service setup | Docker Compose |

---

# 🐳 Running Locally

Clone repository

```bash
git clone https://github.com/RANGAM-JAGADESH/SearchX.git
```

Go into project

```bash
cd SearchX
```

Start containers

```bash
docker compose up --build
```

Open Swagger

```
http://localhost:8000/docs
```

---

# 📈 Future Enhancements

- JWT Authentication
- User Accounts
- Role-Based Access Control (RBAC)
- Vector Database Integration
- Semantic Search
- Hybrid Search (BM25 + Embeddings)
- AI Recommendation Engine
- RAG Integration
- Kubernetes Deployment
- CI/CD Pipeline
- Prometheus Monitoring
- Grafana Dashboards
- Rate Limiting
- API Gateway
- Distributed Search Clusters

---

# 📚 Key Concepts Demonstrated

- Backend Engineering
- REST API Design
- FastAPI Development
- Docker Containerization
- Full-Text Search
- Elasticsearch Indexing
- PostgreSQL Integration
- Redis Caching
- Recommendation Systems
- Search Analytics
- Health Monitoring
- Modular Project Architecture
- Production-Style Backend Development

---

# 🎓 Learning Outcomes

Through SearchX, I gained practical experience in:

- Designing scalable backend architectures
- Building REST APIs using FastAPI
- Working with Elasticsearch search indices
- Integrating PostgreSQL with SQLAlchemy
- Implementing Redis caching
- Managing multi-container applications using Docker Compose
- Creating modular and maintainable Python applications
- Monitoring backend services using health and metrics endpoints
- Developing search pipelines similar to those used in modern e-commerce systems

---

# 👨‍💻 Author

**Jagadesh Rangam**

B.Tech — Computer Science (Artificial Intelligence)

Backend Developer

**Skills**

- Python
- FastAPI
- Django
- PostgreSQL
- Elasticsearch
- Redis
- Docker
- SQLAlchemy
- REST APIs

GitHub:

https://github.com/RANGAM-JAGADESH

---

## ⭐ If you found this project useful, consider giving it a Star.
