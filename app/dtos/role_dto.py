from app.models.role import Role


class RoleDTO():
    def __init__(self) -> None:
        self.roleid   = None
        self.rolename = None

    def entity_to_dto(entity: Role):
        dto = RoleDTO()
        dto.roleid   = entity.role_id
        dto.rolename = entity.rolename

        return dto

    def dto_to_entity(self):
        entity = Role()
        
        entity.role_id  = self.roleid
        entity.rolename = self.rolename

        return entity
