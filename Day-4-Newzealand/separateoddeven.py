# Printing separte odd and even no in an array in separate lines

n=int(input("Enter the no of elements in an array:"))
nums=[]
for i in range(0,n):
    ele=int(input())
    nums.append(ele)
odd=[]
even=[]
for i in nums:
    if i%2==0:
        even.append(i)       
    else:
        odd.append(i)
print("Odd numbers are:",odd)
print("Even numbers are:",even)

