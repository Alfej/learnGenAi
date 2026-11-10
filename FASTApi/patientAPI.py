from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = file.read()

    return data


@app.get("/")
def hello_world():
    return {"message": "Patient Management API is running!"}

@app.get("/about")
def about():
    return {"message": "Fully working FastAPI application for managing patient data."}

@app.get("/view_patients")
def view_patients():
    data = load_data()
    return {"patients": data}

@app.get("/view_patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve",example="1")):
    data = load_data()
    patients = json.loads(data)
    patient = next((p for p in patients if p["id"] == patient_id), None)

    if patient:
        return {"patient": patient}
    else:
        raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found.")

@app.get("/view_patient/sort")
def view_patient_sort(sort_by: str = Query(..., description="The field to sort patients by", example="name"), Order: str = Query(default="asc", description="The order of sorting (asc or desc)", example="asc")):
    valid_fields = ['name','height','weight','BMI']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}. Valid fields are: {', '.join(valid_fields)}")

    if Order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail=f"Invalid order: {Order}. Valid orders are: asc, desc")
    
    data = load_data()
    patients = json.loads(data)

    sorted_patients = sorted(patients, key=lambda x: x[sort_by], reverse=(Order == "desc"))
    
    return {"sorted_patients": sorted_patients}