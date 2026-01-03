from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.auth_service import AuthService
from flask_login import login_required, logout_user, login_user, current_user


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('workouts.index'))
    return render_template('auth/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')

    error = AuthService.validate_signup(name, email, password, confirm_password)
    if error:
        flash(error, 'danger')
        return redirect(url_for('auth.signup'))

    user, error = AuthService.create_user(name, email, password)
    if error:
        flash(error, 'danger')
        return redirect(url_for('auth.signup'))

    flash('Account created successfully!', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('workouts.index'))
    return render_template('auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    user, error = AuthService.authenticate(email, password)
    if error:
        flash(error, 'danger')
        return redirect(url_for('auth.login'))

    # Flask-Login session
    login_user(user, remember=True)

    # Store additional data in Flask session
    session['user_id'] = user.id
    session['user_name'] = user.name
    session['user_email'] = user.email
    session.permanent = True # Make the session permanent

    flash(f'Welcome back, {user.name}!', 'success')
    return redirect(url_for('users.profile'))


@auth.route('/logout')
@login_required
def logout():
    # Clear session data
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)

    logout_user()

    flash('You have been logged out.', 'info')
    return redirect(url_for('workouts.index'))
