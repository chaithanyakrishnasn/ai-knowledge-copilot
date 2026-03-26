from openai import OpenAI
from src.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_answer(query, context_chunks, history=None):
    if history is None:
        history = []
    context = "\n\n".join(context_chunks)

    messages = []

    # Add system instruction
    messages.append({
        "role": "system",
        "content": """You are an enterprise AI assistant.

Answer strictly using provided context.
If not found, say "I don't know".
Be clear and structured."""
    })

    # Add conversation history
    for msg in history:
        messages.append(msg)

    # Add current query with context
    messages.append({
        "role": "user",
        "content": f"""
Context:
{context}

Question:
{query}
"""
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content
