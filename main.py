import random

def calculate_computer_choice():
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    return choices[random.randint(1,3)]

def player_choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    player_input = int(input("Enter choice (1-3): "))
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return choices.get(player_input, "Invalid choice")

def determine_winner(player, computer):
    if player == computer:
        return "Draw!"
    outcomes = {
        ("Rock", "Scissors"): "You win!",
        ("Paper", "Rock"): "You win!",
        ("Scissors", "Paper"): "You win!",
    }
    return outcomes.get((player, computer), "You lose!")

def game():
    print("Rock Paper Scissors")
    player = player_choice()
    if player == "Invalid choice":
        print("Invalid choice. Please try again.")
        return

    computer = calculate_computer_choice()
    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    result = determine_winner(player, computer)
    print(result)

game()
