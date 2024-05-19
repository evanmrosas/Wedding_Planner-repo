from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Guest:
    db = "wedding_schema"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.attending = data['attending']
        self.user = None

    @classmethod
    def save_guest(cls,data):
        query="""
            INSERT INTO guests (first_name, last_name, attending, user_id)
            VALUES (%(first_name)s, %(last_name)s, %(attending)s,  %(user_id)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)
    

    @classmethod
    def get_all_guests(cls):
        query="""
            SELECT * FROM guests
            JOIN users ON guests.user_id = users.id;
        """
        results = connectToMySQL(cls.db).query_db(query)

        all_guests = []

        for row in results:
            one_guest = cls(row)

            user_data={
                'id' :row['users.id'],
                'first_name' :row['first_name'],
                'last_name' :row['last_name'],
                'email' :row['email'],
                'password' :row['password'],
                'created_at' :row['users.created_at'],
                'updated_at' :row['users.updated_at'],
            }
            one_guest.user = user.User(user_data)
            all_guests.append(one_guest)
        return all_guests
    

    @classmethod
    def get_one_guest(cls, id):
        data={
            "guest_id" : id
        }
        query = """
        SELECT guests.*, users.id AS user_id, users.first_name, users.last_name, users.email, users.password, users.created_at AS user_created_at, users.updated_at AS user_updated_at
        FROM guests
        LEFT JOIN users ON guests.user_id = users.id
        WHERE guests.id = %(guest_id)s;
        """

        results = connectToMySQL(cls.db).query_db(query,data)
        

        guest_data = results[0]
        guest = cls(guest_data)

        user_data ={
                'id' :guest_data['user_id'],
                'first_name' :guest_data['first_name'],
                'last_name' :guest_data['last_name'],
                'email' :guest_data['email'],
                'password' :guest_data['password'],
                'created_at' :guest_data['user_created_at'],
                'updated_at' :guest_data['user_updated_at'],
        }
        guest.user = user.User(user_data)
        return guest


    @classmethod
    def update_guest(cls,data):
        query = """
            UPDATE guests
            SET first_name=%(first_name)s, last_name=%(last_name)s,  attending=%(attending)s
            WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            return results


    @classmethod
    def delete_guest(cls,data):
        query = """
            DELETE FROM guests
            WHERE id=%(id)s;
        """
        return connectToMySQL(cls.db).query_db(query,data)
    

    @staticmethod
    def validate_guest(data):
        is_valid=True

        if len(data['first_name']) <2:
            is_valid=False
            flash('First name must be at least 2 characters', 'guest')
        if len(data['last_name']) <2:
            is_valid=False
            flash('Last name must be at least 2 characters', 'guest')
        
        return is_valid