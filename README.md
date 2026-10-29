# EWB Students CRUD Application

## Project Overview

A beginner-friendly Student Database Management System developed using Python, FastAPI, SQLAlchemy, and SQLite.

This application provides REST APIs to create, retrieve, update, and delete student records.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite
* Pydantic

## Features

* Add a new student
* View all students
* View a student by ID
* Update student information
* Delete a student
* Validate input data
* Prevent duplicate email addresses
* Return appropriate HTTP error responses

## Project Structure

```text
EWB_Internship/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
└── students.db
```

## Setup Instructions

### 1. Install Python

Install Python 3 and verify it:

```bash
python --version
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m uvicorn main:app --reload
```

### 6. Open API documentation

Visit:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| GET    | /                      | Welcome message   |
| POST   | /students              | Create a student  |
| GET    | /students              | List all students |
| GET    | /students/{student_id} | Get a student     |
| PATCH  | /students/{student_id} | Update a student  |
| DELETE | /students/{student_id} | Delete a student  |

## Database

The application uses SQLite. The database file is created automatically when the application starts.

## Learning Outcome

This project demonstrates basic REST API development, database integration, data validation, and CRUD operations using Python.

## Author

Mahesh Vasudeo Birari