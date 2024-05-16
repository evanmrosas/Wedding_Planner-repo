from flask import Flask, render_template, redirect, request, session, flash
from server import app
from flask_app.models import gift


#dashboard
@app.route("/dashboard")
def dashboard():
    # if "userID" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")
    
    
    return render_template("dashboard.html")

#show all
@app.route("/giftregistry")
def giftregistry():
    # if "userID" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")
    gifts = gift.Gift.getAllGifts()
    print(gifts)
    return render_template("giftregistry.html", gifts = gifts)

#create new gift form
@app.route("/giftregistry/new")
def new_gift_form():
    # if "userID" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")
    return render_template("newgift.html")

#create new gift ACTION
@app.route("/giftregistry/create", methods=["POST"])
def create_gift():
    # if "userID" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")
    if not gift.Gift.validate_gift(request.form):
        return redirect("/giftregistry/new")
    data = {
        "gift_name": request.form["gift_name"],
    }
    gift.Gift.save(data)
    return redirect("/giftregistry")

#update gift Form
@app.route('/giftregistry/edit/<int:id>')
def edit_gift(id):
    # if "userID" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")
    data={ 
        "id" : id
    }
    gift_id = gift.Gift.get_one_gift(data)
    return render_template("editgift.html",gift=gift_id)

#update gift ACTION
@app.route('/giftregistry/update/<int:id>',methods=['POST'])
def update_gift():
    # if "userID" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")
    if not gift.Gift.validate_gift(request.form):
        return redirect(f"/recipe/edit/{request.form['id']}")
    data = {
        "name" : request.form["name"],
        "id" : id
    }
    gift.Gift.update_gift(data)
    return redirect("/giftregistry")

#delete gift 
@app.route("/giftregistry/delete/<int:id>")
def delete_gift(id):
    # if "userID" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")
    data={ 
        "id" : id
    }
    gift.Gift.delete(id)
    return redirect("/giftregistry")

