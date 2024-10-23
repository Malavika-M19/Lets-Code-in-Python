#Find the factorial of a given number using loops(note the number is received from the user)

n=int(input("Enter the number to get factorial: "))
fact=1
for i in range (1,n+1):
    fact=fact*i
print(f"Factorial of {n} is {fact}")