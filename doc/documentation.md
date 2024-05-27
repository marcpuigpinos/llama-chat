# Simple LLM web chat.

The aim of this project is to test Ollama and do a simple LLM web chat using the **ollama-python** library and **FLET**.

## Installation.

Read *README.md*.

## Console chat.

The first approximation will be to create a python console chat that will ask for prompt after each new question.

Class client:

```python
import ollama

class ollama_client:
    def __init__(self):
        self.__model = "llama3"
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
```

Main application:

```python
from llama.client import ollama_client

def main():
    client = ollama_client()

    while True:
        print("Please ask something...")
        message = input("> ")
        print(client.ask_question(message))
        print("")


if __name__ == "__main__":
    main()
```

Console chat:

```console
❯ python main.py
Please ask something...
> Tell me in a few words what you are, please.
I am LLaMA, an AI chatbot trained to understand and respond to human language.

Please ask something...
>
```
