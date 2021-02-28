from flask import render_template, redirect, url_for, flash, Blueprint
from sqlalchemy.exc import OperationalError
from flask_admin.contrib.sqla import ModelView

from database import app, admin, db
from flask_petclinic.application_model import ApplicationPage
from flask_petclinic.application_model import Owner, Pet, PetType, Specialty, Vet, Visit
from flask_petclinic.application_service import OwnerService, PetService, PetTypeService, SpecialtyService
from flask_petclinic.application_service import VetService, VisitService


@app.route('/')
def url_admin_index():
    page_info = ApplicationPage('Admin', "Covid19 Admin")
    return render_template(
        'admin/index.html',
        page_info=page_info)


@app.route('/tasks')
def url_admin_tasks():
    page_info = ApplicationPage('Admin', "Tasks")
    return render_template(
        'admin/admin_tasks.html',
        page_info=page_info)


@app.route('/info')
def url_admin_info():
    page_info = ApplicationPage('Admin', "Info")
    return render_template(
        'admin/admin_info.html',
        page_info=page_info)
