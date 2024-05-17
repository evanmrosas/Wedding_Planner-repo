from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Budget:
    def __init__(self, data):
        self.id = data('id')
        self.item_name = data('item_name')
        self.price = data('price')
        self.created_at = data('created_at')
        self.updated_at = data('updated_at')

    @classmethod
    def get_all_items(cls):
        query = "SELECT budget_items.id, budget_items.item_name, budget_items.price FROM budget_items;"
        results = connectToMySQL('planners_db').query_db(query)
        print("Results: ", results)
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
        query = "INSERT INTO budget_items (item_name, price, user_id, created_at, updated_at) VALUES (%(item_name)%, %(price)%, %(user_id)%, NOW(), NOW());"
        results = connectToMySQL('planners_db').query_db(query, data)
        return results
    
    @classmethod
    def delete_item(cls, data):
        query = "DELETE FROM budget_items WHERE id = %(id)s;"
        results = connectToMySQL('planners_db').query_db(query, data)
        return results
    
    # @staticmethod
    # def validate_item(item):
    #     is_valid = True
    #     query = "SELECT * FROM users WHERE id = %(id)s;"
    #     results = connectToMySQL('planners_db').query_db(query, item)
    #