import io

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
        "description": "Return list of (word, label) pairs.",
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
    # fd = io.BytesIO()
    # with open(fd,'wb') as file:
    #     write(fd, fs, audio_data)
    # return base64.b64encode(fd.read())
    logger.debug('audio_file: {}', audio_file)
    text = convert_speech_to_text(audio_file)
    logger.debug('text: {}', text)

    # # Print tokens and predicted labels
    # if model_name == "roberta":
    #     input_sent_tokens = tokenizer.decode(tokenized_inputs['input_ids'][0], skip_special_tokens=True).split()
    # else:

    return dict(text=text)
