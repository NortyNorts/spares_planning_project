from flask import Blueprint, Flask, redirect, render_template, request

import repositories.customer_repository as customer_repository
import repositories.unit_repository as unit_repository

from models.part import Part
from models.customer import Customer
from models.unit import Unit

customers_blueprint = Blueprint("customers", __name__)

# INDEX
@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template("customers/customer_list.html", customers=customers)

# Show
@customers_blueprint.route("/customers/<id>/customer")
def view_customer(id):
    customer = customer_repository.select(id)
    return render_template("customers/customer.html", customer=customer)

# New
@customers_blueprint.route("/customers/new_customer")
def new_customer():
    return render_template("customers/new_customer.html")

# Create
@customers_blueprint.route("/customers", methods = ["POST"])
def add_new_customer():
    name = request.form["name"]
    new_customer = Customer(name)
    customer_repository.save(new_customer)
    return redirect("/customers")

# DELETE
@customers_blueprint.route("/customers/<id>/delete", methods = ["POST"])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")

# EDIT
@customers_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    return render_template("customers/edit_customer.html", customer = customer)

# UPDATE
@customers_blueprint.route("/customers/<id>", methods = ["POST"])
def update_customer(id):
    name = request.form["name"]
    customer = Customer(name, id)
    customer_repository.update(customer)
    return redirect("/customers")
