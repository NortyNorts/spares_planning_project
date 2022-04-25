# Import controllers when creating front end
from db.run_sql import run_sql
from repositories import customer_repository, part_repository, unit_repository
from models.customer import Customer
from models.unit import Unit
from models.part import Part

def save(part):
    sql = "INSERT INTO parts (name, number, number_per_unit, hour_exp, unit_id) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values = [part.name, part.number, part.number_per_unit, part.hour_exp, part.unit.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    part.id = id

def select_all():
    parts = []
    sql = "SELECT * FROM parts"
    results = run_sql(sql)
    for result in results:
        unit = unit_repository.select(result["unit_id"])
        part =  Part(result["name"], result["number"], result["number_per_unit"], result["hour_exp"], unit, result["id"])
        parts.append(part)
    return parts

def select(id):
    sql = "SELECT * FROM parts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    unit = unit_repository.select(result["unit_id"])
    part =  Part(result["name"], result["number"], result["number_per_unit"], result["hour_exp"], unit, result["id"])
    return part

def delete_all():
    sql = "DELETE FROM parts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM parts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(part):
    sql = "UPDATE parts SET (name, number, number_per_unit, hour_exp, unit_id) = (%s,%s,%s,%s, %s) WHERE id = %s"
    values = [part.name, part.number, part.number_per_unit, part.hour_exp, part.unit.id]
    run_sql(sql, values)

