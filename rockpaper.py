#scissors, paper and rock game
import random as r

options = ('scissors', 'paper', 'rock')
value = r.choice(options)
cont = True
ans = input("Enter yrs Choice out of scissors,paper,rock: ")
while cont:
  while ans not in options:
    print("Wrong Value! given")
    ans = input("Enter yrs Choice out of scissors,paper,rock: ")
  if ans == value:
    print("Game is Tie")
  elif ans == "scissors" and value == "paper":
    print("You Won!")

  elif ans == "paper" and value == "rock":
    print("You Won!")
  elif ans == "rock" and value == "scissors":
    print("You Won!")
  else:
    print("You Lost!")
  i = input("Do you want to play again? (y/n): ").lower()
  if i == "n":
    cont = False
  else:
    ans = input("Enter yrs Choice out of scissors,paper,rock: ")
