"""
Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
An example run of the program (numbers in bold are typed in by the user)
Enter the month: 3
Month 3 is March
"""
n=int(input("Enter the month: "))
# Determine the month name
if n == 1:
    month_name = "January"
elif n == 2:
    month_name = "February"
elif n == 3:
    month_name = "March"
elif n == 4:
    month_name = "April"
elif n == 5:
    month_name = "May"
elif n == 6:
    month_name = "June"
elif n == 7:
    month_name = "July"
elif n == 8:
    month_name = "August"
elif n == 9:
    month_name = "September"
elif n == 10:
    month_name = "October"
elif n == 11:
    month_name = "November"
elif n == 12:
    month_name = "December"
else:
    month_name = "Invalid month"

# Output the result
print(f"Month {n} is {month_name}")

    