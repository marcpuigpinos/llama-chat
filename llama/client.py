import ollama

class ollama_client:
    def __init__(self):
        self.__model = "llama3.1"
        self.__stream = False

    def ask_question(self, message: str):
        response = ollama.chat(
                model = self.__model,
                messages = [
                        {
                            "role": "user",
                            "content": message,
                        },
                    ],
                stream = self.__stream,
                )
        return response["message"]["content"]
