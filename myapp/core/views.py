from flask import render_template, request, Blueprint
from myapp.models import Post

core = Blueprint('core', __name__)

@core.route('/')
def info():
    return render_template('info.html')

@core.route('/allPosts')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)