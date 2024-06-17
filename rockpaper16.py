#Write a Python program that determines the winner of a rock-paper-scissors game based on user input and displays the result using if-else statements.
choices = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

player1 = input("Player 1, enter your choice (rock, paper, or scissors): ")
player2 = input("Player 2, enter your choice (rock, paper, or scissors): ")

if player1 not in choices or player2 not in choices:
    print("Invalid")
elif player1 == player2:
    print("Tie")
elif choices[player1] == player2:
    print("Player 1 wins")
else:
    print("Player 2 wins")