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


@comments.route('/<int:comment_id>/update',methods=['GET','POST'])
@login_required
def update(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    if comment.author != current_user:
        abort(403)

    form = CommentForm()

    if form.validate_on_submit():
        comment.text = form.text.data
        db.session.commit()
        flash('Comment Updated')
        return redirect(url_for('posts.post', post_id=comment.target.id))

    elif request.method == 'GET':
        form.text.data = comment.text

    return render_template('update_comment.html',title='Updating',form=form)