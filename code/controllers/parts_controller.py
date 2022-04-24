
from flask import Blueprint, Flask, redirect, render_template, request

import repositories.part_repository as part_repository

from models.part import Part
from models.unit import Unit

parts_blueprint = Blueprint("parts", __name__)

# INDEX
@parts_blueprint.route("/parts")
def parts():
    parts = part_repository.select_all()
    return render_template("parts/parts_list.html", parts=parts)