# VaultGuard Finance AI

This is a personal finance tool I'm building to help people look at their spending without worrying about their privacy. Most AI apps make you send your bank info to their servers. This project is unique since it'd let the AI work directly on your own computer so your data stays with you.

## What it does

**Two ways to work**: You can run the app **100%** on your own computer for total privacy. Or, you can use a "Hybrid" mode that cleans your data first and then uses a OpenAI's models for the results.

**Data Cleaning**: I wrote a script that looks at your bank files and hides things like account numbers. It only keeps the prices and the descriptions.

**Smart Searching (RAG)**: Instead of giving the AI your whole bank statement, we'd turn your transactions into **Embeddings**. These are stored in a **Vector Database**. When you ask a question, the app only sends the most relevant "snippets" of your data to the AI. This would help keep the data footprint small and secure.

## How it is built

**Language**: Python

**Local AI**: Ollama (using the Llama 3 model)

**Cloud AI**: OpenAI (for the online demo version)

**Data Handling**: Pandas

**Vector Database**: ChromaDB

## How to run it locally

### 1. Get the code

```bash
git clone https://github.com/pupadh24/VaultGuard-Finance-AI.git
cd VaultGuard-Finance-AI
```

### 2. Set up Python
Create a virtual environment and install the requirements:

```bash
python -m venv venv
pip install -r requirements.txt
```

### 3. Get the AI
Download Ollama from their website and then run this in your terminal:

```bash
ollama pull llama3
```

### 4. Run it
Put your bank CSV file in the folder (the .gitignore will keep it from being uploaded) and run:

```bash
python app.py
```

## What I am working on next

**Base Sanitization**: Building the regex logic in `cleaner.py` to handle bank account masking.

**Brain Integration**: Connecting the Python script to the local Ollama API to process the first real queries.

**Visual Dashboard**: Adding a simple interface to show spending charts alongside the AI advice.
