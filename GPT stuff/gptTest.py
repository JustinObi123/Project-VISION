from dotenv import load_dotenv 
import os
from openai import OpenAI 
from IPython.display import Image, display, Audio, Markdown
import base64
import random

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

OpenAI.api_key = api_key
client = OpenAI()

IMAGE_PATH = "GPT imgs/knife.jpg"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
base64_image = encode_image(IMAGE_PATH)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
  "game": {
    "title": "Survival Adventure Game",
    "description": "A fantasy world adventure where the player faces a series of survival challenges and must draw tools to survive each situation. The player's tool is interpreted by an AI to determine success or failure.",
      {  
        "scenario": {
          "description": "The player is faced with a rapidly rising river blocking their path. The current is swift but shallow.",
          "prompt": "What tool do you draw to cross this obstacle?",
          "valid_tools": ["boat", "raft", "bridge", "rope"],
          "fail_condition": {
            "description": "If the player selects a tool that is ineffective, such as a 'paper boat,' they fail and are swept away by the current.",
            "fail_message": "FAIL: The tool was insufficient to cross the river, and the current sweeps the adventurer away."
          },
          "success_condition": {
            "description": "If the player selects a valid tool, they successfully cross the river and proceed to the next challenge.",
            "success_message": "PASS: The adventurer successfully crosses the river and continues their journey."
          }
        }
      },
      {
        "level_number": 2,
        "scenario": {
          "description": "A hungry wolf pack is closing in behind the adventurer.",
          "prompt": "What tool do you draw to escape the wolves?",
          "valid_tools": ["gun", "sword", "trap", "shield"],
          "fail_condition": {
            "description": "If the player selects a tool that fails to fend off the wolves, they are overpowered and meet their demise.",
            "fail_message": "FAIL: The wolves overpower the adventurer, and their journey ends here."
          },
          "success_condition": {
            "description": "If the player selects a valid tool, the wolves are scared off or defeated, allowing the adventurer to continue.",
            "success_message": "PASS: The wolves retreat, and the adventurer escapes unscathed."
          }
        }
      },
      {
        "level_number": 3,
        "scenario": {
          "description": "A steep, rocky cliff stands before the adventurer. They must scale it to proceed.",
          "prompt": "What tool do you draw to climb the cliff?",
          "valid_tools": ["rope", "grappling hook", "ladder"],
          "fail_condition": {
            "description": "If the player draws an unsuitable tool like 'paper,' the tool crumbles, and the adventurer is left at the base of the cliff.",
            "fail_message": "FAIL: The tool disintegrates, and the adventurer is crushed in a rockslide."
          },
          "success_condition": {
            "description": "If the player selects a valid tool, they scale the cliff successfully and move forward.",
            "success_message": "PASS: The adventurer climbs the cliff and continues their quest."
          }
        }
      }
    ,
    "gameplay_flow": {
      "input": {
        "tool_prompt": "The player draws a tool based on the scenario prompt. The tool is then interpreted by the LLM."
      },
      "llm_interpretation": {
        "description": "The LLM analyzes the player's input (the drawn tool) and compares it to a list of valid tools for the current scenario.",
        "logic": [
          {
            "input_tool_matches_valid_tools": {
              "outcome": "success",
              "message": "The player's tool is valid for the scenario and allows them to pass."
            }
          },
          {
            "input_tool_does_not_match_valid_tools": {
              "outcome": "failure",
              "message": "The player's tool is invalid for the scenario and leads to failure."
            }
          }
        ]
      },
      "pass_fail_system": {
        "description": "Each level evaluates whether the tool selected leads to a successful outcome (pass) or failure.",
        "fail_message": "If the player fails, the game indicates the reason and ends the scenario.",
        "pass_message": "If the player passes, the game continues to the next level."
      },
      "end_of_game": {
        "description": "If the player reaches the final level or dies, the game concludes with a summary of their journey.",
        "summary": {
          "success_summary": "A brief story generated based on the player's successful voyage through all levels.",
          "failure_summary": "A brief story generated based on how the adventurer met their end."
        }
      }
    }
  }
}

        
    ]
)

print(completion.choices[0].message)