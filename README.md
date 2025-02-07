# 🚀 AI-Powered Knowledge Base Pipeline for Patient Information Leaflets (PILs)

An AI-driven document processing pipeline that ingests **Patient Information Leaflets (PILs)**, processes them into structured knowledge, and enables **fast & efficient retrieval** using **Couchbase Vector Search** and **LangChain**.

---

## 🔹 Features
✅ **Ingests PDF-based PILs** – Converts PDFs into structured text.  
✅ **Preserves Context** – Chunks text by **paragraphs**, not characters.  
✅ **Generates Embeddings** – Uses **OpenAI embeddings** for similarity matching.  
✅ **Stores in Couchbase** – Enables **fast vector search** for retrieval.  
✅ **Integrates with AI Chatbot** – Used by an **AI assistant** to help users understand their medicines.  

---

## 🔧 Tech Stack
- **LangChain** – Text processing, chunking, embeddings  
- **Couchbase Vector Search** – Efficient document retrieval  
- **OpenAI API** – Embeddings & LLM-powered responses  
- **Python** – Backend processing  
- **Node.js (for chatbot integration)**  

---

## 🚀 How It Works
1️⃣ **Load Documents** → Extract text from **PDF PILs**.  
2️⃣ **Chunk Text** → Split into **paragraph-based** chunks for better retrieval.  
3️⃣ **Generate Embeddings** → Convert text chunks into **vector embeddings**.  
4️⃣ **Store in Couchbase** → Save text chunks & embeddings for **vector search**.  
5️⃣ **Retrieve Answers** → AI chatbot queries Couchbase, finds relevant text, and responds!  

---
Contributors
Bilal Alam
Taavi Laanemaa
