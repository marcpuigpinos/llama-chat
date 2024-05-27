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
