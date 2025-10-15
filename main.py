import datetime
import random

from fastapi import FastAPI

app = FastAPI(title="Healthcare Management API", version="1.0.0")


# ===========================
# 🔧 UTILITY FUNCTIONS
# ===========================


def random_date(days=30):
    return (
        datetime.datetime.now() - datetime.timedelta(days=random.randint(0, days))
    ).strftime("%Y-%m-%d")


# ===========================
# 🏥 SQL SERVICE ENDPOINTS
# ===========================


@app.post("/query", operation_id="execute_custom_query")
async def custom_query():
    """Execute custom database query"""
    return {
        "query": "SELECT * FROM patients WHERE age > 40",
        "connection_id": "conn_12345",
        "rows": [
            {"patient_id": "P1001", "name": "Arjun Patel", "age": 45, "gender": "Male"},
            {
                "patient_id": "P1002",
                "name": "Meera Sharma",
                "age": 52,
                "gender": "Female",
            },
        ],
        "status": "success",
    }


@app.post("/patient", operation_id="get_patient_details")
async def patient_service():
    """Get patient details"""
    return {
        "patient_id": "P1001",
        "name": "Amit Verma",
        "dob": "1979-08-15",
        "gender": "Male",
        "blood_group": "O+",
        "contact": {"phone": "+91-9876543210", "email": "amit.verma@example.com"},
        "status": "active",
    }


@app.post("/medications", operation_id="get_patient_medications")
async def medication_service():
    """Get patient medications"""
    return {
        "patient_id": "P1001",
        "active_medications": [
            {"drug": "Metformin", "dosage": "500mg", "frequency": "Twice daily"},
            {"drug": "Amlodipine", "dosage": "5mg", "frequency": "Once daily"},
        ],
        "last_updated": random_date(10),
    }


@app.post("/followup", operation_id="get_patient_followup")
async def followup_service():
    """Get next followup details"""
    return {
        "patient_id": "P1001",
        "next_followup": (
            datetime.datetime.now() + datetime.timedelta(days=14)
        ).strftime("%Y-%m-%d"),
        "department": "Cardiology",
        "doctor": "Dr. Neha Singh",
        "remarks": "Monitor blood pressure daily and report any dizziness",
    }


@app.post("/conditions", operation_id="get_patient_medical_conditions")
async def condition_service():
    """Get patient medical conditions"""
    return {
        "patient_id": "P1001",
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


@app.post("/labs", operation_id="get_patient_lab_results")
async def lab_service():
    """Get lab test results"""
    return {
        "patient_id": "P1001",
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


@app.post("/procedures", operation_id="get_patient_procedures")
async def procedure_service():
    """Get patient procedures"""
    return {
        "patient_id": "P1001",
        "procedures": [
            {
                "name": "Angioplasty",
                "date": "2021-09-10",
                "performed_by": "Dr. Rajesh Mehta",
            },
            {"name": "ECG", "date": random_date(3), "performed_by": "Technician Ankit"},
        ],
    }


@app.post("/allergies", operation_id="get_patient_allergies")
async def allergy_service():
    """Get patient allergies"""
    return {
        "patient_id": "P1001",
        "allergies": [
            {"substance": "Penicillin", "reaction": "Rash", "severity": "Mild"},
            {"substance": "Peanuts", "reaction": "Anaphylaxis", "severity": "Severe"},
        ],
    }


@app.post("/appointments", operation_id="get_patient_appointments")
async def appointment_service():
    """Get patient appointments"""
    return {
        "patient_id": "P1001",
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


@app.post("/diet", operation_id="get_patient_diet_plan")
async def diet_service():
    """Get patient diet plan"""
    return {
        "patient_id": "P1001",
        "diet_plan": {
            "breakfast": "Oats with skimmed milk and almonds",
            "lunch": "Brown rice, dal, and mixed salad",
            "dinner": "Vegetable soup and multigrain roti",
        },
        "calories_per_day": 1800,
    }


@app.post("/dashboard", operation_id="get_patient_dashboard_overview")
async def patient_dashboard_service():
    """Get patient dashboard overview"""
    return {
        "patient_id": "P1001",
        "vitals": {"bp": "120/80", "pulse": 78, "bmi": 24.5},
        "active_conditions": ["Diabetes", "Hypertension"],
        "last_lab_result_date": random_date(7),
    }


# ===========================
# 🏥 EPIC SERVICE ENDPOINTS
# ===========================


@app.post("/observations", operation_id="get_patient_observations")
async def generate_patient_observ():
    """Get patient observations"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "observations": {
            "weight": "72 kg",
            "height": "175 cm",
            "blood_pressure": "122/78 mmHg",
            "temperature": "98.4°F",
        },
        "observation_date": random_date(5),
    }


@app.post("/medication-summary", operation_id="get_patient_medication_summary")
async def generate_medication():
    """Get medication summary"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "current": ["Metformin 500mg", "Amlodipine 5mg"],
        "past": ["Atorvastatin 10mg"],
        "last_reviewed": random_date(14),
    }


@app.post("/followup-summary", operation_id="get_patient_followup_summary")
async def generate_agent_Response_followup():
    """Get followup recommendations"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "next_followup": random_date(-10),
        "advice": "Continue medication as prescribed, monitor sugar levels, and maintain diet.",
    }


@app.post("/condition-summary", operation_id="get_patient_condition_summary")
async def generate_condition():
    """Get condition summary"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "conditions": ["Type 2 Diabetes", "Mild Hypertension"],
        "status": "stable",
    }


@app.post("/lab-summary", operation_id="get_patient_lab_summary")
async def generate_lab():
    """Get lab results summary"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "latest_results": {
            "HbA1c": "6.5%",
            "Cholesterol": "180 mg/dL",
            "Vitamin D": "28 ng/mL",
        },
        "date": random_date(5),
    }


@app.post("/procedure-summary", operation_id="get_patient_procedure_summary")
async def generate_procedure():
    """Get procedure summary"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "procedures": [
            {"name": "Echocardiogram", "date": "2023-12-01"},
            {"name": "ECG", "date": random_date(3)},
        ],
    }


