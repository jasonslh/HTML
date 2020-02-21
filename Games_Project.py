import time

#Start_of_level 
#maybe if the player fails, they go back to the start of the level rather than the whole game.

yes_no = ["yes", "no",]
directions = ["left", "right",]
response = ''

def third_choice():
    response_three = input('You come to the door, the flashing green keypad catches your attention. A question appears: "What always ends everything?" Please type in your answer.')
    time.sleep(1)

    if response_three == "g":
        print ("You hear a click, the keypad flashes eratically and the door swings open, the answer was correct and you have now been granted access to the final floor, the vault is close.")
        time.sleep(1)
        print('Next function choice here')
    else:
        print ("The answer is incorrect.")
        time.sleep(1)
        print ("Please try again.")
        third_choice()

def second_choice():
    attack_guards = "1"
    hackerman_distraction = "2"
    #print ("Looking at the state of them, you imagine that they could easily be dealt with.")
    print ("With great haste, you take cover behind some of the clutter. Taking a quick peek they appear to be quite formidable if approached head on, armed with walky talkies to call for back-up and batons. Your gut tells you a distraction could be what is needed to deal with them.")
    #Change this
    time.sleep(1)
    print("(1) Do you attack the guards?")
    time.sleep(1)
    print("(2) Do you call upon Hackermann to cause a distraction on Floor 2?")
    time.sleep(1)
    #Create a function that takes you back to the start of the level if the player choses "1"

    response_two = input("1 or 2?")
    if response_two == "1":
        time.sleep(1)
        print("Going against your gut instinct, you decide to pick a fight with the 2 guards, they appear dimwitted however they prove to be compitent in a scrap and with there being 2 of them they easily overpower you and subdue you.")
        time.sleep(1)
        print("You have been captured.")
        time.sleep(1)
        print("Game over.")
        time.sleep(1)
        print("The game will now restart to the start of the Floor. Choose wisely in future decisions.")
        print("---------------------------------------------")
        first_choice()
    elif response_two == "2":
        print("Your faithful companion Hackerman received your cry for help and through sheer technical skill he was successfully able to contact them through the walky talkies, and ask for back-up on Floor 2. Temporarily removing them from the room.)
        time.sleep(1)
        print("The coast is clear, there is only the final door blocking your way to the final floor.")
        time.sleep(1)
        third_choice()


def first_choice():
    print("After successfully evading the guards and security systems on Floor 2, you make your way down to the 1st floor.")
    time.sleep(1)
    print("The layout of this floor appears to be very simple, as there is only one way to go. Forward.")
    time.sleep(1)
    response = input("You begin to move down the corridor gingerly, being cautious to not create too much noise, you encounter a split in your path, a corridor to the left and one to the right. Do you go left or right?")
    time.sleep(1)

    #def response_one

    if response == "left": 
        print("You creep with the agility of a cat down the corridor. An intimidating steel door blocks your path, conviniently this door is unlocked. You muster the courage to enter.")
        time.sleep(1)
        print ("You enter into a huge room, filled with clutter and trash, two gormless guards block the only other door in the room.")
        time.sleep(1)
        second_choice()
    elif response == "right":
        print("You follow the other corridor and encounter a small wooden door with a rusty old door knob, a quick wiggle and shake of the handle, the door remains shut.")
        #Do you try and force the door open or do you go back?
        #("the door swings open. A security room. The")
        time.sleep(1)
        print("Pity.")
        time.sleep(1)
        print("---------------------------------------------")
        time.sleep(1)
        first_choice()
    #Create a function that takes you back to the start of the level if the player chooses to go "right"
    else:
        
        print("I didn't understand that.")
        time.sleep(1)
        print('Please type in either "left" or "right"')
        print("---------------------------------------------")
        first_choice()

first_choice()

#Floor 3

#Reorganise the list so it's a clearer distinction - easier to read. Possible colours. "\n" = new line
#Also create a function to reset the question incase player types in incorrectly
#Lift - dead end option.


#Floor 2
#

#Floor 1
#Make a clearer distinction between "Left" + "Right", previous questions had A, B + C
#Baited in and punished for listening to the sugestions.
#Make it clearer if you fail. 2nd floor alarm, ends the game yet there's a distraction on 2nd floor that doesn't end the game. Doesn't make sense
#
#Trial and error, possibly have multiple ways to progress instead of a singular route. Give more player choice
#Has a lot of charm considering 
#If the player chooses a game over, need to create a game over function.
#If the answer is correct, it needs to carry on.





# def response_three():
#     a_response_three = input('You come to the door, the flashing green keypad catches your attention. A question appears: "What always ends everything?" What is the answer?')
#     a_response_three()

# def a_response_three():
#     time.sleep(2)
#     if a_response_three == "g":
#         print("You hear a click, the keypad flashes eratically and the door swings open, the answer was correct and you have now been granted access to the final floor, the vault is close.")
#         time.sleep(2)
#     else:
#         print("The answer is incorrect.")
#         time.sleep(2)
#         print('Please enter another answer to progress')
#         response_three()
# a_response_three()





#def lift_option():
#     time.sleep(2)
#     print("You go towards the lift and enter it.")
#     time.sleep(2)
#     print("Once you are inside you see that the buttons for the lower floors are not illuminated.")
#     print("You are unable to use the lift.")
#     time.sleep(2)
#     print("(Please enter B when asked to choose again. This will take you to the door option.)")
#     doorlift()
# # third floor option
# def doorlift():
#     choice2 = input("A or B:")
#     if choice2 == "A" or choice2 == "a":
#         lift_option()
#     elif choice2 == "B" or choice2 == "b":
#         time.sleep(2)
#         print("You go towards the door and open it. There is a staircase going downwards. You go down the stairs to Floor 2.")


# def event():
#     choice = int(input('example event: Do you want to [1] call hackermann to create a distraction on the previous floor?[2] use a item to distract the guards yourself? or [3] do you want to pick a fight with the guards?'))
#     if choice == 1:
#         print('Your faithful companion Hackermann was successfully able to create a distraction on the previous floor, drawing the attention of the moronic guards away from the room. The room is empty and there is nothing blocking your path.')
#     elif choice == 2:
#         print('item select goes here')
#         eventitemcheck()
#         item_used = int(input('which item are you going to use?([1], [2], [3], ect) '))
#         if item_used == 1:
#             print('you used item {} to do _____________ this and this happened # this is where you enter what happens in your event'.format(inventory[0]))
#             print('item {} removed from inventory _________ something happened and the item was used up'.format(inventory[0]))
#             inventory.pop(0)
#             eventitemcheck()
#         elif item_used == 2:
#             print('you used item {} to do _____________ this and this happened # this is where you enter what happens in your event'.format(inventory[1]))
#             print('item {} removed from inventory _________ something happened and the item was used up'.format(inventory[1]))
#             inventory.pop(1)
#             eventitemcheck()
#         elif item_used == 3:
#             print('you used item {} to do _____________ this and this happened # this is where you enter what happens in your event'.format(inventory[2]))
#             print('item {} removed from inventory _________ something happened and the item was used up'.format(inventory[2]))
#             inventory.pop(2)
#             eventitemcheck()
#     else:
#         print('need to implement a way to restart the event that would go here')

