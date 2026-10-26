from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model

retriever = None

def get_retriever():
    global retriever

    if retriever is None:
        embeddings = get_embedding_model()

        db = FAISS.load_local(
            "vector_db",
            embeddings,
            allow_dangerous_deserialization=True
        )

        retriever = db.as_retriever(
            search_kwargs={"k": 2}
        )

    return retriever