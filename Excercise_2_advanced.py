import math

num = int(input("Enter a number :"))
check = int(input("Enter a number to divide : "))

result = num%check

if result == 0 :
    print("Evenly divisible by given number")
else:
    print("Not divisible by given number")