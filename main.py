from ollama import chat, pull
from ollama import ChatResponse
from ollama import ResponseError

import os

# TODO: Add argparse for prompt and model

# TODO: Add a Django API for LLM query

# TODO: check the model (after fully pulled) without internet. (to ensure data privacy)

# TODO: Can we provide the models locally to the chat(...)? (this way no connection to Ollama server is needed and data will be safe)
MODEL_NAME='llama3.2'  # works 100%
# MODEL_NAME='llama3.2-vision'
# MODEL_NAME='deepseek-r1:1.5b'
# MODEL_NAME='deepseek-r1:7b'

# Pass in the prompt
MESSAGE_CONTENT = input("enter your prompt:")
# Pass in the path to the image (only for Multi-Modal models, e.g., llama3.2-vision)
# TODO: the ollama might have a method or attrib that can check which models are multi-modal and support input image (this way we only ask for image for relevant models).
# IMAGE_PATH = input('Please enter the path to the image: ')
# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

flag = True
while flag:
    try:
        # TODO: add logging INFO
        # e.g., [Calling the model with the prompt]
        # print('try: call model')
        response: ChatResponse = chat(model=MODEL_NAME, messages=[
          {
            'role': 'user',
            'content': MESSAGE_CONTENT,
            # TODO: activate only for multi-modal models
            # 'images': [IMAGE_PATH],
          },
          #TODO: enable 'model streaming'--for interactive prompting
          # https://medium.com/@revlae/how-to-stop-ollama-model-streaming-600a222b4797
          # stream=True,
        ])
        flag=False
    except ResponseError as e:
        print('except: call model')
        print('Error:', e.error)
        if e.status_code == 404:
            # TODO: add logging WARNING
            # e.g., [the model:{} is not installed. Now trying to pull it from Ollama server]
            try:
                print('try: pull model')
                print(f'======= Pulling the {MODEL_NAME}: Start ======')
                pull(MODEL_NAME)
                print(f'======= Pulling the {MODEL_NAME}: End ======')
            except Exception as e:
                print('except: pull model')
                print('Error', e.error)
                break
        else:
            print('no e.status_code == 404')
            # TODO: add logging DEBUG
            break
else:
    print(f'Successful: Got the response from "{MODEL_NAME}" with no Error')
    # TODO: add logging INFO

# print the response
# method 1
# print(response['message']['content'])
# method 2: or access fields directly from the response object
# print(response.message.content)

# Save the response to a file
# Note: the response is in Markdown format. You can use an online Markdown editor to view them better (e.g. https://stackedit.io/).
if response:
    with open('response.md', 'w') as f:
        #TODO: Add [Response from {MODEL_NAME}:\n]
        f.write(response['message']['content'])
