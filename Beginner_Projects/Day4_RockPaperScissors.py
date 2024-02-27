import random

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
       __________)
      (____)
---.__(___)
'''
print("Let's play Rock Paper Scissors!")
player_choice = int(input("What do you choose:\n\t1-Rock\n\t2-Paper\n\t3-Scissors\n>>"))
computer_choice = random.randint(1,3)

if player_choice == 1:
    print(rock)
elif player_choice == 2:
    print(paper)
elif player_choice == 3:
    print(scissors)
else:
    print("Invalid choice!")

print("The computer chose:")

if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
    print(paper)
elif computer_choice == 3:
    print(scissors)

if computer_choice == 1 and player_choice == 2:
    print("You win (paper beats rock)")
elif computer_choice == 1 and player_choice == 3:
    print("You lose! (rock beats paper)")
elif computer_choice == 2 and player_choice == 1:
    print("You lose! (paper beats rock)")
elif computer_choice == 2 and player_choice == 3:
    print("You win! (scissors beats paper)")
elif computer_choice == 3 and player_choice == 1:
    print("You win! (rock beats scissors)")
elif computer_choice == 3 and player_choice == 2:
    print("You lose! (scissors beats paper)")
else:
    print("It's a draw, try again!")