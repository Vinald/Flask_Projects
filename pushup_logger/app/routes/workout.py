from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.services.workout_service import WorkoutService

workouts = Blueprint('workouts', __name__)


@workouts.route('/')
def index():
    return render_template('workouts/index.html')


@workouts.route('/add_workout')
@login_required
def add_workout():
    return render_template('workouts/add_workout.html')


@workouts.route('/add_workout', methods=['POST'])
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


@workouts.route('/workouts')
@login_required
def all_workouts():
    user_workouts = WorkoutService.get_user_workouts(current_user.id)
    return render_template('workouts/workouts.html', workouts=user_workouts)


@workouts.route('/delete_workout/<int:workout_id>', methods=['POST'])
@login_required
def delete_workout(workout_id):
    success = WorkoutService.delete_workout(workout_id)
    if not success:
        flash('Workout not found.', 'danger')
        return redirect(url_for('workouts.all_workouts'))

    flash('Workout deleted successfully!', 'success')
    return redirect(url_for('workouts.all_workouts'))


@workouts.route('/edit_workout/<int:workout_id>')
@login_required
def edit_workout(workout_id):
    workout = WorkoutService.get_workout_by_id(workout_id)
    if not workout:
        flash('Workout not found.', 'danger')
        return redirect(url_for('workouts.all_workouts'))
    return render_template('workouts/edit_workout.html', workout=workout)


@workouts.route('/edit_workout/<int:workout_id>', methods=['POST'])
@login_required
def edit_workout_post(workout_id):
    date = request.form.get('date')
    pushups = request.form.get('pushups')
    comment = request.form.get('comment')

    workout, error = WorkoutService.update_workout(workout_id, date, pushups, comment)
    if error:
        flash(error, 'danger')
        return redirect(url_for('workouts.edit_workout', workout_id=workout_id))

    flash('Workout updated successfully!', 'success')
    return redirect(url_for('workouts.all_workouts'))
