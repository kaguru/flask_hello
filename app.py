from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/age')
def age():
    return 'I am 36 years Old'


@app.route('/location')
def age():
    return 'I Live at Muthiga'


if __name__ == '__main__':
    app.run()
