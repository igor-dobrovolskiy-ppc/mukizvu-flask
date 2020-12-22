import os
import logging

#from flask import Flask, render_template, flash, redirect, url_for
from flask import render_template
from webapp import create_app
# from webapp.cli import register
from webapp.dao import Performer

log = logging.getLogger(__name__)
env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())
# register(app)


@app.route('/')
def home():
    performers = Performer.performers()

    log.info("Persons: %s" % (str(performers)))

    return render_template(
        'home.html',
        performers=performers
    )


@app.route('/performer/<int:performer_id>', methods=('GET', 'POST'))
def performer(performer_id):
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
    person = Performer.query.filter_by(id=performer_id).first().person()

    return "<html>Hello %s %s" % (person.name, person.surname)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
