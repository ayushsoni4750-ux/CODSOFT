"""
Task 3 - Rock, Paper, Scissors Game
CodSoft Python Programming Internship

Classic Rock-Paper-Scissors game against the computer,
with score tracking across multiple rounds.
"""

import random

CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice():
    return random.choice(CHOICES)


def get_winner(user, computer):
    if user == computer:
        return "tie"

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if beats[user] == computer:
        return "user"
    else:
        return "computer"


def main():
    print("===== ROCK - PAPER - SCISSORS =====")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").strip().lower()

        if user_choice not in CHOICES:
            print("Invalid choice. Please type rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congrats, you won overall!")
            elif user_score < computer_score:
                print("Computer won overall. Try again!")
            else:
                print("Overall it's a tie!")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
