from flask import session

from app.dtos.user_dto import UserDTO

from app.services.user_service import UserService

from app.framework.decorators.inject import inject


class AuthService():
    @inject
    def __init__(self, userservice: UserService):
        self.userservice = userservice
     
    def get_current_user(self):
        if session.get('userid'):
            return self.userservice.find_one(session.get('userid')) 
        return UserDTO()