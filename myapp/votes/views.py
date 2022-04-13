from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Vote


votes = Blueprint('votes', __name__)

@votes.route('/<int:post_id>/addVotePro', methods=['GET', 'POST'])
@login_required
def add_vote_pro(post_id):
  vote =  Vote.query.filter_by(post_id=post_id, user_id=current_user.id).first()
  if vote:
    vote.vote_pro = 1
    vote.vote_against = 0
    db.session.commit()
    flash('Comment Created')
    print('Vote was updated to pro')
  else:  
    vote = Vote(user_id=current_user.id, post_id=post_id, vote_pro = 1, vote_against=0)
    db.session.add(vote)
    db.session.commit()
    flash('Comment Created')
    print('Vote was created')
  return redirect(url_for('posts.post', post_id=post_id))    


@votes.route('/<int:post_id>/addVoteAgainst', methods=['GET', 'POST'])
@login_required
def add_vote_against(post_id):
  vote =  Vote.query.filter_by(post_id=post_id, user_id=current_user.id).first()
  print(vote)
  if vote:
    vote.vote_pro = 0
    vote.vote_against = 1
    db.session.commit()
    flash('Comment Created')
    print('Vote was updated to against')
  else:  
    vote = Vote(user_id=current_user.id, post_id=post_id, vote_pro = 0, vote_against=1)
    db.session.add(vote)
    db.session.commit()
    flash('Comment Created')
    print('Vote was created')      
  return redirect(url_for('posts.post', post_id=post_id))