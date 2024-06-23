l1 = ["ret","ale"," ole,"]
l2 = ["ale"," ole,","ret" ,"ale","ole"]
l3 =  ["apple",3," ture"]
l4 = ["shruti","swati","cherry"]
print(l1[1:3])
if "apple" in l3:
    print("yes,'apple' is in the fruits list")# searching in list
l2[2]="blackcurrent"
print(l2)
l1[1:2]=["orange","melon"]# inserting in range from index 1 to 2
print(l1)
l1[1:2]=["water"]
print(l1)
l4.insert(1,'shruti') #insert at specific position
print(l4)
l2.append("nuts")# at the end
print(l2)
l5 = ["sh","ru","ti"]
l3.extend(l5)# add two list or tuple etc
print(l3)
t6 = ("ki","wi")
l3.extend(t6)
print(l3)
l3.remove(3)
print(l3)
l1.pop(1)
print(l1)
l1.pop()# removes last item of list(default)
print(l1)
del l1 # removes l1 out of existence
l2.clear # removes the items out of existence
print(l2)
for x in l3:# for loop
    print(x)# prints one item per line
for i in range(len(l3)):
    print(l3[i])   # prints items respective to their idex number 
[print(x)for x in l4]# for loop
l6 = [" shruti"," swati","sakshi","aashi","ran"]
nl6=[]
for x in l6:   # specified searching
   if "s" in x:
      nl6.append(x)
print(nl6)    
nl7=[x for x in l6 if "s" in x]#expression for item in iterable if condition == true
print(nl7)
nl8=[x for x in l6 if x != "shruti"]
print(nl8)
l7=[x for x in range(20) if x<7]
print(l7)
l8=[x if x !="shruti" else "love hate " for x in l6]
print(l8)
l9=["me","Shruti","aditi","shivangi"]
l9.sort()#  sort list according to alphabetical
print(l9)
l10 =[1,2,3,4,5,8,3,5,2,4]
l10.sort(reverse= True)
print(l10)
l11 = l9.copy()
print(l11)
l12 = l9+l10
print(l12) 
s = l2.index("ale")
print(s)

    