from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value >= 1 and value <= 50:
            self.__table_number = value
        else:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")