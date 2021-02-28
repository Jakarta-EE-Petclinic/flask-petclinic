from sqlalchemy import and_, func
from datetime import date
from database import db, ITEMS_PER_PAGE
from sqlalchemy.orm import joinedload


class ApplicationPage:

    def __init__(self, default_title, default_subtitle=None, default_subtitle_info=None):
        self.title = default_title
        self.subtitle = default_subtitle
        self.subtitle_info = default_subtitle_info
        if self.subtitle is None:
            self.subtitle = """This is a simple hero unit, a simple jumbotron-style component 
                            for calling extra attention to featured content or information."""
        if self.subtitle_info is None:
            self.subtitle_info = """It uses utility classes for typography and spacing 
                    to space content out within the larger container."""


class Owner(db.Model):
    __tablename__ = 'petclinic_owner'
    __table_args__ = (
        db.UniqueConstraint('region', 'lastName', 'zipCode', name='uix_petclinic_owner'),
    )
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False, unique=True)
    lastName = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False, unique=True)
    houseNumber = db.Column(db.String(255), nullable=False, unique=True)
    addressInfo = db.Column(db.String(255), nullable=False, unique=True)
    city = db.Column(db.String(255), nullable=False, unique=True)
    zipCode = db.Column(db.String(255), nullable=False, unique=True)
    phoneNumber = db.Column(db.String(255), nullable=False, unique=True)
    phoneNumber = db.Column(db.String(255), nullable=False, unique=True)
    pets = db.relationship("Pet", primaryjoin="Owner.id==Visit.owner_id")

    @classmethod
    def create_new_object_factory(cls, my_date_rep):
        my_datum = date.fromisoformat(my_date_rep)
        (my_iso_year, week_number, weekday) = my_datum.isocalendar()
        my_year_week = "" + str(my_iso_year)
        if week_number < 10:
            my_year_week += "-0"
        else:
            my_year_week += "-"
        my_year_week += str(week_number)
        return Owner(
            asdf=my_date_rep,
            datum=my_datum,
            year=my_datum.year,
            month=my_datum.month,
            day_of_month=my_datum.day,
            day_of_week=weekday,
            week_of_year=week_number,
            year_week=my_year_week
        )


class Pet(db.Model):
    __tablename__ = 'petclinic_pet'
    __table_args__ = (
        db.UniqueConstraint('name', name='uix_petclinic_pet'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    petType_id = db.Column(db.Integer, db.ForeignKey('petclinic_pet_type.id'), nullable=False)
    petType = db.relationship(
        'PetType',
        foreign_keys=[petType_id],
        lazy='joined',
        cascade='all, delete',
        order_by='PetType.name')
    owner_id = db.Column(db.Integer, db.ForeignKey('petclinic_owner.id'), nullable=False)
    owner = db.relationship('Owner', foreign_keys="[Pet.owner_id]",
                            lazy='joined', cascade='all, delete', order_by='Owner.lastName')
    visits = db.relationship("Visit", primaryjoin="Pet.id==Visit.pet_id")


class PetType(db.Model):
    __tablename__ = 'petclinic_pet_type'
    __table_args__ = (
        db.UniqueConstraint('name', name='uix_petclinic_pet_type'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class Specialty(db.Model):
    __tablename__ = 'petclinic_specialty'
    __table_args__ = (
        db.UniqueConstraint('name', name='uix_petclinic_specialty'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    # n-to-m

class Vet(db.Model):
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('firstName', 'lastName', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False, unique=True)
    lastName = db.Column(db.String(255), nullable=False, unique=True)
    # n-to-m
    # specialties = db.relationship("Specialty", primaryjoin="Vet.id==Specialty.owner_id")


class Visit(db.Model):
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('region', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False, unique=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('petclinic_pet.id'), nullable=False)
    pet = db.relationship('Pet', foreign_keys="[Visit.pet_id]",
                            lazy='joined', cascade='all, delete', order_by='Pet.name')

