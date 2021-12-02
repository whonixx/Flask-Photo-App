import re
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/photography')
def photography():
    return render_template('photography.html')


@app.route('/abandoned')
def abandoned():
    return render_template('abandoned.html')


@app.route('/landscapes')
def landscapes():
    return render_template('landscapes.html')


@app.route('/humans')
def humans():
    return render_template('humans.html')


@app.route('/programming')
def programming():
    pass


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
