# espnet2onnx_demo

This is a Kazakh_ASR demo page without torch dependency. Please install the required packages first:
```shell
pip install -r /path/to/requirements.txt
```
Unzip the pretrained model in the current directory:
```shell
unzip train_asr_ksc_v1.zip
```
To run the demo, please run the `run.py` script as follows:
```shell
python run.py --file /path/to/file.wav 
```
