from flask_app import app
from flask_app.controllers import budgets, users, gifts, guests, weddings

if __name__ == "__main__":
    app.run(debug=True)
