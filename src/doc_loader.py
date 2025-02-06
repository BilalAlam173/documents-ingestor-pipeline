import os
from langchain_community.document_loaders import PyPDFLoader

def load_all_documents(folder_path):
    """Loads all PDF documents from the specified folder."""
    all_documents = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"📄 Loading: {pdf_path}")
            
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()
            all_documents.extend(documents)

    return all_documents
