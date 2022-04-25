# Import controllers when creating front end
from db.run_sql import run_sql
from repositories import customer_repository, part_repository, unit_repository
from models.customer import Customer
from models.unit import Unit

def save(customer):
    sql = "INSERT INTO customers (name, unit_id) VALUES (%s,%s) RETURNING id"
    values = [customer.name, customer.unit.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    customer.id = id

def select_all():
    customers = []
    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    print(results)
    for result in results:
        print(result["unit_id"])
        unit = unit_repository.select(result["unit_id"])
        customer =  Customer(result["name"], unit, result["id"])
        customers.append(customer)
    return customers

def select(id):
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    unit = unit_repository.select(result["unit_id"])
    customer = Customer(result["name"], unit, result["id"])
    return customer

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(customer):
    sql = "UPDATE customers SET (name, unit_id) = (%s, %s) WHERE id = %s"
    values = [customer.name, customer.unit.id]
    run_sql(sql, values)