# Simple in-memory chat storage

chat_history = []


def add_message(role: str, content: str):
    chat_history.append({
        "role": role,
        "content": content
    })


def get_history(limit: int = 5):
    return chat_history[-limit:]


def clear_history():
    chat_history.clear()
