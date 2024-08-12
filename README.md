# Django Django Backend Project

## Project Overview
<p>
  This Django backend project provides an API for interacting with a database using the Django REST framework. It supports creating, reading, updating, and deleting (CRUD) operations through the API and offers an admin panel for managing the database.
</p>


### Features
Django REST Framework: Enables API creation for data handling. <br />
Data Handling: Supports data input, retrieval, and management from a frontend application. <br />
Admin Panel: Provides an interface for managing database records directly. <br />
Installation
Follow these steps to set up the project on your local machine:

### Clone the Repository:
git clone [https://[(https://github.com/rolandiartmeladze/PortfolioBackend.git)]](https://github.com/rolandiartmeladze/PortfolioBackend.git) <br />
cd PortfolioBackend<br />

##Create and Activate Virtual Environment:

python -m venv env <br /> 
source env/bin/activate  

# Install Dependencies:

pip install -r requirements.txt

## Set Up the Database:

### Run the following commands to apply migrations:

python manage.py migrate <br />

### If necessary, create a superuser for the admin panel:

python manage.py createsuperuser

## Run the Development Server:

python manage.py runserver <br />
The server will be available at http://127.0.0.1:8000/.

## API Endpoints
### The project provides the following REST API endpoints:

GET/POST /api/posts/: Retrieve a list of all records. <br />
POST/GET /api/comments//: Create a new record. <br />
GET /admin/: Retrieve a specific record by its ID. user: admin  Pass:admin <br />

## Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ to manage the database using the credentials you set up earlier.

# Deployment
Instructions for deploying the project to a production environment, such as setting up on Vercel, will go here.

# Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

# License
This project is open-source and available under the MIT License.
