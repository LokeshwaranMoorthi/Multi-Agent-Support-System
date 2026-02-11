import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def query_support_docs(query):
    # This connects to your Pinecone index for FAQ/Troubleshooting
    index = pc.Index("swades-support")
    # In a full RAG, you'd embed the query here. 
    # For the MVP, we return a simulated search result.
    return "Check the user manual section 4.2 for troubleshooting power issues."