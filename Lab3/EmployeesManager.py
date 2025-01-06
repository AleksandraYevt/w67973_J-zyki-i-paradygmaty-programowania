# 2. EmployeesManager – klasa która jest odpowiedzialna za zarządzanie listą pracowników. Posiada nastepujące funkcjonalności:
from Employee import Employee

class EmployeesManager:
        def __init__(self):
            self.employee_list = []
            
        def employee_add(self):     # • dodanie nowego pracownika do listy,
            print("Enter information about the new employee: ")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            self.employee_list.append(Employee(first_name, last_name, age, salary))
            
        def employee_view(self):    # • wyświetlenie listy wszystkich istniejących pracowników,
            if len(self.employee_list) == 0:
                print("There are no employees in database!")
                return
            else:
                for emp in self.employee_list:
                    print(emp) 
                    
                    
        def employee_remove_by_age(self, min_age, max_age):   # • usunięcie pracowników w określonym przedziale wiekowym,
            self.employee_list = [emp for emp in self.employee_list if not (min_age <= emp.age <= max_age)]
            
        def employee_find_by_name(self, first_name, last_name):    # • wyszukanie pracownika według jego imienia i nazwiska,
            for emp in self.employee_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    return emp
                return None
            
        def employee_new_salary_by_name(self, first_name, last_name, new_salary): # • aktualizacja wynagrodzenia pracownika według jego imienia i nazwiska.
            emp = self.employee_find_by_name(first_name, last_name)
            if emp == None:
                print("There's no such employee!")
            else:
                emp.salary = new_salary

