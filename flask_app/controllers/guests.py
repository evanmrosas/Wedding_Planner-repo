from flask_app import app
from flask import render_template,redirect,session,flash,request
from flask_app.models import guest,user


@app.route('/guests')
def guest_dashboard():
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    
    
    return render_template('rsvp_dash.html')

@app.route('/guests/new')
def new_guest():
    return render_template('rsvp_new.html')

@app.route('/guests/create', methods=['POST'])
def add_guest():
    if not guest.Guest.validate_guest(request.form):
        return redirect('/guests/new')
    guest.Guest.save_guest(request.form)
    return redirect('/guests')

@app.route('/guests/edit/<int:id>')
def edit_guest(id):
    #if "userID" not in session:
    #    flash("Please log in.", "login")
    #    return redirect("/")
    return render_template('edit_guest.html', one_guest=guest.Guest.get_one_guest)

@app.route('/guests/edit', methods=['POST'])
def update_guest():
    if not guest.Guest.validate_guest(request.form):
        return redirect(f'/guests/edit/{request.form["id"]}')
    
    guest.Guest.update_guest(request.form)
    return redirect('/guests')

@app.route('/guests/delete/<int:id>')
def delete_guest(id):
    data={
        'id':id
    }
    guest.Guest.delete_guest(data)
    return redirect('/guests')