import io

import requests
from loguru import logger
import re
from typing import List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

from pydantic import conlist, Field

from app.utils import convert_speech_to_text

app = FastAPI()


class Response(BaseModel):
    text: str


response_example = {
    200: {
        "description": "Speech to Text conversion",
        "content": {
            "application/json": {
                "examples": {
                    "Example": {
                        "text": "таңғы шоу жалғастырамыз студияда бүгін бізде қонақта әнші ерасыл хасен қош келдіңіз тағы да"
                    }
                }
            }
        }
    },
}


@app.get("/data", response_model=Response, responses=response_example)
def get_result(audio_file: str):
    response = requests.get(audio_file)
    fd = io.BytesIO(response.content)
    text = convert_speech_to_text(fd)
    return dict(text=text)
