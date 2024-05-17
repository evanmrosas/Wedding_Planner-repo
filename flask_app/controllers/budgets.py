from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.budget import Budget

@app.route('/budget', methods=['GET'])
def budget_page():
    # if 'user_id' not in session:
    #     return redirect('/logout')
    # else:
    items = Budget.get_all_items()
    return render_template('budget.html', items = items)

@app.route('/add-item', methods=['POST'])
def add_item():
    data = {
        "item_name": request.form['item_name'],
        "price": request.form['price']
        # "user_id": session['user_id']
    }
    print(data)
    Budget.add_item(data)
    return redirect('/budget')