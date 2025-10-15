from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import datetime
import random

app = FastAPI(title="Healthcare Management API", version="1.0.0")


# ===========================
# 🔧 UTILITY FUNCTIONS
# ===========================

def random_date(days=30):
    return (
        datetime.datetime.now() - datetime.timedelta(days=random.randint(0, days))
    ).strftime("%Y-%m-%d")


# ===========================
# 📋 REQUEST MODELS
# ===========================

class CustomQueryRequest(BaseModel):
    connection_id: str
    user_query: str


class PatientRequest(BaseModel):
    patient_id: str
    connection_id: str


class EpicRequest(BaseModel):
    patient_id: str
    organization: str


# ===========================
# 🏥 SQL SERVICE ENDPOINTS
# ===========================

@app.post("/query")
async def custom_query(request: CustomQueryRequest):
    """Execute custom database query"""
    return {
        "query": request.user_query,
        "connection_id": request.connection_id,
        "rows": [
            {"patient_id": "P1001", "name": "Arjun Patel", "age": 45, "gender": "Male"},
            {"patient_id": "P1002", "name": "Meera Sharma", "age": 52, "gender": "Female"},
        ],
        "status": "success",
    }


@app.post("/patient")
async def patient_service(request: PatientRequest):
    """Get patient details"""
    return {
        "patient_id": request.patient_id,
        "name": "Amit Verma",
        "dob": "1979-08-15",
        "gender": "Male",
        "blood_group": "O+",
        "contact": {"phone": "+91-9876543210", "email": "amit.verma@example.com"},
        "status": "active",
    }


@app.post("/medications")
async def medication_service(request: PatientRequest):
    """Get patient medications"""
    return {
        "patient_id": request.patient_id,
        "active_medications": [
            {"drug": "Metformin", "dosage": "500mg", "frequency": "Twice daily"},
            {"drug": "Amlodipine", "dosage": "5mg", "frequency": "Once daily"},
        ],
        "last_updated": random_date(10),
    }


@app.post("/followup")
async def followup_service(request: PatientRequest):
    """Get next followup details"""
    return {
        "patient_id": request.patient_id,
        "next_followup": (
            datetime.datetime.now() + datetime.timedelta(days=14)
        ).strftime("%Y-%m-%d"),
        "department": "Cardiology",
        "doctor": "Dr. Neha Singh",
        "remarks": "Monitor blood pressure daily and report any dizziness",
    }


@app.post("/conditions")
async def condition_service(request: PatientRequest):
    """Get patient medical conditions"""
    return {
        "patient_id": request.patient_id,
        "diagnoses": [
            {
                "condition": "Type 2 Diabetes Mellitus",
                "diagnosed_on": "2016-05-10",
                "status": "chronic",
            },
            {
                "condition": "Hypertension",
                "diagnosed_on": "2018-03-21",
                "status": "controlled",
            },
        ],
    }


@app.post("/labs")
async def lab_service(request: PatientRequest):
    """Get lab test results"""
    return {
        "patient_id": request.patient_id,
        "lab_results": [
            {
                "test": "HbA1c",
                "result": "6.8%",
                "reference_range": "< 7%",
                "date": random_date(15),
            },
            {
                "test": "Cholesterol",
                "result": "190 mg/dL",
                "reference_range": "< 200 mg/dL",
                "date": random_date(10),
            },
        ],
    }


@app.post("/procedures")
async def procedure_service(request: PatientRequest):
    """Get patient procedures"""
    return {
        "patient_id": request.patient_id,
        "procedures": [
            {
                "name": "Angioplasty",
                "date": "2021-09-10",
                "performed_by": "Dr. Rajesh Mehta",
            },
            {"name": "ECG", "date": random_date(3), "performed_by": "Technician Ankit"},
        ],
    }


@app.post("/allergies")
async def allergy_service(request: PatientRequest):
    """Get patient allergies"""
    return {
        "patient_id": request.patient_id,
        "allergies": [
            {"substance": "Penicillin", "reaction": "Rash", "severity": "Mild"},
            {"substance": "Peanuts", "reaction": "Anaphylaxis", "severity": "Severe"},
        ],
    }


@app.post("/appointments")
async def appointment_service(request: PatientRequest):
    """Get patient appointments"""
    return {
        "patient_id": request.patient_id,
        "appointments": [
            {
                "date": random_date(-5),
                "doctor": "Dr. Alok Bansal",
                "department": "Endocrinology",
            },
            {
                "date": random_date(15),
                "doctor": "Dr. Neha Singh",
                "department": "Cardiology",
            },
        ],
    }


