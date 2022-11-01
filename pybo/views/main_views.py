from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')    # __name__ 에는 모듈명인 main_views가 인수로 전달됨


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))

