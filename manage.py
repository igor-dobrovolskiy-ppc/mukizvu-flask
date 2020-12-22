from main import app
from webapp import db, migrate
from webapp.dao import Person, Author, Performer


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Person=Person, Performer=Performer, Author=Author, migrate=migrate)


# @event.listens_for(Engine, "connect")
#     def set_sqlite_pragma(dbapi_connection, connection_record):
#         cursor = dbapi_connection.cursor()
#         cursor.execute("PRAGMA foreign_keys=ON")
#         cursor.close()
