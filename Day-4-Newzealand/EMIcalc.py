#LOAN EMI CALCULATOR
def EMI(p,r,n):
    return (p*r*((1+r)**n))/((1+r)**n-1)
    
p=float(input("Enter the princicpal amount:"))
R=float(input("Enter the rate of interest in % per annum:"))
r=R/12/100
N=float(input("Enter the no of years in whch you want to pay back:"))
n=N*12

print("Your monthly EMI is Rs. {}".format(EMI(p,r,n)))
