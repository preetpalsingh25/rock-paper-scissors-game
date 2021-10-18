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

ch=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors or 9 to Exit.\n"))

comp=random.randint(0,2)
l=[rock,paper,scissors]

if ch==0:
  print(rock)
  print("Computer Chose")
  print(l[comp])

  if comp==0:
    print("Tie")
  elif comp==1:
    print("You Loose")
  else:
    print("You Win")

elif ch==1:
  print(paper)
  print("Computer Chose")
  print(l[comp])

  if comp==1:
    print("Tie")
  elif comp==2:
    print("You Loose")
  else:
    print("You Win")

elif ch==2:
  print(scissors)
  print("Computer Chose")
  print(l[comp])

  if comp==2:
    print("Tie")
  elif comp==0:
    print("You Loose")
  else:
    print("You Win")
