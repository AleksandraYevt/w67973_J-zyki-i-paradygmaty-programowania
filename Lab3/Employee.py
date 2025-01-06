# 1. Employee - reprezentuje indywidualnego pracownika z następującymi atrybutami:
# • name: Imię i nazwisko pracownika.
# • age: Wiek pracownika.
# • salary: Wynagrodzenie pracownika.
# Klasa ma udostępniać metody pozwalające na reprezentację informacji o pracownikach, które zostały wprowadzone jako dane wejściowe. 

class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary 
        
    def employee_info(self):
        return(f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nSalary: {self.salary}")
    
# first_employee = Employee('Agata', 'Christi', 23, 100)
# print(first_employee.employee_info())