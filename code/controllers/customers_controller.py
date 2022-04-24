from flask import Blueprint, Flask, redirect, render_template, request

import repositories.customer_repository as customer_repository

from models.part import Part
from models.customer import Customer
from models.unit import Unit

customers_blueprint = Blueprint("customers", __name__)

# INDEX
@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template("customers/customer_list.html", customers=customers)