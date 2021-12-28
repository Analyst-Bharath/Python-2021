print("Solving quadratic equations")

#ax^2+bx+c = 0;  where a,b,c are real numbers and a=! 0

a = int(input("Enter first vlaue: "))
b = int(input("Enter second vlaue: "))
c = int(input("Enter third vlaue: "))

import cmath

d = (b**2) - (4*a*c)

solution_1 = (-b-cmath.sqrt(d))/(2*a)
solution_2 = (-b+cmath.sqrt(d))/(2*a)

print("The square root of the quadratic equation, where ", a, b, c, "where", d, "is", solution_1, ";" ,solution_2)
input("Type Q to exit")
