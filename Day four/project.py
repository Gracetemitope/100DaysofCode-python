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


# player_choice = random.randint(0, 2)
computer_choice = random.randint(0, 2)
print(computer_choice)

player_choice = input("Please select a weapon. 0 for rock, 1 for Paper and 2 for Scissor ")
player_choice = int(player_choice)
print(player_choice)
print(computer_choice)

if player_choice == 0 and computer_choice == 1:
    print(f"Computer chose{paper}\nand you have chosen {rock}. Congratulations, you have won")
elif player_choice == 1 and computer_choice == 2:
    print(f"Computer chose{scissor}\nand you have chosen {paper}. oops! You lost and computer won!")
elif player_choice == 2 and computer_choice == 0:
        print(f"Computer chose{rock}\nand you have chosen {scissor}. oops! You lost and computer won!")
elif player_choice == computer_choice:
     print("That is smart! I give it to you!")
else:
    print("Today is not your day")
