import random

print("================================")
print(" ROCK - PAPER - SCISSORS GAME ")
print("================================")
print("Instructions:")
print("Choose Rock, Paper, or Scissors.")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour Choice:", user_choice.capitalize())
    print("Computer Choice:", computer_choice.capitalize())

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n===== FINAL SCORE =====")
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("Congratulations! You are the overall winner.")
elif computer_score > user_score:
    print("Computer is the overall winner.")
else:
    print("The game ended in a tie.")

print("Thank you for playing!")
