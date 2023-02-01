from datetime import datetime

import flask
from flask import Blueprint, jsonify, request, abort

from .util import state, url_for, get_article_or_404, get_comment_or_404

mod = Blueprint('comments', __name__)

@mod.route('/article/<article_id>/comments')
def get_comments(article_id):
    article = get_article_or_404(article_id)
    comment_links = [
        url_for('comments.get_comment', article_id=article_id, comment_id=i) 
        for i, comment in enumerate(article['comments'])
    ]
    return jsonify(
        _links={'self': url_for('.get_comments', article_id=article_id)},
        data=[dict(_links=dict(self=link)) for link in comment_links])

@mod.route('/article/<article_id>/comments', methods=['POST'])
def create_comment(article_id):
    article = get_article_or_404(article_id)
    comment_id = len(article['comments'])
    comment = {
        'postedDate': datetime.utcnow(),
        'authorName': request.authorization.username,
        **request.json,
    }
    article['comments'].append(comment)
    result = jsonify_comment(article_id, comment_id, comment)
    result.headers['Location'] = url_for('.get_comment', article_id=article_id, comment_id=comment_id)
    return result, 201

@mod.route('/article/<article_id>/comments/<int:comment_id>')
def get_comment(article_id, comment_id):
    comment = get_comment_or_404(article_id, comment_id)
    return jsonify_comment(article_id, comment_id, comment)
    
@mod.route('/article/<article_id>/comments/<int:comment_id>', methods=['PUT'])
def update_comment(article_id, comment_id):
    comment = get_comment_or_404(article_id, comment_id)
    comment.update({
        'postedDate': datetime.utcnow(),
        'authorName': request.authorization.username,
        **request.json,
    })
    return jsonify_comment(article_id, comment_id, comment)

@mod.route('/article/<article_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(article_id, comment_id):
    article = get_article_or_404(article_id)
    if len(article[comments]) <= comment_id:
        abort(404)
    del article['comments'][comment_id]
    return '', 204

    
def jsonify_comment(article_id, comment_id, comment):
    return jsonify(
        _links={
            'self': url_for('.get_comment', article_id=article_id, comment_id=comment_id),
            'article': url_for('articles.get_article', article_id=article_id)
        },
        authorName=comment['authorName'],
        body=comment['body'],
    )
