from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('Jarvys.html')

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
