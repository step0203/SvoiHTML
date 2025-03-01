from flask import Flask, render_template, redirect
from forms.loginform import LoginForm
app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    param = dict()
    param['username'] = "Степан"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    param = dict()
    param['username'] = "УСПЕХ!"
    param['title'] = 'успех'
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'mimimamumu'
    app.run(port=8080, host='127.0.0.1')