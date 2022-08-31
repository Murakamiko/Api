from app import db
from app.models.base_entity import BaseEntity


class UserService(db.Model, BaseEntity):
    __tablename__ = "user_services"
    user_service_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.user_id"), nullable=False)
    service_id = db.Column(db.ForeignKey("services.service_id"), nullable=False)

    db.UniqueConstraint('user_id', 'service_id', name='uk_user_services')

    rel_user = db.relationship('User', back_populates="services")
    rel_service = db.relationship('Service', back_populates="users")