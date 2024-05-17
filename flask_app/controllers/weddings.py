from flask_app import app
from flask import render_template, redirect, request
# from flask_app.models.user import User
from flask_app.models.wedding import Wedding


@app.route('/new_wedding')
def new_wedding():
    return render_template("new_wedding.html")

@app.route('/add_wedding', methods=['POST'])
def add_wedding():
    data = {
        ''
    }