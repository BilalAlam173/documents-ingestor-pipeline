from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
import os
import uuid
load_dotenv()
# Load credentials securely
COUCHBASE_USERNAME = os.getenv("COUCHBASE_USERNAME")
COUCHBASE_PASSWORD = os.getenv("COUCHBASE_PASSWORD")
COUCHBASE_HOST = os.getenv("COUCHBASE_HOST")

# Connect to Couchbase
auth = PasswordAuthenticator(COUCHBASE_USERNAME, COUCHBASE_PASSWORD)
cluster = Cluster(COUCHBASE_HOST, ClusterOptions(auth))
bucket = cluster.bucket("cs-hackathon")
collection = bucket.default_collection()

# Initialize OpenAI Embeddings
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=os.getenv("OPENAI_API_KEY"))

def convert_to_vectors_and_store(chunks):
    """Converts text chunks into vectors and stores them in CouchDB."""
    for chunk in chunks:
        chunk_id = str(uuid.uuid4())  # Unique ID for each chunk
        vector = embedding_model.embed_query(chunk.page_content)  # Convert to vector

        # Store in CouchDB
        collection.upsert(chunk_id, {
            "content": chunk.page_content,
            "vector": vector,
            "source": chunk.metadata.get("source", "unknown")  # Track original document
        })

        print(f"✅ Stored chunk {chunk_id}")
