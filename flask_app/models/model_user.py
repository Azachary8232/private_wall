# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #<--- Add to /model top
model_db = "private_wall"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True 

        # for ***Text Input*** unknown
        if len(user['first_name']) < 2: 
            flash("First name must be included.", category= "first_name")
            is_valid = False 
        if len(user['last_name']) < 2: 
            flash("Last name must be included.", category= "last_name")
            is_valid = False 
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", category= "email")
            is_valid = False
        if len(user['password']) < 2: 
            flash("A password must be included.", category= "password")
            is_valid = False  
        if user['password'] != user['confirm_password']: 
            flash("Passwords must match.", category= "confirm_pw")
            is_valid = False  
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True 
        if len(user['email']) < 1: 
            flash("Please insert valid Email.", category= "login_email")
            is_valid = False  
        if len(user['password']) < 1: 
            flash("Please include a valid Password.", category= "login_password")
            is_valid = False  
        return is_valid



    # ***CREATE***

    @classmethod
    def create(cls,data):
        print("!!!!!")
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL("private_wall").query_db(query, data)




    # ***Retreive***

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(model_db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(model_db).query_db(query)
        return  result




    # ***Update***







    # ***Delete***