from flask import Flask, render_template, request, abort
from Order import Order

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/my_index')
def my_index():
    return render_template('my_index.html')


orders = {43: Order(43, 'Оплата картой, через почту', ['Кружка', 'Майка', 'Стикеры']),
          69: Order(69, 'Оплата наличными, через почту', ['Медные диски'])}


@app.route("/order", methods=["POST"])
def render_send():
    # client_message = request.form.get('id')
    if int(request.form.get('id')) in orders.keys():
        return repr(orders[int(request.form.get('id'))])
    else:
        return "Ошибка"


news = {}
news['Успешный разработчик'] = 'Вы не поверите, но он добился успеха после изучения Flask!'
news['Красный и белый'] = 'Эти удивительные цвета прекрасно гармонируют при выборе одежды.'

@app.route("/", methods=["GET", "POST"])
def render_post():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        news[title] = content
        if title == None or title == "" or content == None or content == "":
            return abort(404)  # Ошибка не найденного ресурса
        return render_template('news.html', news=news)


@app.route('/pow2/<string:chislo>/')
def pow_index(chislo):
    anstext = "Ваше число " + chislo + ", умноженное на 2: " + str(float(chislo) * 2)
    return render_template('pow_index.html', text=anstext)


@app.route('/round_square/radius/<string:chislo>/')
def round_square(chislo):
    return render_template('round_square.html', r=float(chislo), pi=float(3.14))


# калькулятор в jinja
@app.route('/calc/<string:a>/<string:operate>/<string:b>/')
def calcJinja(a, b, operate):
    return render_template('calc.html', a=float(a), b=float(b), operate=operate)


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

# калькулятор в python
@app.route('/calc/<string:operate>/')
def calcFunction(operate):
    result = ''
    if "+" in operate:
        parts = operate.split(sep='+', maxsplit=--1)
        result = parts[0] + ' + ' + parts[1] + ' = ' + str(int(parts[0]) + int(parts[1]))
    if "-" in operate:
        parts = operate.split(sep='-', maxsplit=--1)
        result = parts[0] + ' - ' + parts[1] + ' = ' + str(int(parts[0]) - int(parts[1]))
    if ":" in operate:
        parts = operate.split(sep=':', maxsplit=--1)
        result = parts[0] + ' : ' + parts[1] + ' = ' + str(int(parts[0]) / int(parts[1]))
    if "**" in operate:
        parts = operate.split(sep='**', maxsplit=--1)
        result = parts[0] + ' ** ' + parts[1] + ' = ' + str(int(parts[0]) ** int(parts[1]))
        return "Калькулятор python вернул результат " + result
    if "*" in operate:
        parts = operate.split(sep='*', maxsplit=--1)
        result = parts[0] + ' * ' + parts[1] + ' = ' + str(int(parts[0]) * int(parts[1]))
    return "Калькулятор python вернул результат " + result


if __name__ == '__main__':
    app.run(host='localhost', port='5000')
