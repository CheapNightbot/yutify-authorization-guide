from app import create_app

app = create_app()


if __name__ == "__main__":
    # Run the Flask application
    app.run(port=3500, debug=True)
