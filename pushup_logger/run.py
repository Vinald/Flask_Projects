from src import create_app   # or inner import if needed
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)