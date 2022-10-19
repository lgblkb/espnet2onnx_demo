import argparse
import os
import sys

from app.utils import convert_speech_to_text


def main():
    wav_file = get_args().file
    if os.path.exists(wav_file):
        text = convert_speech_to_text(wav_file)
        print(text)
    else:
        print(wav_file, 'does not exist. Check the path')
    pass


def get_args():
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--file", help="path to wav audio", required=True)
    print(' '.join(sys.argv))
    return parser.parse_args()


if __name__ == '__main__':
    main()
