import flask
from flask import abort

state = {'articles': {}}

def url_for(*args, **kwargs):
    return flask.url_for(*args, _external=True, **kwargs)

def get_article_or_404(article_id):
    article = state['articles'].get(article_id)
    if not article:
        abort(404)
    return article
    
def get_comment_or_404(article_id, comment_id):
    article = get_article_or_404(article_id)
    if comment_id < len(article['comments']):
        comment = article['comments'][comment_id]
    else:
        abort(404)
    return comment
    
