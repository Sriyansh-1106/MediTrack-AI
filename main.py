from fastapi import FastAPI
from app.models import PatientProfile


app = FastAPI(
    title="MediTrack-AI",
    description="Personal medical history–aware recommendation system",
    version="0.1.0"
)
patient_store = {}


@app.get("/")
def root():
    return {"message": "MediTrack-AI backend is running"}
@app.post("/patient")
def save_patient(profile: PatientProfile):
    patient_store["current"] = profile
    return {
        "message": "Patient profile saved successfully",
        "patient": profile
    }
