# Student Number 000000

# Import random for the game
import random

# Scores start with 0
score = 0
computerscore = 0
round = 1

while True:
    # Check that the game is not over
    if score == 3:
        print("!!!! YOU WIN THE GAME !!!!!")
        break
    elif computerscore == 3:
        print("!!! YOU LOSE THE GAME!!!!!")
        break
    else:
        print(" # # # Your Score is", score, " | Computer's Score is ", computerscore, " # # #")

    # Play the game
    print("ROUND:", round)
    round += 1

    # User choice
    choice = input("Please select R, P or S: ")
    choice = choice.upper()

    # Computer's Choice
    r = random.randint(1,3)
    if r == 1:
        computerchoice = "R"
    elif r == 2:
        computerchoice = "P"
    elif r == 3:
        computerchoice = "S"

    # Check who wins the round
    if choice == "R" and computerchoice == "R":
        print("Computer picked R")
        print("Draw")
    elif choice == "R" and computerchoice == "P":
        print("Computer picked P")
        print("Computer Wins")
        computerscore += 1
    elif choice == "R" and computerchoice == "S":
        print("Computer picked S")
        print("You Win")
        score += 1
    elif choice == "P" and computerchoice == "R":
        print("Computer picked R")
        print("You Win")
        score += 1
    elif choice == "P" and computerchoice == "P":
        print("Computer picked P")
        print("Draw")
    elif choice == "P" and computerchoice == "S":
        print("Computer picked S")
        print("Computer Wins")
        computerscore += 1
    elif choice == "S" and computerchoice == "R":
        print("Computer picked R")
        print("Computer Wins")
        computerscore += 1
    elif choice == "S" and computerchoice == "P":
        print("Computer picked P")
        print("You Win")
        score += 1
    elif choice == "S" and computerchoice == "S":
        print("Computer picked S")
        print("Draw")

# Quit
quit()