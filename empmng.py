class Employee:#base class
   
    def __init__(self,name,employee_id,base_salary):#constructor with parameters
        self.name=name
        self.employee_id=employee_id
        self.base_salary=base_salary

    def __str__(self):#returns string representation of employee
      return f"{self.name}{self.employee_id}{self.base_salary}"

    def calculate_salary(self):#method for calculate_salary
     return self.base_salary
    pass#does nothing

class FullTimeEmployee(Employee):#inherits properties and behaviour of employee class

    def __init__(self, name, employee_id, base_salary, benefits):
        super().__init__(name,employee_id,base_salary)#inheritance
        self.benefits=benefits#new attribute
    def __str__(self):
      return f"{self.name}{self.employee_id}{self.base_salary}{self.benefits}"
         
    def calculate_salary(self):
     return self.base_salary+self.benefits #calculates the total salry of a full time employee

class PartTimeEmployee(Employee):#inherits from Employee class
  
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
          super().__init__(name,employee_id)#inheritance
          self.hourly_rate=hourly_rate#new attribute
          self.hours_worked=hours_worked#new attribute

    def __str__(self):
             return f"{self.name}{self.employee_id}{self.hourly_rate}{self.hours_worked}"
    def calculate_salary(self):
     return self.hourly_rate*self.hours_worked#calculate salary for partTimeEmployee
    
class Company:#allows the company to add and display the emeployee's details

  def __init__(self):
    self.employees=[]#create an empty list
  def add_employee(self, employee):#method for adding employees
        self.employees.append(employee)
       
  def display_employees(self):#displays content of employee's
   for employee in self.employees:
        print(f"Name: {employee.name}, Employee ID: {employee.employee_id}" )

 
   
  def calculate_salary(self):#gives the total salary expenses of the company
    total_salary = 0
    for employee in self.employees:
        total_salary += employee.calculate_salary()
    return total_salary

company=Company()
emp1 = FullTimeEmployee("Alice", "E001", 50000, 10000)
emp2 = PartTimeEmployee("Bob", "E002", 20, 100)
emp3=FullTimeEmployee("Elizabeth","E003",40000,10000)
#add employees details to the empty list:name and employee's ID
company.add_employee(emp1)
company.add_employee(emp2)
company.add_employee(emp3)
#display details
company.display_employees()


total_salary = company.calculate_salary()
print(f"Total Salary Expense: ${total_salary}")#display total expenses
#end