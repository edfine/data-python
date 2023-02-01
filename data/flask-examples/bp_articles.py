from datetime import datetime
from uuid import uuid4

import flask
from flask import Blueprint, jsonify, request, abort

from .util import state, url_for, get_article_or_404

mod = Blueprint('articles', __name__)

@mod.route('/article')
def get_articles():
    article_links = [url_for('.get_article', article_id=article_id) for article_id in state['articles']]
    return jsonify(
        _links={'self': url_for('.get_articles')},
        data=[dict(_links=dict(self=link)) for link in article_links])

@mod.route('/article', methods=['POST'])
def create_article():
    article_id = uuid4().hex
    article = {
        'postedDate': datetime.utcnow(),
        'authorName': request.authorization.username,
        **request.json,
        'comments': [],
    }
    state['articles'][article_id] = article
    result = jsonify_article(article_id, article)
    result.headers['Location'] = url_for('.get_article', article_id=article_id)
    return result, 201

@mod.route('/article/<article_id>')
def get_article(article_id):
    article = get_article_or_404(article_id)
    return jsonify_article(article_id, article)

@mod.route('/article/<article_id>', methods=['PUT'])
def update_article(article_id):
    article = get_article_or_404(article_id)
    article.update({
        'postedDate': datetime.utcnow(),
        'authorName': request.authorization.username,
        **request.json
    })
    return jsonify_article(id, article)

@mod.route('/article/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    state['articles'].pop(article_id)
    return '', 204

def jsonify_article(article_id, article, **kwargs):
    return jsonify(
        _links={
            'self': url_for('.get_article', article_id=article_id),
            'comments': url_for('comments.get_comments', article_id=article_id)
        },
        postedDate=article['postedDate'].isoformat(),
        authorName=article['authorName'],
        title=article['title'],
        body=article['body']
    )
