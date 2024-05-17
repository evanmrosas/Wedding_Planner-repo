from flask_app import app
# ...server.py
from flask_app.controllers import weddings

#from flask_app.models.user import User
from flask_app.models.wedding import Wedding

if __name__ == '__main__':
    app.run(debug = True)