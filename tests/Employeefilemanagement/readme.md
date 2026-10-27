Problem Statement
The goal is to design and implement a file-based Employee Information Management and Analytics System using Python. The program must store raw comma-separated employee records in a flat text file and provide utility functions to parse, query, filter, and aggregate this data.

Logic Used/Approach:
The program achieves its functionality by breaking down the data life-cycle into three distinct stages: Serialization, Deserialization (Object Mapping), and In-Memory Analytics.
1. File Access & Relative Paths

    Logic: To ensure the code runs flawlessly on any computer regardless of where it is saved, it avoids hardcoded file pathways.
    Implementation: It uses os.path.dirname(__file__) to dynamically grab the exact folder where the script resides, safely appending employees.txt to it.

2. Data Writing (Serialization)

    Logic: Records are structured into a standardized, tabular format using a delimiter (comma) and terminated by a newline indicator (\n).
    Implementation: Opening the file with 'w' overwrites/creates the base file, while opening with 'a' safely appends a new record to the end of the text stream without erasing existing historical data.

3. Data Reading & Object Parsing (Deserialization)

    Logic: Text data must be converted back into structured memory components to make it actionable.

Implementation:

    The file is read line-by-line using a for line in file loop.
    .strip() cleans up hidden trailing whitespaces or newline breaks (\n).
    .split(',') cuts the plain string into an array of individual strings separated by commas.
    These values are immediately fed into the Employee constructor, where the salary string is cast explicitly into a numerical integer (int(salary)) to prepare it for mathematical operations.

4. Conditional Filtering & Linear Searches

    Logic: Finding specific data groups relies on a linear search approach (checking items one by one).

Implementation:

    Salary Filter: Iterates through the list of objects, executing an evaluation (if employee.salary > 50000) to selectively trigger the record's printing routine.
    Role Lookup: Converts both the target criteria and the record value to lowercase via .lower() (e.g., evaluating "tester" == "tester"), ensuring that mismatched casing won't cause the lookup to fail.

5. Extremum Evaluation (Highest Salary)

    Logic: Isolating a single peak record within a collection of complex objects.
    Implementation: It passes a inline lambda function as a key parameter directly into Python's built-in max() utility. The lambda tells the execution engine: "Ignore the text attributes, evaluate the objects strictly by comparing their internal numerical .salary values."

6. Aggregation & Frequency Distribution

    Logic: Counting unique occurrences on the fly requires an indexable associative map (a Dictionary).

Implementation:

    An empty dictionary (role_count = {}) maps unique roles to counter numbers.
    For each record, if the role isn't tracked yet, it seeds the dictionary key with a starting value of 1.
    If the key already exists, it increments the tracking index (role_count[role] += 1).

Sample Input:
101,Venkat,Tester,45000
102,Prabha,Developer,60000
103,Swamy,Tester,55000
104,Prabhu,Developer,49000

Sample Output:
File created
Employees detailes created

 \ All employees: 
101 - Venkat - Tester - 45000
102 - Prabha - Developer - 60000
103 - Swamy - Tester - 55000
104 - Prabhu - Developer - 49000

 employees whose salary is more than 50000 : 
102 - Prabha - Developer - 60000
103 - Swamy - Tester - 55000

Employees in role:Tester 
101 - Venkat - Tester - 45000
103 - Swamy - Tester - 55000

 employee with highest salary : 
102 - Prabha - Developer - 60000

 employee count: 
Tester : 2
Developer : 2

A simple Python console application to create, read, parse, and analyze employee records stored in a text file (`employees.txt`).


File Initialization: Automatically generates `employees.txt` with initial employee rows.
Data Parsing: Converts comma-separated text lines into structured `Employee` class objects.
Filtering: Lists employees with salaries above a threshold (`> 50000`).
Role Search: Case-insensitive search for employees matching a specified job role.
Analytics: Identifies the employee with the highest salary and counts total employees per role.

How to Run
1. Save the Python script as `employeefilemanagement.py`.
2. Open your terminal or command prompt in the script's directory.
3. Run the script:
   ```bash
   python employee_manager.py
   ```
4. An `employees.txt` file will be generated in the same directory alongside t

Python Concepts Covered

    File I/O (open, read, write, append): Opening files in write ('w'), read ('r'), and append ('a') modes.
    Path Manipulation (os.path): Using os.path.dirname() and os.path.join() to safely handle file paths relative to the script location.
    Object-Oriented Programming (OOP Classes & Constructors): Defining an Employee class with an __init__ constructor method and custom instance methods (display_details).
    String Manipulation: Stripping whitespace (.strip()) and splitting CSV-style lines (.split(',')).
    Lambda Functions & Higher-Order Functions: Finding the maximum value using a custom key selector (max(..., key=lambda emp: emp.salary)).
    Control Flow & Collections: Using lists, dictionaries (role_count), for/while loops, and if-else condition checks.

Employee Management System

A simple Python console application to create, read, parse, and analyze employee records stored in a text file (`employees.txt`).

Features
File Initialization: Automatically generates `employees.txt` with initial employee rows.
Data Parsing: Converts comma-separated text lines into structured `Employee` class objects.
Filtering: Lists employees with salaries above a threshold (`> 50000`).
Role Search: Case-insensitive search for employees matching a specified job role.
Analytics: Identifies the employee with the highest salary and counts total employees per role.


How to Run
1. Save the Python script as `employeefilemanagement.py`.
2. Open your terminal or command prompt in the script's directory.
3. Run the script:bash
   python employee_manager.py
4. An `employees.txt` file will be generated in the same directory alongside the console output.

Input:
The script automatically generates and writes the following data into employees.txt:

101,Venkat,Tester,45000
102,Prabha,Developer,60000
103,Swamy,Tester,55000
104,Prabhu,Developer,49000

Sample Output:
text

File created
Employees detailes created

 \ All employees: 
101 - Venkat - Tester - 45000
102 - Prabha - Developer - 60000
103 - Swamy - Tester - 55000
104 - Prabhu - Developer - 49000

 employees whose salary is more than 50000 : 
102 - Prabha - Developer - 60000
103 - Swamy - Tester - 55000

Employees in role:Tester 
101 - Venkat - Tester - 45000
103 - Swamy - Tester - 55000

 employee with highest salary : 
102 - Prabha - Developer - 60000

 employee count: 
Tester : 2
Developer : 2

Python Concepts Covered:
• File I/O (open, read, write, append): Opening files in write ('w'), read ('r'), and append ('a') modes.
• Path Manipulation (os.path): Using os.path.dirname() and os.path.join() to safely handle file paths relative to the script location.
• Object-Oriented Programming (OOP Classes & Constructors): Defining an Employee class with an __init__ constructor method and custom instance methods (display_details).
• String Manipulation: Stripping whitespace (.strip()) and splitting CSV-style lines (.split(',')).
• Lambda Functions & Higher-Order Functions: Finding the maximum value using a custom key selector (max(..., key=lambda emp: emp.salary)).
• Control Flow & Collections: Using lists, dictionaries (role_count), for/while loops, and if-else condition checks.


