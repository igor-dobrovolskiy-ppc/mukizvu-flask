import datetime
from webapp import db
from webapp.models import Person, Author, Performer, Opus, Band, Personnel, personnel_performer_roles, PerformerRole, \
    PerformerActivity, role_activities, PerformancePlace, PerformanceEvent

db.create_all()

ds1 = personnel_performer_roles.delete()
db.session.query(Performer).delete()
db.session.query(Person).delete()
ds2 = role_activities.delete()
db.session.execute(ds1)
db.session.execute(ds2)
db.session.commit()



person_pl = Person(name="Sergii", surname="aka 'Platon' aka 'Beard' Distriyanov")
db.session.add(person_pl)
person_vit = Person(name="Vitalii", surname="Melnik")
db.session.add(person_vit)
person_ih = Person(name="Ihor", surname="aka 'INgW4R' Dobrovolskyi")
db.session.add(person_ih)
person_mx = Person(name="Maxim", surname="Voronko")
db.session.add(person_mx)
person_tr = Person(name="Alex", surname="aka 'Travis'")
db.session.add(person_tr)
person_val = Person(name="Valentina", surname="Taisija (Mamchyna)")
db.session.add(person_val)
db.session.commit()

db.session.query(Author).delete()

author = Author(person_id=person_pl.id)
db.session.add(author)
author2 = Author(person_id=person_vit.id)
db.session.add(author2)


performer_pl = Performer(person_id=person_pl.id)
db.session.add(performer_pl)
performer_vit = Performer(person_id=person_vit.id)
db.session.add(performer_vit)
performer_ih = Performer(person_id=person_ih.id)
db.session.add(performer_ih)
performer_mx = Performer(person_id=person_mx.id)
db.session.add(performer_mx)
performer_tr = Performer(person_id=person_tr.id)
db.session.add(performer_tr)
performer_val = Performer(person_id=person_val.id)
db.session.add(performer_val)
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

personnel_w_vit = Personnel(band.id, start_date=datetime.date(2005, 6, 5), end_date=datetime.date(2008, 10, 23))
personnel_latest = Personnel(band.id, start_date=datetime.date(2010, 6, 1))
db.session.add(personnel_w_vit)
db.session.add(personnel_latest)
db.session.commit()

db.session.query(PerformerRole).delete()

role_pl = PerformerRole(is_main_cast=True)
role_vit = PerformerRole(is_main_cast=True)
role_ih = PerformerRole(is_main_cast=True)
role_mx = PerformerRole(is_main_cast=True)
role_tr = PerformerRole(is_main_cast=True)
role_val = PerformerRole(is_main_cast=True)
db.session.add(role_pl)
db.session.add(role_vit)
db.session.add(role_ih)
db.session.add(role_mx)
db.session.add(role_tr)
db.session.add(role_val)
db.session.commit()

db.session.query(PerformerActivity).delete()

acs = [PerformerActivity("Rhythm Guitar"),      #0
       PerformerActivity("Bass Guitar"),        #1
       PerformerActivity("Solo Guitar"),        #2
       PerformerActivity("Acoustic Guitar"),    #3
       PerformerActivity("Drums"),              #4
       PerformerActivity("Leading Vocal"),      #5
       PerformerActivity("Back Vocal"),         #6
       PerformerActivity("Percussion"),         #7
       PerformerActivity("Keyboards")]          #8

for a in acs:
    db.session.add(a)
db.session.commit()

s = personnel_performer_roles.insert().values([
    (performer_pl.id, personnel_w_vit.id, role_pl.id),
    (performer_vit.id, personnel_w_vit.id, role_vit.id),
    (performer_ih.id, personnel_w_vit.id, role_ih.id),
    (performer_pl.id, personnel_latest.id, role_pl.id),
    (performer_ih.id, personnel_latest.id, role_ih.id),
    (performer_mx.id, personnel_latest.id, role_mx.id),
    (performer_tr.id, personnel_latest.id, role_tr.id),
    (performer_val.id, personnel_latest.id, role_val.id)
])
db.session.execute(s)
db.session.commit()

ras = role_activities.insert().values([
    (role_pl.id, acs[4].id),
    (role_pl.id, acs[7].id),
    (role_vit.id, acs[0].id),
    (role_vit.id, acs[2].id),
    (role_vit.id, acs[3].id),
    (role_vit.id, acs[5].id),
    (role_ih.id, acs[1].id),
    (role_mx.id, acs[0].id),
    (role_mx.id, acs[2].id),
    (role_tr.id, acs[5].id),
    (role_tr.id, acs[3].id),
    (role_tr.id, acs[7].id),
    (role_val.id, acs[8].id),
    (role_val.id, acs[5].id)
])
db.session.execute(ras)
db.session.commit()

db.session.query(PerformancePlace).delete()

place = PerformancePlace(name="NIPIASUtransgas")
db.session.add(place)
db.session.commit()

db.session.query(PerformanceEvent).delete()

event = PerformanceEvent(perf_place_id=place.id, personnel_id=personnel_w_vit.id,
                         date=datetime.date(year=2008, month=3, day=8), name="8th of March Celebration, 2008")
db.session.add(event)
db.session.commit()


# print(personnel_w_vit)
# print(personnel_latest)

# print(", ".join([e.name for e in performer_vit.roles[0].activities]))
