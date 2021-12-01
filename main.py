# Student Number 000000

# Import random for the game
import random

# Scores start with 0
score = 0
computerscore = 0

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
    choice = input("Please select R, P or S: ")
    r = random.randint(1,3)
    if r == 1:
        computerchoice = "R"
    elif r == 2:
        computerchoice = "P"
    elif r == 3:
        computerchoice = "S"

    # Check who wins the round
    if choice == "R" and computerchoice == "R":
        print("Draw")
    elif choice == "R" and computerchoice == "P":
        print("Computer Wins")
        computerscore += 1
    elif choice == "R" and computerchoice == "S":
        print("You Win")
        score += 1
    elif choice == "P" and computerchoice == "R":
        print("You Win")
        score += 1
    elif choice == "P" and computerchoice == "P":
        print("Draw")
    elif choice == "P" and computerchoice == "S":
        print("Computer Wins")
        computerscore += 1
    elif choice == "S" and computerchoice == "R":
        print("Computer Wins")
        computerscore += 1
    elif choice == "S" and computerchoice == "P":
        print("You Win")
        score += 1
    elif choice == "S" and computerchoice == "S":
        print("Draw")

# Quit
quit()