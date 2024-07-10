class Employee:
   
    def __init__(self,name,employee_id,base_salary):
        self.name=name
        self.employee_id=employee_id
        self.base_salary=base_salary

        def __str__(self):
             return f"{self.name}{self.employee_id}{self.base_salary}"

def calculate_salary(self):
  return self.base_salary
pass

class FullTimeEmployee(Employee):

    def __init__(self, name, employee_id, base_salary, benefits):
        self.name=name
        self.employee_id=employee_id
        self.base_salary=base_salary

        self.benefits=benefits
        def __str__(self):
          return f"{self.name}{self.employee_id}{self.base_salary}{self.benfits}"
         
    def calculate_salary(self):
     return self.base_salary+self.benefits 

class PartTimeEmployee(Employee):
  
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
         self.name = name
         self.employee_id = employee_id
         self.hourly_rate=hourly_rate
         self.hours_worked=hours_worked

    def __str__(self):
             return f"{self.name}{self.employee_id}{self.hourly_rate}{self.hours_worked}"
    def calculate_salary(self):
     return self.hourly_rate*self.hours_worked
    
class Company:

  def __init__(self):
    self.employees=[]
  def add_employee(self, employee):
        self.employees.append(employee)
       
  def display_employees(self):
   for employee in self.employees:
        print(f"Name: {employee.name}, Employee ID: {employee.employee_id}" )

 
   
  def calculate_salary(self):
    total_salary = 0
    for employee in self.employees:
        total_salary += employee.calculate_salary()
    return total_salary

company=Company()
emp1 = FullTimeEmployee("Alice", "E001", 50000, 10000)
emp2 = PartTimeEmployee("Bob", "E002", 20, 100)
emp3=FullTimeEmployee("Elizabeth","E003",40000,10000)
company.add_employee(emp1)
company.add_employee(emp2)
company.add_employee(emp3)
company.display_employees()


total_salary = company.calculate_salary()
print(f"Total Salary Expense: ${total_salary}")