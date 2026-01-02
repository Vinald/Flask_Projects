# Pushup Logger

A Flask web application to track and log your daily pushup workouts. Keep yourself accountable and monitor your fitness progress over time.

## Features

- **User Authentication**: Secure signup, login, and logout functionality
- **Workout Tracking**: Log your daily pushups with date and optional comments
- **CRUD Operations**: Create, view, edit, and delete workout entries
- **Pagination**: Browse through your workout history with paginated results
- **User Profiles**: Personal dashboard to view your workout statistics

## Tech Stack

- **Backend**: Flask 3.1
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Frontend**: Jinja2 templates with Bootstrap
- **Server**: Gunicorn (production)

## Project Structure

```
pushup_logger/
├── run.py                 # Application entry point
├── requirements.txt       # Python dependencies
├── app/
│   ├── __init__.py       # App factory
│   ├── extensions.py     # Flask extensions (db)
│   ├── models/
│   │   ├── user.py       # User model
│   │   └── workout.py    # Workout model
│   ├── routes/
│   │   ├── auth.py       # Authentication routes
│   │   ├── user.py       # User profile routes
│   │   └── workout.py    # Workout CRUD routes
│   ├── services/
│   │   ├── auth_service.py    # Auth business logic
│   │   └── workout_service.py # Workout business logic
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── auth/
│       ├── partials/
│       ├── users/
│       └── workouts/
└── instance/
    └── push.sqlite3      # SQLite database
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Vinald/Flask_Projects.git
   cd Flask_Projects/pushup_logger
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)

   Create a `.env` file in the project root:

   ```env
   SECRET_KEY=your-secret-key
   SQLALCHEMY_DATABASE_URI=sqlite:///push.sqlite3
   ```

5. **Run the application**

   ```bash
   python run.py
   ```

   The app will be available at `http://127.0.0.1:5000`

## Usage

1. **Sign Up**: Create a new account with your name, email, and password
2. **Log In**: Access your personal dashboard
3. **Add Workout**: Log your pushups with the date and an optional comment
4. **View Workouts**: Browse all your logged workouts with pagination
5. **Edit/Delete**: Modify or remove workout entries as needed

## API Routes

| Route                  | Method    | Description                   |
| ---------------------- | --------- | ----------------------------- |
| `/`                    | GET       | Home page                     |
| `/signup`              | GET, POST | User registration             |
| `/login`               | GET, POST | User login                    |
| `/logout`              | GET       | User logout                   |
| `/workouts`            | GET       | View all workouts (paginated) |
| `/add_workout`         | GET, POST | Add a new workout             |
| `/edit_workout/<id>`   | GET, POST | Edit an existing workout      |
| `/delete_workout/<id>` | POST      | Delete a workout              |
| `/profile`             | GET       | User profile page             |

## License

This project is open source and available under the [MIT License](../LICENSE).
