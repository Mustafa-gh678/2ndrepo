import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', 'scissors', or 'quit' to exit.\n")

while True:
  player = input("Your choice: ").lower()

  if player == "quit":
    print(f"Final score: You {player_score}, Computer {computer_score}.")
    break

  if player not in choices:
    print("Invalid choice. Choose rock, paper, scissors, or quit.")
    continue

  computer = random.choice(choices)
  print(f"Computer chose {computer}.")

  if player == computer:
    print("Draw.")
  elif (
      (player == "rock" and computer == "scissors")
      or (player == "paper" and computer == "rock")
      or (player == "scissors" and computer == "paper")
  ):
    print("You win this round.")
    player_score += 1
  else:
    print("Computer wins this round.")
    computer_score += 1

  print(f"Score -> You: {player_score} | Computer: {computer_score}\n")
