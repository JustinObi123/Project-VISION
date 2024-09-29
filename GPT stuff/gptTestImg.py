from dotenv import load_dotenv 
import os
from openai import OpenAI 
from IPython.display import Image, display, Audio, Markdown
import base64

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

OpenAI.api_key = api_key
client = OpenAI()

IMAGE_PATH = "GPT imgs/hehe.jpg"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
base64_image = encode_image(IMAGE_PATH)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "you are trying to detect a tool out of a given image"},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "what is this image? respond with one word at all times. even if you dont recognize the image, make a guess"},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/jpg;base64,{base64_image}"}
                }
            ]}
        
    ]
)

print(completion.choices[0].message.content)