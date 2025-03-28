# Django REST API for Patient & Doctor Management  

This project is a **Django REST Framework (DRF) API** for managing patients, doctors, and their assignments.  
It uses **JWT authentication** for security and **PostgreSQL** as the database.  

##  Features  
- **User Authentication**: Register/Login with JWT tokens  
- **Manage Patients**: Create, update, delete, and list patients  
- **Manage Doctors**: Create, update, delete, and list doctors  
- **Assign Doctors to Patients**: Link patients to doctors  
- **Role-based access**: Only authenticated users can access the system  

---

## Tech Stack  
- **Backend**: Django, Django REST Framework (DRF)  
- **Authentication**: JWT (`djangorestframework-simplejwt`)  
- **Database**: PostgreSQL  
- **ORM**: Django ORM  
- **Environment Variables**: `python-dotenv`  

---

##  Setup & Installation  

### 1️ Clone the Repository  
```sh
git clone https://github.com/rishisni/HealthCare 
cd healthcare

### 2 Create a Virtual Environment
python -m venv venv  
source venv/bin/activate   # On macOS/Linux  
venv\Scripts\activate      # On Windows 

### 3 Install Dependencies
pip install -r requirements.txt  

### 4 Set Up Environment Variables (.env)
DB_NAME=datbase_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=database_host
DB_PORT=database_port

### 5 Apply Migrations
python manage.py makemigrations  
python manage.py migrate  


### 6 Create a Superuser
python manage.py createsuperuser  (Follow the prompts to enter email, name, password, etc.)


### 7 Run the Development Server 
python manage.py runserver  



---
Authentication (JWT)

