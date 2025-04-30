# helpers.py

class ZephyrApp:
    def __init__(self):
        self.reset()

    def reset(self):
        self.history = []

    def chat(self, message):
        self.history.append(message)
        # This is a placeholder; replace with real model/chatbot call
        return f"[Fake Response] You said: {message}"

