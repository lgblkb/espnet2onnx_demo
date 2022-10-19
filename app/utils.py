import os
from pathlib import Path

import librosa
from espnet_onnx import Speech2Text

data_folder = Path(os.environ['STORAGE_FOLDER'])
model_dir = data_folder / 'train_asr_ksc_v1'
assert model_dir.exists()
speech2text = Speech2Text(model_dir=model_dir, use_quantized=True)


def convert_speech_to_text(wav_file: str):
    y, sr = librosa.load(wav_file, sr=16000)
    text = speech2text(y)[0][0]
    return text
