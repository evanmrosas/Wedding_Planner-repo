from flask_app.config.mysqlconnection import connectToMySQL

class Budget_Items:
    db = "wedding_planner_db"
    def __init__(self, data):
        self.id = data['id']
        self.item_name = data['item_name']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_items(cls):
        query = "SELECT id, item_name, price FROM budget_items;"
        results = connectToMySQL(cls.db).query_db(query)
        budget_list = []
        for result in results:
            budget_data = {
                'id': result['id'],
                'item_name': result['item_name'],
                'price': result['price']
            }
            budget_list.append(budget_data)
        return budget_list
    
    @classmethod
    def add_item(cls, data):
        query = "INSERT INTO budget_items (item_name, price, budget_id, created_at, updated_at) VALUES (%(item_name)s, %(price)s, %(budget_id)s, NOW(), NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def delete_item(cls, data):
        query = "DELETE FROM budget_items WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
