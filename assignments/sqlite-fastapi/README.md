# 📘 Assignment: SQLite-backed FastAPI REST API

## 🎯 Objective

Build a RESTful API using FastAPI and SQLite so students can practice database persistence, routing, and data validation.

## 📝 Tasks

### 🛠️ Create a database-backed API

#### Description

Implement a FastAPI app that stores items in a SQLite database and exposes standard CRUD endpoints.

#### Requirements
Completed program should:

- Create a SQLite database table for items
- Provide endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Use Pydantic models to validate request and response data
- Return correct HTTP status codes and clear error messages

Example request (create):

```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"notebook","price":4.50}'
```

Example response:

```json
{ "id": 1, "name": "notebook", "price": 4.5 }
```

### 🛠️ Validate input and run locally

#### Description

Add input validation and instructions for running the API on a local development server.

#### Requirements
Completed program should:

- Define request and response schemas using Pydantic models
- Initialize and use SQLite for persistent storage
- Provide clear setup and run instructions with `uvicorn`
- Include example curl commands for each endpoint

---

## Run Locally

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the server:

```bash
uvicorn starter_code:app --reload
```

3. Open the docs at `http://localhost:8000/docs` to explore the API.

---

## Learning Outcomes

- Build REST routes with FastAPI and SQLite
- Persist data using a relational database
- Validate request payloads with Pydantic
- Use interactive OpenAPI docs for API testing
