from app import db
from app.models.base_entity import BaseEntity
from app.models.user import User
from app.models.user_service import UserService


class Service(db.Model, BaseEntity):
    __tablename__ = "services"
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    service_type = db.Column(db.ForeignKey('service_types.service_type_id'), nullable=False)
    request = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.Text)

    users = db.relationship('UserService', cascade='all')
    type = db.relationship('ServiceType')

    def add_user(self, user: User):
        if user in self.get_users():
            return
        user_service = UserService()
        user_service.rel_user = user
        user_service.rel_service = self
        self.users.append(user_service)

    def remove_user(self, user: User):
        user_service: UserService
        for user_service in self.users:
            if user_service.user_id == user.user_id:
                self.users.remove(user_service)
                break

    def get_users(self):
        return [user.rel_user for user in self.users]

    def __str__(self):
        return f"[{self.service_id}] {self.name} {self.service_type} {self.request} {self.description}"