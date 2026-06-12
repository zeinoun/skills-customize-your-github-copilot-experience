# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework to learn request handling, data validation with Pydantic, and running a development server.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description

Implement a basic REST API that exposes endpoints to create, list, retrieve, and delete simple resources (items).

#### Requirements
Completed program should:

- Provide endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `DELETE /items/{id}`
- Validate request bodies using Pydantic models
- Use an in-memory list or dict to store items (persistence not required)
- Return appropriate HTTP status codes for success and errors

Example request (create):

```
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name":"apple","price":1.25}'
```

Example response:

```
{ "id": 1, "name": "apple", "price": 1.25 }
```

### 🛠️ Validation & Developer Experience

#### Description

Add input validation and document how to run and test the API locally.

#### Requirements
Completed program should:

- Use Pydantic models for request/response schemas
- Provide clear run instructions using `uvicorn`
- Include example curl requests for each endpoint

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

Open the automatic docs at `http://localhost:8000/docs` to explore the API.

---

## Learning Outcomes

- Understand routing and HTTP methods in FastAPI
- Validate data using Pydantic models
- Run a local development server and use interactive OpenAPI docs
