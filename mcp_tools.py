from fastmcp import FastMCP
from tools.diagnosis_tools import get_diagnosis
from tools.symptom_extractor import extract_symptoms
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text

mcp = FastMCP("medical diagnosis custom mcp")

@mcp.tool()
def full_medical_analysis(symptom_text):
    """
    Analyzes symptoms, provides diagnosis, and finds relevant medical research.
    
    Args:
        symptom_text: A text description of the patient's symptoms
        
    Returns:
        A dictionary with symptoms, diagnosis, and PubMed summary
    """
    symptoms = extract_symptoms(symptom_text)
    diagnosis = get_diagnosis(symptoms)
    pubmed_raw = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
    summary = summarize_text(pubmed_raw)
    
    return {
        "symptoms": symptoms,
        "diagnosis": diagnosis,
        "pubmed_summary": summary
    }

if __name__ == "__main__":
    mcp.run()