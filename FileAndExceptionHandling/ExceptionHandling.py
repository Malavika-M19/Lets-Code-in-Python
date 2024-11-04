"""
Write a Python program that prompts the user to input a string and converts it to an integer.
Use try-except blocks to handle any exceptions that might occur
"""
userInput=input("Enter a string: ")
try:
    userInput=int(userInput)
except Exception as e:
    print("Erorr: ",e)
else:
    print("The input given by user is converted to integer and the value is: ",userInput)


"""
Write a Python program that prompts the user to input a list of integers 
and raises an exception if any of the integers in the list are negative
"""
list1=input("Enter a list of integers: ")
try:
    numbersList=list1.split()
    numbers=[int(i) for i in numbersList]
    for i in numbers:
        if i<0:
            raise Exception
except:
    print("Error: The list contains negative numbers")
else:
    print("Thanks for the input.")


"""
Write a Python program that prompts the user to input a list of integers and computes the average of those integers. 
Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message indicating that 
the program has finished running.
"""
list1 = input("Enter the list of integers whose average is to be calculated: ")
try:
    numbersList = list1.split()
    numbers = [int(i) for i in numbersList]
    sum=sum(numbers)
    count=len(numbers)
    avg=sum/count
except ZeroDivisionError as e:
    print("Error: ",e)
except Exception as e:
    print("Error: ",e)
else:
    print("Average is: ",avg)
finally:
    print("Program finished successfully")


"""
Write a Python program that prompts the user to input a filename and writes a string to that file. 
Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.
"""
fileName=input("Please suggest a file name: ")
try:
    f1=open(fileName,'w')
    f1.write("You have created a file")
    f1.close()
    print("Welcome to file handling...!")
except Exception as e:
    print("Error occured ",e)
