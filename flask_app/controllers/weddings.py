from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.wedding import Wedding

# adds wedding if none has been set, shows wedding if one has been set
@app.route('/wedding/info')
def wedding_info():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    session['user_id'] = 1
    data = {'id' : session['user_id']}
    user = User.get_one_by_id(data)
    wedding = Wedding.get_all_for_user(session['user_id'])
    if wedding is None:
        return render_template("new_wedding.html", user = user)
    else:
        return render_template('/wedding_info.html', wedding = wedding, user = user)

@app.route('/add_wedding', methods=['POST'])
def add_wedding():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    data = {
        'partner_name_1' : request.form['partner_name_1'],
        'partner_name_2' : request.form['partner_name_2'],
        'location' : request.form['location'],
        'date' : request.form['date'],
        'reception' : request.form['reception'],
        'total_guest' : request.form['total_guest'],
        'notes' : request.form['notes'],
        'user_id' : request.form['user_id']
    }
    if not Wedding.validate_wedding(data):
        return redirect('/wedding/info')
    Wedding.save(data)
    return redirect('/wedding/info')


# edit wedding, get and post
# if no wedding is set, you can create a new wedding
@app.route('/wedding/info/edit')
def edit_wedding_info():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    session['user_id'] = 1
    data = {'id' : session['user_id']}
    user = User.get_one_by_id(data)
    wedding = Wedding.get_all_for_user(session['user_id'])
    if wedding is None:
        return render_template("new_wedding.html", user = user)
    else:
        return render_template('/edit_wedding.html', wedding = wedding, user = user)


@app.route('/edit_wedding', methods=['POST'])
def edit_wedding():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    data = {
        'partner_name_1' : request.form['partner_name_1'],
        'partner_name_2' : request.form['partner_name_2'],
        'location' : request.form['location'],
        'date' : request.form['date'],
        'reception' : request.form['reception'],
        'total_guest' : request.form['total_guest'],
        'notes' : request.form['notes'],
        'user_id' : request.form['user_id']
    }
    if not Wedding.validate_wedding(data):
        return redirect('/wedding/info/edit')
    Wedding.update(data)
    return redirect('/wedding/info')