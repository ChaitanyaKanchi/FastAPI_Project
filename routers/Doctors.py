from fastapi import Depends, status, HTTPException, APIRouter
import models
from sqlalchemy.orm import Session
from database import get_db
from schemas import DoctorData

router = APIRouter(
    tags = ["Doctors"]
)

# for adding doctors
@router.post("/Docters", status_code=status.HTTP_201_CREATED)
async def create_doctor(Doctor: DoctorData, db: Session = Depends(get_db)):
    db_doctors = models.Doctors(id=Doctor.id,DoctorId=Doctor.DoctorId, DoctorName=Doctor.DoctorName, Specilization=Doctor.Specilization, Department=Doctor.Department)
    db.add(db_doctors)
    db.commit()
    db.refresh(db_doctors) 
    return {"message": "Doctor created successfully", "user_id": db_doctors.id}

# to get all the doctors
@router.get("/Doctors/")
async def read_doctors(db: Session = Depends(get_db)):
    doctors = db.query(models.Doctors).all()
    return doctors


#to get specific doctors according to the doctor id
@router.get("/Doctors/{id}", status_code=status.HTTP_200_OK)
async def read_user(id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Doctors).filter(models.Doctors.id == id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return patient


# Update an existing doctor's details
@router.put("/Doctors/{id}", status_code=status.HTTP_200_OK, tags=["Doctors"])
async def update_doctor(id: int, updated_doctor: DoctorData, db: Session = Depends(get_db)):
    doctor = db.query(models.Doctors).filter(models.Doctors.id == id).first()
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    # Update the doctor's details
    doctor.DoctorId = updated_doctor.DoctorId
    doctor.DoctorName = updated_doctor.DoctorName
    doctor.Specilization = updated_doctor.Specilization
    doctor.Department = updated_doctor.Department
    
    db.commit()
    db.refresh(doctor)
    return {"message": "Doctor updated successfully", "user_id": doctor.id}

# Delete a doctor record
@router.delete("/Doctors/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Doctors"])
async def delete_doctor(id: int, db: Session = Depends(get_db)):
    doctor = db.query(models.Doctors).filter(models.Doctors.id == id).first()
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    db.delete(doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}
