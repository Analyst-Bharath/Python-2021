#Complex
#Customizable

name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a narrow road, it has come to an end and you can go left or right. Which way would you like to go?: ")

if answer== "left":
    answer =  input("You come to a lake. You can swim across/walk around it. Choose - Walk or Swim: ")

    if answer == "swim":
        print("You swam across and drowned.")

    elif answer == "walk":
        print("Walked for many miles and dies out of exhaution. You lost the game!.")
    else:
         print("Not a valid option. You lose!.")
               
elif answer == "right":
    answer= input("You come across a bridge. Do you want to cross it or walk-back?. Type cross or back: ")

    if answer == "back":
        print("You go back to the main road end.")

    elif answer == "cross":
        answer= input("You crossed the bridge and and meet a stranger. Do you want to talk to them? Yes/No?: ")
    if answer == "yes":
        print("You talk and they give you a prize. You win the game!. Hurray!")
    elif answer == "no":
        print("You donot talk and lose the game. Booo!")
        
    else:
        print("Not a valid option. You Lose!.")

else:
    print("Not a valid option. You Lose!.")
print("Thank you for playing!")
