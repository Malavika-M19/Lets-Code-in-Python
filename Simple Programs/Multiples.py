#Finding the multiples of a number using loop
num=int(input("Please enter the number to find multiples: "))
count=int(input("Please enter the number of multiples needed: "))
multiples=[]
for i in range (1,count+1):
    multiples.append(i*num)
print("The multiples are: ",multiples)