# Chat with PDF - RAG Application

A RAG (Retrieval-Augmented Generation) application built using LangChain, Streamlit, ChromaDB, HuggingFace Embeddings, and Groq.

## Features

* Upload PDF
* Ask questions from PDF
* Semantic search
* Vector embeddings
* AI-generated answers

## Tech Stack

* Python
* LangChain
* Streamlit
* ChromaDB
* HuggingFace Embeddings
* Groq
* Llama 3.1

## Screenshots

The following screenshots show the working of the application from PDF upload to AI-generated answers.

![Screenshot 1](screenshots/screenshot1.png)

![Screenshot 2](screenshots/screenshot2.png)

![Screenshot 3](screenshots/screenshot3.png)

![Screenshot 4](screenshots/screenshot4.png)

## Run Project

```bash
pip install -r requirements.txt

streamlit run app.py
```

## Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

## Deployment

This app can be hosted on Streamlit Community Cloud or any Python web host that supports Streamlit.

Steps:

1. Push the repo to GitHub.
2. Go to https://streamlit.io/cloud and connect your GitHub account.
3. Select this repository and deploy `app.py`.
4. Add any needed secret keys in the app settings (do not commit `.env`).

Once deployed, copy the live app URL and add it to your README or GitHub repo description.

