from flask_app.config.mysqlconnection import connectToMySQL

class Budget:
    db = "wedding_schema"
    def __init__(self, data):
        self.id = data['id']
        self.total = data['total']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.budget_items = []

    @classmethod
    def get_budget(cls):
        query = "SELECT * FROM budget"
        results = connectToMySQL(cls.db).query_db(query)
        if results:
            return results[0]
        else:
            return None
    
    @classmethod
    def add_budget(cls, data):
        query = "INSERT INTO budget (total , user_id, created_at, updated_at) VALUES (%(total)s, %(user_id)s, NOW(), NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def update_budget(cls, data):
        query = "UPDATE budget SET total = %(total)s, updated_at = NOW() WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results