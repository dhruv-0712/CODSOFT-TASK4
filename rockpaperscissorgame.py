import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    return choice.lower() == "yes"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rock beats scissors, scissors beat paper, and paper beats rock.")

    player_score = 0
    computer_score = 0

    while True:
        print("\nChoose one: rock, paper, or scissors")
        player_choice = input("Your choice: ").lower()

        while player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose again.")
            player_choice = input("Your choice: ").lower()

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print("Your choice:", player_choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print("Player score:", player_score)
        print("Computer score:", computer_score)

        if not play_again():
            break

play_game()