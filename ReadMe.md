Employee Management API Documentation
Introduction
This API allows for managing employee records, including the ability to retrieve, create, update, and delete employees. It also provides endpoints for searching employees by name, province, department, and function.

Installation
Prerequisites
Python 3.6 or higher
Django 3.x or higher
PostgreSQL or any database supported by Django
pip (Python package installer)
Step-by-Step Installation
Clone the repository:

bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
pip install -r requirements.txt
Set up the database:

Update your settings.py file with your database configuration.

Run migrations:

bash
python manage.py migrate
Create a superuser (optional):

bash
python manage.py createsuperuser
Run the server:

bash
python manage.py runserver
Your API should now be running at http://127.0.0.1:8000/.

API Endpoints

1. Get All Employees
   Endpoint: /api/
   Method: GET
   Response:
   json
   Copier le code
   [
   {
   "id": 1,
   "name": "Doe",
   "first_name": "John",
   "function": "Manager",
   "department": "Finance",
   "province": "Ontario",
   "age": 30,
   "matricule": "12345",
   "address": "123 Main St"
   },
   ...
   ]
2. Get Employee by ID
   Endpoint: /api/<int:id>/
   Method: GET
   Response:
   json
   Copier le code
   {
   "id": 1,
   "name": "Doe",
   "first_name": "John",
   "function": "Manager",
   "department": "Finance",
   "province": "Ontario",
   "age": 30,
   "matricule": "12345",
   "address": "123 Main St"
   }
3. Create Employee
   Endpoint: /api/create/
   Method: POST
   Request Body:
   json
   Copier le code
   {
   "name": "Doe",
   "first_name": "John",
   "function": "Manager",
   "department": "Finance",
   "province": "Ontario",
   "age": 30,
   "matricule": "12345",
   "address": "123 Main St"
   }
   Response:
   json
   Copier le code
   {
   "id": 1,
   "message": "Employee created successfully"
   }
4. Update Employee
   Endpoint: /api/update/<int:id>/
   Method: PUT
   Request Body:
   json
   Copier le code
   {
   "name": "Smith",
   "first_name": "John"
   }
   Response:
   json
   Copier le code
   {
   "message": "Employee updated successfully"
   }
5. Delete Employee
   Endpoint: /api/delete/<int:id>/
   Method: DELETE
   Response:
   json
   Copier le code
   {
   "message": "Employee deleted successfully"
   }
6. Search Employee by Name
   Endpoint: /api/search/name/?name=<string:name>
   Method: GET
   Response:
   json
   Copier le code
   [
   {
   "id": 1,
   "name": "Doe",
   "first_name": "John",
   ...
   },
   ...
   ]
7. Search Employee by Province
   Endpoint: /api/search/province/?province=<string:province>
   Method: GET
   Response:
   json
   Copier le code
   [
   {
   "id": 1,
   "name": "Doe",
   "first_name": "John",
   ...
   },
   ...
   ]
8. Search Employee by Department
   Endpoint: /api/search/departement/?department=<string:department>
   Method: GET
   Response:
   json
   Copier le code
   [
   {
   "id": 1,
   "name": "Doe",
   "first_name": "John",
   ...
   },
   ...
   ]
9. Search Employee by Function
   Endpoint: /api/search/fonction/?function=<string:function>
   Method: GET
   Response:
   json
   Copier le code
   [
   {
   "id": 1,
   "name": "Doe",
   "first_name": "John",
   ...
   },
   ...
   ]
