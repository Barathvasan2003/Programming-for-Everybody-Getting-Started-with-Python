"""3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.

Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly."""

hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
gross_pay = 0
if hours <= 40:
    gross_pay = hours * rate_per_hour
else:
    extra_hr = hours - 40
    extra_pay = 1.5 * extra_hr * rate_per_hour #1.5 * 5 hr extra * 10.50 hr rate
    gross_pay = 40 * rate_per_hour + extra_pay #40 hr fixed * rate per hr + extra hr(5hr)
print(gross_pay)






