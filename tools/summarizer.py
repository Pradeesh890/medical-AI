import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def summarize_text(articles_data) -> str:
    """
    Summarizes medical articles data.
    
    Args:
        articles_data: Either a list of article dictionaries or a string to summarize
    
    Returns:
        A summarized text about the medical information
    """
    # Handle input that's already a string
    if isinstance(articles_data, str):
        text_to_summarize = articles_data
    
    # Handle list of article dictionaries
    elif isinstance(articles_data, list) and len(articles_data) > 0:
        # Format the articles data into a coherent text
        formatted_articles = []
        
        for article in articles_data:
            if not isinstance(article, dict):
                continue
                
            title = article.get("title", "No title")
            abstract = article.get("abstract", "No abstract")
            authors = ", ".join(article.get("authors", ["Unknown authors"]))
            
            formatted_article = f"TITLE: {title}\nAUTHORS: {authors}\nABSTRACT: {abstract}\n"
            formatted_articles.append(formatted_article)
            
        text_to_summarize = "\n\n".join(formatted_articles)
    else:
        return "Error: Invalid input format for summarization"
    
    # Truncate to avoid token limits
    if len(text_to_summarize) > 4000:
        text_to_summarize = text_to_summarize[:4000] + "..."
    
    prompt = f"Summarize the following medical information into a concise summary highlighting key medical findings:\n\n{text_to_summarize}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [
            {"role": "system", "content": "You are a medical research summarizer"},
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error during summarization: {e}")
        return f"Error generating summary: {str(e)}"
