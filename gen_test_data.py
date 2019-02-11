import datetime
from webapp import db
from webapp.models import Person, Author, Performer, Opus, Band, Personnel, personnel_performer_roles, PerformerRole, \
    PerformerActivity, role_activities

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
personnel = Personnel(band.id, start_date=datetime.date(1960, 8, 15), end_date=datetime.date(1970, 4, 10))
db.session.add(personnel)
db.session.commit()
role = PerformerRole(is_main_cast=True)
role2 = PerformerRole(is_main_cast=True)
db.session.add(role)
db.session.add(role2)
db.session.commit()

acs = [PerformerActivity("Rhythm Guitar"),
       PerformerActivity("Bass Guitar"),
       PerformerActivity("Solo Guitar"),
       PerformerActivity("Acoustic Guitar"),
       PerformerActivity("Drums"),
       PerformerActivity("Leading Vocal"),
       PerformerActivity("Back Vocal"),
       PerformerActivity("Percussion"),
       PerformerActivity("Keyboards")]

for a in acs:
    db.session.add(a)
db.session.commit()

s = personnel_performer_roles.insert().values([
    (performer.id, personnel.id, role.id),
    (performer2.id, personnel.id, role2.id)
])
db.session.execute(s)
db.session.commit()


ras = role_activities.insert().values([
    (role.id, acs[0].id),
    (role.id, acs[3].id),
    (role.id, acs[5].id),
    (role.id, acs[6].id),
    (role2.id, acs[1].id),
    (role2.id, acs[5].id),
    (role2.id, acs[6].id)
])
db.session.execute(ras)
db.session.commit()
