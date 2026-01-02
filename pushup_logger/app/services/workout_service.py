from datetime import datetime
from app.extensions import db
from app.models.workout import Workout


class WorkoutService:
    @staticmethod
    def create_workout(user_id: int, date: str, pushups: str, comment: str) -> tuple[Workout | None, str | None]:
        """Create a new workout. Returns (workout, None) on success or (None, error_message) on failure."""
        error = WorkoutService.validate_workout(date, pushups)
        if error:
            return None, error

        workout = Workout(
            user_id=user_id,
            date=datetime.strptime(date, '%Y-%m-%d').date(),
            pushups=int(pushups),
            comment=comment or None
        )
        db.session.add(workout)
        db.session.commit()
        return workout, None

    @staticmethod
    def validate_workout(date: str, pushups: str) -> str | None:
        """Validate workout data. Returns error message or None if valid."""
        if not date:
            return "Date is required"
        if not pushups:
            return "Pushups count is required"
        try:
            if int(pushups) < 0:
                return "Pushups must be a positive number"
        except ValueError:
            return "Pushups must be a valid number"
        return None

    @staticmethod
    def get_user_workouts(user_id: int) -> list[Workout]:
        """Get all workouts for a user."""
        return Workout.query.filter_by(user_id=user_id).order_by(Workout.date.desc()).all()