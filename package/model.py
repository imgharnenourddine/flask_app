from package import db
from datetime import datetime
class user(db.Model):
    id_user=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(25),nullable=False)
    lname=db.Column(db.String(25),nullable=False)
    username=db.Column(db.String(25),unique=True,nullable=False)
    email=db.Column(db.String(60),unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    image_field=db.Column(db.String(60),nullable=False,default='default.jpg')
    date_inser=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    lesson=db.relationship('lesson',backref='author',lazy=True)#la 1 ere ligne que je veux comrendre
    def __repr__(self):
        return f'USER({self.fname},{self.lname},{self.username},{self.email},{self.image_field})'
class lesson(db.Model):
    id_lesson=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(25),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id_user'),nullable=False)#la 2 eme ligne que je veux comrendre
    def __repr__(self):
        return f'ce livre est de nome {self.fname}'