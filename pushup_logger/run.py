from app import create_app   # or inner import if needed
app = create_app()

# Print URL map for debugging when the server starts
if __name__ == "__main__":
    print("Registered routes:")
    for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
        methods = ','.join(sorted(rule.methods))
        print(f"{rule.rule} -> {rule.endpoint} [{methods}]")
    app.run(debug=True, use_reloader=True)