from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 

model_db = 'private_wall'




class Message:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.sender = data['sender']
        self.receiver_id = data['reveiver_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
