#import random
#rand (range)--
#Random_Number = random.randrange(-1, 11)
#print (r)

#import random
#rand (int)--
#Random_Number= random.randint(-1, 11)
#print (r)

#Convert string to Integer
#int("x")
#while user_guess != random_number:
#continue runs the loop again
#break breaks the loop
 #else:
        #if User_guess > Random_Number:
            #print("You were above the number!")
        #else:
            #print("You were below the number!")

import random
Top_Of_Range = input("Type a Number: ")

if Top_Of_Range.isdigit():
    Top_Of_Range = int(Top_Of_Range)

    if Top_Of_Range <= 0:
        print("Please insert a value greater than 0.")
        quit()
else:
    print("Please insert a value.")
    quit()
        
Random_Number = random.randint(0,Top_Of_Range)
guessess = 0

while True:
    guessess +=1
    User_guess = input("Make a Guess: ")
    if User_guess.isdigit():
        User_guess = int(User_guess)

    else:
        print("Please insert a value.")
        continue

    if User_guess == Random_Number:
        print("Your answer is right")
        break

    elif User_guess > Random_Number:
        print("You were above the number!")
    else:
        print("You were below the number!")
            
print ("You got it in", guessess, "guessess")
