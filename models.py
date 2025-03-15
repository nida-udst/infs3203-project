from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Library(db.Model):
    __tablename__ = 'library'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), nullable=False)
    choices = db.Column(db.JSON, nullable=True)
    answer = db.Column(db.String(100), nullable = False)

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'choices': self.choices,
            'answer': self.answer
        } 