# llama-chat

Implement a simple web app to chat with Meta Llama3 model. The web app is done with Flet and the communication with Llama3 model is done through Ollama Python Library. 

## Links

* **Ollama website**: https://ollama.com/
* **Ollama Python Library**: https://github.com/ollama/ollama-python
* **Flet website**: https://flet.dev/

## Installation of Ollama

As I use Linux, all the information here is related to Linux based systems. For Mac or Windows, visit Ollama website.

```console
curl -fsSL https://ollama.com/install.sh | sh
```

To install and run Llama3 model:

```console
ollama run llama3
```

This command installs llama3 and starts a terminal chat. To exit write */bye*. 

At this point, Ollama and Llama3 model are sucssesfully installed. The next commands are to start, enable, stop and disable Ollama services.

* Enable and start the service:

```console
sudo systemctl enable ollama.service
sudo systemctl start ollama.service
```

* Stop and disable the service:

```console
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
```

## Running the web app Llama-chat

1. Clone the repository and enter the directory:

```console
git clone git@github.com:marcpuigpinos/llama-chat.git
cd llama-chat
```

2. Create a Python virtual enviroment:

```console
python -m venv .env
```

3. Activate the virtual enviroment (bash shell):

```console
source .env/bin/activate
```

4. Install requirements:

```console
pip install -r requirements.txt
```

5. Run the code:

    - App mode:

    ```console
    flet run
    ```

    - Web mode: (address is 127.0.0.1:8000)
    
    ```console
    flet run --web --port 8000
    ```
