from app.dtos.abstract_dto import AbstractDTO
from app.dtos.service_type_dto import ServiceTypeDTO
from app.dtos.user_dto import UserDTO
from app.models.service import Service


class ServiceDTO(AbstractDTO):
    def __init__(self):
        self.service_id = None
        self.name = None
        self.description = None
        self.request = None
        self.service_type = None
        self.type = None
        self.users = []

    @staticmethod
    def build_from_entity(service: Service):
        service_dto = ServiceDTO()

        service_dto.service_id = service.service_id
        service_dto.name = service.name
        service_dto.description = service.description
        service_dto.request = service.request
        service_dto.type = ServiceTypeDTO.build_from_entity(service.type)
        service_dto.users = []
        for user in service.get_users():
            service_dto.users.append(UserDTO.entity_to_dto(user))
        return service_dto

    def is_user_related(self, user_id):
        return user_id in [user.user_id for user in self.users]

    def get_json_parsable(self):
        return self.__dict__

    def __str__(self):
        return f"{self.service_id} - {self.name} {self.description} {self.service_type} {self.request}"