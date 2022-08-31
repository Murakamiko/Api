from app import db
from app.models.base_entity import BaseEntity


class ServiceType(db.Model, BaseEntity):
    __tablename__ = "service_types"
    service_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)