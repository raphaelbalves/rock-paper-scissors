import random

def rock():
  print("""
    _______
  ---'   ____)
      (_____)
      (_____)
      (____)
  ---.__(___)
  """)

def paper():
  print("""
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  """)

def scissors():
  print("""
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)

def win():
  options[you]()
  print("Computer chose:")
  options[computer]()
  print("You win")

def lose():
  options[you]()
  print("Computer chose:")
  options[computer]()
  print("You lose")

def draw():
  options[you]()
  print("Computer chose:")
  options[computer]()
  print("It's a draw")
  
  
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer = random.randint(0,2)

options = [rock, paper, scissors]

if you == 0 and computer == 0:
  draw()
elif you == 0 and computer == 1:
  lose()
elif you == 0 and computer == 2:
  win()
elif you == 1 and computer == 0:
  win()
elif you == 1 and computer == 1:
  draw()
elif you == 1 and computer == 2:
  lose()
elif you == 2 and computer == 0:
  lose()
elif you == 2 and computer == 1:
  win()
elif you == 2 and computer == 2:
  draw()
else:
  print("Bad option.")







