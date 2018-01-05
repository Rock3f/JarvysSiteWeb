from __future__ import absolute_import, division, print_function
from flask import Flask,render_template,request
import os

from deepspeech.model import Model

from sys import byteorder
from array import array
import scipy.io.wavfile as wav


BEAM_WIDTH = 500
LM_WEIGHT = 1.75
WORD_COUNT_WEIGHT = 1.00
VALID_WORD_COUNT_WEIGHT = 1.00
N_FEATURES = 26
N_CONTEXT = 9

ds = Model("output_graph.pb", N_FEATURES, N_CONTEXT, "alphabet.txt", BEAM_WIDTH)
ds.enableDecoderWithLM("alphabet.txt", 'lm.binary', 'trie' , LM_WEIGHT,
WORD_COUNT_WEIGHT, VALID_WORD_COUNT_WEIGHT)

root_dir = os.path.dirname(os.getcwd())
app = Flask(__name__,static_url_path=root_dir)


@app.route('/')
def hello_world():
	return render_template('Jarvys2.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'speech' in request.files:
        speech = request.files['speech']
        fs,audio = wav.read(speech)
        stt = ds.stt(audio, fs)
    return 'You did upload "' + stt + '"'
