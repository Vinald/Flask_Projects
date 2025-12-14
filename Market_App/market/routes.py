from market import app
from flask import render_template


@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    return render_template('market.html')


@app.route('/register')
def register_page():
    return render_template('register.html')