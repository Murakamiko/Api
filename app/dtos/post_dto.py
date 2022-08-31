from app.dtos.abstract_dto import AbstractDTO
from app.models.post import Post


class PostDTO(AbstractDTO):
    def __init__(self):
        self.post_id = None
        self.author_id = None
        self.content = None

    @staticmethod
    def build_from_entity(entity):
        post_dto = PostDTO()

        if isinstance(entity, Post):
            post_dto.comment_id = entity.comment_id
            post_dto.author_id = entity.rel_author.user_id
            post_dto.author_name = entity.rel_author.username
            post_dto.content = entity.content
            post_dto.create_date = entity.createdate

        return post_dto


    def get_json_parsable(self):
        return self.__dict__