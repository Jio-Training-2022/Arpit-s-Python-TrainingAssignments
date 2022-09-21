# THROUGH single loop LOOPS
n=int(input("Enter the no of elements in an array:"))
A=[]
for i in range(0,n):
    ele=int(input())
    A.append(ele)

largest=0
secondlargest=0
for i in A: 
    if i > largest:
        secondlargest = largest
        largest=i
    elif i > secondlargest and i!=largest:
        secondlargest=i
    else:
        pass

print("Second largest element is: ",secondlargest)

""" # USING TWO LOOPS
n=int(input("Enter the no of elements in an array:"))
A=[]
for i in range(0,n):
    ele=int(input())
    A.append(ele)

largest=0
for i in A:
     if largest<i:
         largest=i
secondlargest=0        
for j in A:
     if (j<largest) & (j>secondlargest):
         secondlargest=j
     else:
         pass
print ("Second largest element is: ",secondlargest) """
