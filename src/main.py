from doc_loader import load_new_documents
from doc_chunker import chunk_documents
from vector_converter import convert_to_vectors_and_store
import time

def main():
    print("🚀 Starting the appliance manual ingestion pipeline...")

    # Step 1: Load Only New Documents
    print("\n📥 Loading only new PDF documents...")
    documents = load_new_documents("manuals/")
    if not documents:
        print("✅ No new documents found. Exiting pipeline.")
        return
    
    print(f"✅ Loaded {len(documents)} new documents.")

    # Step 2: Chunk Documents
    print("\n✂️ Chunking documents...")
    chunks = chunk_documents(documents)
    print(f"✅ Created {len(chunks)} text chunks.")

    # Step 3: Convert Chunks to Embeddings & Store in CouchDB
    print("\n🔄 Converting chunks to vectors and storing them...")
    start_time = time.time()
    convert_to_vectors_and_store(chunks)
    end_time = time.time()
    print(f"✅ Successfully stored {len(chunks)} chunks in CouchDB.")
    print(f"⏳ Processing Time: {round(end_time - start_time, 2)} seconds.")

    print("\n🎉 Pipeline execution completed successfully!")

if __name__ == "__main__":
    main()
