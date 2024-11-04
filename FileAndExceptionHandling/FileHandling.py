"""
Write a Python program to read a file and display its contents
"""

file1=open("EmployeeDetails.txt",'r')
print(file1.read())

"""
Write a Python program to copy the contents of one file to another file
"""
#Reading the contents from first file
with open ("EmployeeDetails.txt",'r') as firstFile:
    data=firstFile.read()

#Creating second file and writing this contents
with open("NewEmployeeDetails.txt",'w') as secondFile:
    secondFile.write(data)

#Read contents of second file
secondFile=open("NewEmployeeDetails.txt",'r')
print(secondFile.read())


"""
Write a Python program to read the content of a file and count the total number of words in that file.
"""
file=open("EmployeeDetails.txt",'r')
contents=file.read()
words=contents.split()
wordCount=len(words)
print(f"Total number of words in this file is {wordCount}")

