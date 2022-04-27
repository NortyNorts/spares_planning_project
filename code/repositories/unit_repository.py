# Import controllers when creating front end
from db.run_sql import run_sql
from repositories import customer_repository, part_repository, unit_repository
from models.customer import Customer
from models.unit import Unit
from models.part import Part

def save(unit):
    sql = "INSERT INTO units (unit_type, serial_number, hours_run, customer_id) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [unit.unit_type, unit.serial_number, unit.hours_run, unit.customer.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    unit.id = id

def select_all():
    units = []
    sql = "SELECT * FROM units"
    results = run_sql(sql)
    for result in results:
        customer = customer_repository.select(result["customer_id"])
        unit = Unit(result["unit_type"], result["serial_number"], result["hours_run"], customer, result["id"])
        units.append(unit)
    return units

def select(id):
    sql = "SELECT * FROM units WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    customer = customer_repository.select(result["customer_id"])
    unit = Unit(result["unit_type"], result["serial_number"], result["hours_run"], customer, result["id"])
    return unit

def delete_all():
    sql = "DELETE FROM units"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM units WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(unit):
    sql = "UPDATE units SET (unit_type, serial_number, hours_run, customer_id) = (%s, %s, %s,%s) WHERE id = %s"
    values = [unit.unit_type, unit.serial_number, unit.hours_run, unit.customer.id, unit.id]
    run_sql(sql, values)

def select_by_unit(id):
    units = []
    sql = "SELECT * FROM units WHERE customer_id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        for result in results:
            customer = customer_repository.select(result["customer_id"])
            unit =  Unit(result["unit_type"], result["serial_number"], result["hours_run"], customer, result["id"])
            units.append(unit)
        return units
    else:
        return []