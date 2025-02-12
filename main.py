import random

from flask import Flask, request
from flask import url_for
import re

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


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}"><img>
                  </body>
                </html>"""


@app.route('/<path:path>/promotion_image', defaults={'path': ''})
def promotion_image(path):
    g = ['Человечество вырастает из детства.', "Человечеству мала одна планета.",
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    h = []
    bootstrap = ['secondary', 'success', 'danger', 'warning']
    for i in g:
        print(i)
        h.append(f'<div class="alert alert-{random.choice(bootstrap)}"role="alert">{i}')
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    </br><img src="{url_for('static', filename='img/mars.jpg')}"><img><br>
                    {'</div>'.join(h)}
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
