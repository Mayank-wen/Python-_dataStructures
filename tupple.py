t1=("shruti" ,"swati",1)  # Define a tuple t1 with three elements: "shruti", "swati", and 1
print(t1)  # Print the tuple t1
print(len(t1))  # Print the length of the tuple t1

t2=("shruti",)  # Define a tuple t2 with one element: "shruti"
print(t2)  # Print the tuple t2

t3 =tuple(("shruti","swati"))  # Define a tuple t3 with two elements: "shruti" and "swati"
print(t3)  # Print the tuple t3

# Conversion of tuple into list
y=list(t3)  # Convert the tuple t3 into a list y
y.append("riddhi")  # Append "riddhi" to the list y
t3=tuple(y)  # Convert the list y back into a tuple t3
print(t3)  # Print the updated tuple t3

(s,S,r)=t3  # Unpack the tuple t3 into three variables: s, S, and r
print(s)  # Print the value of s
print(S)  # Print the value of S
print(r)  # Print the value of r

(s,*r)=t3  # Unpack the tuple t3 into two variables: s and r (using the * operator)
print(s)  # Print the value of s
print(r)  # Print the value of r

t4=("sh","ru","ti","ri","dd","hi")  # Define a tuple t4 with six elements
i=0  # Initialize a counter variable i
while i< len(t4):  # Loop until i is less than the length of t4
    print(t4[i])  # Print the element at index i in t4
    i=i+1  # Increment i by 1

t5 =t4*2  # Create a new tuple t5 by duplicating t4
print(t5)  # Print the tuple t5

x= t5.count("sh")  # Count the occurrences of "sh" in t5
print(x)  # Print the count

y=t5.index("ri")  # Find the index of "ri" in t5
print(y)  # Print the index