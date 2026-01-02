from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.auth_service import AuthService
from flask_login import login_required, logout_user, login_user


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')

    # Validate
    error = AuthService.validate_signup(name, email, password, confirm_password)
    if error:
        flash(error, 'danger')
        return redirect(url_for('auth.signup'))

    # Create user
    user, error = AuthService.create_user(name, email, password)
    if error:
        flash(error, 'danger')
        return redirect(url_for('auth.signup'))

    flash('Account created successfully!', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    user, error = AuthService.authenticate(email, password)
    if error:
        flash(error, 'danger')
        return redirect(url_for('auth.login'))

    login_user(user, remember=True)
    return redirect(url_for('users.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('workouts.index'))