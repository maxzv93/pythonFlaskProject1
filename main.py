from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'

# @app.route('/albums/1')
# def hello_world():
#     return 'Hello, Flask'
#
#
# @app.route('/albums/<album_number>')
# def albums(album_number):
#     return 'The {} album.'.format(album_number)
#
#
# @app.route('/albums/<int:album_number><song_number>')
# def albums(album_number, song_number):
#     return 'The {} album and {} musician performer.'.format(album_number, song_number)

@app.route('/<string:operate>/')
def calcFunction(operate):
    result = ''
    if "+" in operate:
        parts = operate.split(sep='+', maxsplit=--1)
        result = str(int(parts[0]) + int(parts[1]))
    if "-" in operate:
        parts = operate.split(sep='-', maxsplit=--1)
        result = str(int(parts[0]) - int(parts[1]))
    if ":" in operate:
        parts = operate.split(sep=':', maxsplit=--1)
        result = str(int(parts[0]) / int(parts[1]))
    if "**" in operate:
        parts = operate.split(sep='**', maxsplit=--1)
        result = str(int(parts[0]) ** int(parts[1]))
        print(result)
        return result
    if "*" in operate:
        parts = operate.split(sep='*', maxsplit=--1)
        result = str(int(parts[0]) * int(parts[1]))
    print(result)
    return result


if __name__ == '__main__':
    app.run(host='localhost',port='5000')
