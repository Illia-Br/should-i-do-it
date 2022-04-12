from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Comment
from myapp.comments.forms import CommentForm

comments = Blueprint('comments', __name__)

@comments.route('/<int:post_id>/addComment', methods=['GET', 'POST'])
@login_required
def add_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.text.data, user_id=current_user.id, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment Created')
        print('Comment was created')
        
    return redirect(url_for('posts.post', post_id=post_id))