from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/hello/')
def hello_blank():
    return render_template('page_blank.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')