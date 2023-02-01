from flask import Flask, jsonify, url_for

from . import bp_articles
from . import bp_comments
from .util import url_for

app = Flask(__name__)

app.register_blueprint(bp_articles.mod, url_prefix='/api')
app.register_blueprint(bp_comments.mod, url_prefix='/api')

@app.route('/')
def get_root():
    return jsonify(_links={'articles': url_for('articles.get_articles')})
