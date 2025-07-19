#School Calculator – Python Project#

A command-line calculator written in Python for school-level math operations. This tool supports both basic arithmetic and advanced scientific calculations, including history tracking.

Features
Basic Operations

Addition

Subtraction

Multiplication

Division

Scientific Functions

Power (Exponentiation)

Square Root

Factorial

Sine, Cosine, Tangent (in degrees)

Logarithm (base 10 or custom base)

Natural Logarithm (ln)

History Tracking

View calculation history

Clear history

Technologies Used
Python 3

Standard math module

How to Run
Make sure Python 3 is installed on your computer.

Save the code to a file, for example: calculator.py

Open a terminal or command prompt.

Run the program using:

nginx
Copy
Edit
python calculator.py
Menu Example
markdown
Copy
Edit
=== calculator for school ===
1.  Addition (+)
2.  Subtraction (-)
3.  Multiplication (×)
4.  Division (÷)
5.  Power (^)
6.  Square Root (√)
7.  Factorial (!)
8.  Sin (degrees)
9.  Cos (degrees)
10. Tan (degrees)
11. Logarithm (base 10)
12. Natural Logarithm (ln)
13. Show History
14. Clear History
15. Exit
=========================
Input Examples
Addition Example:

sql
Copy
Edit
Enter your choice (1-15): 1
Enter first number: 12
Enter second number: 5
Result: 17.0
Show History Example:

cpp
Copy
Edit
Enter your choice (1-15): 13
--- Calculation History ---
1. 12.0 + 5.0 = 17.0
Error Handling
Prevents division by zero

Validates input for square root and logarithms (must be positive)

Checks for valid integer input for factorial

Catches invalid menu selections and non-numeric input

Educational Use
This project is ideal for learning:

Python class and object design

Exception handling

Command-line interface development

Basic mathematical logic in code

License
This project is free to use for educational and personal learning purposes.




