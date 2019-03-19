import math

a = float(input("Enter value of A: "))
b = float(input("Enter value of B: "))
c = float(input("Enter value of C: "))

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area in Herone's Formula: ", area)
