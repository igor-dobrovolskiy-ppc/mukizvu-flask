import datetime
from webapp import db
from webapp.models import Person, Author, Performer, Opus, Band, Personnel, personnel_performer_roles, PerformerRole, \
    PerformerActivity, role_activities, PerformancePlace, PerformanceEvent

db.create_all()

ds1 = personnel_performer_roles.delete()
ds2 = role_activities.delete()
db.session.execute(ds1)
db.session.execute(ds2)
db.session.commit()

db.session.query(Person).delete()

person2 = Person(name="Sergei", surname="aka 'Platon' aka 'Beard' Distriyanov")
db.session.add(person2)
person3 = Person(name="Vitalii", surname="Melnik")
db.session.add(person3)
person4 = Person(name="Ihor", surname="aka 'INgW4R' Dobrovolskyi")
db.session.add(person4)
person5 = Person(name="Maxim", surname="Voronko")
db.session.add(person5)
person6 = Person(name="Alex", surname="aka 'Travis'")
db.session.add(person6)
person7 = Person(name="Valentina", surname="Taisija (Mamchyna)'")
db.session.add(person7)
db.session.commit()

db.session.query(Author).delete()

author = Author(person_id=person2.id)
db.session.add(author)
author2 = Author(person_id=person3.id)
db.session.add(author2)

db.session.query(Performer).delete()

performer = Performer(person_id=person2.id)
db.session.add(performer)
performer2 = Performer(person_id=person3.id)
db.session.add(performer2)
performer3 = Performer(person_id=person4.id)
db.session.add(performer3)
performer4 = Performer(person_id=person5.id)
db.session.add(performer4)
performer5 = Performer(person_id=person6.id)
db.session.add(performer5)
performer6 = Performer(person_id=person7.id)
db.session.add(performer6)
db.session.commit()

db.session.query(Opus).delete()

opus = Opus(name="Mole")
opus.authors = [author]
db.session.add(opus)
opus2 = Opus(name="Sharik")
opus2.authors = [author, author2]
db.session.commit()

db.session.query(Band).delete()

band = Band.from_name("Muki Zvu")
db.session.add(band)
db.session.commit()

db.session.query(Personnel).delete()

personnel = Personnel(band.id, start_date=datetime.date(2005, 6, 5))
db.session.add(personnel)
db.session.commit()

db.session.query(PerformerRole).delete()

role = PerformerRole(is_main_cast=True)
role2 = PerformerRole(is_main_cast=True)
db.session.add(role)
db.session.add(role2)
db.session.commit()

db.session.query(PerformerActivity).delete()

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

db.session.query(PerformancePlace).delete()

place = PerformancePlace(name="NIPIASUtransgas")
db.session.add(place)
db.session.commit()

db.session.query(PerformanceEvent).delete()

event = PerformanceEvent(perf_place_id=place.id, personnel_id=personnel.id,
                         date=datetime.date(year=2008, month=3, day=8), name="8th of March Celebration, 2008")
db.session.add(event)
db.session.commit()
