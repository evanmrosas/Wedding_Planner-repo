from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.inspiration import Inspiration



@app.route("/wedding/inspiration/user_photos")
def show_inspirations():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    data = {'id' : session['user_id']}
    user = User.get_one_by_id(data)
    inspirations = Inspiration.get_all_for_user(data)
    return render_template("user_photos.html")

@app.route("/add_photos", methods=['POST'])
def add_photos():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    data = {
        'file' : request.form['partner_name_1'],
        'category' : request.form['partner_name_2'],
        'description' : request.form['location'],
        'user_id' : request.form['date']
    }