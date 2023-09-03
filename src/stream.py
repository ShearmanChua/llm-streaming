from typing import Union

from fastapi import FastAPI, Header
from typing_extensions import Annotated
from fastapi.responses import StreamingResponse
import time
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

"""
Run by executing `uvicorn stream:app --reload`
Usage: 

import requests

url = "http://localhost:8000/"
data = {'prompt':some_text_here}
with requests.post(url, data=json.dumps(data), stream=True) as r:
    for chunk in r.iter_content(1024):  # or, for line in r.iter_lines():
        print(chunk.decode('UTF-8'), end=" ")
"""

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

class Data(BaseModel):
    prompt: str
    mode: str

def fake_data_streamer(text):
    print(text)
    for i in text.split():
        yield i
        time.sleep(0.015)


@app.post('/chat')
async def main(user_agent: Annotated[Union[str, None], Header()], request:Data):
    request = request.dict()
    print(request['prompt'])
    return StreamingResponse(fake_data_streamer(request['prompt']), headers = {"type": "textResponse", "uuid": "1q23fawet", "error":"false"}, media_type='text/plain')