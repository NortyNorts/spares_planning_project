from flask import Blueprint, Flask, redirect, render_template, request

import repositories.unit_repository as unit_repository
import repositories.part_repository as part_repository
import repositories.customer_repository as customer_repository

from models.part import Part
from models.customer import Customer
from models.unit import Unit

units_blueprint = Blueprint("units", __name__)

# INDEX
@units_blueprint.route("/units")
def units():
    units = unit_repository.select_all()
    return render_template("units/units.html", units=units)

# SHOW
@units_blueprint.route("/units/<id>/unit_detail")
def unit_details(id):
    unit = unit_repository.select(id)
    parts = part_repository.select_by_unit_id(id)
    return render_template("/units/unit_detail.html", unit=unit, parts = parts)

# New
@units_blueprint.route("/units/new_unit")
def new_customer():
    customers = customer_repository.select_all()
    return render_template("units/new_unit.html", customers = customers)

# Create
@units_blueprint.route("/units", methods = ["POST"])
def add_new_customer():
    unit_type = request.form["unit_type"]
    unit_sn = request.form["serial_number"]
    unit_hr = request.form["unit_hours_run"]
    customer_id = request.form["customer_id"]
    customer = customer_repository.select(customer_id)
    new_unit = Unit(unit_type, unit_sn, unit_hr, customer)
    unit_repository.save(new_unit)
    return redirect("/units")

# DELETE
@units_blueprint.route("/units/<id>/delete", methods = ["POST"])
def delete_unit(id):
    unit_repository.delete(id)
    return redirect("/units")

# EDIT
@units_blueprint.route("/units/<id>/edit")
def edit_unit(id):
    customers = customer_repository.select_all()
    unit = unit_repository.select(id)
    return render_template("units/edit_unit.html", unit=unit, customers = customers)

# UPDATE
@units_blueprint.route("/units/<id>", methods = ["POST"])
def update_unit(id):
    unit_type = request.form["unit_type"]
    unit_sn = request.form["serial_number"]
    unit_hr = request.form["hours_run"]
    customer_id = request.form["customer_id"]
    customer = customer_repository.select(customer_id)
    unit = Unit(unit_type, unit_sn, unit_hr, customer, id)
    unit_repository.update(unit)
    return redirect("/units")