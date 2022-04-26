
from flask import Blueprint, Flask, redirect, render_template, request

import repositories.part_repository as part_repository
import repositories.unit_repository as unit_repository

from models.part import Part
from models.unit import Unit

parts_blueprint = Blueprint("parts", __name__)

# INDEX
@parts_blueprint.route("/parts")
def parts():
    parts = part_repository.select_all()
    return render_template("parts/parts_list.html", parts=parts)

# New
@parts_blueprint.route("/parts/new_part")
def new_customer():
    units = unit_repository.select_all()
    return render_template("parts/new_part.html", units = units)

# Create
@parts_blueprint.route("/parts", methods = ["POST"])
def add_new_part():
    name = request.form["name"]
    number = request.form["number"]
    num_per_unit = request.form["num_per_unit"]
    hours_exp = request.form["hours_exp"]
    unit_id = request.form["unit_id"]
    unit = unit_repository.select(unit_id)
    new_part = Part(name, number, num_per_unit, hours_exp , unit)
    part_repository.save(new_part)
    return redirect("/parts")

# # DELETE
# @units_blueprint.route("/units/<id>/delete", methods = ["POST"])
# def delete_unit(id):
#     unit_repository.delete(id)
#     return redirect("/units")

# # EDIT
# @units_blueprint.route("/units/<id>/edit")
# def edit_unit(id):
#     unit = unit_repository.select(id)
#     return render_template("units/edit_unit.html", unit=unit)

# # UPDATE
# @units_blueprint.route("/units/<id>", methods = ["POST"])
# def update_unit(id):
#     unit_type = request.form["unit_type"]
#     unit_sn = request.form["serial_number"]
#     unit_hr = request.form["hours_run"]
#     unit = Unit(unit_type, unit_sn, unit_hr, id)
#     unit_repository.update(unit)
#     return redirect("/units")