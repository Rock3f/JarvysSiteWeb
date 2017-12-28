from flask import Flask,render_template
import os


root_dir = os.path.dirname(os.getcwd())
app = Flask(__name__,static_url_path=root_dir)


@app.route('/')
def hello_world():
	return render_template('Jarvys2.html')