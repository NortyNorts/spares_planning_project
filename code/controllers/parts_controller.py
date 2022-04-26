
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

# Show
@parts_blueprint.route("/parts/<id>/part")
def view_part(id):
    part = part_repository.select(id)
    return render_template("parts/part.html", part=part)

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

# DELETE
@parts_blueprint.route("/parts/<id>/delete", methods = ["POST"])
def delete_part(id):
    part_repository.delete(id)
    return redirect("/parts")

# EDIT
@parts_blueprint.route("/parts/<id>/edit")
def edit_part(id):
    units = unit_repository.select_all()
    part = part_repository.select(id)
    return render_template("parts/edit_part.html", part=part, units = units)

# UPDATE
@parts_blueprint.route("/parts/<id>", methods = ["POST"])
def update_part(id):
    name = request.form["name"]
    number = request.form["number"]
    num_per_unit = request.form["num_per_unit"]
    hours_exp = request.form["hours_exp"]
    unit_id = request.form["unit_id"]
    unit = unit_repository.select(unit_id)
    part = Part(name, number, num_per_unit, hours_exp , unit, id)
    part_repository.update(part)
    return redirect("/parts")