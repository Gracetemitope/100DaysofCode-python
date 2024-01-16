print(r"""\                /\      /\
                                               ||______||
                                               || ^  ^ ||
                                               \| |  | |/
                                                |______|
              __                                |  __  |
             /  \       ________________________|_/  \_|__
            / ^^ \     /=========================/ ^^ \===|
           /  []  \   /=========================/  []  \==|
          /________\ /=========================/________\=|
       *  |        |/==========================|        |=|
      *** | ^^  ^^ |---------------------------| ^^  ^^ |--
     *****| []  [] |           _____           | []  [] | |
    *******        |          /_____\          |      * | |
   *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| |
  ***********]  [] |  []  []  |  |  |  []  []  | ===***** |
 *************     |         @|__|__|@         |/ |*******|
***************   ***********--=====--**********| *********
***************___*********** |=====| **********|***********
 *************     ********* /=======\ ******** | *********""")

print("Welcome to Treasure Island.\nYour mission is to find the treasure")

# Choose a direction
direction = input("Please choose a direction. Left or Right?\n")

# swim_wait = input("Do you want to swim or wait?/n")
# door = input("Which door do you want to go? Read, Blue, Yellow ")
if str(direction).lower() == "left":
    swim_wait = input("Do you want to swim or wait?\n")
    if str(swim_wait).lower() == "wait":
        door = input("Which door do you want to go? Red, Blue, Yellow ")
        if str(door).lower() == "Blue":
            print("You have been eaten by beasts. Game Over!!!")
        elif str(door) == "Red":
            print("You have been burned by fire. Game over!!!")
        elif str(door) == "Yellow":
            print("What a Champ!! You won the game!")
        else:
            print("Must be tough being a loser! Boy bye!!")


    else:
        print("You have been attacked by trout. Game overrr!!!")
    
else:
    print("oopss..You have fallen into a hole. Game over!!!")
