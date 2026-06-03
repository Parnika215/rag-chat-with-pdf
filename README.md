# Chat with PDF - RAG Application

A RAG (Retrieval-Augmented Generation) application built using LangChain, Streamlit, ChromaDB, and Gemini API.

## Features
- Upload PDF
- Ask questions from PDF
- Semantic search
- Vector embeddings
- AI-generated answers

## Tech Stack
- Python
- LangChain
- Streamlit
- ChromaDB
- Gemini API

## Run Project

pip install -r requirements.txt

streamlit run app.py

## Deployment

This app can be hosted on Streamlit Community Cloud or any Python web host that supports Streamlit.

Steps:
1. Push the repo to GitHub.
2. Go to https://streamlit.io/cloud and connect your GitHub account.
3. Select this repository and deploy `app.py`.
4. Add any needed secret keys in the app settings (do not commit `.env`).

Once deployed, copy the live app URL and add it to your README or GitHub repo description.

Example live-demo link:
`https://share.streamlit.io/<your-username>/<repo-name>/main/app.py`