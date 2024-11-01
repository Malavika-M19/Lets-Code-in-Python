"""
len()
This function is used to find the number of items in a collection such as list, tuple, dictionary, string etc.
It returns an integer representing the length of the collection, which is called.
"""
L1=[1,2,3,4,5,10]
#find the number of items in L1
print("Number of items in this list is: ", len(L1))




"""
Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!"
"""
def greet(name):
    print(f'Hello, {name}!')
#function call
greet("Malavika")




"""
Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using 
the built-in max() function. Use a loop to iterate through the list and compare values.
"""
def find_maximum(numbers):
    # Initialize the maximum value with the first element of the list
    max_value = numbers[0]
    for i in numbers:
        # Compare each number with the current max_value
        if i > max_value:
            max_value = i

    return max_value

# function call:
numbers_list = [3, 5, 2, 19, 0]
maximum_value = find_maximum(numbers_list)
print("The maximum value is:", maximum_value)




"""
Difference between local and global variables in a Python function. 
Local Variables: They are declared within a function and their lifetime is restricted to the function
Global Variables: They are defined outside of any function and can be accessed anywhere in the code, including within functions. 
                  They remain in memory for the duration of the program
When a local variable and a global variable have the same name, Python will prioritize the local variable within its scope, 
effectively shadowing the global variable.
"""
sum=10 #global variable
a=5
b=3
print("Value of sum: ",sum)
def sumOfNum(x,y):
    sum=a+b
    print("Value of sum (inside function): ",sum)

sumOfNum(a,b)




"""
Create a function calculate_area(length, width=5) that calculates the area of a rectangle. 
If only the length is provided, the function should assume the width is 5. 
Show how the function behaves when called with and without the width argument
"""

def calculate_area(length,width=5):
    area = length*width
    return area
#Function call
areaABCD=calculate_area(10,4)
print("Area of ABCD with length 10 and width 4 is : ",areaABCD)
areaPQRS=calculate_area(3)
print("Area of PQRS with length 3 is : ",areaPQRS)
