from bcrypt import gensalt, hashpw, checkpw
from app    import db

from app.models.user    import User
from app.models.role    import Role

from app.services.base_service import BaseService

from app.forms.user_register_form import UserRegisterform
from app.forms.user_login_form    import UserLoginform

from app.dtos.user_dto import UserDTO



class UserService(BaseService):
    def find_one(self, entity_id: int):
        return UserDTO.entity_to_dto(User.query.filter_by(user_id= entity_id).first())

    def find_all(self):
        return [UserDTO.entity_to_dto(user) for user in User.query.filter_by().all()]

    def find_one_by(self, **kwargs):
        try:
            return UserDTO.entity_to_dto(User.query.filter_by(**kwargs).first())
        except Exception as e:
            print(e)
            return None

    def find_one_by_address(self, **kwargs):
        try:
            return UserDTO.entity_to_dto(User.query.join(Address).filter_by(**kwargs).first())
        except Exception as e:
            print(e)
            return None


    def insert(self, data: UserDTO):
        user = data.dto_to_entity()
        encrypted_pass = hashpw(user.password.encode('utf-8'), gensalt()).decode('utf-8')
        user.password = encrypted_pass
        try:
            role_user = Role.query.filter_by(rolename="USER").first()
            user.add_role(role_user)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def login(self, data: UserLoginform):
        user = User.query.filter_by(username=data.login.data).first()
        if not user:
            user = User.query.filter_by(mail=data.login.data).first()
        if not user:
            return {"errors": f"username '{data.login.data}' does not exist"}
        
        if checkpw(data.password.data.encode('utf-8'), user.password.encode('utf-8')):
            return UserDTO.entity_to_dto(user)
        return {"errors" : "wrong password"}

    def update(self, userid: int, data: UserRegisterform):
        user = User.query.filter_by(user_id=userid).first()
        if not user:
            return None

        attr = user.get_attributes()
        for key, val in data.get_attributes().items():
            if val and val != "":
                attr[key] = val
        user.load_from_attr_dict(attr)

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return user

    def delete(self, entity_id: int):
        pass

    def add_role(self, userid: int, role: Role):
        user = User.query.filter_by(user_id=userid).first()
        if not user:
            return None

        user.add_role(role)
        db.session.commit()