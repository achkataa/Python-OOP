from abc import abstractmethod, ABC


class Employee:
    def __init__(self, first_name, last_name, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title

    def __repr__(self):
        return f"{self.first_name} {self.last_name}: {self.job_title}"

employee1 = Employee("Gosho", "Petrov", "Seller")
employee2 = Employee("Peter", "Stoyanov", "Perogrammer")
employee3 = Employee("Stoyan", "Goshov", "HR")



class EmployeeList(ABC):
    def __init__(self):
        self.employee_list = []

    @abstractmethod
    def order_by(self, x: Employee):
        pass

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def list_employees(self):
        return sorted(self.employee_list, key=lambda x: self.order_by(x))


class EmployeesListByFirstName(EmployeeList):
    def order_by(self, x: Employee):
        return x.first_name

class EmployeesListByLastName(EmployeeList):
    def order_by(self, x: Employee):
        return x.last_name




el = EmployeesListByFirstName()
el.add_employee(employee1)
el.add_employee(employee2)
el.add_employee(employee3)

[print(e) for e in el.list_employees()]