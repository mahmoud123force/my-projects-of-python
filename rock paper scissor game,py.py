print("welcome to rock paper scissors in python")
#This is a simple game of rock, paper, scissors.
import random
#i will use the random module to generate a random choice for the computer
# step 1 : i will make player 1 and computer scores
player1_score = 0
computer_score = 0
# step 2: i will create a list of rock, paper, scissors
choices = ["rock", "paper", "scissors"]
# step 3 : i will create a input for player 1 and player 2 to choose how many rounds they want to play
round = int(input("rounds do u want to play:"))
while True:
    # step 4: i will create a input for player 1 and player 2 to choose rock, paper, scissors
    player1_choice = input("player 1 choose rock,paper,scissors: ").lower()
    computer_choice = random.choice(choices)
    if player1_choice=="rock" and computer_choice=="scissors":
        print("player 1 wins")
        player1_score += 1
    elif player1_choice is "paper" and computer_choice=="rock":
        print("player 1 wins")
        player1_score += 1
    elif player1_choice=="scissors" and computer_choice=="paper":
        print("player 1 wins")
        player1_score += 1
    elif player1_choice == computer_choice:
        print("its a tie")
    elif player1_choice=="rock" and computer_choice=="paper":
        print("computer wins")
        computer_score += 1
    elif player1_choice=="paper" and computer_choice=="scissors":
        print("computer wins")
        computer_score += 1
    elif player1_choice=="scissors" and computer_choice=="rock":
        print("computer wins")
        computer_score += 1
    else:
        print("invalid choice, please choose rock, paper, or scissors")
    if player1_score == round or computer_score == round:
        break

    
# step 5: i will print the final scores
print("Final Scores:")
print("Player 1:", player1_score)
print("Computer:", computer_score)