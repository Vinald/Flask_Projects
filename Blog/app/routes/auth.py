from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.auth_form import RegistrationForm, LoginForm

auth_route = Blueprint('auth_route', __name__, template_folder='templates/auth', url_prefix='/auth')


@auth_route.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('auth_route.login'))

    return render_template('auth/register.html', form=form, title='Register')


@auth_route.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash('You have been logged in!', 'success')
        return redirect(url_for('blog_route.index'))
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', form=form, title='Login')


@auth_route.route('/logout')
def logout():
    pass


@auth_route.route('/reset_password', methods=('GET', 'POST'))
def reset_request():
    pass