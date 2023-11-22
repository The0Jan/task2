from project import db, app
import random

def hide_confidential(data:str, up_rand:int) -> str:
    str_len:int = len(data)
    if up_rand == 0:
        return str_len * '*'
    randomized_len = random.randrange(str_len, str_len + up_rand)
    return '*'*randomized_len

# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)
    pesel = db.Column(db.String(64))
    street = db.Column(db.String(128))
    appNo = db.Column(db.String(10))

    def __init__(self, name, city, age, pesel, street, appNo):
        self.name = name
        self.city = city
        self.age = age
        self.pesel = pesel
        self.street = street
        self.appNo = appNo
        print("Getting: " + str(self),flush=True)

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age}, Pesel: {hide_confidential(self.pesel, 0)}, Street: {hide_confidential(self.street, 4)}, AppNo: {hide_confidential(self.appNo, 1)})"


with app.app_context():
    db.create_all()
