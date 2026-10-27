import os
FILE_NAME= os.path.join(os.path.dirname(__file__),"employees.txt")
def create_employee_file():
    with open(FILE_NAME,"w") as file:
        print("File created")
        file.write("101,Venkat,Tester,45000\n")
        file.write("102,Prabha,Developer,60000\n")
        file.write("103,Swamy,Tester,55000\n")
        file.write("104,Prabhu,Developer,49000\n")
    print("Employees detailes created")

class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id=employee_id
        self.name=name
        self.role=role
        self.salary=int (salary)

    def display_details(self):
        print(self.employee_id, "-",self.name, "-",self.role, "-",self.salary)

#Read file info
def read_employees():
    employees = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            data=line.strip().split(",")
            employee=Employee(data[0],data[1],data[2],data[3])
            employees.append(employee)
    return employees

def add_employee(employee_id,name,role,salary):
    with open(FILE_NAME, "a") as file:
        file.write(f"{employee_id},{name},{role},{salary}\n")
        print("employee added")

#Display all emp
def display_employees(employees):
    print("\, All employees:")
    for employee in employees:
        employee.display_details()


#employees has salary more than 50000
def find_employee_salary(employees):
    print("\n employees whose salary is more than 50000 :")
    for employee in employees:
        if employee.salary>50000:            
         employee.display_details()

def find_highest_salary(employees):
    highest=max(employees, key=lambda emp:emp.salary)
    print("\n employee with highest salary :")
    highest.display_details()
# find employee role


def find_employee_role(employees, role):
    print("\nEmployees in role:role")
    found=False
    for employee in employees:
        if employee.role.lower() == role.lower():
            employee.display_details()
            found=True
        if not found:
            print("no employee found")

#count emplyee
def count_emplyee(employees):
    role_count={}
    for employee in employees:
        role=employee.role
        if role in role_count:
            role_count[role]+=1
        else:
            role_count[role]=1
    print("\n employee count:")
    for role, count in role_count.items():
     print(role, ":",count)

create_employee_file()
employees=read_employees()
display_employees(employees)
find_employee_salary(employees)
find_employee_role(employees, "Tester")
find_highest_salary(employees)
count_emplyee(employees)







