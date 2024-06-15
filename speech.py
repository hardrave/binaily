from pathlib import Path
from openai import OpenAI
import os

api_key = os.getenv("APIKEY")

# Ensure the api_key is passed when creating the client
client = OpenAI(api_key=api_key)

speech_file_path = "/home/mich/source/binaily/voice/disscus.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="nova",
  input="Maybe you have any questions about recycling in Warsaw? I can help you!",
)

response.stream_to_file(speech_file_path)
