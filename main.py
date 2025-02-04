from utils.llm.ollama import ollama_model_call

# TODO: Add argparse for prompt and model
# e.g., reading the prompt from a file (that has been written from an API call)

# TODO: Add a Django API for LLM query

# TODO: call the constants from a config file

# TODO: Can we provide the models locally to the chat(...)? (this way no connection to Ollama server--for pulling the model--is needed and data will be safe)
# llama models: 'llama3.2', 'llama3.2-vision' (multi-modal with image input), ???
# MODEL_NAME='llama3.2'
# Deepseek-R1 models: 'deepseek-r1:1.5b', 'deepseek-r1:7b', 'deepseek-r1:8b', 'deepseek-r1:14b', 'deepseek-r1:32b', 'deepseek-r1:70b', 'deepseek-r1:671b'
MODEL_NAME='deepseek-r1:32b'

# Pass in the prompt
PROMPT = input("enter your prompt:")
# Pass in the path to the image (only for Multi-Modal models, e.g., llama3.2-vision)
# TODO: the ollama might have a method or attrib that can check which models are multi-modal and support input image (this way we only ask for image for relevant models).
# IMAGE_PATH = input('Please enter the path to the image: ')
# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

response = ollama_model_call(PROMPT, model=MODEL_NAME)

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
