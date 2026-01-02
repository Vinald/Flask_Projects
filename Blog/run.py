from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Registered routes:")
    for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
        methods = ','.join(sorted(rule.methods))
        print(f"{rule.rule} -> {rule.endpoint} [{methods}]")
    app.run(debug=True, use_reloader=True)