import openai
import json
from pathlib import Path

PROMPT = "3D render of a fururistic castle in a clear sky, digital art"
DATA_DIRECTORY = Path.cwd()
DATA_DIRECTORY.mkdir(exist_ok=True)

openai.api_key = "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"

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json"
)

file_name = DATA_DIRECTORY / f"{PROMPT[:5]} {response['created']}.json"

with open(file_name, mode="w", encoding='utf-8') as file:
    json.dump(response, file)
