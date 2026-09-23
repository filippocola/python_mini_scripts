from ollamafreeapi import OllamaFreeAPI

if __name__ == "__main__":
    client = OllamaFreeAPI()

    # stream Response in real time:
    # for chunk in client.stream_chat("chi ha inventato il linguaggio python?", model='llama3.2:3b'):
    #     print(chunk, end="", flush=True)

    # NO streaming response:
    response = client.chat(model="gpt-oss:20b", prompt="chi ha inventaato il linguaggio python?", temperature=0.7)
    print(response)