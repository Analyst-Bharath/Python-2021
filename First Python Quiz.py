print ("Hello")
       
print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
print(playing)

if playing.lower()!= "yes":
    quit()

print ("Okay! Let's play :-)")
score=0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    print('Try again!')

answer = input("What is GPU? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score +=1
    
else:
    print("Incorrect!")
    print('Try again!')

answer = input("What is AI ")
if answer.lower() == "artificial intelligence":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
    print('Try again!')

answer = input("What is RAM ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print('Try again!')

print("You got "  +str(score)+ " Questions Correct!")
print("You got "  +str(score/4)*100)+ " %.")
    
