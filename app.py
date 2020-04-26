from flask import Flask, render_template
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

app = Flask(__name__)

@app.route('/')
def index():
    user = {'username': 'Viktor'}
    return render_template('index.html', title='Home', user=user)

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/hello/')
def hello_blank():
    return render_template('page_blank.html')

if __name__ == '__main__':
    app.run(debug=True, host=s.getsockname()[0])