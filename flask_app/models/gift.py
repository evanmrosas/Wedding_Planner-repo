#import mysql connection
from flask_app.config.mysqlconnection import connectToMySQL

#import flash for error messages
from flask import Flask, flash
#import user model for including in methods 
from flask_app.models import user
#import re for validation just in case needed
import re


class Gift:
    db= "wedding_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["gift_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["created_at"]



#create
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO gifts (gift_name) 
        VALUES (%(gift_name)s);
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            return results



#read one
    @classmethod
    def get_one_gift(cls, id):
        data = {
            "id" : id
        }
        query="SELECT * FROM gifts LEFT JOIN users ON user_id = users.id WHERE gifts.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        gift = cls(results[0])

        user_data ={
                "id" : results[0]["users.id"],
                "first_name" : results[0]["first_name"],
                "last_name" : results[0]["last_name"],
                "email" : results[0]["email"],
                "password" : results[0]["password"],
                "created_at" : results[0]["users.created_at"],
                "updated_at" : results[0]["users.updated_at"] 
        }
        gift.user = user.User(user_data)
        return gift



#read all
#read
    @classmethod 
    def getAllGifts(cls):
        query = "SELECT * FROM gifts;"
        results = connectToMySQL(cls.db).query_db(query)
        gifts = []
        for gift in results:
            gifts.append(cls(gift))
        return gifts


#update
    @classmethod
    def update_gift(cls, data):
        query="UPDATE gifts SET gift_name = %(gift_name)s WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            return results



#delete 
    @classmethod
    def delete_gift(cls, id):
        data = {
            "id" : id
        }
        query= "DELETE FROM gifts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            return results



#validate
    @staticmethod
    def validate_gift(gift):
        is_valid = True
        if len(gift['gift_name']) <1:
            flash("Gift must have a name", "gift")
            is_valid = False


        return is_valid