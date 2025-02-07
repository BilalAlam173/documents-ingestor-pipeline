import os
import hashlib
from langchain_community.document_loaders import PyPDFLoader
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
from dotenv import load_dotenv
load_dotenv()

# Couchbase Connection
COUCHBASE_USERNAME = os.getenv("COUCHBASE_USERNAME")
COUCHBASE_PASSWORD = os.getenv("COUCHBASE_PASSWORD")
COUCHBASE_HOST = os.getenv("COUCHBASE_HOST", "couchbase://localhost")

auth = PasswordAuthenticator(str(COUCHBASE_USERNAME), str(COUCHBASE_PASSWORD))
cluster = Cluster(COUCHBASE_HOST, ClusterOptions(auth))
bucket = cluster.bucket("cs-hackathon")
collection = bucket.default_collection()


def get_file_hash(file_path):
    """Generate a unique hash for a file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def is_already_processed(file_path):
    """Check if the document has already been processed by comparing hashes."""
    file_hash = get_file_hash(file_path)
    query = f"SELECT file_hash FROM `{bucket.name}` WHERE file_hash = $1"
    result = cluster.query(query, file_hash).execute()
    # Convert to list and count rows
    rows = list(result)
    num_rows = len(rows)
    return num_rows > 0  # If hash exists, document is already processed


def load_new_documents(folder_path):
    """Load and return only new documents from the folder."""
    all_documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)

            # Check if file has already been processed
            if is_already_processed(pdf_path):
                print(f"⚠️ Skipping already processed file: {filename}")
                continue

            print(f"📄 Processing new file: {pdf_path}")

            # Load PDF and store its hash
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()

            # Store the file hash in Couchbase to track it
            collection.upsert(filename, {"file_name": filename, "file_hash": get_file_hash(pdf_path)})

            all_documents.extend(documents)

    return all_documents
