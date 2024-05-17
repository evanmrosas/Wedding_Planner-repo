# import all the things to make the app work 
from flask import Flask, render_template, redirect, request, session
#import the models
from flask_app.models import gift, user

#create the app itself
app = Flask(__name__)
#secret key for session
app.secret_key = "secret"