from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def q():
    return 'Миссия колонизации Марса'
@app.route('/index')
def index():
    return 'И на марсе будут яблони цвести'
@app.route('/promotion')
def promotion():
    return render_template('2.html')

@app.route('/image_mars')
def img_mars():
    # return 'dsgfsdgfsdgs'
    return render_template('1.html')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')