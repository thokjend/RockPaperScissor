import random

player_score = 0
computer_score = 0

def calculate_computer_choice():
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return choices[random.randint(1, 3)]

def player_choice():
    print("\nPlease choose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player_input = int(input("Enter choice (1-3): "))
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return choices.get(player_input, "Invalid choice")

def determine_winner(player, computer, player_score, computer_score):
    if player == computer:
        return "It's a Draw!", player_score, computer_score
    outcomes = {
        ("Rock", "Scissors"): "You win!",
        ("Paper", "Rock"): "You win!",
        ("Scissors", "Paper"): "You win!",
    }
    result = outcomes.get((player, computer), "You lose!")

    if result == "You win!":
        player_score += 1
    elif result == "You lose!":
        computer_score += 1
    return result, player_score, computer_score

def game():
    global player_score, computer_score
    print("***** Welcome to Rock, Paper, Scissors! *****")
    
    while True:
        print("\n***************************************")
        print("Starting a new round...")
        player = player_choice()
        
        if player == "Invalid choice":
            print("\nInvalid choice. Please try again with a number between 1 and 3.")
            continue

        computer = calculate_computer_choice()
        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")

        result, player_score, computer_score = determine_winner(player, computer, player_score, computer_score)
        print(f"\nResult: {result}")
        print("***************************************")
        print(f"Scores: Player: {player_score} | Computer: {computer_score}")
        print("***************************************")
        
        play_again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThank you for playing! Final Scores:")
            print(f"Player: {player_score} | Computer: {computer_score}")
            break

game()
