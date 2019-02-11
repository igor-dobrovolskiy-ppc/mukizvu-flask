from builtins import classmethod

from .. import db


opus_authors = db.Table(
    'm3vu_opus_author',
    db.Column('opus_id', db.Integer, db.ForeignKey('m3vu_opus.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('m3vu_author.id'))
)


class Person(db.Model):
    __tablename__ = 'm3vu_person'

    id = db.Column(db.Integer(), primary_key=True)
    # name = db.Column(db.String(255), nullable=False, index=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(255), nullable=True)  # TODO: rework into Gender table ref.
    # posts = db.relationship('Post', backref='flt_user', lazy='subquery')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return '<Person#{}: {} {} >'.format(self.id, self.name, self.surname)


class Author(db.Model):
    __tablename__ = 'm3vu_author'

    id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('m3vu_person.id'))
    # opuses = db.relationship(
    #     'Opus',
    #     secondary=opus_authors,
    #     backref=db.backref('authors', lazy='dynamic')
    # )

    def person(self):
        return Person.query.filter_by(id=self.person_id).first()

    def __init__(self, person_id):
        self.person_id = person_id

    def __repr__(self):
        return '<Author#{}: -> Person: {}>'.format(self.id, self.person())


class Performer(db.Model):
    __tablename__ = 'm3vu_performer'

    id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('m3vu_person.id'), nullable=True)

    def person(self):
        return Person.query.filter_by(id=self.person_id).first()

    def __init__(self, person_id):
        self.person_id = person_id

    def __repr__(self):
        return '<Performer#{}: -> Person: {}>'.format(self.id, self.person())


class Opus(db.Model):
    __tablename__ = 'm3vu_opus'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    authors = db.relationship(
        'Author',
        secondary=opus_authors,
        backref=db.backref('opuses', lazy='dynamic')
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Opus#{}: {}, authors: {}>'.format(self.id, self.name, self.authors)


class Band(db.Model):
    __tablename__ = 'm3vu_band'

    id = db.Column(db.Integer(), primary_key=True)
    performer_id = db.Column(db.Integer(), db.ForeignKey('m3vu_performer.id'), nullable=False, index=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    # personnel = db.relationship('Performer', backref='flt_performer', lazy='subquery')

    def performer(self):
        return Performer.query.filter_by(id=self.performer_id).first()

    def __init__(self, name, performer_id):
        self.name = name
        self.performer_id = performer_id

    @classmethod
    def from_name(cls, name):
        performer = Performer(None)
        db.session.add(performer)
        db.session.commit()
        return cls(name, performer.id)

    def __repr__(self):
        return '<Band#{}: {}, performer: {}>'.format(self.id, self.name, self.performer())


personnel_performer_roles = db.Table(
    'm3vu_personnel_performer_role',
    db.Column('performer_id', db.Integer, db.ForeignKey('m3vu_performer.id')),
    db.Column('personnel_id', db.Integer, db.ForeignKey('m3vu_personnel.id')),
    db.Column('performer_role_id', db.Integer, db.ForeignKey('m3vu_performer_role.id'), nullable=True)
)


class Personnel(db.Model):
    __tablename__ = 'm3vu_personnel'

    id = db.Column(db.Integer(), primary_key=True)
    band_id = db.Column(db.Integer(), db.ForeignKey('m3vu_band.id'), nullable=False, index=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)

    performers = db.relationship(
        'Performer',
        secondary=personnel_performer_roles,
        backref=db.backref('personnels', lazy='dynamic')
    )

    def __init__(self, band_id, start_date, end_date=None):
        self.band_id = band_id
        self.start_date = start_date
        self.end_date = end_date

    def band(self):
        return Band.query.filter_by(id=self.band_id).first()

    def __repr__(self):
        return '<Personnel#{}: {}-{}, band: {}, performers: {}>'.format(self.id, self.start_date, self.end_date,
                                                                        self.band(), self.performers)


role_activities = db.Table(
    'm3vu_role_activity',
    db.Column('performer_id', db.Integer, db.ForeignKey('m3vu_performer_role.id')),
    db.Column('personnel_id', db.Integer, db.ForeignKey('m3vu_performer_activity.id'))
    # TODO: think over adding start-end dates here
)


class PerformerRole(db.Model):
    __tablename__ = 'm3vu_performer_role'

    id = db.Column(db.Integer(), primary_key=True)
    is_main_cast = db.Column(db.Boolean(), nullable=False, default=True)

    activities = db.relationship(
        'PerformerActivity',
        secondary=role_activities,
        backref=db.backref('roles', lazy='dynamic')
    )

    def __init__(self, is_main_cast):
        self.is_main_cast = is_main_cast

    def __repr__(self):
        return '<PerformerRole#{}: isMainCast: {}; activities: {}>'.format(self.id, self.is_main_cast, self.activities)


class PerformerActivity(db.Model):
    __tablename__ = 'm3vu_performer_activity'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text(), nullable=True)

    def __init__(self, name, desc=None):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return '<PerformerActivity#{}: {} ({})>'.format(self.id, self.name, self.desc)
