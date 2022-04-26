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

customer1 = Customer("CodeClan")
customer_repository.save(customer1)

rs_5 = Unit("RS 5kg", "C123", 0, customer1)
unit_repository.save(rs_5)

part1 = Part("Snap_ring", "DF1115497",1,2500, rs_5)
part_repository.save(part1)

part2 = Part("Sealing set for tank", "RS2599191", 1, 2500, rs_5)
part_repository.save(part2)

part3 = Part("Scale collector & connection ring", "RS2599233", 1, 5000, rs_5)
part_repository.save(part3)

part4 = Part("Tank gasket", "DF1101516", 1, 5000, rs_5)
part_repository.save(part4)

part5 = Part("Collector foil", "RS2579858", 1, 5000, rs_5)
part_repository.save(part5)

part6 = Part("Steam outlet hose", "RS2579820", 1, 5000, rs_5)
part_repository.save(part6)

part7 = Part("Hose set for level control", "RS2579888", 1, 5000, rs_5)
part_repository.save(part7)

part8 = Part("Float assembly", "RS2579882", 1, 10000, rs_5)
part_repository.save(part8)

part9 = Part("Steam hose nipple", "RS2579893", 1, 10000, rs_5)
part_repository.save(part9)

part10 = Part("Cylinder insert with foil", "2579856", 1, 10000, rs_5)
part_repository.save(part10)

part11 = Part("Main Contactor 25A", "1115507", 1, 10000, rs_5)
part_repository.save(part11)

part12 = Part("Inlet Vv", "2579874", 1, 20000, rs_5)
part_repository.save(part12)

part13 = Part("Water cup cpl", "2579884", 1, 20000, rs_5)
part_repository.save(part13)

part14 = Part("Hose set for drain pump ", "2579887", 1, 20000, rs_5)
part_repository.save(part14)

part15 = Part("Hose set for inlet and drain", "2579885", 1, 20000, rs_5)
part_repository.save(part15)


