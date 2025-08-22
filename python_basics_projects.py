"""
==========================================
 Beginner Python Projects
 Based on: Programming for Everybody (Dr. Chuck)
==========================================
"""

# -------------------------------------------------
# 1. Hello World Greeter
#    Ask the user’s name and greet them with a custom message.
# -------------------------------------------------
print("Welcome Greeter")
from datetime import datetime
current_time = datetime.now()
hour = current_time.hour
while True:
    user_name = input("Enter your name: ").strip()

    if user_name.replace(" ","").isalpha():
        print("Welcome",user_name)
        if 0 < hour < 12:
            print("Good morning")
        elif 12 < hour < 18:
            print("Good evening")
        else:
            print("Good night")
        break
    else:
        print("Please dont enter a valid name")
print("\n")


# -------------------------------------------------
# 2. Simple Calculator
#    Take two numbers and an operator (+, -, *, /) as input and display the result.
# -------------------------------------------------
print("Simple Calculator")
while True:
    first_no = float(input("Enter first number: "))
    sec_no = float(input("Enter second number: "))
    operator = input("Enter your operator(+, -, *, /,%,**): ")
    result = None
    try:
        if operator == "+":
            result = first_no + sec_no
        elif operator == "-":
            result = first_no - sec_no
        elif operator == "*":
            result = first_no * sec_no
        elif operator == "/":
            result = first_no / sec_no
        elif operator == "%":
            result = first_no % sec_no
        elif operator == "**":
            result = first_no ** sec_no
        else:
            print("Invalid operator")
            continue
        print("Result:",result)
    except ValueError:
        print("Error: Please enter valid numbers only ❌")
    except ZeroDivisionError:
        print("Error: Division or modulus by zero is not allowed ❌")
    do_continue = input("Do you want to continue? (y/n): ").lower()
    if do_continue == "n":
        print("Goodbye")
        break
    print("\n")


# -------------------------------------------------
# 3. Grade Checker
#    Input marks (0–100) and output the grade (A, B, C, D, F).
# -------------------------------------------------
print("Grade Checker")
try:
    marks = float(input("Enter your marks: "))
    if 0 <= marks <= 100:
        if marks >= 90:
            print("Your grade is A+, 🌟 Outstanding! Keep shining!")
        elif marks >= 80:
            print("Your grade is A,💪 Excellent work, stay consistent!")
        elif marks >= 70:
            print("Your grade is B,👍 Good job, you’re improving well!")
        elif marks >= 50:
            print("Your grade is D,🙂 Not bad, keep practicing!")
        elif marks >= 45 :
            print("Your grade is C,⚡ You can do better, don’t give up!")
        elif  marks >= 0 :
            print("Your grade is F,❌ Failure is a step to success, keep trying!")
    else:
        print("Please enter a valid number only(0-100)")
except ValueError:
    print("Error: Please enter valid numbers only")
print("\n")
# -------------------------------------------------
# 4. Odd or Even Number Checker
#    Ask for a number and print whether it is odd or even.
# -------------------------------------------------
print("Odd or Even Number Checker")
count = 0
num = int(input("Enter a number: "))
if num < 0:
    print("please enter a valid number to calculate prime numbers")
