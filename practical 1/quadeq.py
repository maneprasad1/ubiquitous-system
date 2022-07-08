import math


a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))
d = math.sqrt((b**2) - 4*a*c)

r1 = (-b + d)/2*a
r2 = (-b - d)/2*a

print("Value of root 1 is ", r1)
print("Value of root 2 is ", r2)
