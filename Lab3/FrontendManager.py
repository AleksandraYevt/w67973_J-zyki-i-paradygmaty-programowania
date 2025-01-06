# 3. FrontendManager - klasa zapewnia interfejs użytkownika do interakcji z EmployeesManager.
# Użytkownicy mogą wykonywać akcje takie jak:
# • Dodawanie nowych pracowników.
# • Wyświetlenie listy istniejących pracowników.
# • Usuwanie pracowników na podstawie przedziału wiekowego.
# • Aktualizacja wynagrodzeń pracowników według nazwiska.

from Employee import *
from EmployeesManager import *
from Utility import inputValue

class FrontendManager:
    
    def __init__(self):
        self.manager = EmployeesManager()
        
    def Menu(self):
        print("\nEmployee Manager: \n")
        message = [
            "1. Add employee",
            "2. List of employees",
            "3. Remove employee",
            "4. Update employee's salary",
            "5. Exit",
        ]
        print('\n'.join(message))
        
        msg = f"Choose an option: (1 - {len(message)})\n"
        return inputValue(msg, 1, len(message))
    
    def run(self):
        while True:
            choice = self.printMenu()
            if choice == 1:
                self.EmployeesMenager.AddEmployee()
            elif choice == 2:
                self.EmployeesMenager.viewEmployees()
            elif choice == 3:
                ageFrom = int(input("Enter age from 1 to 100: "))
                ageTo = int(input("Enter age to 1 to 100: "))
                self.EmployeesMenager.deleteEmployeesByAge(ageFrom, ageTo)
            elif choice == 4:
                firstName = input("Enter employee first name: ")
                lastName = input("Enter employee last name: ")
                salary = int(input("Enter employee new salary: "))
                self.EmployeesMenager.updateSalaryByName(firstName, lastName, salary)
            elif choice == 5:
                break
            else:
                continue