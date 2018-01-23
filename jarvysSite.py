from __future__ import absolute_import, division, print_function
from flask import Flask,render_template,request
from flask_cors import CORS
from textblob import TextBlob
import os
from deepspeech.model import Model

from sys import byteorder
from array import array
import scipy.io.wavfile as wav

import subprocess



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
CORS(app)

@app.route('/')
def hello_world():
	return render_template('Jarvys.html')

@app.route('/upload', methods=['POST'])
def upload():
	if 'speech' in request.files:
		speech = request.files['speech']
		speech.save('tmp/tmp.mp3')
		subprocess.call(['sox','tmp/tmp.mp3','-c 1', '-r 16000','tmp/tmp.wav'])
		fs,audio = wav.read('tmp/tmp.wav')
		stt = ds.stt(audio, fs)
		blob = TextBlob(stt)
		blob = blob.correct().translate(to="fr")
	elif 'speech' in request.values:
		speech = request.values['speech']
		with open('tmp/tmp.mp3',"w+") as f:
			f.write(speech)
		subprocess.call(['sox','tmp/tmp.mp3','-c 1', '-r 16000','tmp/tmp.wav'])
		fs,audio = wav.read('tmp/tmp.wav')
		stt = ds.stt(audio, fs)
		blob = TextBlob(stt)
		blob = blob.correct().translate(to="fr")
	else:
		print(request.files)
		blob = TextBlob("nothing")
	return 'You did upload "{0}"'.format(blob)


@app.route('/pwa')
def pwa():
	return render_template('index.html')

@app.route('/service-worker.js', methods=['GET'])
def sw():
    return app.send_static_file('service-worker.js')

@app.route('/index.html', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/offline.html', methods=['GET'])
def offline():
    return app.send_static_file('oui.html')



if __name__ == "__main__":
	myapp.run(host='0.0.0.0', port='8080')
