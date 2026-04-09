# CourseMate AI

An AI-powered document retrieval and assistant tool built with Python, LangChain, Mistral AI, and Chroma DB. CourseMate AI processes educational PDFs, generates embeddings, and stores them in a local vector database for fast and accurate context retrieval.

## Features

- **Document Loading:** Automatically parses PDF documents using `PyPDFLoader`.
- **Intelligent Chunking:** Splits text into manageable, overlapping tokens using `RecursiveCharacterTextSplitter`.
- **State-of-the-art Embeddings:** Generates vector embeddings using Mistral AI (`mistral-embed`).
- **Local Vector Store:** Persists the processed document vectors locally using Chroma DB for efficient semantic search.

## Prerequisites

- Python 3.9+
- A Mistral AI API key (for embeddings)
- A Hugging Face account/token (optional, depending on other models used)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<YOUR-GITHUB-USERNAME>/<REPO-NAME>.git
   cd <REPO-NAME>
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your required API keys:
   ```env
   MISTRAL_API_KEY=your_mistral_api_key_here
   # HF_TOKEN=your_huggingface_token_here (if needed)
   ```

## Usage

1. Place your course PDFs in the `document loaders/` directory (or update the path in the script).
2. Run the script to process the documents and create the local Chroma database:
   ```bash
   python create_database.py
   ```
3. A `chroma_db` folder will be generated containing your local vector database, ready to be connected to a Retriever or LLM chat interface.

## Project Structure

- `create_database.py` - Main script to ingest PDFs, split texts, embed, and store in Chroma.
- `vector store/` - Modules interacting with the vector database.
- `document loaders/` - Original PDF documents and testing scripts.
- `chroma_db/` - (Ignored) Local folder where the active Chroma database is persisted.
- `requirements.txt` - Python dependencies needed to run the project.
