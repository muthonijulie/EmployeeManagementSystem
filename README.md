Create a simple employee management system using Object-Oriented Programming (OOP) concepts in Python. The system should manage different types of employees, and should support the following operations:


1. Add new employees to the system.


2. Display the details of all employees.


3. Calculate the total salary expense of the company.


Requirements:


1. Employee Base Class:


    - Attributes: `name`, `employee_id`, `base_salary`.


    - Methods:


        - `__init__(self, name, employee_id, base_salary)`: Initializes a new employee with the given details.


        - `__str__(self)`: Returns a string representation of the employee.


        - `calculate_salary(self)`: Returns the base salary (to be overridden by subclasses if needed).


2. FullTimeEmployee Class (inherits from Employee):


    - Additional Attributes: `benefits`.


    - Methods:


        - `__init__(self, name, employee_id, base_salary, benefits)`: Initializes a new full-time employee with the given details.


        - `__str__(self)`: Returns a string representation of the full-time employee.


        - `calculate_salary(self)`: Returns the total salary including benefits.


3. PartTimeEmployee Class (inherits from Employee):


    - Additional Attributes: `hourly_rate`, `hours_worked`.


    - Methods:


        - `__init__(self, name, employee_id, hourly_rate, hours_worked)`: Initializes a new part-time employee with the given details.


        - `__str__(self)`: Returns a string representation of the part-time employee.


        - `calculate_salary(self)`: Returns the total salary based on hourly rate and hours worked.


4. Company Class:


    - Attributes: `employees` (a list of Employee objects).


    - Methods:


        - `__init__(self)`: Initializes the company with an empty list of employees.


        - `add_employee(self, employee)`: Adds a new employee to the company.


        - `display_employees(self)`: Displays the details of all employees.


        - `calculate_total_salary(self)`: Calculates and returns the total salary expense of the company.


Implementation


Provide the implementation for the `Employee`, `FullTimeEmployee`, `PartTimeEmployee`, and `Company` classes. Ensure that your code follows the OOP principles and includes appropriate use of inheritance.


Example Usage


# Creating a company
company = Company()

# Adding employees to the company
emp1 = FullTimeEmployee("Alice", "E001", 50000, 10000)
emp2 = PartTimeEmployee("Bob", "E002", 20, 100)
company.add_employee(emp1)
company.add_employee(emp2)

# Displaying employees
company.display_employees()

# Calculating total salary expense
total_salary = company.calculate_total_salary()
print(f"Total Salary Expense: ${total_salary}")

