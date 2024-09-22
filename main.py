from fastapi import FastAPI
from routers import Doctors, Patients
from database import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(Doctors.router)

app.include_router(Patients.router)

