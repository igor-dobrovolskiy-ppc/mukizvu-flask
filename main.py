import os
import logging

#from flask import Flask, render_template, flash, redirect, url_for
from flask import render_template
from webapp import create_app
# from webapp.cli import register
from webapp.models import Person

log = logging.getLogger(__name__)


# from logging.config import dictConfig
#
# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })


# import logging
# from flask.logging import default_handler



env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())
# register(app)

# root = logging.getLogger()
# root.addHandler(default_handler)
# for logger in (
#     app.logger,
#     logging.getLogger('sqlalchemy'),
# ):
#     logger.addHandler(default_handler)


@app.route('/')
def home():
    persons = Person.query.all()

    log.info("Persons: %s" % (str(persons)))

    return render_template(
        'home.html',
        persons=persons
    )

@app.route('/person/<int:person_id>', methods=('GET', 'POST'))
def person(person_id):
    # form = CommentForm()
    # if form.validate_on_submit():
    #     new_comment = Comment()
    #     new_comment.name = form.name.data
    #     new_comment.text = form.text.data
    #     new_comment.post_id = post_id
    #     try:
    #         db.session.add(new_comment)
    #         db.session.commit()
    #     except Exception as e:
    #         flash('Error adding your comment: %s' % str(e), 'error')
    #         db.session.rollback()
    #     else:
    #         flash('Comment added', 'info')
    #     return redirect(url_for('post', post_id=post_id))
    #
    # post = Post.query.get_or_404(post_id)
    # tags = post.tags
    # comments = post.comments.order_by(Comment.date.desc()).all()
    # recent, top_tags = sidebar_data()
    #
    # return render_template(
    #     'post.html',
    #     post=post,
    #     tags=tags,
    #     comments=comments,
    #     recent=recent,
    #     top_tags=top_tags,
    #     form=form
    # )
    return "<html>Hello Person"


if __name__ == '__main__':
    app.run()


# tags = db.Table(
#     'post_tags',
#     db.Column('post_id', db.Integer, db.ForeignKey('flt_post.id')),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
# )
#
#
# class User(db.Model):
#     __tablename__ = 'flt_user'
#
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(255), nullable=False, index=True, unique=True)
#     password = db.Column(db.String(255))
#     posts = db.relationship('Post', backref='flt_user', lazy='subquery')
#
#     def __init__(self, username):
#         self.username = username
#
#     def __repr__(self):
#         # formats what is shown in the shell when print is
#         # called on it
#         return '<User {}>'.format(self.username)
#
#
# class Post(db.Model):
#     __tablename__ = 'flt_post'
#
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     text = db.Column(db.Text())
#     publish_date = db.Column(db.DateTime(), default=datetime.datetime.now)
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
#     comments = db.relationship(
#         'Comment',
#         backref='post',
#         lazy='dynamic'
#     )
#     tags = db.relationship(
#         'Tag',
#         secondary=tags,
#         backref=db.backref('posts', lazy='dynamic')
#     )
#
#     def __init__(self, title):
#         self.title = title
#
#     def __repr__(self):
#         return "<Post '{}'>".format(self.title)
#
#
# class Comment(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     text = db.Column(db.Text(), nullable=False)
#     date = db.Column(db.DateTime(), default=datetime.datetime.now)
#     post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
#
#     def __repr__(self):
#         return "<Comment '{}'>".format(self.text[:15])
#
#
# class Tag(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(255), nullable=False, unique=True)
#
#     def __init__(self, title):
#         self.title = title
#
#     def __repr__(self):
#         return "<Tag '{}'>".format(self.title)
#
#
# # class User(db.Model):
# #     __tablename__ = 'flt_user'
# #
# #     id = db.Column(db.Integer(), primary_key=True)
# #     username = db.Column("user_name", db.String(255))
# #     password = db.Column(db.String(255))
# #     posts = db.relationship(
# #         'Post',
# #         # backref='subquery',
# #         backref='flt_user',
# #         lazy='dynamic'
# #     )
# #
# #     def __init__(self, username):
# #         self.username = username
# #
# #     def __repr__(self):
# #         return "<User '{}'>".format(self.username)
# #
# #
# # class Post(db.Model):
# #     __tablename__ = 'flt_post'
# #
# #     id = db.Column(db.Integer(), primary_key=True)
# #     title = db.Column(db.String(255))
# #     text = db.Column(db.Text())
# #     publish_date = db.Column(db.DateTime())
# #     user_id = db.Column(db.Integer(), db.ForeignKey('flt_user.id'))
# #
# #     def __init__(self, title):
# #         self.title = title
# #
# #     def __repr__(self):
# #         return "<Post '{}'>".format(self.title)
