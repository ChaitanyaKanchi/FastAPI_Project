from pydantic import BaseModel


# Pydantic models for data validation
class PatientData(BaseModel):
    id: int
    PatientsName: str
    Age: int
    Gender: str
    HealthIssue: str
    MobileNumber: int
    RoomNumber: int
    DoctorId: int



class DoctorData(BaseModel):
    id: int
    DoctorId: int
    DoctorName: str
    Specilization: str
    Department: str