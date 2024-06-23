# Sets are unordered collections of unique elements, similar to tuples but mutable
s1 = {"shruti", "swati", "riddhi"}
print(s1)  # Output: {'shruti', 'wati', 'riddhi'}

# Sets do not allow duplicate values
s2 = {"shruti", "swati", "riddhi", "shruti", "swati"}
print(s2)  # Output: {'shruti', 'riddhi', 'wati'}

# Sets can contain different data types
s3 = {True, 1}
print(s3)  # Output: {True, 1}

# Checking if an element is in a set
s4 = {1, 2, 4, 5, 6, 7}
print(3 in s4)  # Output: False

# Adding a new element to a set
s3.add("appy")
print(s3)  # Output: {True, 1, 'appy'}

# Updating a set with another set
s2.update(s4)
print(s2)  # Output: {'shruti', 'riddhi', 'wati', 1, 2, 4, 5, 6, 7}

# Updating a set with a list
l13 = ["lo", "ll", "oo"]
s3.update(l13)
print(s3)  # Output: {True, 1, 'appy', 'lo', 'll', 'oo'}

# Removing a specific element from a set
s2.discard("riddhi")
print(s2)  # Output: {'shruti', 'wati', 1, 2, 4, 5, 6, 7}

# Removing an arbitrary element from a set
x = s2.pop()
print(x)  # Output: one of the elements in s2
print(s2)

# Finding the union of two sets
s2.union(s3)
print(s2)  # Output: {'shruti', 'wati', 1, 2, 4, 5, 6, 7, True, 'appy', 'lo', 'll', 'oo'}

# Finding the intersection of two sets and updating the first set
s1.intersection_update(s2)
print(s1)  # Output: {'shruti', 'wati'}

# Finding the intersection of two sets
s6 = s1.intersection(s2)
print(s6)  # Output: {'shruti', 'wati'}

# Finding the symmetric difference of two sets and updating the first set
s1.symmetric_difference_update(s2)
print(s1)  # Output: {1, 2, 4, 5, 6, 7}

# Checking if two sets are disjoint
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)  # Output: False

# Finding the difference of two sets and updating the first set
s1.difference_update(s2)
print(s1)  # Output: set()

# Checking if a set is a subset of another set
s = {1, 2, 3, 4, 5}
m = {1, 2, 3, 4, 5, 6, 7, 8}
S = s.issubset(m)
print(S)  # Output: True