from flask import Flask,render_template

myapp = Flask(__name__)

@myapp.route('/')
def hello_world():
	return render_template('Jarvys.html')

if __name__ == "__main__":
	myapp.run(host='0.0.0.0', port='8080')
