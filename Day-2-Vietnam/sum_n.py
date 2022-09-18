a=int(input("Enter n:\n"))
sum=0
def sum_of_n(a):
    sum=0
    for i in range(1,a+1):
        sum=sum+i
    return sum
# By 'For' loop
""" 
for i in range(a+1):
    sum=sum+i
print(sum) """


# By 'While' loop

""" i=0
while (i<=a):
    sum=sum+i
    i=i+1
print(sum) """


 # by function
print("Sum:",sum_of_n(a))
