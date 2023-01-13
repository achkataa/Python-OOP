from project.bakery import Bakery

b = Bakery("Na gosho")
b.add_food("Cake", "sladka torta", 10)
b.add_food("Cake", "solena torta", 20)
b.add_food("Cake", "kisela torta", 30)

b.add_drink("Water", "mineralna", 1, "devin")
b.add_drink("Tea", "nemineralna", 2, "burgaska")


b.add_table("OutsideTable", 56, 20)

b.order_food(56, "solena torta", "torta", "kisela torta")
b.order_drink(56, "mineralna", "nemineralna", "nz")

print(b.reserve_table(6))

