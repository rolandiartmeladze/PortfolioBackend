# Django Django Backend Project

## Project Overview
<p>

  This repository contains the backend API for a personal portfolio and blog application. It is built using **Django** and **Django REST Framework**, providing endpoints for managing blog posts, comments, and user interactions.
</p>


## Features

- **CRUD Operations**: Create, Read, Update, and Delete blog posts and comments.
- **Django Admin Panel**: Manage posts and comments through a user-friendly interface.
- **REST API**: Provides endpoints for frontend to interact with the database.
- **User Authentication**: Optional feature for managing post and comment creation.

## Technologies Used

- **Python**: The programming language used for backend logic.
- **Django**: A high-level Python web framework for rapid development.
- **Django REST Framework**: For creating RESTful APIs to serve the frontend.
- **SQLite**: Local development database (can be switched to PostgreSQL for production).


### Prerequisites

- **Python 3.x**: Download from [https://www.python.org/](https://www.python.org/)
- **pip**: Python package installer, installed with Python.
  


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
