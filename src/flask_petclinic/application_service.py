from flask import flash

from database import app
from flask_petclinic.application_model import Owner, Pet, PetType, Specialty, Vet, Visit

class OwnerService:
    def __init__(self, database):
        app.logger.debug("------------------------------------------------------------")
        app.logger.debug(" OwnerService [init]")
        app.logger.debug("------------------------------------------------------------")
        self.__database = database
        app.logger.debug("------------------------------------------------------------")
        app.logger.info(" OwnerService [ready]")

    def pretask_database_drop_create(self):
        flash("WhoService.pretask_database_drop_create started")
        return self


class PetService:
    def __init__(self, database):
        app.logger.debug("------------------------------------------------------------")
        app.logger.debug(" PetService [init]")
        app.logger.debug("------------------------------------------------------------")
        self.__database = database
        app.logger.debug("------------------------------------------------------------")
        app.logger.info(" PetService [ready]")

    def pretask_database_drop_create(self):
        flash("WhoService.pretask_database_drop_create started")
        return self


class PetTypeService:
    def __init__(self, database):
        app.logger.debug("------------------------------------------------------------")
        app.logger.debug(" PetTypeService [init]")
        app.logger.debug("------------------------------------------------------------")
        self.__database = database
        app.logger.debug("------------------------------------------------------------")
        app.logger.info(" PetTypeService [ready]")

    def pretask_database_drop_create(self):
        flash("WhoService.pretask_database_drop_create started")
        return self


class SpecialtyService:
    def __init__(self, database):
        app.logger.debug("------------------------------------------------------------")
        app.logger.debug(" SpecialtyService [init]")
        app.logger.debug("------------------------------------------------------------")
        self.__database = database
        app.logger.debug("------------------------------------------------------------")
        app.logger.info(" SpecialtyService [ready]")

    def pretask_database_drop_create(self):
        flash("WhoService.pretask_database_drop_create started")
        return self


class VetService:
    def __init__(self, database):
        app.logger.debug("------------------------------------------------------------")
        app.logger.debug(" VetService [init]")
        app.logger.debug("------------------------------------------------------------")
        self.__database = database
        app.logger.debug("------------------------------------------------------------")
        app.logger.info(" VetService [ready]")

    def pretask_database_drop_create(self):
        flash("WhoService.pretask_database_drop_create started")
        return self


class VisitService:
    def __init__(self, database):
        app.logger.debug("------------------------------------------------------------")
        app.logger.debug(" VisitService [init]")
        app.logger.debug("------------------------------------------------------------")
        self.__database = database
        app.logger.debug("------------------------------------------------------------")
        app.logger.info(" VisitService [ready]")

    def pretask_database_drop_create(self):
        flash("WhoService.pretask_database_drop_create started")
        return self
