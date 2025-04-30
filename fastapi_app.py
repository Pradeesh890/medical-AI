from fastapi import FastAPI
from pydantic import BaseModel
from tools.diagnosis_tools import get_diagnosis
from tools.symptom_extractor import extract_symptoms
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text
import uvicorn

app = FastAPI(
    title="Medical AI API",
    description="API for medical diagnosis and PubMed article retrieval",
    version="1.0.0"
)

class SymptomInput(BaseModel):
    description: str

@app.post("/diagnosis")
def diagnose_patient(data: SymptomInput):
    symptoms = extract_symptoms(data.description)
    diagnosis = get_diagnosis(symptoms)
    pubmed_raw = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
    summary = summarize_text(pubmed_raw)

    return {
        "symptoms": symptoms,
        "diagnosis": diagnosis,
        "pubmed_summary": summary
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical AI API. Use /diagnosis endpoint with a POST request."}

if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8000, reload=True)