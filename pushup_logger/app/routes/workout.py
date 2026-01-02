from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.services.workout_service import WorkoutService

main = Blueprint('workouts', __name__)


@main.route('/')
def index():
    return render_template('workouts/index.html')


@main.route('/add_workout')
@login_required
def add_workout():
    return render_template('workouts/add_workout.html')


@main.route('/add_workout', methods=['POST'])
@login_required
def add_workout_post():
    date = request.form.get('date')
    pushups = request.form.get('pushups')
    comment = request.form.get('comment')

    workout, error = WorkoutService.create_workout(current_user.id, date, pushups, comment)
    if error:
        flash(error, 'danger')
        return redirect(url_for('workouts.add_workout'))

    flash('Workout added successfully!', 'success')
    return redirect(url_for('workouts.index'))


@main.route('/workouts')
@login_required
def workouts():
    workouts = WorkoutService.get_user_workouts(current_user.id)
    return render_template('workouts/workouts.html', workouts=workouts)