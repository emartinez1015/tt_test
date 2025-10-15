
# 🧩 Project Management API

A lightweight **FastAPI** application for managing **projects** and their associated **taunsks**.  
It allows you to create, update, and delete projects, and manage tasks under each project — all through a clean and efficient REST API.

---

## 🚀 Features

- Create, update, and delete **projects**
- Add and manage **tasks** within projects
- Async database operations with **SQLAlchemy (async engine)**
- Clean architecture with routers, CRUD modules, and schemas
- Designed for scalability and easy testing

---

## 🧠 Tech Stack

- **Python 3.9+**
- **FastAPI**
- **SQLAlchemy (Async ORM)**
- **PostgreSQL**
- **Uvicorn** for development server

---

## ⚙️ Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/emartinez1015/tt_test.git
cd tt_test
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

The app requires an API key for security middleware.
You can set it via the environment variable `API_KEY`.

For example:

#### On macOS/Linux:

```bash
export API_KEY="your-secret-key"
```

#### On Windows (PowerShell):

```bash
$env:API_KEY="your-secret-key"
```

If no value is provided, the app defaults to:

```text
API_KEY=dev-secret-key
```

*(recommended only for local development/testing)*

---

## 🏃 Run the Application

### Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

The app will start at:

```
http://127.0.0.1:8000
```
## Run with Docker Compose

This project can also be run using Docker Compose:

Make sure you have Docker and Docker Compose installed.

```
docker-compose up -d --build

http://127.0.0.1:8000
```

### API Documentation

Once the server is running, access the interactive API docs at:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧩 Example Endpoints

| Method   | Endpoint                        | Description                  |
| -------- | ------------------------------- | ---------------------------- |
| `POST`   | `/projects/`                    | Create a new project         |
| `GET`    | `/projects/{project_id}`        | Retrieve project details     |
| `PUT`    | `/projects/{project_id}`        | Update a project             |
| `DELETE` | `/projects/{project_id}`        | Delete a project             |
| `POST`   | `/projects/{project_id}/tasks/` | Add a task to a project      |
| `GET`    | `/projects/{project_id}/tasks/` | List all tasks for a project |
| `PUT`    | `/tasks/{task_id}`              | Update a task                |
| `DELETE` | `/tasks/{task_id}`              | Delete a task                |

---

## 🧱 Project Structure

```
app/
├── api/
│   ├── crud/
│   │   ├── projects.py
│   │   └── tasks.py
│   ├── routers/
│   │   ├── projects.py
│   │   └── tasks.py
│   ├── schemas/
│   │   ├── project.py
│   │   └── task.py
│   └── deps.py
├── core/
│   ├── config.py
│   └── security.py
├── db/
│   ├── base.py
│   ├── models/
│   │   ├── project.py
│   │   └── task.py
│   └── session.py
└── main.py

```

---

## 🧰 Example Usage (with `curl`)

Create a new project:

```bash
curl -X POST "http://127.0.0.1:8000/projects/" \
-H "Content-Type: application/json" \
-H "X-API-KEY: dev-secret-key" \
-d '{"name": "My First Project", "description": "A demo project"}'
```

Create a task under a project:

```bash
curl -X POST "http://127.0.0.1:8000/projects/1/tasks/" \
-H "Content-Type: application/json" \
-H "X-API-KEY: dev-secret-key" \
-d '{"title": "First task", "priority": "1"}'
```

---

## 💡 Notes

* The app automatically creates tables if they don’t exist.
* Use `dev-secret-key` only for **local development**.
* For production, always set a secure `API_KEY`.

---

## 📄 License
```
This project is licensed under the MIT License.

```