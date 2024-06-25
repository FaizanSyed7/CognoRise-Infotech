import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

def play_again():
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again in ['yes', 'no']:
            return again == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def rock_paper_scissors():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to Rock, Paper, Scissors Game!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit the game.")

    while True:
        print(f"\nRound {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"Scores: You - {user_score}, Computer - {computer_score}")

        if not play_again():
            break

        round_number += 1

    print("\nThank you for playing! Final scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Goodbye!")

if __name__ == "__main__":
    rock_paper_scissors()
