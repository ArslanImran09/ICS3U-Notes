import math
a = float(input("Please enter the length of the first side of the triangle"))
b = float(input("Please enter the length of the second side of the triangle"))
c = float(input("Please enter the length of the third side of the triangle"))
s = float((a + b + c)/2)
print("The value of \"s\" is", s)
area = math.pow((s*(s-a)*(s-b)*(s-c)), 1/2)
print("The area of the triangle is", area,"meter squared")