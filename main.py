from llama.client import ollama_client

import click

@click.command()
@click.option("--model", required=True, help="Select one compatible model with Ollama. See https://ollama.com/")
@click.option("--address", required=True, help="Address to the server running the model.")
@click.option("--port", required=False, default=11434, help="Communication port with the server.")
def main(model: str, address: str, port: int):
    try:
        client = ollama_client(model=model, address=address, port=port)
    except Exception as error:
        print(f"Ollama client could not be initialized: {error}")

    while True:
        print("Please ask something...")
        message = input("> ")
        print(client.ask_question(message))
        print("")


if __name__ == "__main__":
    main()
