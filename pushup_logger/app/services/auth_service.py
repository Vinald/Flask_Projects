from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.models.user import User


class AuthService:
    @staticmethod
    def create_user(name: str, email: str, password: str) -> tuple[User | None, str | None]:
        """Create a new user. Returns (user, None) on success or (None, error_message) on failure."""
        if User.query.filter_by(email=email).first():
            return None, "Email already registered"

        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return user, None

    @staticmethod
    def authenticate(email: str, password: str) -> tuple[User | None, str | None]:
        """Authenticate user. Returns (user, None) on success or (None, error_message) on failure."""
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None, "Invalid email or password"
        return user, None

    @staticmethod
    def validate_signup(name: str, email: str, password: str, confirm_password: str) -> str | None:
        """Validate signup data. Returns error message or None if valid."""
        if not all([name, email, password, confirm_password]):
            return "All fields are required"
        if password != confirm_password:
            return "Passwords do not match"
        if len(password) < 6:
            return "Password must be at least 6 characters"
        return None