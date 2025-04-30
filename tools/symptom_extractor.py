import re

def extract_symptoms(text: str) -> list[str]:
    common_symptoms = [
        # Original symptoms
        "headache", "fever", "nausea", "fatigue", "pain",
        # Additional common symptoms
        "cough", "sore throat", "shortness of breath", "dizziness", "vomiting", 
        "diarrhea", "chills", "rash", "congestion", "runny nose", "chest pain", 
        "back pain", "abdominal pain", "muscle ache", "joint pain", "insomnia", 
        "anxiety", "depression", "loss of appetite", "weight loss", "sweating"
    ]
    
    # Create a regex pattern for all symptoms
    pattern = r"\b(" + "|".join(common_symptoms) + r")\b"
    
    # Find all symptoms mentioned in the text
    symptoms = re.findall(pattern, text.lower())
    
    # Remove duplicates by converting to set and back to list
    return list(set(symptoms))