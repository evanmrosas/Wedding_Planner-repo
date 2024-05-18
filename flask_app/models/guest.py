from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.controllers import guests
from flask_app.models import user


class Guest:
    db = "planners_db"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.attending = data['attending']
        self.attendee = None

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
            one_guest.attendee = user.User(user_data)
            all_guests.append(one_guest)
        return all_guests
    

    @classmethod
    def get_one_guest(cls,data):
        query = """
            SELECT * FROM guests
            JOIN users ON guests.user_id = users.id
            WHERE guests.id = %(id)s;
        """

        results = connectToMySQL(cls.db).query_db(query,data)
        one_guest = cls(results[0])

        user_data ={
                'id' :results[0]['users.id'],
                'first_name' :results[0]['first_name'],
                'last_name' :results[0]['last_name'],
                'email' :results[0]['email'],
                'password' :results[0]['password'],
                'created_at' :results[0]['users.created_at'],
                'updated_at' :results[0]['users.updated_at'],
        }
        one_guest.attendee = user.User(user_data)
        return one_guest


    @classmethod
    def update_guest(cls,data):
        query = """
            UPDATE guests
            SET first_name=%(first_name)s, last_name=%(last_name)s,  attending=%(attending)s
            WHERE id=%(id)s;
        """
        return connectToMySQL(cls.db).query_db(query,data)


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
            flash('Last name must be at least 2 characters' 'guest')
        if len(data['attending']) <3:
            is_valid=False
            flash('Comments must be at least 3 charcters long', 'show')
        return is_valid