print("Caculate the area of a triangle: ")

a = float(input("Length of side a: "))
b = float(input("Length of side b: "))
c = float(input("Length of side c: "))

print ("Perimeter is s ")
       
s = (a + b + c)/2

print (s)

area = ((s*(s- a)*(s-b)*(s-c)))**0.5

print (" The perimeter of a traingle with sides ", a, b, c, "is ", s)
print (" The area of traingle with sides ", a, b, c, area, "sq.m")
input("Press enter to exit")
