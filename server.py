#import the app and the controller files 
from flask_app import app 
from flask_app.controllers import gifts, users





#never forget the name/main part

if __name__ == "__main__":
    app.run(debug = True)