from dotenv import load_dotenv 
import os
from openai import OpenAI 
from IPython.display import Image, display, Audio, Markdown
import base64
import random
import re

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

OpenAI.api_key = api_key
client = OpenAI()

IMAGE_PATH = "GPT imgs/knife.jpg"

system_content = (
    "You are a master storyteller writing an adventure story set in a fantasy world. "
    "Your task is to judge whether the user's chosen tool will help them survive each scenario. Do not give them a tool, the user must come up with a tool themselves "
    "The response should be 2-3 sentences. "
    "The decision must be logical and based on the effectiveness of the user's tool in the given scenario. "
    "If successful must end with the phrase 'success!' exactly as is, do not differ  then continue the story by presenting the next, more difficult scenario. "
    "If the tool fails, the user dies and the story ends. "
    "Scenarios start with an easy difficulty and each becomes progressively harder."
    "start off with an easy scenario in which almost any tool can help the user survive."
)

success_check = (
  "interpret response"
  "must return either '1' or '2'"
  "if response is a successful mission, print the number 1 else print the number 2"
)



count = 0

messages=[
            {
                "role": "system",
                "content": system_content
            }
        ]



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    base64_image = encode_image(IMAGE_PATH)


def get_completion(messages, model="gpt-4", ):
        response = client.chat.completions.create(
            model=model,  # Use a valid model name
            messages=messages,    
        )
        return response.choices[0].message.content.strip()
def extract_success(reply):
    """
    Extracts the Success flag from the assistant's reply.
    Returns True, False, or None if not found.
    """
    
    
    if reply:
      response = get_completion(reply)
      print(reply)
      return False
      if response == 1:
        return True
      else:
        return False
    else:
      return False
    

assistant_response = get_completion(messages)
if assistant_response:
    print(f"ChatGPT: {assistant_response}")
    messages.append({
        "role": "assistant",
        "content": assistant_response
    })


while count < 5:

      message = input("User : ")
      if message:
        messages.append({
          "role": "user", "content": message},
        )
        reply = get_completion(messages)
        if reply:
            print(f"ChatGPT: {reply}")
            # Append assistant's reply to the messages
            messages.append({
                "role": "assistant",
                "content": reply
            })
            success = extract_success(messages)
            if success is  False:
                break
        
        count += 1
      else:
        print("Please enter a valid tool.")
  

