#data models
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
#first entity
class User_Info(db.Model):
  __tablename__="user_info"
  id=db.Column(db.Integer, primary_key=True)
  email=id.Column(db.String, unique=True, nullable=False)
  password=db.Column(db.String,nullable=False)
  role=db.Column(db.Integer, default=1)
  full_name=db.Column(db.String,nullable=False)
  address=db.Column(db.String, nullable=False)
  pin_code=db.Column(db.Integer, nullable=False)
  #relations we write later

#entity2 theatre
class Theatre(db.Model):
  __tablename__="theatre"
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String,nullable=False)
  location=db.Column(db.String,nullable=False)
  pin_code=db.Column(db.Integer, nullable=False)
  capacity=db.Column(db.Integer, nullable=False)
  #relationships to be defined

#entity3 show table
class Show(db.Model):
  __tablename__="show"
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String,nullable=False)
  tags=db.Column(db.String,nullable=False)
  pin_code=db.Column(db.Integer, nullable=False)
  rating=db.Column(db.Integer,default=0)
  tkt_price=db.Column(db.Float, default=0.0)
  date_time=db.Column(db.DateTime, nullable=False)
  theatre_id=db.Column(db.Interger, db.ForeignKey("theater.id"),nullable=False)
  #relationships ...

#entity4 ticket
class Ticket(db.Model):
  __tablename__="ticket"
  id=db.Column(db.Integer,primary_key=True)
  no_of_tickets=db.Column(db.Integer,nullable=False)
  sl_nos=db.Column(db.String,nullable=False)
  user_rating=db.Column(db.Integer,default=0)
  user_id=db.Column(db.Interger, db.ForeignKey("user_info.id"),nullable=False)
  show_id=db.Column(db.Interger, db.ForeignKey("show.id"),nullable=False)