@app.post("/diet")
async def diet_service(request: PatientRequest):
    """Get patient diet plan"""
    return {
        "patient_id": request.patient_id,
        "diet_plan": {
            "breakfast": "Oats with skimmed milk and almonds",
            "lunch": "Brown rice, dal, and mixed salad",
            "dinner": "Vegetable soup and multigrain roti",
        },
        "calories_per_day": 1800,
    }


@app.post("/dashboard")
async def patient_dashboard_service(request: PatientRequest):
    """Get patient dashboard overview"""
    return {
        "patient_id": request.patient_id,
        "vitals": {"bp": "120/80", "pulse": 78, "bmi": 24.5},
        "active_conditions": ["Diabetes", "Hypertension"],
        "last_lab_result_date": random_date(7),
    }


# ===========================
# 🏥 EPIC SERVICE ENDPOINTS
# ===========================

@app.post("/observations")
async def generate_patient_observ(request: EpicRequest):
    """Get patient observations"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "observations": {
            "weight": "72 kg",
            "height": "175 cm",
            "blood_pressure": "122/78 mmHg",
            "temperature": "98.4°F",
        },
        "observation_date": random_date(5),
    }


@app.post("/medication-summary")
async def generate_medication(request: EpicRequest):
    """Get medication summary"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "current": ["Metformin 500mg", "Amlodipine 5mg"],
        "past": ["Atorvastatin 10mg"],
        "last_reviewed": random_date(14),
    }


@app.post("/followup-summary")
async def generate_agent_Response_followup(request: EpicRequest):
    """Get followup recommendations"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "next_followup": random_date(-10),
        "advice": "Continue medication as prescribed, monitor sugar levels, and maintain diet.",
    }


@app.post("/condition-summary")
async def generate_condition(request: EpicRequest):
    """Get condition summary"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "conditions": ["Type 2 Diabetes", "Mild Hypertension"],
        "status": "stable",
    }


@app.post("/lab-summary")
async def generate_lab(request: EpicRequest):
    """Get lab results summary"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "latest_results": {
            "HbA1c": "6.5%",
            "Cholesterol": "180 mg/dL",
            "Vitamin D": "28 ng/mL",
        },
        "date": random_date(5),
    }


@app.post("/procedure-summary")
async def generate_procedure(request: EpicRequest):
    """Get procedure summary"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "procedures": [
            {"name": "Echocardiogram", "date": "2023-12-01"},
            {"name": "ECG", "date": random_date(3)},
        ],
    }


@app.post("/allergy-summary")
async def generate_allergy(request: EpicRequest):
    """Get allergy summary"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "allergies": [
            {"allergen": "Dust", "reaction": "Cough"},
            {"allergen": "Pollen", "reaction": "Sneezing"},
        ],
    }


@app.post("/upcoming")
async def generate_agent_Response_upcoming(request: EpicRequest):
    """Get upcoming appointments"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "appointments": [
            {
                "date": random_date(-2),
                "department": "Cardiology",
                "doctor": "Dr. Alok Bansal",
            },
        ],
        "preparation": "Avoid heavy meals before tests.",
    }


@app.post("/nutrition")
async def generate_agent_Response_nutrition(request: EpicRequest):
    """Get nutrition recommendations"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "nutrition_summary": "Balanced diet with reduced sodium and increased fiber.",
        "recommended_foods": ["Oats", "Broccoli", "Apple"],
    }


@app.post("/diet-data")
async def get_diet_data(request: EpicRequest):
    """Get diet breakdown"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "diet": {
            "carbs": "50%",
            "proteins": "25%",
            "fats": "25%",
            "restrictions": ["No sugar", "Low salt"],
        },
    }


@app.post("/risk")
async def riskpanel(request: EpicRequest):
    """Get risk assessment"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "risk_scores": {"cardiac": 0.35, "diabetes": 0.7, "stroke": 0.2},
        "overall_risk": "moderate",
    }


@app.post("/aftercare")
async def aftercare(request: EpicRequest):
    """Get aftercare instructions"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "instructions": [
            "Take medications on time.",
            "Avoid strenuous activity for 7 days.",
            "Report any chest discomfort immediately.",
        ],
    }


@app.post("/vitals")
async def get_patient_vitals(request: EpicRequest):
    """Get patient vitals"""
    return {
        "organization": request.organization,
        "patient_id": request.patient_id,
        "vitals": {"bp": "118/78 mmHg", "pulse": 76, "temp": "98.6°F", "spo2": "98%"},
        "recorded_at": random_date(1),
    }


# ===========================
# 🏥 HEALTH CHECK
# ===========================

@app.get("/")
async def root():
    """API information"""
    return {
        "message": "Healthcare Management API",
        "version": "1.0.0",
        "documentation": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}


# ===========================
# 🚀 RUN APPLICATION
# ===========================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)