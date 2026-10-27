Problem Statement:
The goal of this program is to automate grading and performance analysis. It takes a collection of student records containing individual subject marks, computes their total and average scores, assigns pass/fail statuses and letter grades, identifies the top-performing student, and filters out high-achievers.

Approach / Logic Used:

The program uses a structured approach to process and analyze the academic data:
• In-Memory Data Architecture: Instead of a text file, it uses a List of Dictionaries. The list holds all students, and each dictionary represents one student with key-value pairs ("id", "name", "python", etc.).
• Dynamic Record Updates: The program runs a loop over the students. It calculates the total and average inside the loop and immediately injects these new metrics back into the student's dictionary (student["grade"] = grade).
• Conditional Branching Rules: A custom function executes conditional rules (if/elif/else) to assign a grade benchmark ("A", "B", "C", "F") based on the calculated average.
• Tracking Variables: To find the highest scorer, it initializes a tracker with the first student's records, compares it against everyone else in a loop, and updates the tracker whenever a higher average score is found.
• Inline Data Filtering: It applies list comprehension filters to quickly scan the completed list and pull out names matching a specific criterion without writing a long, multi-line loop.

How to Run the Program:
1. Ensure Python is installed on your computer.
2. Save this script inside a file named marks_manager.py.
3. Open your terminal or console window.
4. Run the script using this command:bash
python marks_manager.py
Use code with caution.
(Note: Your code includes the line from playwright.sync_api import expect, which is used for web automation testing. However, the rest of your code doesn't actually use it. If you get an error saying ModuleNotFoundError, you can safely delete or comment out that specific line, as it isn’t needed for this program to work).

Sample Input:
The input is hardcoded inside the script as a collection of structured dictionaries:
python
Students=[
    {"id":10,"name":"venkat", "python":80, "SQL":75, "AI":85},
    {"id":11,"name":"prabha", "python":60, "SQL":70, "AI":65 },
    {"id":12,"name":"swamy", "python":90, "SQL":86, "AI":95 },
    {"id":13,"name":"vardhineni", "python":33, "SQL":25, "AI":22 }    
]


Sample Output:
======Student results=======

tudent ID: 10
Student name: venkat
grade: A
Total: 240
Average: 80.0
Result: pass

Student ID: 11
Student name: prabha
grade: B
Total: 195
Average: 65.0
Result: pass

Student ID: 12
Student name: swamy
grade: A
Total: 271
Average: 90.33
Result: pass

Student ID: 13
Student name: vardhineni
grade: F
Total: 80
Average: 26.67
Result: fail

Highest Scoring student: priya
students above 75: ['Rahul', 'priya']

Python Concepts Used:

This script highlights excellent basic-to-intermediate core Python mechanics:
• Dictionaries ({}): Using key-value pairs to represent records, allowing quick access to items using strings like student["python"].
• Lists of Dictionaries ([{}]): Nesting complex structures together to model database-like tables directly in your code code blocks.
• Custom Functions with return Statements: Writing def student_grade(average): to execute a reusable logical task that accepts inputs and explicitly feeds back a specific result string.
• The round() Function: A built-in mathematical helper function that keeps floating-point decimals clean on screen (round(..., 2) forces two decimal positions).
• Linear Maximum Search Algorithm: The classic programming logic pattern where you pick a baseline starting element (highest_student = students[0]) and repeatedly test elements sequentially to track down the absolute highest value.
• List Comprehension: An advanced, idiomatic Python shortcut feature ([student["name"] for student in students if ...]) that compresses a loop, a conditional test, and an accumulation setup into one fast line.
