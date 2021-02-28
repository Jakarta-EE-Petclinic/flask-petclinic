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
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('region', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    asdf = db.Column(db.String(255), nullable=False, unique=True)

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
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('region', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    asdf = db.Column(db.String(255), nullable=False, unique=True)


class PetType(db.Model):
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('region', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    asdf = db.Column(db.String(255), nullable=False, unique=True)


class Specialty(db.Model):
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('region', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    asdf = db.Column(db.String(255), nullable=False, unique=True)


class Vet(db.Model):
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('region', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    asdf = db.Column(db.String(255), nullable=False, unique=True)


class Visit(db.Model):
    __tablename__ = 'application_region'
    __table_args__ = (
        db.UniqueConstraint('region', name='uix_application_region'),
    )
    id = db.Column(db.Integer, primary_key=True)
    asdf = db.Column(db.String(255), nullable=False, unique=True)

