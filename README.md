# Hospital Management System

This is a backend system built using **FastAPI** and **SQLAlchemy** for managing hospital data, including patients and doctors. The system allows CRUD operations on patient and doctor records, such as creating, updating, reading, and deleting information. It uses a RESTful API for communication.

## Features

- **Patient Management**
  - Add a new patient record.
  - Retrieve all patients.
  - Retrieve a specific patient by their ID.
  - Update patient details.
  - Delete patient records.
  
- **Doctor Management**
  - Add a new doctor record.
  - Retrieve all doctors.
  - Retrieve a specific doctor by their ID.
  - Update doctor details.
  - Delete doctor records.
  
## Endpoints

### Patients

- `POST /Patients/` - Add a new patient
- `GET /Patients/` - Retrieve all patients
- `GET /Patients/{id}` - Retrieve a specific patient by ID
- `PUT /Patients/{id}` - Update a patient record by ID
- `DELETE /Patients/{id}` - Delete a patient record by ID

### Doctors

- `POST /Doctors/` - Add a new doctor
- `GET /Doctors/` - Retrieve all doctors
- `GET /Doctors/{id}` - Retrieve a specific doctor by ID
- `PUT /Doctors/{id}` - Update a doctor record by ID
- `DELETE /Doctors/{id}` - Delete a doctor record by ID

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ChaitanyaKanchi/FastAPI_Project
   cd FastAPI_Project

2. Setup Environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
  
3. Run the Application
   ```bash
   uvicorn app:app --reload
