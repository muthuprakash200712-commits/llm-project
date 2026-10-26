import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.retriever import get_retriever

load_dotenv()


def ask_question(question):
    try:
        # Load retriever
        retriever = get_retriever()

        # Retrieve relevant chunks
        docs = retriever.invoke(question)

        if not docs:
            return "No relevant information found in the uploaded documents."

        # Build context
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # Gemini LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-flash-latest",
            temperature=0.2
        )

        # Prompt
        prompt = f"""
You are an intelligent document assistant.

Instructions:
- Answer only from the provided context.
- Use simple and easy-to-understand language.
- Give concise answers.
- Use bullet points when appropriate.
- Do not include technical metadata.
- Do not mention JSON, signatures, or system information.

Context:
{context}

Question:
{question}

Answer:
"""

        # Generate answer
        response = llm.invoke(prompt)

        # Extract clean text
        if hasattr(response, "content"):
            answer = response.content

            if isinstance(answer, list):
                cleaned = []

                for item in answer:
                    if isinstance(item, dict) and "text" in item:
                        cleaned.append(item["text"])

                answer = "\n".join(cleaned)

            return str(answer)

        return str(response)

    except Exception as e:
        return f"Error: {str(e)}"