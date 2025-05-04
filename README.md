Student Portal

## Description

This project is an API for managing student records. It allows users to create, read, update, and delete student information, using FastAPI and MySQL as the backend.

# Setup Instructions

# 1. Clone the repository:
git clone https://github.com/your-username/student-portal-api.git

# set up your environment
cd student-portal-api
python -m venv venv
source venv/Scripts/activate  # On Windows
pip install -r requirements.txt

# Set up MYSQL Database
mysql -u root -p < database.sql

# Run the FastAPI Application
uvicorn main:app --reload
