import ollama

MODELS = ["llama3"]

class ollama_client:
    def __init__(self, model: str, address: str, port: int):
        if model not in MODELS:
            raise Exception(f"The model introduced is invalid. Please select one of the following:\n{MODELS}")
        self.__model = model
        try:
            self.__client = ollama.Client(host=f"{address}:{port}")
        except Exception as error:
            print(f"Connection couldn't be established: {error}.")
            exit(-1)

    def ask_question(self, message: str):
        response = self.__client.chat(model=self.__model, messages=[
                {
                    'role': 'user',
                    'content': message
                }

            ]
        )

        print(response["message"]["content"])
