from datetime import datetime 
from app import db 

class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float(precision=10, scale=2), nullable=False)
    idNumber = db.Column(db.Integer, nullable=False)
    passportNumber = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    dateCreated = db.Column(db.Datetime, default=datetime.utcnow(), nullable=False)
    lastUpdate = db.Column(db.Datetime, default=datetime.utcnow(), nullable=False)
    active = db.Column(db.Boolean, default=True nullable=False)
    expiryDate = db.Column(db.Datetime, nullable=False)


    def __repr__(self) -> str:
        return f"<Customer: {self.name}, {self.surname}>"