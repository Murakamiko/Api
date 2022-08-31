from app.dtos.service_type_dto import ServiceTypeDTO
from app.models.service_type import ServiceType
from app.services.base_service import BaseService


class ServiceTypeService(BaseService):
    def find_all(self):
        return [ServiceTypeDTO.build_from_entity(service_type) for service_type in ServiceType.query.all()]

    def find_one(self, entity_id: int):
        pass

    def find_one_by(self, **kwargs):
        return ServiceTypeDTO.build_from_entity(ServiceType.query.filter_by(**kwargs).one())

    def find_one_entity_by_name(self, name: str):
        return ServiceType.query.filter_by(name=name).one()

    def insert(self, data):
        pass

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass