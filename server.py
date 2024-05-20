from flask_app import app
from flask_app.controllers import budgets, gifts, guests, users, weddings

if __name__ == "__main__":
    app.run(debug=True)
