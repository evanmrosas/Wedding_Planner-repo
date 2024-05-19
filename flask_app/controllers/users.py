from flask import Flask, render_template, redirect, session, flash,request
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def reg_login():
    print('==== in reg login route ====')
    return render_template('/reg_login.html')

@app.route('/register', methods=['POST'])
def register():
    print('==== in register post route ====')
    if not User.is_valid_register(request.form):
        return redirect('/')
    data={"email": request.form['email']}
    user_in_db = User.get_one_by_email(data)
    if user_in_db:
        flash("Account already exists!","reg")
        return redirect('/')
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.save_user(data)
    session['user_id'] = user_id
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    print('==== in login route ====')
    data = {
        'email': request.form['email']
    }
    user= User.get_one_by_email(data)
    if not user:
        flash('Invalid Email/Password', 'login')
        return redirect ('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid password', 'login')
        return redirect('/')
    
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    print('in login route')
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')