from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask("iiecapp")
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb/data.sqlite'


#ORM
db=SQLAlchemy(app)

print(db)

class IIEC(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    remarks=db.Column(db.Text)

    def __init__(self,name,age,remarks):
      self.name=name
      self.age=age
      self.remarks=remarks

db.create_all()
    
    
jACK=IIEC("jack",20,"ok")
db.session.add(jack)
db.session.commit()



r2=IIEC.query.get(2)
print(r2)
    

