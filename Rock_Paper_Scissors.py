# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer = random.randint(0,2)

choice = [Rock, Paper, Scissors]
print(choice[player])
print("Computer chose:")
print(choice[computer])

if player==0 and computer==2:
    print("You win")
elif player==1 and computer==0:
    print("You win")
elif player==2 and computer==1:
    print("You win")
elif player==computer:
    print("Draw")
else:
    print("you lose")
