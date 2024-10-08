from openai import OpenAI
from dotenv import load_dotenv
import os
import time
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)

def run(messages, model, response_format=None):
    while True:        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=0.01,
            # response_format=response_format,
        )
        
        if chat_completion.choices == []:
            print(chat_completion)
            time.sleep(1)
            continue
        else:
            break
    return chat_completion.choices[0].message.content
        
        
    
    