Medical Diagnosis AI Tool

This project develops a custom Medical Diagnosis Tool designed to assist in preliminary medical assessments by leveraging AI for symptom extraction, diagnosis generation, and medical article summarization. It's built to expose its functionality as a Model Context Protocol (MCP) tool, making it accessible for integration with various platforms.
Features

    Symptom Extraction: Automatically identifies and pulls out key symptoms from patient descriptions.
    AI-Powered Diagnosis: Provides a potential medical diagnosis based on extracted symptoms, powered by a sophisticated AI model.
    PubMed Article Fetching: Searches for and retrieves relevant medical articles from PubMed based on symptoms.
    AI-Powered Article Summarization: Summarizes fetched medical articles concisely using Llama 4 Maverick via the OpenRouter API.
    MCP Tool: Exposes the entire functionality as an MCP tool for seamless integration into cloud environments or other compatible platforms.

Project Structure

The project is neatly organized into several Python files, each handling a specific part of the tool's functionality:

medical diagnosis AI MCP/
├── .env                  # Environment file for API keys
├── .gitignore            # Git ignore file
├── fastAPI_app.py        # Local FastAPI application for testing individual tools
├── mcp_tools.py          # Defines and exposes the MCP tool
├── pyproject.toml        # Project configuration file (managed by uv)
└── tools/
    ├── __init__.py       # Initializes the tools package
    ├── diagnosis_tools.py  # Handles AI diagnosis generation
    ├── pubmed_fetcher.py   # Fetches articles from PubMed
    ├── summarizer.py       # Summarizes text using AI (Llama 4 Maverick)
    └── symptom_extractor.py# Extracts symptoms from text

Technologies Used

    Python 3.x
    FastAPI: For building the local testing API.
    FastMCP: For converting the tool into an MCP-compatible service.
    OpenRouter API: For accessing the Llama 4 Maverick AI model for summarization.
    openai: For interacting with the AI model for diagnosis.
    python-dotenv: For securely managing environment variables (API keys).
    requests: For making HTTP requests to external APIs (e.g., PubMed, OpenRouter).
    BeautifulSoup4 (bs4): For parsing HTML/XML responses (e.g., PubMed articles).
    uv: A fast Python package installer and dependency resolver.

Setup and Installation
1. Clone the Repository

Start by cloning the project to your local machine:
Bash

git clone https://github.com/your-username/medical-diagnosis-ai-mcp.git # Replace with your repo URL
cd medical-diagnosis-ai-mcp

2. Configure Your .env File

Create a file named .env in the root directory of your project. This file will store your sensitive API keys securely:

OPENAI_API_KEY="your_openai_api_key_for_diagnosis_if_applicable"
OPENROUTER_API_KEY="your_openrouter_api_key"

Important: Replace "your_openai_api_key_for_diagnosis_if_applicable" and "your_openrouter_api_key" with your actual API keys.
3. Install Dependencies with uv

Navigate to the project's root directory in your terminal and run the following commands to initialize uv and install all necessary dependencies:
Bash

uv init
uv add fast-mcp openai python-dotenv requests beautifulsoup4

Running the Local FastAPI Application (for Testing)

You can test the individual tool functionalities and the API integration by running the FastAPI application locally:
Bash

uvicorn fastAPI_app:app --reload --port 8080

Once the server is up and running, open your web browser and navigate to http://127.0.0.1:8080/docs. This will take you to the Swagger UI, where you can interact with and test the /diagnosis endpoint. Send a POST request with a JSON body like this:
JSON

{
  "description": "patient has a joint pain and fever"
}

The response will show the extracted symptoms, the AI-generated diagnosis, and a summary of relevant PubMed articles.
Converting and Deploying as an MCP Tool

The mcp_tools.py file is where the magic happens for the MCP conversion. It defines the full_medical_analysis function and registers it as an MCP tool.

To run the MCP tool locally for development or pre-deployment testing, simply execute:
Bash

python mcp_tools.py

For deploying the MCP tool to a cloud environment or other compatible platforms, refer to the specific instructions provided by your MCP provider. This usually involves packaging your project and utilizing fast-mcp's deployment commands, which can vary based on your cloud setup.
