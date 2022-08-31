from app import db
from app.models.base_entity import BaseEntity

class Role(db.Model, BaseEntity):
    __tablename__ = "roles"
    roleid = db.Column(db.Integer, primary_key = True)
    rolename = db.Column(db.String(50), nullable, unique = True, index = True)
    users = db.relationship('UserRole')