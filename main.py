from llama.client import ollama_client

def main():
    client = ollama_client(model="llama3", address="127.0.0.1", port=11434 )

    while True:
        print("Please ask something...")
        message = input("> ")
        print(client.ask_question(message))
        print("")


if __name__ == "__main__":
    main()
