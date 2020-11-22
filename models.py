import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Boolean, Date, Numeric
from flask_migrate import Migrate

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    print("Setting up DB")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
Model Customer
    Defines Table Customer
'''
class Customer(db.Model):
  __tablename__ = 'customer'

  id = Column(Integer, primary_key=True)
  first_name = Column(String(100))
  last_name = Column(String(100))
  address = Column(String(100))
  date_of_birth = Column(Date)
  recieve_newsletter = Column(Boolean)

  orders = db.relationship('Order', backref='customer')

# not complete yet
  def format(self):
    return {
    'id': self.id,
    'first_name': self.first_name,
    'last_name': self.last_name}


def insert(self):
  db.session.add(self)
  db.session.commit()

def update():
  db.session.commit()

def delete(self):
  db.session.delete(self)
  db.session.commit()

'''
Model Customer
    Defines Table Customer
'''
class Order(db.Model):
  __tablename__ = 'order'

  id = Column(Integer, primary_key=True)
  manufacturer = Column(String(100))
  name_long = Column(String(100))
  name_short = Column(String(100))
  molecules = Column(String(100))
  price = Column(Numeric) 

  customer_id = Column(Integer, ForeignKey('customer.id'))

'''
CRUD functions for DB interaction
  defines functions in model scope
'''
def insert(self):
  db.session.add(self)
  db.session.commit()

def update():
  db.session.commit()

def delete(self):
  db.session.delete(self)
  db.session.commit()



