from app import db
from app.dtos.post_dto import PostDTO
from app.mappers.post_mapper import PostMapper
from app.models.post import Post
from app.services.base_service import BaseService


class PostService(BaseService):
    def find_all(self):
        return [PostDTO.build_from_entity(post) for post in Post.query.all()]

    def find_one(self, entity_id: int):
        return PostDTO.build_from_entity(Post.query.filter_by(comment_id=entity_id).one())

    def find_all_by(self, **kwargs):
        return [PostDTO.build_from_entity(post) for post in Post.query.filter_by(**kwargs)]

    def find_one_by(self, **kwargs):
        return PostDTO.build_from_entity(Post.query.filter_by(**kwargs).one())

    def insert(self, data):
        post = Post()
        PostMapper.form_to_entity(data, post)
        post.author_id = 1
        post.service_id = 1

        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(e)
            raise e
            db.session.rollback()

        return self.find_one(post.post_id)

    def update(self, entity_id: int, post):
        post = Post.query.filter_by(post_id=entity_id).one()

        if post is None:
            return None

        PostMapper.content_data_to_entity(content, post)

        try:           
            db.session.commit()
        except Exception as e:
            print(e)
            raise e
            db.session.rollback()

        return self.find_one(entity_id)

    def delete(self, entity_id: int):
        post = Post.query.filter_by(post_id=entity_id).one()

        if post is None:
            return None

        try:
            db.session.delete(post)
            db.session.commit()
        except Exception as e:
            print(e)
            raise e
            db.session.rollback()

        return post.post_id