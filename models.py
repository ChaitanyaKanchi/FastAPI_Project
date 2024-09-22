from sqlalchemy import Column, Boolean, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Patients(Base):
    __tablename__ = "Patients"

    id = Column(Integer, primary_key=True)
    PatientsName = Column(String, unique=True)
    Age = Column(Integer)
    Gender = Column(String)
    HealthIssue = Column(String)
    MobileNumber = Column(Integer)
    RoomNumber = Column(Integer)
    DoctorId = Column(Integer, ForeignKey("Doctors.DoctorId"))


    doctor = relationship("Doctors", back_populates="patients")


class Doctors(Base):
    __tablename__ = "Doctors"

    id = Column(Integer, primary_key=True)
    DoctorId = Column(Integer, unique=True, nullable=False)
    DoctorName = Column(String(50))
    Specilization = Column(String(100))
    Department = Column(String)


    patients = relationship("Patients", back_populates="doctor")



