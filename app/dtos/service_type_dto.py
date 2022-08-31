from app.dtos.abstract_dto import AbstractDTO
from app.models.service_type import ServiceType


class ServiceTypeDTO(AbstractDTO):

    def __init__(self):
        self.service_type_id = None
        self.name = None

    @staticmethod
    def build_from_entity(service_type: ServiceType):
        service_type_dto = ServiceTypeDTO()
        service_type_dto.service_type_id = service_type.service_type_id
        service_type_dto.name = service_type.name
        return service_type_dto

    def get_json_parsable(self):
        return self.__dict__

    def __str__(self):
        return f"[DTO] {self.service_type_id} - {self.name}"