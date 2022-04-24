from flask import Blueprint, Flask, redirect, render_template, request
from controllers.parts_controller import part
from repositories import customer_repository, part_repository, unit_repository
from models.part import Part
from models.customer import Customer
from models.unit import Unit

parts_blueprint = Blueprint("parts", __name__)