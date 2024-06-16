from pathlib import Path
from openai import OpenAI
import os

api_key = os.getenv("APIKEY")

# Ensure the api_key is passed when creating the client
client = OpenAI(api_key=api_key)

speech_file_path = "/home/mich/source/binaily/voice/perfect.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="nova",
  input="I can see that through my camera. I'll recycle your rubbish. Just please present one piece of rubbish at a time and keep it still for 2 seconds.",
)

response.stream_to_file(speech_file_path)
