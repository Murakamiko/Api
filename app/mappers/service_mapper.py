from app.dtos.service_dto import ServiceDTO
from app.dtos.service_type_dto import ServiceTypeDTO
from app.forms.service_form import ServiceForm
from app.framework.decorators.inject import inject
from app.mappers.abstract_mapper import AbstractMapper
from app.models.service import Service
from app.services.service_type_service import ServiceTypeService


class ServiceMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(service: Service):
        return ServiceDTO.build_from_entity(service)

    @staticmethod
    @inject
    def form_to_entity(form, service: Service, service_type_service: ServiceTypeService):
        if isinstance(form, ServiceForm):
            service.name = form.name.data
            service.description = form.description.data
            service.request = True if form.request.data == 'request' else False
            service.service_type = service_type_service.find_one_by(name=form.service_type.data).service_type_id

        return service