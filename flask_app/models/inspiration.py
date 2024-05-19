from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Inspiration:
    db= 'wedding_schema'
    def __init__(self, data):
        self.id = data['id']
        self.file = data['file']
        self.category = data['category']
        self.description = data['description']
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = """INSERT INTO  inspirations (file, cateogory, description, user_id, created_at, updated_at) 
                VALUES ( %(file)s, %(category)s, %(description)s, %(user_id)s, %(user_id)s, NOW(), NOW())
            """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_for_user(cls, user_id):
        query = """SELECT * from inspirations 
                WHERE user_id = %(user_id)s """
        data = {"user_id" : user_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        if not result:
            return None
        return cls(result[0])

    @classmethod
    def get_one(cls, inspiration_id):
        query = """SELECT * from inspirations 
        WHERE id = %(inspiration_id)s
            """
        data = {"id" : inspiration_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = """UPDATE inspirations
                SET file = %(file)s, category = %(category)s, description = %(description)s, user_id = %(user_id)s
            """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, inspiration_id):
        query = """DELETE from inspirations 
                WHERE id = %(inspiration_id)s """
        data = {"id" : inspiration_id}
        return connectToMySQL(cls.db).query_db(query, data)