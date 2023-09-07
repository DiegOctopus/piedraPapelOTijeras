rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       ____)
      (____)
---.__(_________)
'''

#Write your code below this line 👇
print("Welcome to rock paper scissors game\nplay vs artificial intelligence")
player1 = input('Choose "r" rock, "p" paper or "s" scissors : ')

if player1 == "r":
  player1 = 1
  print(rock)
elif player1 == "p":
  player1 = 2
  print(paper)
else:
  player1 = 3
  print(scissors)

import random
player2 = random.randint(1,3)
if player2 == 1:
  print(rock)
elif player2 == 2:
  print(paper)
else:
  print(scissors)

print("______________________")
if player1 == player2:
  print("tied game, try again !!")
elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
  print("You win !!!")
else:
  print("You lost, try again !!")
