from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.budget import Budget
from flask_app.models.budget_item import Budget_Items

@app.route('/budget', methods=['GET'])
def budget_page():
    budget = Budget.get_budget()
    print("budget data", budget)
    items = Budget_Items.get_all_items()
    return render_template('budget.html', items=items, budget=budget, budget_exists=budget is not None)

@app.route('/add-budget', methods=['POST'])
def add_budget():
    data = {
        "total": request.form['total'],
        "user_id": 1
    }
    Budget.add_budget(data)
    return redirect('/budget')

@app.route('/update-budget', methods=['POST'])
def update_budget():
    data = {
        "total": request.form['total'],
        "id": 2  # Assuming you have only one budget entry, or you need to pass the correct budget id
    }
    Budget.update_budget(data)
    return redirect('/budget')

@app.route('/add-item', methods=['POST'])
def add_item():
    data = {
        "item_name": request.form['item_name'],
        "price": request.form['price'],
        "budget_id": 2  # Default user_id until you set up user authentication
    }
    print(data)
    Budget_Items.add_item(data)
    return redirect('/budget')

@app.route('/update-item/<int:id>', methods=['POST'])
def update_item(id):
    data = {
        "id": id,
        "price": request.form['price']
    }
    print("updated data: ", data)
    Budget_Items.update_item(data)
    return redirect('/budget')

@app.route('/delete-item/<int:id>')
def delete_item(id):
    data = {"id": id}
    Budget_Items.delete_item(data)
    return redirect('/budget')
