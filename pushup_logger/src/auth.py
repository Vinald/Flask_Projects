from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    print('$$$$$$$$$$$$$$', name, email, password, confirm_password)

    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$', email, password)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
def logout():
    return render_template('auth/logout.html')
