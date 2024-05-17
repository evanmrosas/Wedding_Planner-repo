from flask_app.config.mysqlconnection import connectToMySQL

class Wedding:
    db="wedding_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.partner_name_1 = data["partner_name_1"]
        self.partner_name_2 = data["partner_name_2"]
        self.location = data["location"]
        self.date = data['date']
        self.reception = data["reception"]
        self.total_guest = data['total_guest']
        self.notes = data["notes"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
        # date
        # guest list
        # gift list
        # partner1
        # partner 2
        # location
        # reception - can potentially be a whole other planning center ordeal, but 
        #   maybe we stick with a dictionary: address, time, kids_allowed
        # notes
        # user_id because a wedding cant exist without a user

    @classmethod
    def save(cls, data):
        query = """INSERT INTO  --database--(partner_name_1, partner_name_2, location, date, reception, total_guest, notes, user_id, created_at, updated_at) 
                VALUES ( %(partner_name_1)s, %(partner_name_2)s, %(location)s, %(date)s, %(reception)s, %(total_guest)s, %(notes)s, %(user_id)s, NOW(), NOW())
            """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_for_user(cls, user_id):
        query = """SELECT * from weddings 
                WHERE user_id = %(user_id)s """
        data = {"id" : user_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result)
        

    @classmethod
    def get_one(cls, wedding_id):
        query = """SELECT * from weddings 
        WHERE id = %(wedding_id)s
            """
        data = {"id" : wedding_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE weddings
                SET partner_name_1 = %(partner_name_1)s, partner_name_2%(partner_name_2)s, location = %(location)s, date = %(date)s, recption = %(reception)s, total_guest = %(total_guest)s, notes = %(notes)s, user_id = %(user_id)s
            """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls, wedding_id):
        query = """DELETE from weddings 
                WHERE id = %(wedding_id)s """
        data = {"id" : wedding_id}
        return connectToMySQL(cls.db).query_db(query, data)