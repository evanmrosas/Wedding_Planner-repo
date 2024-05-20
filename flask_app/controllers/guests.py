from flask_app import app
from flask import render_template,redirect,session,flash,request
from flask_app.models import guest


@app.route('/guests')
def guest_dashboard():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    guests = guest.Guest.get_all_guests()
    
    return render_template('rsvp_dash.html', guests = guests)

@app.route('/guests/new')
def new_guest():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    guests = guest.Guest.get_all_guests()
    return render_template('rsvp_new.html', guest = guests)

@app.route('/guests/create', methods=['POST'])
def add_guest():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    if not guest.Guest.validate_guest(request.form):
        return redirect('/guests/new')
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "attending": request.form["attending"],
        "user_id":session["user_id"]
    }
    guest.Guest.save_guest(data)
    return redirect('/guests')

@app.route('/guests/edit/<int:id>')
def edit_guest(id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    one_guest = guest.Guest.get_one_guest(id)
    
    return render_template('edit_rsvp.html', one_guest= one_guest)

@app.route('/guests/update/<int:id>', methods=['POST'])
def update_guest(id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    if not guest.Guest.validate_guest(request.form):
        return redirect(f'/guests/edit/{request.form["id"]}')
    data={'id':id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "attending" : request.form["attending"]
    }
    guest.Guest.update_guest(data)
    return redirect('/guests')

@app.route('/guests/delete/<int:id>')
def delete_guest(id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    data={
        'id':id
    }
    guest.Guest.delete_guest(data)
    return redirect('/guests')