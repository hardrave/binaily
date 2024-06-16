import base64
import requests
import os
import json

def trash(imagepath):

  image_path = imagepath
  api_key  = os.getenv("APIKEY")

  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

  

  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "You are an AI recycling bin. You give a one-word reply, classifying the image. Always classify what you see in human hands in fron of you, ignore background noises. If it's metal or plastic, you say 'plastic'. If it's glass, you say 'glass'. If it's paper, you say 'paper'. For e-waste, reply 'ewaste'. For biodegradable items, reply 'bio'. If you see multiple items, reply 'multiple'. If you really cannot classify, say 'no'."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  response = response.json()  
  content = response['choices'][0]['message']['content']

  print(content)
  return content.lower()


