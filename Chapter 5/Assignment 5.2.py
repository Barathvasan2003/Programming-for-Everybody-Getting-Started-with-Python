"""5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message
and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
Desired Output
Invalid input
Maximum is 10
Minimum is 2
"""


largest_no = None
smallest_no = None
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break

    try:
        num = int(inp)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if largest_no is None or num > largest_no:
        largest_no = num
    if smallest_no is None or num < smallest_no:
        smallest_no = num
print("Largest no:", largest_no)
print("Smallest no:", smallest_no)


