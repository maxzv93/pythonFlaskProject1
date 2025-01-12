from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/my_index')
def my_index():
    return render_template('my_index.html')


@app.route('/pow2/<string:chislo>/')
def pow_index(chislo):
    anstext = "Ваше число "  + chislo + ", умноженное на 2: "+ str(float(chislo)*2)
    return render_template('pow_index.html', text = anstext)

@app.route('/round_square/radius/<string:chislo>/')
def round_square(chislo):
    return render_template('round_square.html', r = float(chislo), pi=float(3.14))

@app.route('/calc/<string:a>/<string:operate>/<string:b>/')
def calcJinja(a, b, operate):
    return render_template('calc.html', a = float(a), b = float(b), operate = operate)

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
