import os
from pathlib import Path

import librosa
from espnet_onnx import Speech2Text
from loguru import logger

data_folder = Path(os.environ['STORAGE_FOLDER'])
logger.debug('data_folder: {}', data_folder)
# model_dir = data_folder / 'train_asr_ksc_v1'
# assert model_dir.exists()
# logger.info('model_dir: {}', model_dir)
curdir = os.curdir
os.chdir(data_folder)
speech2text = Speech2Text(model_dir='train_asr_ksc_v1', use_quantized=True)
os.chdir(curdir)


def convert_speech_to_text(wav_file):
    y, sr = librosa.load(wav_file, sr=16000)
    text = speech2text(y)[0][0]
    return text
