from fastapi import Depends, status, HTTPException, APIRouter
import models
from sqlalchemy.orm import Session
from database import get_db
from schemas import PatientData

router = APIRouter(
    tags = ["Patients"]
)

# for adding patients
@router.post("/Patients/", status_code=status.HTTP_201_CREATED)
async def create_patient(Patient: PatientData, db: Session = Depends(get_db)):
    db_patients = models.Patients(PatientsName=Patient.PatientsName, Age=Patient.Age, Gender=Patient.Gender, HealthIssue=Patient.HealthIssue, MobileNumber=Patient.MobileNumber, RoomNumber=Patient.RoomNumber, DoctorId=Patient.DoctorId)
    db.add(db_patients)
    db.commit()
    db.refresh(db_patients) 
    return {"message": "Patient created successfully", "user_id": db_patients.id}


# to get the all patients 
@router.get("/Patients/")
async def read_patients(db: Session = Depends(get_db)):
    patients = db.query(models.Patients).all()
    return patients


# to get specific patients according with the id
@router.get("/Patients/{id}", status_code=status.HTTP_200_OK)
async def read_user(id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patients).filter(models.Patients.id == id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient



# Update an existing patient's details
@router.put("/Patients/{id}", status_code=status.HTTP_200_OK)
async def update_patient(id: int, updated_patient: PatientData, db: Session = Depends(get_db)):
    patient = db.query(models.Patients).filter(models.Patients.id == id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Update the patient's details
    patient.PatientsName = updated_patient.PatientsName
    patient.Age = updated_patient.Age
    patient.Gender = updated_patient.Gender
    patient.HealthIssue = updated_patient.HealthIssue
    patient.MobileNumber = updated_patient.MobileNumber
    patient.RoomNumber = updated_patient.RoomNumber
    patient.DoctorId = updated_patient.DoctorId
    
    db.commit()
    db.refresh(patient)
    return {"message": "Patient updated successfully", "user_id": patient.id}

# Delete a patient record
@router.delete("/Patients/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patients).filter(models.Patients.id == id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db.delete(patient)
    db.commit()
    return {"message": "Patient deleted successfully"}




