from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.services.workout_service import WorkoutService

user = Blueprint('users', __name__)

@user.route('/profile')
@login_required
def profile():
    return render_template('users/profile.html', name=current_user.name)