import os
from webapp import create_app
# from webapp.cli import register

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())
# register(app)


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
