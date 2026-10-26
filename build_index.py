from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store

docs = load_documents("data/documents")

print("Documents Loaded:", len(docs))

chunks = split_documents(docs)

print("Chunks Created:", len(chunks))

embeddings = get_embedding_model()

create_vector_store(chunks, embeddings)

print("Vector Database Created Successfully!")