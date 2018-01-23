from flask import Flask,render_template

myapp = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('Jarvys.html')

@app.route('/pwa')
def pwa():
	return render_template('index.html')

@app.route('/pwa/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')


if __name__ == "__main__":
	myapp.run(host='0.0.0.0', port='8080')
