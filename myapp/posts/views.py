from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Posts
from myapp.posts.forms import PostForm

posts = Blueprint('posts', __name__)

@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, description=form.description.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post Created')
        print('Post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)