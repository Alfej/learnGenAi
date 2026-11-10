from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Patient Management API is running!"}

@app.get("/about")
def about():
    return {"message": "Fully working FastAPI application for managing patient data."}
