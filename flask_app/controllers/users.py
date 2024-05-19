from flask import Flask, render_template, redirect, session, flash,request
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def welcome():
    print('==== in welcome route ====')
    return render_template('/welcome.html')

@app.route('/register')
def register_form():
    print('====IN REGISTER ROUTE====')
    return render_template('/register.html')

@app.route('/login')
def login_form():
    print('====IN LOGIN ROUTE====')
    return render_template('/login.html')


@app.route('/dashboard')
def dashboard():

    return render_template('/dashboard.html')


@app.route('/register', methods=['POST'])
def register():
    print('==== in register post route ====')
    if not User.is_valid_register(request.form):
        flash("Invalid registration data", "error")
        return redirect('/register')
    data={"email": request.form['email']}
    user_in_db = User.get_one_by_email(data)
    if user_in_db:
        flash("Account already exists!", "error")
        return redirect('/register')
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
        return redirect ('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid password', 'login')
        return redirect('/login')
    
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    print('in login route')
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


