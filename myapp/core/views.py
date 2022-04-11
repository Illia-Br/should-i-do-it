from flask import render_template, request, Blueprint
from myapp.models import Posts

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Posts.query.order_by(Posts.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)

@core.route('/info')
def info():
    return render_template('info.html')