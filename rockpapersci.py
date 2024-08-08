import random

# Define choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

# Function to display the result
def display_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

# Initialize scores
user_score = 0
computer_score = 0

# Number of rounds
rounds = int(input("Enter the number of rounds you want to play: "))

for _ in range(rounds):
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1

    display_result(user_choice, computer_choice, result)
    print(f"Score -> You: {user_score}, Computer: {computer_score}")
    print("-" * 20)

# Display final scores
print("Final Scores:")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game.")
elif user_score < computer_score:
    print("Better luck next time. Computer won the game.")
else:
    print("The game is a tie!")
