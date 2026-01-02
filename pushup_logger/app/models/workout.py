from app.extensions import db


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    pushups = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship('User', backref=db.backref('workouts', lazy=True))

    def __repr__(self):
        return f'<Workout {self.date} - {self.pushups} pushups>'