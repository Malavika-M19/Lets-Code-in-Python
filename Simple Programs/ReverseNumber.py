#Reverse a number using while loop
num=int(input("Please enter the number: "))
rev=0
while num>0:
    remainder=num%10
    rev=rev*10+remainder
    num=num//10
print("The reversed number is :",rev)