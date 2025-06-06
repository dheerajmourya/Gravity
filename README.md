# Django REST API: Customer Management with JWT & PostgreSQL

##  Objective

A secure and RESTful Django API to manage customers. It supports JWT-based authentication and PostgreSQL integration, allowing users to register, log in, and perform full CRUD operations on customer data.

---

## Features

- JWT Authentication (`djangorestframework-simplejwt`)
- User Registration/Login
- Customer CRUD: Create, Retrieve, Update, Delete
- PostgreSQL Database
- Pagination & Search (by name/email)
- Proper validation and custom response format
- Environment config via `.env`

---

## 🛠 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- SimpleJWT
- python-decouple
- Postman (for testing)

---

## Project Structure

project/
├── customers/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│
├── users/
│ ├── views.py
│ ├── serializers.py
│
├── project/
│ ├── settings.py
│ ├── urls.py
│
├── utils/
│ └── response.py
│
├── .env.example
├── requirements.txt
├── README.md


## Setup Instructions
1. Clone the Repository
git clone https://github.com/dheerajmourya/Gravity.git
cd customer-api

2. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Setup .env
Create a .env file based on the .env.example:
DB_NAME=customer_api
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret
DEBUG=True

4. Create PostgreSQL DB
Make sure PostgreSQL is installed and running. Then create a database named:
customer_api

5. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Run the Server
python manage.py runserver

## JWT Authentication Flow
Action              Endpoint              Method
Register            /api/register/        POST
Get Token           /api/token/           POST
Refresh Token       /api/token/refresh/   POST

## Add this in headers for protected routes:
Authorization: Bearer <access_token>

## Customer APIs (Protected)
Action           Endpoint                     Method
List All         /api/customers/              GET
Get One          /api/customers/<id>/         GET
Create           /api/customers/              POST
Update           /api/customers/<id>/         PUT
Delete           /api/customers/<id>/         DELETE

## Search & Pagination
Search by name/email:  /api/customers/?search=John
Pagination:            /api/customers/?page=2

## Postman Collection
Import the CustomerAPI.postman_collection.json in Postman for quick testing.

## Environment Example File
.env.example
DB_NAME=customer_api
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
