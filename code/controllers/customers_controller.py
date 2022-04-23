from flask import Blueprint, Flask, redirect, render_template, request
from controllers.zombies_controller import zombies
from models.biting import Biting
from repositories import biting_repository, zombie_repository, human_repository