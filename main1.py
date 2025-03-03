from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import JSONResponse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    "http://localhost:8000",  # Adjust this to your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Global variables to hold the vector database and retriever
vectordb = None
retriever = None

# Route for PDF upload
@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not os.path.exists('data'):
        os.makedirs('data')
    file_path = os.path.join('data', file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"message": f"File {file.filename} uploaded successfully."}

# Route to load PDFs and create the vector database
@app.post("/load_pdfs")
def load_pdfs():
    global vectordb, retriever
    loader = DirectoryLoader('data', glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
    texts = text_splitter.split_documents(documents)
    
    persist_directory = 'db'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=texts, 
                                     embedding=embedding,
                                     persist_directory=persist_directory)
    
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    return {"message": "PDFs loaded and vector database created."}

# Route to answer questions using RAG
@app.post("/answer_question")
async def answer_question(request: Request):
    global retriever
    if retriever is None:
        return {"error": "Please load PDFs first."}
    
    data = await request.json()
    query = data.get('query', '')
    
    llm = ChatOpenAI()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever, 
        return_source_documents=True
    )
    
    llm_response = qa_chain(query)
    return {"result": llm_response['result']}
