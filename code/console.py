import pdb

from models.customer import Customer
import repositories.customer_repository as customer_repository

from models.part import Part
import repositories.part_repository as part_repository

from models.unit import Unit
import repositories.unit_repository as unit_repository

part_repository.delete_all()
unit_repository.delete_all()
customer_repository.delete_all()

unit1 = Unit("RS5", "C123", 500)
unit_repository.save(unit1)

part1 = Part("Snap_ring", "A123",1,100, unit1)
part_repository.save(part1)

part2 = Part("Gasket", "B123", 1, 200, unit1)
part_repository.save(part2)

customer1 = Customer("Aberdeen_Uni", unit1)
customer_repository.save(customer1)


