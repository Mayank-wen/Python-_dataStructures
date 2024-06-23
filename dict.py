d1 = {
    "name": "shruti",
    "age" : 21,
    "year" : 2002, 
    "year": 2003
}   # duplicates not allowed duplicates overwrite the data
print(d1)
print(d1["name"])
print(len(d1))
d2 = {
    "name": "shruti",
    "age" : 21,
    "year" : 2002, 
    "food": ["apple","orange"]
}
print(d2)
d3 = dict(name = "shruti", age = 21, country = "India")
print(d3)# constructor
x = d2["food"]
print(x)# accessing the key 'model'
y=d2.get("year")
print(y)
X = d2.keys()
print(X)# returns all keys of dict
#d2["COLOR"] = "RED"
print(d2)
Y=d2.items()
print(Y)
if "year" in d2:
   print("yes , 'year' is one the if the keys in the d1")
d2.update({"year" : 2020})# updates  the item if the item is not there then it will add it
print(d2)
#d2.pop("COLOR")
print(d2)# removes the item
d2.popitem()# removes the last inserted item
print(d2)
#del d2["COLOR"]# removes the key name with item
print(d2)
for x in d2: # loop
   print(x)
for x in d2:
    print(d2[x])   # prints values one by one
for x in d2.values():
    print(x)   # returns value
for x,y in d2.items():
    print(x,y)      
    d3= d2.copy()
    print(d3) 
    # nested dict
# Define a dictionary to store family members' information
fam = {
    "1stborn": {
        "name": "swati",
        "year": 1999
    },
    "2ndborn": {
        "name": "shruti",
        "year": "2002"
    }
}

# Print the family members' information
print(fam)

# Define a dictionary for the 1st born family member
stborn = {
    "name": "swati",
    "year": 1999
}

# Define a dictionary for the 2nd born family member
ndborn = {
    "name": "shruti",
    "year": "2002"
}

# Define a dictionary to store the family members' dictionaries
fam = {
    "stborn": stborn,
    "ndborn": ndborn
}#FAM IS reinitialized

# Print the family members' information
print(fam)

# Access and print the name of the 2nd born family member
print(fam["ndborn"]["name"])  # accessing nested dict

# Create a tuple of keys
s = ('k1', 'k2', 'k3')

# Initialize a variable to store the default value for the dictionary
m = 0

# Create a dictionary using the fromkeys() method, with the specified keys and default value
d5 = dict.fromkeys(s, m)

# Print the created dictionary
print(d5)