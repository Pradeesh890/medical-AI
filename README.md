# Medical Diagnosis AI MCP Tool

This project is an AI-powered tool designed to assist in medical diagnosis by extracting symptoms from text, fetching relevant articles from PubMed, generating possible diagnoses using the OpenAI GPT-4 model, and summarizing related medical literature. It is also integrated into a Model Context Protocol (MCP) tool for streamlined integration into broader AI systems.

---

## Features

- **Symptom Extraction** from user-provided clinical descriptions.
- **AI Diagnosis Generation** using OpenAI’s GPT-4 model.
- **PubMed Integration** for fetching relevant medical literature.
- **Summarization** of article content using GPT-4.
- **FastAPI Server** for local testing of the API.
- **MCP Tool** for modular plug-in use.

---

## Project Structure

```
medical-diagnosis-ai-mcp/
│
├── tools/
│   ├── __init__.py
│   ├── symptom_extractor.py
│   ├── diagnosis_tools.py
│   ├── pubmed_fetcher.py
│   └── summarizer.py
│
├── .env
├── fastAPI_app.py
├── mcp_tools.py
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medical-diagnosis-ai-mcp.git
cd medical-diagnosis-ai-mcp
```

### 2. Initialize Project with `uv`

```bash
uv init
```

This creates the `pyproject.toml` and `.gitignore`.

### 3. Install Dependencies

```bash
uv add fast-mcp openai python-dotenv requests beautifulsoup4
```

### 4. Configure API Key

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_key_here
```

---

## Module Details

### tools/symptom_extractor.py

- **Purpose**: Extracts symptoms using regular expressions.
- **Returns**: A list of unique symptoms from a clinical description.

### tools/diagnosis_tools.py

- **Purpose**: Uses OpenAI GPT-4 to suggest a diagnosis based on symptoms.
- **Uses**: `openai.chat.completions.create` and `.env` for API key.

### tools/pubmed_fetcher.py

- **Purpose**: Fetches article metadata from PubMed.
- **Process**:
  - Queries PubMed E-Search to get article IDs.
  - Retrieves XML using E-Fetch.
  - Parses XML with BeautifulSoup.
- **Returns**: Titles, abstracts, authors, dates, and URLs.

### tools/summarizer.py

- **Purpose**: Summarizes fetched PubMed articles.
- **Uses**: GPT-4 with a summarization prompt.

---

## Running Locally with FastAPI

### fastAPI_app.py

Provides a local API to test all functions together.

### Endpoint

```http
POST /diagnosis
Content-Type: application/json

{
  "description": "patient has a joint pain and fever"
}
```

### Response

```json
{
  "symptoms": ["joint pain", "fever"],
  "diagnosis": "Possible diagnosis based on symptoms...",
  "summary": "Summary of related medical articles..."
}
```

### Start the Server

```bash
uvicorn fastAPI_app:app --reload --port 8080
```

Visit [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs) to test with Swagger UI.

---

## MCP Tool Integration

### mcp_tools.py

- **Purpose**: Converts the application into a reusable MCP tool.
- **Method**: Uses `fast_mcp.FastMCP` and `@mcp.tool()` decorator.
- **Tool Function**: `full_medical_analysis()` — performs symptom extraction, diagnosis, article fetching, and summarization.

### Run MCP Tool

```bash
python mcp_tools.py
```

---
