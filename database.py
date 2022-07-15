from datetime import datetime 
from app import db 

class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    addresses= db.relationship('Addresses', backref='customer', lazy=True)
    idNumber = db.Column(db.Integer, nullable=False)
    passportNumber = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    lastUpdate = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    active = db.Column(db.Boolean)
    expiryDate = db.Column(db.DateTime, nullable=False)


    def __repr__(self) -> str:
        return f"<Customer: {self.name}, {self.surname}>"


class Addresses(db.Model):

    sequenceNo = db.Column(db.Integer, primary_key=True)
    line1 = db.Column(db.String(80), nullable=True)
    line2 = db.Column(db.String(80), nullable=True)
    line3 = db.Column(db.String(80), nullable=True)
    line4 = db.Column(db.String(80), nullable=True)
    code = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String(80), default="RESIDENTIAL")
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self) -> str:
        return f"<Address: {self.sequenceNo}, {self.line1}>"