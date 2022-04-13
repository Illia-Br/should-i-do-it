from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Post, Comment, Vote
from myapp.posts.forms import PostForm
from myapp.comments.forms import CommentForm

posts = Blueprint('posts', __name__)

@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.description.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post Created')
        print('Post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

# Make sure the blog_post_id is an integer!

@posts.route('/<int:post_id>')
def post(post_id):
    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    page = request.args.get('page', 1, type=int)
    comments =  Comment.query.filter_by(target=post).order_by(Comment.date.desc()).paginate(page=page, per_page=5)
    vote = Vote.query.filter_by(target=post, user_id = current_user.id).first()
    pro_votes = Vote.query.filter_by(target=post, vote_pro = 1).count()
    votes_against = Vote.query.filter_by(target=post, vote_against = 1).count()
    return render_template('post.html', title=post.title, date=post.date, post=post, form=form, comments = comments, pro_votes = pro_votes, votes_against = votes_against, vote = vote)


@posts.route('/<int:post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post Deleted')
    return redirect(url_for('core.index'))