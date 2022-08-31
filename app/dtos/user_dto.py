from typing import Any, Dict, List

from app.models.user        import User
from app.dtos.address_dto   import AddressDTO
from app.dtos.role_dto      import RoleDTO


class UserDTO():
    def __init__(self) -> None:
        self.user_id     = None
        self.username    = None
        self.password    = None
        self.mail        = None
        self.description = None
        self.roles: List[RoleDTO]  = []

    def getDTO(self):
        return self

    def getJSON(self):
        return self.__dict__

    @staticmethod
    def entity_to_dto(user: User):
        userdto = UserDTO()

        userdto.user_id     = user.user_id
        userdto.username    = user.username
        userdto.mail        = user.mail
        userdto.description = user.description
        userdto.roles       = [RoleDTO.entity_to_dto(role.rel_role) for role in user.roles]

        return userdto

    def dto_to_entity(self) -> User:
        user = User()

        user.user_id     = self.user_id
        user.username    = self.username
        user.password    = self.password
        user.mail        = self.mail
        user.description = self.description

        user.roles       = [role.dto_to_entity() for role in self.roles]

        return user

    def get_attributes(self):
        return {
        "username":     self.username,
        "mail":         self.mail,
        "description":  self.description
        }

    def load_from_attr_dict(self, dict: Dict[Any, Any]):
        self.username        = dict['username']
        self.mail            = dict['mail']
        self.description     = dict['description']

        return self

    def get_roles(self):
        return [role.rolename for role in self.roles]
        
"""class UserService(BaseService):
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
        db.session.commit()"""