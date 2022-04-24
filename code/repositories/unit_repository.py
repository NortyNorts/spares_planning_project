# Import controllers when creating front end
from db.run_sql import run_sql
from repositories import customer_repository, part_repository, unit_repository
from models.customer import Customer
from models.unit import Unit
from models.part import Part

def save(unit):
    sql = "INSERT INTO unit (type, serial_number, part_id, hours_run) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [unit.type, unit.serial_number, unit.part.id, unit.hours_run]
    results = run_sql(sql, values)
    id = results [0]['id']
    unit.id = id

def select_all():
    units = []
    sql = "SELECT * FROM units"
    results = run_sql(sql)
    for result in results:
        part = part_repository.select(result["part_id"])
        unit = Unit(result["type"], result["serial_number"], parts_list, result["id"])
        units.append(unit)
    return units