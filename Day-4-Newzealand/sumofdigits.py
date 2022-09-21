# Sum of digits in a number

n=int(input("Enter a number whose sum of digits you'd like to find:\n"))


def sum_of_digits(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10
    return sum
print("Sum of digits:",sum_of_digits(n))