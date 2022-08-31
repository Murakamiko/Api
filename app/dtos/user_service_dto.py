from app.models.user_service            import UserService
from app.dtos.abstract_dto              import AbstractDTO
from app.dtos.user_dto                  import UserDTO
from app.dtos.service_dto               import ServiceDTO

class UserServiceDTO(AbstractDTO):
    def __init__(self):
        self.user_service_id = None
        self.user_id         = None
        self.service_id      = None

        self.user            = UserDTO()
        self.service         = ServiceDTO()

    @staticmethod
    def build_from_entity(user_service: UserService):
        user_service_dto = UserServiceDTO()

        user_service_dto.user_service_id = user_service.user_service_id
        user_service_dto.user_id         = user_service.user_id
        user_service_dto.service_id      = user_service.service_id

        user_service_dto.rel_user        = UserDTO.entity_to_dto       (user_service.rel_user).user_id
        user_service_dto.rel_service     = ServiceDTO.build_from_entity(user_service.rel_service).service_id

        user_service_dto.user            = UserDTO.entity_to_dto       (user_service.rel_user)
        user_service_dto.service         = ServiceDTO.build_from_entity(user_service.rel_service)

        return user_service_dto

    def get_json_parsable(self):
        return self.__dict__

    def __str__(self):
        return f"{self.user_service_id} - {self.user_id} {self.service_id}"