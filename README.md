# Medical Diagnosis AI Tool

This project develops a custom Medical Diagnosis Tool designed to assist in preliminary medical assessments by leveraging AI for symptom extraction, diagnosis generation, and medical article summarization. It's built to expose its functionality as a Model Context Protocol (MCP) tool, making it accessible for integration with various platforms.

---

## Features

- **Symptom Extraction**: Automatically identifies and pulls out key symptoms from patient descriptions.
- **AI-Powered Diagnosis**: Provides a potential medical diagnosis based on extracted symptoms, powered by a sophisticated AI model.
- **PubMed Article Fetching**: Searches for and retrieves relevant medical articles from PubMed based on symptoms.
- **AI-Powered Article Summarization**: Summarizes fetched medical articles concisely using Llama 4 Maverick via the OpenRouter API.
- **MCP Tool**: Exposes the entire functionality as an MCP tool for seamless integration into cloud environments or other compatible platforms.

---

## Project Structure

```
medical-diagnosis-ai-mcp/
├── .env                    # Environment file for API keys
├── .gitignore              # Git ignore file
├── fastAPI_app.py          # Local FastAPI application for testing individual tools
├── mcp_tools.py            # Defines and exposes the MCP tool
├── pyproject.toml          # Project configuration file (managed by uv)
└── tools/
    ├── __init__.py
    ├── diagnosis_tools.py     # Handles AI diagnosis generation
    ├── pubmed_fetcher.py      # Fetches articles from PubMed
    ├── summarizer.py          # Summarizes text using AI (Llama 4 Maverick)
    └── symptom_extractor.py   # Extracts symptoms from text
```

---

## Technologies Used

- Python 3.x  
- FastAPI – For building the local testing API.  
- FastMCP – For converting the tool into an MCP-compatible service.  
- OpenRouter API – For accessing the Llama 4 Maverick AI model for summarization.  
- python-dotenv – For securely managing environment variables (API keys).  
- requests – For making HTTP requests to external APIs (e.g., PubMed, OpenRouter).  
- BeautifulSoup4 (bs4) – For parsing HTML/XML responses (e.g., PubMed articles).  
- uv – A fast Python package installer and dependency resolver.

---

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/medical-diagnosis-ai-mcp.git
cd medical-diagnosis-ai-mcp
```

### 2. Configure Your `.env` File

Create a `.env` file in the root directory with the following contents:

```env
OPENAI_API_KEY="your_openai_api_key_for_diagnosis_if_applicable"
OPENROUTER_API_KEY="your_openrouter_api_key"
```

> 🔐 Replace the placeholders with your actual API keys.

---

### 3. Install Dependencies with `uv`

```bash
uv init
uv add fast-mcp openai python-dotenv requests beautifulsoup4
```

---

## Running the Local FastAPI Application (for Testing)

You can test the tool by running the FastAPI app locally:

```bash
uvicorn fastAPI_app:app --reload --port 8080
```

Then, open your browser and go to:

[http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

Use the Swagger UI to send a `POST` request to the `/diagnosis` endpoint with this JSON body:

```json
{
  "description": "patient has a joint pain and fever"
}
```

You will receive a response with:
- Extracted symptoms
- AI-generated diagnosis
- Summary of relevant PubMed articles

---

## Converting and Deploying as an MCP Tool

The `mcp_tools.py` file contains the core logic to convert the tool into an MCP-compatible service using FastMCP.

### Run Locally

```bash
python mcp_tools.py
```

### Deploying

For deployment to cloud environments or other MCP-compatible platforms:

1. Package your project as needed.
2. Use deployment commands provided by your MCP platform (these may vary depending on the provider).
3. Ensure environment variables (`.env`) are properly set up in your deployment environment.

Refer to the official [FastMCP](https://pypi.org/project/fast-mcp/) documentation for advanced deployment steps.

---

Happy Diagnosing! 🚑
