print("Convert Kilometers to Miles and Miles to Kilometers")

a = float(input("Enter a value to convert "))

b = input("Do you want to convert from Kilometers to Miles, then type M else press K ")

conv_fac = 0.62137

kilometers = float(a/conv_fac)
miles = float(a*conv_fac)

if b == "M":
    kilometers = float(a/conv_fac)
    print ("Distance ", float(a),"in kilometers ", "in miles ", "is", float(miles))
    
else:
    miles = float(a*conv_fac)
    print ("Distance ", float(a),"in miles ", "in kilometers ", "is", float(kilometers))

input("Press enter to exit")
