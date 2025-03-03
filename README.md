Here's a rewritten version of the README in Markdown format, designed to be more visually appealing and ready for adding images:

---

# Multiple PDF Chat App
==========================

## Introduction
---------------

This project implements a Retrieval-Augmented Generation (RAG) system using FastAPI as the backend framework and HTML for the frontend. It leverages the Chroma vector database to efficiently store and retrieve documents, enabling accurate question-answering capabilities.

## Overview
------------

- **Backend**: Built with FastAPI, the backend handles PDF uploads, loads documents into a vector database using Chroma, and provides endpoints for querying the database.
- **Frontend**: A simple HTML interface allows users to upload PDFs, load them into the database, and ask questions based on the content.
- **Technology Stack**:
  - **Chroma**: Used for creating and managing the vector database.
  - **OpenAI Embeddings**: Utilized for generating embeddings of documents.
  - **LangChain**: Provides the framework for building the RAG workflow.

## Features
------------

- **PDF Upload**: Users can upload PDF files to the server.
- **Document Loading**: Loaded PDFs are processed and stored in a vector database.
- **Question Answering**: Users can input questions, and the system retrieves relevant answers from the stored documents.
- 


![Screenshot 2025-03-03 at 1 17 19 PM (2)](https://github.com/user-attachments/assets/3b51bc7a-52df-441b-845a-897d4e5a5179)
![Screenshot 2025-03-03 at 1 18 16 PM (2)](https://github.com/user-attachments/assets/c220d472-5d9a-49b6-913f-6ea22448aa70)
![Screenshot 2025-03-03 at 1 17 53 PM (2)](https://github.com/user-attachments/assets/03b74682-06d9-436c-992b-e2f769296f24)

## Setup
---------

### Environment Setup

1. **Python Installation**: Ensure you have Python installed.
2. **Package Installation**: Install required packages using:
   ```bash
   pip install fastapi uvicorn langchain chromadb openai
   ```

### Run the Backend

- Execute the FastAPI application using:
  ```bash
  uvicorn main:app --host 127.0.0.1 --port 8000
  ```

### Access the Frontend

- Open the provided HTML file in a web browser to interact with the application.

## Endpoints
------------

- **`/upload_pdf`**: Upload a PDF file to the server.
- **`/load_pdfs`**: Load uploaded PDFs into the vector database.
- **`/answer_question`**: Send a question to retrieve an answer based on the loaded documents.

## CORS Configuration
---------------------

The backend is configured to allow CORS requests from specific origins. You can adjust the `origins` list in the `main.py` file to include your frontend's URL.

## Future Enhancements
----------------------

- **Expand Document Support**: Add support for other document formats.
- **Improve UI/UX**: Enhance the frontend for better user experience.
- **Optimize Performance**: Optimize database queries and document processing for larger datasets.

## Contributing
--------------

Contributions are welcome! Please submit pull requests with detailed explanations of changes. Ensure all tests pass before submitting.

---


