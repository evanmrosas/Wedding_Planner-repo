from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"


class User:
    db= 'wedding_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save_user(cls,data):
        print('====in save user method user model ====')
        query = """INSERT INTO users (first_name, last_name, email, password)
                VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"""
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    
    @classmethod
    def update_user(cls,data):
        ('====in update user method user model ====')
        query="""UPDATE users SET first_name=%(first_name)s,
                last_name=%(last_name)s,email=%(email)s
                WHERE id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    
    @classmethod
    def get_one_by_id(cls,data):
        print('====get one by id user model ====')
        query="""SELECT * FROM users WHERE id = %(id)s """
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        if result:
            return cls(result[0])
        
    @classmethod
    def get_one_by_email(cls,data):
        print('====get by email user model====')
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) <1 :
            return False
        return cls(results[0])
    
    @classmethod
    def delete_user(cls,data):
        print('==== in delete method user model ====')
        query="DELETE FROM users WHERE id = %(id)s"
        result =  connectToMySQL(cls.db).query_db(query,data)
        return result
    


    @staticmethod
    def is_valid_register(user_info):
        is_valid = True
        if len(user_info["first_name"]) <=1:
            flash("First name required! Must have 2 characters","reg")
            is_valid=False
        if len(user_info["last_name"]) <=1:
            flash("Last name required! Must have 2 characters","reg")
            is_valid = False
        if len(user_info["email"]) <=1:
            flash("Email name required!","reg")
        if not EMAIL_REGEX.match(user_info['email']): 
            flash("Invalid email address!","reg")
            is_valid = False
        if len(user_info["password"]) <=7:
            flash("Password required / Or to weak!","reg")
            is_valid = False
        if user_info["confirm_password"] != user_info["password"]:
            flash("Password must match!","reg")
            is_valid = False
        if not re.match(pattern, user_info['password']):
            flash("Password must contain an uppercase and lowercase letter and a number.","reg")
            is_valid = False
        print("validating user is valid:", is_valid)
        
        return is_valid