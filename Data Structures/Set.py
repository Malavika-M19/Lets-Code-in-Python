"""
Topic: Set
Exercise
Q1.Create a set with values 1, 2, 3, 4, and 5.
Q2. Add the value 6 to the set created in Q1.
Q3. Remove the value 3 from the set created in Q1.
"""
#Create a set with values 1, 2, 3, 4, and 5
setA = {1, 2, 3, 4, 5}
print("Original set:", setA)

#Add the value 6 to the set
setA.add(6)
print("Set after adding 6:", setA)

# Q3: Remove the value 3 from the set
setA.discard(3)
print("Set after removing 3:", setA)
