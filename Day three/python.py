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
direction = input("Please choose a direction. Left or Right?\n").lower()
# swim_wait = input("Do you want to swim or wait?/n")
# door = input("Which door do you want to go? Read, Blue, Yellow ")

if str(direction) == "Left":
    swim_wait = input("Do you want to swim or wait?\n").lower()
    if str(swim_wait) == "wait":
        door = input("Which door do you want to go? Red, Blue, Yellow ").lower()
        if str(door) == "Blue":
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
