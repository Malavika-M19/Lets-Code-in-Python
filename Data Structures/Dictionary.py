"""
Topic: Dictionary
Exercise
Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
"""

#Create a dictionary with keys 'name', 'age', and 'address'
person_info = {
    'name': 'John',
    'age': 25,
    'address': 'New York'
}
print("Dictionary:", person_info)

#Add a new key-value pair with key 'phone' and value '1234567890'
person_info['phone'] = '1234567890'

# Print the updated dictionary
print("Updated Dictionary:", person_info)
