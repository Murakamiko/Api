from app import db
from app.models.base_entity import BaseEntity

class Post(db.Model, BaseEntity):
    __tablename__ = "posts"
    postid = db.Column(db.Integer,primary_key = True)
    authorid = db.Column(db.ForeignKey("users.userid"), nullable = False)
    content = db.Column(db.String(2000), nullable = False)
    
    rel_author = db.relationship("User", back_populates = "user")

