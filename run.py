import argparse, sys, os

import librosa
from espnet_onnx import Speech2Text

def get_args():
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--file", help="path to wav audio", required=True)
    print(' '.join(sys.argv))
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    wav_file = args.file
    if os.path.exists(wav_file): 
        speech2text = Speech2Text(model_dir='train_asr_ksc_v1')
        y, sr = librosa.load(wav_file, sr=16000)
        text = speech2text(y)[0][0]
        print(text)
    else: print(wav_file, 'does not exist. Check the path')
