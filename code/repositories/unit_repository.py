# Import controllers when creating front end
from db.run_sql import run_sql
from repositories import customer_repository, part_repository, unit_repository
from models.customer import Customer
from models.unit import Unit
from models.part import Part

def save(unit):
    sql = "INSERT INTO units (type, serial_number, hours_run) VALUES (%s,%s,%s) RETURNING id"
    values = [unit.type, unit.serial_number, unit.hours_run]
    results = run_sql(sql, values)
    id = results [0]['id']
    unit.id = id

def select_all():
    units = []
    sql = "SELECT * FROM units"
    results = run_sql(sql)
    for result in results:
        unit = Unit(result["type"], result["serial_number"], result["id"])
        units.append(unit)
    return units

def select(id):
    sql = "SELECT * FROM units WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    unit = Unit(result["type"], result["serial_number"], result["id"])
    return unit

def delete_all():
    sql = "DELETE FROM units"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM units WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(unit):
    sql = "UPDATE units SET (type, serial_number, hours_run) = (%s, %s, %s) WHERE id = %s"
    values = [unit.type, unit.serial_number, unit.hours_run, unit.id]
    run_sql(sql, values)

def parts_list(unit):
    sql = "SELECT parts.* FROM parts INNER JOIN units ON "