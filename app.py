import os
from dotenv import load_dotenv

import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings


# Load API key
load_dotenv()


# Streamlit UI
st.set_page_config(page_title="Chat with PDF")

st.title("📄 Chat with PDF")
st.write("Upload a PDF and ask questions")


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type="pdf"
)


if uploaded_file:

    # Save uploaded PDF temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    # Load PDF
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    # Create vector database
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    # Retriever
    retriever = vectorstore.as_retriever()

    # User question
    question = st.text_input(
        "Ask a question about the PDF"
    )

    if question:

        # Retrieve relevant chunks
        docs = retriever.invoke(question)

        # Combine retrieved text
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # Prompt
        prompt = f"""
        Answer ONLY using the context below.

        Context:
        {context}

        Question:
        {question}
        """

        # Gemini model
        llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0
)

        # Generate response
        response = llm.invoke(prompt)

        # Display answer
        st.subheader("Answer")
        st.write(response.content)