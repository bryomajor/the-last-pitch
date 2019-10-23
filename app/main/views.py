from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User, Comment, Upvote, Downvote
from .forms import PitchForm, CommentForm, UpvoteForm
from flask.views import View, MethodView
from .. import db

@main.route('/', methods = ['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    title = 'Home'
    pitch = Pitch.query.filter_by().first()
    pickuplines = Pitch.query.filter_by(category='pickuplines')
    interviewpitch = Pitch.query.filter_by(category='interviewpitch')
    promotionpitch = Pitch.query.filter_by(category='promotionpitch')
    productpitch = Pitch.query.filter_by(category='productpitch')

    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)

    return render_template('home.html', title = title, pitch = pitch, pickuplines = pickuplines, interviewpitch = interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch, upvotes = upvotes)

@main.route('/pitches/new/', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user.get_current_object().id)
        new_pitch = Pitch(owner_id=current_user.get_current_object().id, title=title, descrihttp://127.0.0.1:5000/ption=description, category
        =category)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitches.html', form=form)


@main.route('/comment/new/<int:pitch_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', pitch_id = pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch = pitch)