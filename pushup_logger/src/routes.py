from flask import Blueprint, render_template

main = Blueprint('src', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/profile')
def profile():
    return render_template('main/profile.html')