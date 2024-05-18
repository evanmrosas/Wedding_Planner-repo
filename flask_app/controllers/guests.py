from flask_app import app
from flask import render_template,redirect,session,flash,request
from flask_app.models import guest,user


@app.route('/guests')
def guest_dashboard():
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    guests = guest.Guest.get_all_guests()
    
    return render_template('rsvp_dash.html', guests = guests)

@app.route('/guests/new')
def new_guest():
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    return render_template('rsvp_new.html')

@app.route('/guests/create', methods=['POST'])
def add_guest():
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    if not guest.Guest.validate_guest(request.form):
        return redirect('/guests/new')
    guest.Guest.save_guest(request.form)
    return redirect('/guests')

@app.route('/guests/edit/<int:id>')
def edit_guest(id):
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    one_guest = guest.Guest.get_one_guest(id)
    
    return render_template('edit_guest.html', one_guest= one_guest)

@app.route('/guests/edit', methods=['POST'])
def update_guest():
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    if not guest.Guest.validate_guest(request.form):
        return redirect(f'/guests/edit/{request.form["id"]}')
    data={'id':id
    }
    guest.Guest.update_guest(data)
    return redirect('/guests')

@app.route('/guests/delete/<int:id>')
def delete_guest(id):
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    data={
        'id':id
    }
    guest.Guest.delete_guest(data)
    return redirect('/guests')