else:
    if num > 1:
        for i in range (1 ,num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print("The number is prime")
        else:
            print("The number is not prime")
    if num >= 0:
        if num % 2 == 0:
            print(num, "is an even number.")
        else:
            print(num, "is an odd number.")
print("\n")

# -------------------------------------------------
# 5. Unit Converter
#    Write a function to convert Celsius to Fahrenheit.
# -------------------------------------------------
print("""
Unit Converter
===MENU===
1. convert Celsius to Fahrenheit
2. convert Fahrenheit to Celsius
3. convert km to miles
4. convert kg to pounds
 """)
def unit_converter(value,no):
    if no == 1:
        return (value * 9/5) + 32
    elif no == 2:
        return (value - 32) * 5/9
    elif no == 3:
        return value / 1.609
    elif no == 4:
        return value * 2.205
    else:
        return "invalid choice_no"

choice_no = int(input("Enter your choice: "))
inp = int(input("Enter a the value: "))
print(unit_converter(inp,choice_no))
print("\n")

# -------------------------------------------------
# 6. Tip Calculator
#    Write a function that takes bill amount and tip % and returns final amount.
# -------------------------------------------------
print("Tip Calculator")
def tip_calculator(bill, tip,people):
    tip_amount = (bill * tip) / 100
    amount = round(int(bill + tip_amount),2)
    total_amount = amount / people
    return total_amount

bill_amount = float(input("Enter your bill: "))
raw_tip_percentage = input("Enter your percentage: ")
tip_percentage = int(raw_tip_percentage)  if raw_tip_percentage else 5
raw_total_people = input("Enter how many people should be split?")
total_people = int(raw_total_people)   if raw_total_people else 1
print(tip_calculator(bill_amount, tip_percentage,total_people))
print("\n")

# -------------------------------------------------
# 7. Countdown Timer
#    Input a number and print countdown to 0.
# -------------------------------------------------
import time
print("Countdown Timer")
minutes = int(input("Enter a time in minutes: "))
seconds = minutes * 60
while seconds > 0:
    print(seconds,"sec")
    time.sleep(1)
    seconds -= 1
print("Time Over")
print("\n")


# -------------------------------------------------
# 8. Multiplication Table Generator
#    Ask for a number and print its multiplication table (1–10).
# -------------------------------------------------
print("Multiplication Table Generator")

def generate_table(choice, number=None):
    raw_table_range = input("Enter a range for the table: ")
    table_range = int(raw_table_range) if raw_table_range.isdigit() else 10

    if choice == 1 and number is not None:
        print(f"\nMultiplication Table for {number}")
        for i in range(1, table_range + 1):
            print(f"{number} * {i} = {number * i}")
    elif choice == 2:
        print("\nSquares Table")
        for i in range(1, table_range + 1):
            print(f"{i}^2 = {i ** 2}")
    elif choice == 3 and number is not None:
        print(f"\nCubes Table for {number}")
        for i in range(1, table_range + 1):
            print(f"{i}^3 = {i ** 3}")
    else:
        print("Invalid choice or missing number.")

# Menu
print("""
===MENU===
1.) Multiplication table
2.) Squares table
3.) Cubes table
""")
try:
    user_choice = int(input("Enter your choice: "))
    if user_choice not in [1, 2, 3]:
        raise ValueError("Invalid choice.")
    number = None
    if user_choice in [1,2,3]:
        if user_choice == 1:
            number = int(input("Enter a number: "))
        generate_table(user_choice, number)
except ValueError as e:
        print(f"Invalid input: {e}")
        quit()

print("\n")
# -------------------------------------------------
# 9. Number Analyzer
#    Take numbers from user until "done" is entered.
#    Print count, sum, average, min, and max.
# -------------------------------------------------
print("Find count, sum, average, min, and max")
largest_no = None
smallest_no = None
count = 0
total_no = 0
average = 0
while True:
    numbers = input("Enter a number: ")
    if numbers == "done":
        break
    try:
        number = int(numbers)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if largest_no is None or number > largest_no:
        largest_no = number
    if smallest_no is None or number < smallest_no:
        smallest_no = number
    count += 1
    total_no += number
    average = int(total_no / count)

print(f"sum no:{total_no}\n"
      f"count:{count}\n"
      f"avg no:{average}\n"
      f"max no:{largest_no}\n"
      f"min no:{smallest_no}")
print("\n")

# -------------------------------------------------
# 10. Guess the Number Game
#     Program picks a random number (1–20).
#     User keeps guessing until correct, with hints.
# -------------------------------------------------
print("Guess the Number Game")
import random
computer_choice = random.randint(1, 20)
print(f"computer choice: {computer_choice}") #testing purpose
computer_choice = str(computer_choice)
while True:
    user_input = input("Enter a number: ")
    if user_input == computer_choice:
        break

print(f"computer choice: {computer_choice} and Your choice: {user_input}\nGame Over")
print("\n")