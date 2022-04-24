from flask import Blueprint, Flask, redirect, render_template, request

import repositories.unit_repository as unit_repository

from models.part import Part
from models.customer import Customer
from models.unit import Unit

units_blueprint = Blueprint("units", __name__)

# INDEX
@units_blueprint.route("/units")
def units():
    units = unit_repository.select_all()
    return render_template("customers/customer_list.html", units=units)