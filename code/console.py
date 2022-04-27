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

customer2 = Customer("Edinburgh Castle")
customer_repository.save(customer2)

rs_5 = Unit("RS 5kg", "A123", 0, customer1)
unit_repository.save(rs_5)

rs_8 = Unit("RS 8kg", "B123", 0, customer2)
unit_repository.save(rs_8)

rs_10 = Unit("RS 10kg", "C123", 0, customer1)
unit_repository.save(rs_10)

part1 = Part("Snap ring", "DF1115497",1,2500, rs_5)
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

part16 = Part("Snap ring", "DF1115497",1,2500, rs_8)
part_repository.save(part16)

part17 = Part("Sealing set for tank", "RS2599191", 1, 2500, rs_8)
part_repository.save(part17)

part18 = Part("Scale collector & connection ring", "RS2599233", 1, 5000, rs_8)
part_repository.save(part18)

part19 = Part("Tank gasket", "DF1101516", 1, 5000, rs_8)
part_repository.save(part19)

part20 = Part("Collector foil", "RS2579858", 1, 5000, rs_8)
part_repository.save(part20)

part21 = Part("Steam outlet hose", "RS2579820", 1, 5000, rs_8)
part_repository.save(part21)

part22 = Part("Hose set for level control", "RS2579888", 1, 5000, rs_8)
part_repository.save(part22)

part23 = Part("Float assembly", "RS2579882", 1, 10000, rs_8)
part_repository.save(part23)

part24 = Part("Steam hose nipple", "RS2579893", 1, 10000, rs_8)
part_repository.save(part24)

part25 = Part("Cylinder insert with foil", "2579856", 1, 10000, rs_8)
part_repository.save(part25)

part26 = Part("Main Contactor 25A", "1115507", 1, 10000, rs_8)
part_repository.save(part26)

part27 = Part("Inlet Vv", "2579874", 1, 20000, rs_8)
part_repository.save(part27)

part28 = Part("Water cup cpl", "2579884", 1, 20000, rs_8)
part_repository.save(part28)

part29 = Part("Hose set for drain pump ", "2579887", 1, 20000, rs_8)
part_repository.save(part29)

part30 = Part("Hose set for inlet and drain", "2579885", 1, 20000, rs_8)
part_repository.save(part30)

part31 = Part("Snap ring", "DF1115497",1,2500, rs_10)
part_repository.save(part31)

part32 = Part("Sealing set for tank", "RS2599191", 1, 2500, rs_10)
part_repository.save(part32)

part33 = Part("Scale collector & connection ring", "RS2599233", 1, 5000, rs_10)
part_repository.save(part33)

part34 = Part("Tank gasket", "DF1101516", 1, 5000, rs_10)
part_repository.save(part34)

part35 = Part("Collector foil", "RS2579858", 1, 5000, rs_10)
part_repository.save(part35)

part36 = Part("Steam outlet hose", "RS2579820", 1, 5000, rs_10)
part_repository.save(part36)

part37 = Part("Hose set for level control", "RS2579888", 1, 5000, rs_10)
part_repository.save(part37)

part38 = Part("Float assembly", "RS2579882", 1, 10000, rs_10)
part_repository.save(part38)

part39 = Part("Steam hose nipple", "RS2579893", 1, 10000, rs_10)
part_repository.save(part39)

part40 = Part("Cylinder insert with foil", "2579856", 1, 10000, rs_10)
part_repository.save(part40)

part41 = Part("Main Contactor 25A", "1115507", 1, 10000, rs_10)
part_repository.save(part41)

part42 = Part("Inlet Vv", "2579874", 1, 20000, rs_10)
part_repository.save(part42)

part43 = Part("Water cup cpl", "2579884", 1, 20000, rs_10)
part_repository.save(part43)

part44 = Part("Hose set for drain pump ", "2579887", 1, 20000, rs_10)
part_repository.save(part44)

part45 = Part("Hose set for inlet and drain", "2579885", 1, 20000, rs_10)
part_repository.save(part45)



