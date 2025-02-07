import openai

# Set your OpenAI API key
openai.api_key = "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"

# Convert text to embedding
response = openai.embeddings.create(
    model="text-embedding-3-small",  # Use OpenAI's small embedding model
    input="Oven"
)

# Extract embedding vector
embedding_vector = response.data[0].embedding

# Print the embedding vector
print("Embedding for 'Oven':", embedding_vector)
