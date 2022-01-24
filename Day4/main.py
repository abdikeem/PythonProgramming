import random
from signal import pthread_kill

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

#Write your code below this line 👇

possible_actions = [rock, paper, scissors]
user_action = int(input(f"What do you choose? 'rock=0', 'paper=1', 'scissors=2': "))
print(f"You chose: \n{user_action}")
print(possible_actions[user_action])


computer_actions = random.randint(0, 2)
print(f"computer chose:")
print(possible_actions[computer_actions])

if computer_actions == 0 and user_action == 0:
    print('Its a tie')
elif computer_actions == 1 and user_action == 1:
    print('Its a tie')
elif computer_actions == 2 and user_action == 2:
    print('Its a tie')
# Rock computer_actions
elif computer_actions == 0 and user_action == 1:
    print('You won')
elif computer_actions == 0 and user_action == 2:
    print('You lost')
# Rock user_action
elif computer_actions == 1 and user_action == 0:
    print('You lost')
elif computer_actions == 2 and user_action == 0:
    print('You won')
# Paper computer_actions
elif computer_actions == 1 and user_action == 0:
    print('You lost')
elif computer_actions == 1 and user_action == 2:
    print('You won')
# Paper user_action
elif computer_actions == 0 and user_action == 1:
    print('You won')
elif computer_actions == 2 and user_action == 1:
    print('You lost')
# 2 computer_actions
elif computer_actions == 2 and user_action == 1:
    print('You lost')
elif computer_actions == 2 and user_action == 0:
    print('You won')
# 2 user_action
elif computer_actions == 1 and user_action == 2:
    print('You won')
elif computer_actions == 0 and user_action == 2:
    print('You lost')
# else:
#     print('You chose incorrect number, You lose')