from flask import Flask, request
from flask import url_for
i = 0
app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    g = ['Человечество вырастает из детства.', "Человечеству мала одна планета.",
                     'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(g)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
