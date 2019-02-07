import datetime
from webapp import db
from webapp.models import Person, Author, Performer, Opus, Band, Personnel, personnel_performer_roles


db.create_all()

person = Person(name="Adam", surname="First")
db.session.add(person)
person2 = Person(name="John", surname="Lennon")
db.session.add(person2)
person3 = Person(name="Paul", surname="McCartney")
db.session.add(person3)
db.session.commit()
author = Author(person_id=person2.id)
db.session.add(author)
author2 = Author(person_id=person3.id)
db.session.add(author2)
performer = Performer(person_id=person2.id)
db.session.add(performer)
performer2 = Performer(person_id=person3.id)
db.session.add(performer2)
db.session.commit()
opus = Opus(name="Imagine")
opus.authors = [author]
db.session.add(opus)
opus2 = Opus(name="Help!")
opus2.authors = [author, author2]
db.session.commit()
band = Band.from_name("The Beatles")
db.session.add(band)
db.session.commit()
personnel = Personnel(band.id, datetime.date(1961, 1, 1), datetime.date(1968, 10, 11))
db.session.add(personnel)
db.session.commit()
personnel_performer_roles.insert().values((performer.id, personnel.id, None))
db.session.commit()
