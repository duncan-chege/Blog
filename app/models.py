from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(writer_id):
    return User.query.get(int(writer_id))

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)

    writer_id = db.Column(db.Integer, db.ForeignKey('writer.id'))       #one writer is shared by many users

    def __repr__(self):     #makes it easier to debug our applications.
        return f'User {self.username}'

class Writer(UserMixin,db.Model):
    __tablename__ = 'writer'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
   
    users = db.relationship('User',backref = 'writer',lazy="dynamic")     #db.relationship to create a virtual column that will connect with the foreign key

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