@app.post("/allergy-summary", operation_id="get_patient_allergy_summary")
async def generate_allergy():
    """Get allergy summary"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "allergies": [
            {"allergen": "Dust", "reaction": "Cough"},
            {"allergen": "Pollen", "reaction": "Sneezing"},
        ],
    }


@app.post("/upcoming", operation_id="get_patient_upcoming_appointments")
async def generate_agent_Response_upcoming():
    """Get upcoming appointments"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "appointments": [
            {
                "date": random_date(-2),
                "department": "Cardiology",
                "doctor": "Dr. Alok Bansal",
            },
        ],
        "preparation": "Avoid heavy meals before tests.",
    }


@app.post("/nutrition", operation_id="get_patient_nutrition_recommendations")
async def generate_agent_Response_nutrition():
    """Get nutrition recommendations"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "nutrition_summary": "Balanced diet with reduced sodium and increased fiber.",
        "recommended_foods": ["Oats", "Broccoli", "Apple"],
    }


@app.post("/diet-data", operation_id="get_patient_diet_data")
async def get_diet_data():
    """Get diet breakdown"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "diet": {
            "carbs": "50%",
            "proteins": "25%",
            "fats": "25%",
            "restrictions": ["No sugar", "Low salt"],
        },
    }


@app.post("/risk", operation_id="get_patient_risk_assessment")
async def riskpanel():
    """Get risk assessment"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "risk_scores": {"cardiac": 0.35, "diabetes": 0.7, "stroke": 0.2},
        "overall_risk": "moderate",
    }


@app.post("/aftercare", operation_id="get_patient_aftercare_instructions")
async def aftercare():
    """Get aftercare instructions"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "instructions": [
            "Take medications on time.",
            "Avoid strenuous activity for 7 days.",
            "Report any chest discomfort immediately.",
        ],
    }


@app.post("/vitals", operation_id="get_patient_vitals")
async def get_patient_vitals():
    """Get patient vitals"""
    return {
        "organization": "Apollo Hospitals",
        "patient_id": "P1001",
        "vitals": {"bp": "118/78 mmHg", "pulse": 76, "temp": "98.6°F", "spo2": "98%"},
        "recorded_at": random_date(1),
    }


# ===========================
# 🚀 RUN APPLICATION
# ===========================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
