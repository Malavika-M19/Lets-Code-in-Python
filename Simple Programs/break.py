"""
Write a program to print the inputted value as it is and break the loop if the value is 'done'.
Example run of the program
:hello there
hello there
:finished
finished
:done
Done
"""
while True:
    # Get input from the user
    word = input("Enter a word: ")

    # Check if the input is 'done'
    if word.lower() == 'done':
        print("Done")
        break

    # Print the input value
    print(word)
