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
        self.gift_name = data["gift_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["created_at"]
        self.user_id = data["user_id"]



#create
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO gifts (gift_name, user_id) 
        VALUES (%(gift_name)s, %(user_id)s);
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            return results



#read one
    # @classmethod
    # def get_one_gift(cls, id):
    #     data = {
    #         "id" : id
    #     }
    #     query="SELECT * FROM gifts LEFT JOIN users ON user_id = users.id WHERE gifts.id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     gift = cls(results[0])

    #     user_data ={
    #             "id" : results[0]["users.id"],
    #             "first_name" : results[0]["first_name"],
    #             "last_name" : results[0]["last_name"],
    #             "email" : results[0]["email"],
    #             "password" : results[0]["password"],
    #             "created_at" : results[0]["users.created_at"],
    #             "updated_at" : results[0]["users.updated_at"] 
    #     }
    #     gift.user = user.User(user_data)
    #     return gift

    @classmethod
    def get_one_gift(cls, id):
        print("=======get_one_gift classmethod========")
        data = {
            "gift_id" : id
        }
        query = """
        SELECT gifts.*, users.id AS user_id, users.first_name, users.last_name, users.email, users.password, users.created_at AS user_created_at, users.updated_at AS user_updated_at
        FROM gifts
        LEFT JOIN users ON gifts.user_id = users.id
        WHERE gifts.id = %(gift_id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        
        if not results:
            return None

        gift_data = results[0]
        gift = cls(gift_data)

        user_data = {
            "id": gift_data["user_id"],
            "first_name": gift_data["first_name"],
            "last_name": gift_data["last_name"],
            "email": gift_data["email"],
            "password": gift_data["password"],
            "created_at": gift_data["user_created_at"],
            "updated_at": gift_data["user_updated_at"]
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