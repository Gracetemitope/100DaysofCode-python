import random

print("Welcome to rock paper and Scissor game!\n")
paper = r""" _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              """

scissor = r"""_       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\."""

rock = r"""               _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\""""

print(rock)
print(scissor)
print(paper)

player_choice = random.randint(0, 2)
computer_choice = random.randint(0, 2)
print(player_choice)
print(computer_choice)

choosing_a_weapon = input("Please select a weapon. 0 for rock, 1 for Paper and 2 for Scissor ")

if player_choice == 0 & computer_choice == 1:
    print(f"Computer chose{paper}\nand you have chosen {rock}. Congratulations, you have won")
else:
    print("Today is not your day")
