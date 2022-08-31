from app import app
from app.services.post_service import PostService
from flask import render_template, request, redirect, url_for, jsonify, json
from app.framework.decorators.inject import inject
"""from app.forms.comment.comment_add_form import CommentAddForm"""

@app.route('/posts', methods=['GET'])
def get_all():
    return render_template('post/index.html')

"""@app.route('/comments', methods=['GET'])
def get_comments():
    return render_template('comment/comments.html')

@app.route('/comments/all', methods=['GET'])
@inject
def get_all_comments(comment_service: CommentService):
    return jsonify([comment.get_json_parsable() for comment in comment_service.find_all()])


@app.route('/comments/add', methods=['GET', 'POST'])
@inject
def add_comment(comment_service: CommentService):
    form = CommentAddForm(request.form)

    if request.method == 'POST':
        if form.validate():
            try:
                comment = comment_service.insert(form)
                res = {
                    "type": "response",
                    "data": comment.get_json_parsable()
                }

                return jsonify(res)

            except Exception as e:
                print(e)
        else:
            res = {
                "type": "error",
                "message": form.errors['content']
            }

            return jsonify(res)

    return render_template('comment/new_comment.html', form=form)

@app.route('/comments/update', methods=['POST'])
@inject
def update_comment(comment_service: CommentService):
    data = json.loads(request.data)
    try:
        comment = comment_service.update(data['comment_id'], data['content'])
        res = {
            "type": "response",
            "data": comment.get_json_parsable()
        }

        return jsonify(res)

    except:
        res = {
            "type": "error",
            "message": "error"
        }

        return jsonify(res)
    

    return render_template('home/home.html')


@app.route('/comments/service', methods=['GET', 'POST'])
@inject
def get_comments_by_service(comment_service: CommentService):
    service_id = int(request.data)

    return jsonify([comment.get_json_parsable() for comment in comment_service.find_all_by(service_id=service_id)])


@app.route('/comments/user_service', methods=['GET', 'POST'])
@inject
def get_comments_by_user_service(comment_service: CommentService):
    user_service_id = int(request.data)

    return jsonify([comment.get_json_parsable() for comment in comment_service.find_all_by(user_service_id=user_service_id)])"""