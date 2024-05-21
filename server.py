from flask_app import app

from flask_app.controllers import budgets, gifts, users, weddings, guests


if __name__ == "__main__":
    app.run(debug=True)
