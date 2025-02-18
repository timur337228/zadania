import random

from flask import Flask, request, url_for, redirect, render_template_string
import re, os

i = 0
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


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


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        prov = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода, киберинженер, штурман, пилот дронов'
        prov = prov.split(', ')
        for i in range(len(prov)):
            prov[i] = (f'<input type="checkbox" class="form-check-input" id=acceptRules" name="{prov[i]}">'
                       f'<label class="form-check-label" for="acceptRules">{prov[i]}</label></input>')
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div>
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <form class="login_form" method="post">
                                    <div class="name_lastname">
                                        <input type="text" class="form-control" id="lastname" aria-describedby="lastnameHelp" placeholder="Введите фамилию" name="lastname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <div/>
                                    <br/>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Образование</label>
                                        <select class="form-control" id="obrazov" name="obrazov">
                                          <option>Начальное</option>
                                          <option>Средние</option>
                                          <option>Высшие</option>
                                          <option>Без образования</option>
                                        </select>
                                     </div>
                                    <label for="classSelect">Какое у вас есть профессии</label>
                                    <div class="form-group form-check">
                                        {'</br>'.join(prov)}
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                            <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group 2 form-check">
                                        <input type="checkbox" class="form-check-input" id=acceptRules" name="go mars">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label></input>
                                    <div/>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet>')
def choice_planet(planet):
    g = ['Эта планета близка к земле;',
         "На ней много необходимых ресурсов;",
         'На ней есть вода и атмосфера;',
         'Наа ней есть небольшое магнитное поле;']
    random.shuffle(g)
    g.append('Наконец, она просто красива!')
    h = []
    bootstrap = ['secondary', 'success', 'danger', 'warning']
    for i in range(1, len(g)):
        h.append(f'<div class="alert alert-{random.choice(bootstrap)}"role="alert">{g[i]}')

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet}</h1>
                    <div class="main">
                    </br>{g[0]}
                    {'</div>'.join(h[1:])}
                    </div>
                  </body>
                </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def result_otbor(nickname, level: int, rating: float):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на миссию {nickname}:
                    <div class="alert alert-success"role="alert">Поздравляем! Ваш рейтинг после {level} этапа</div>
                    составляет {rating}!
                    <div class="alert alert-warning"role="alert">Желаем удачи!</div>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
                photo.save(filepath)
    return render_template_string('''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet"
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}" />
                <title>Отбор астронавтов</title>
              </head>
              <body>
                <div>
                    <h1>Загрузка фотографии</h1>
                    <h2>для участия в миссии</h2>
                    <form class="login_form" method="post" enctype="multipart/form-data">
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="photo">
                            {% if photo_url %}
                            <img src="{{ photo_url }}"style="max-width: 100%; height: auto;">
                            {% endif %}
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
              </body>
            </html>
        ''', photo_url=f'static/img/{photo.filename}' if request.method == 'POST' else None)


@app.route("/carousel")
def carousel():
    sledes = []
    li = []
    for indx, i in enumerate(os.listdir('static/giants')):
        if indx == 0:
            li.append(
                f'''<li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="{indx}" class="active"></li>''')
            sledes.append(f'''<div class="carousel-item active">
                  <img class="d-block w-100" src="static/giants/{i}" alt="{i}">
                </div>''')
        else:
            li.append(f'''<li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="{indx}"></li>''')
            sledes.append(f'''<div class="carousel-item">
                              <img class="d-block w-100" src="static/giants/{i}" alt="{i}">
                            </div>''')

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Пейзажи</h1>
                    <div class="container w-50"> 
                        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                          <ol class="carousel-indicators">
                            {"".join(li)}
                          </ol>
                          <div class="carousel-inner">
                            {"".join(sledes)}
                          </div>
                          <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                          </a>
                          <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                          </a>
                        </div>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
