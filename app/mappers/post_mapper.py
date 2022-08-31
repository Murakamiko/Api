from app.dtos.post_dto import PostDTO
from app.forms.post_form import PostForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.post import Post


class PostMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(post: Post):
        return PostDTO.build_from_entity(comment)

    @staticmethod
    def form_to_entity(form, post: Post):
        if isinstance(form, PostForm):
            post.content = form.content.data

        return post

    @staticmethod
    def content_data_to_entity(content, post: Post):
        post.content = content

        return post