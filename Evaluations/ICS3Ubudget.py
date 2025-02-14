import math
import random
a = 200
b = 400
Food = round(random.uniform(a,b), 2)
c = 100
d = 200
Clothing = round(random.uniform(a,b), 2)
e = 100
f = 200
Entertainment = round(random.uniform(c,d), 2)
g = 1500
h = 2500
Rent = round(random.uniform(g,h), 2)
TotalCost = round((Food + Clothing + Entertainment + Rent), 2)
Percentage1 = round(((Food/TotalCost)*100), 2)
Percentage2 = round(((Clothing/TotalCost)*100), 2)
Percentage3 = round(((Entertainment/TotalCost)*100), 2)
Percentage4 = round(((Rent/TotalCost)*100), 2)
print("The total cost in a month would be $",TotalCost)
print("The cost of food per month makes up for $",Food,"and it makes up for",Percentage1,"% of the total cost")
print("The cost of clothing per month makes up for $",Clothing,"and it makes up for",Percentage2,"% of the total cost")
print("The cost of entertainment per month makes up for $",Entertainment,"and it makes up for",Percentage3,"% of the total cost")
print("The cost of monthly rent makes up for $",Rent,"and it makes up for",Percentage4,"% of the total cost")