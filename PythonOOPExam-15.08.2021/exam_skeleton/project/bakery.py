from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class FoodFactory:
    @staticmethod
    def create_food(food_type, name, price):
        if food_type == "Bread":
            return Bread(name, price)
        elif food_type == "Cake":
            return Cake(name, price)
        else:
            return None

class DrinksFactory:
    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        elif drink_type == "Water":
            return Water(name, portion, brand)
        else:
            return None

class TablesFactory:
    @staticmethod
    def create_table(table_type, table_number, capacity):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)
        else:
            return None



class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.food_names = []
        self.drinks_menu = []
        self.drink_names = []
        self.tables_repository = []
        self.tables_numbers = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value


    def add_food(self, food_type: str, name: str, price: float):
        if name in self.food_menu:
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = FoodFactory().create_food(food_type, name, price)
        self.food_menu.append(food)
        self.food_names.append(name)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand:str):
        if name in self.drink_names:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = DrinksFactory().create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        self.drink_names.append(name)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in self.tables_numbers:
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = TablesFactory().create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        self.tables_numbers.append(table_number)
        return f"Added table number {table_number} in the bakery"

    def find_free_table(self, number_of_people):
        return [t for t in self.tables_repository if t.is_reserved == False and t.capacity >= number_of_people]

    def reserve_table(self, number_of_people: int):
        table_ll = self.find_free_table(number_of_people)
        if not table_ll:
            return f"No available table for {number_of_people} people"
        table = table_ll[0]
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def __get_table(self, table_number):
        return [t for t in self.tables_repository if t.table_number == table_number][0]

    def get_food_obj_by_name(self, food_name):
        return [food for food in self.food_menu if food.name == food_name][0]


    def order_food(self, table_number: int, *args):
        if not table_number in self.tables_numbers:
            return f"Could not find table {table_number}"
        table = self.__get_table(table_number)

        available_foods = [self.get_food_obj_by_name(food_name) for food_name in args if food_name in self.food_names]
        unavailable_foods = [food_name for food_name in args if food_name not in self.food_names]

        for food in available_foods:
            table.order_food(food)

        result = ""
        result += f"Table {table_number} ordered:\n"
        result += '\n'.join([repr(food) for food in available_foods])
        result += "\n"
        result += f"{self.name} does not have in the menu:\n"
        result += '\n'.join(unavailable_foods)

        return result

    def get_drink_obj_by_name(self, drink_name):
        return [drink for drink in self.drinks_menu if drink.name == drink_name][0]

    def order_drink(self, table_number: int, *args):
        if not table_number in self.tables_numbers:
            return f"Could not find table {table_number}"
        table = self.__get_table(table_number)

        available_drinks = [self.get_drink_obj_by_name(drink_name) for drink_name in args if drink_name in self.drink_names]
        unavailable_drinks = [drink_name for drink_name in args if drink_name not in self.drink_names]

        for drink in available_drinks:
            table.order_drink(drink)

        result = ""
        result += f"Table {table_number} ordered:\n"
        result += '\n'.join([repr(drink) for drink in available_drinks])
        result += "\n"
        result += f"{self.name} does not have in the menu:\n"
        result += '\n'.join(unavailable_drinks)

        return result

    def get_table_by_number(self, table_number):
        return [table for table in self.tables_repository if table.table_number == table_number][0]

    def leave_table(self, table_number: int):
        table = self.get_table_by_number(table_number)
        bill = table.get_bill()
        table.clear()
        result = f"Table: {table_number}\nBill: {bill}"
        return result

    def get_free_tables_info(self):
        free_tables_infos = [t.free_table_info() for t in self.tables_repository if t.is_reserved == False]
        return '\n'.join(free_tables_infos)


    def get_total_income(self):
        total_income = sum([t.get_bill() for t in self.tables_repository])
        return f"Total income: {total_income:.2f}lv"