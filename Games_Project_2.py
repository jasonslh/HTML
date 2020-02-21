import time

yes_no = ["yes", "no",]
directions = ["left", "right",]
response = ''

def third_choice():
    response_three = input('You come to the door, the flashing green keypad catches your attention. A question appears: "What always ends everything?" Please type in your answer.')
    time.sleep(1)

    if response_three == "g":
        print ("You hear a click, the keypad flashes eratically and the door swings open, the answer was correct and you have now been granted access to the final floor, the vault is close.")
        time.sleep(1)
        print("---------------------------------------------")
        time.sleep(1)
        print('Next function choice here - next section of the game goes here.')
    else:
        print ("The answer is incorrect.")
        time.sleep(1)
        print ("Please try again.")
        time.sleep(1)
        print("---------------------------------------------")
        third_choice()

def second_choice():
    attack_guards = "1"
    hackerman_distraction = "2"
    print ("With great haste, you take cover behind some of the clutter. Taking a quick peek they appear to be quite formidable if approached head on, armed with walky talkies to call for back-up and batons. Your gut tells you a distraction could be what is needed to deal with them.")
    time.sleep(1)
    print("(1) Do you attack the guards?")
    time.sleep(1)
    print("(2) Do you call upon Hackerman to cause a distraction?")
    #Possibly include the code for Hackerman number of uses
    #If this is included maybe include a code to use an item on the player to use as a distraction?
    #print("(3) Do you throw a tool across the room to cause a distraction?")
    time.sleep(1)

    response_two = input("1 or 2?") #if we add the code to use an item, add "or 3?" in the brackets.
    if response_two == "1":
        time.sleep(1)
        print("Going against your gut instinct, you decide to pick a fight with the 2 guards, they appear dimwitted however they prove to be compitent in a scrap and with there being 2 of them they easily overpower you and subdue you.")
        time.sleep(1)
        print("You have been captured.")
        time.sleep(1)
        print("Game over.")
        time.sleep(1)
        print("You will now be asked to choose again.")
        time.sleep(1)
        print("---------------------------------------------")
        second_choice()
    elif response_two == "2":
        print("Your faithful companion Hackerman received your cry for help and through sheer technical skill he was successfully able hack into the walky talkies and drain the batteries.")
        time.sleep(1)
        print("The guards being notified by the beepeing of their walky talkies are aware that the batteries are low. They proceed to leave the room in search of fresh batteries.")
        time.sleep(1)
        print("The coast is clear, there is only the final door blocking your way to the final floor.")
        time.sleep(1)
        third_choice()
    #else response_two == "3":
        #print("Which tool do you wish to use?")
        #then include the code for the inventory list
        #third_choice()


def first_choice():
    print("After successfully evading the guards and security systems on Floor 2, you make your way down to the 1st floor.")
    time.sleep(1)
    print("The layout of this floor appears to be very simple, as there is only one way to go. Forward.")
    time.sleep(1)
    print("You begin to move down the corridor gingerly, being cautious to not create too much noise, you encounter a split in your path, a corridor to the left and one to the right.")
    time.sleep(1)
    print("(1) Do you go left")
    time.sleep(1)
    print("(2) Do you go right?")
    response = input("1 or 2?")
    time.sleep(1)
    
    if response == "1": 
        print("You creep with the agility of a cat down the corridor. An intimidating steel door blocks your path, conviniently this door is unlocked. You muster the courage to enter.")
        time.sleep(1)
        print ("You enter into a huge room, filled with clutter and trash, two gormless guards block the only other door in the room.")
        time.sleep(1)
        second_choice()
    elif response == "2":
        print("You follow the other corridor and encounter a small wooden door with a rusty old door knob, a quick wiggle and shake of the handle, the door remains shut.")
        time.sleep(1)
        print("Do you:")
        time.sleep(1)
        print("(1) Do you want to kick the door open?")
        time.sleep(1)
        print("(2) Do you decide not to risk it and go back?")
        time.sleep(1)
        response = input("1 or 2?")
        if response == "1":
            print("You use all your strength to force the door open, after a quick struggle the door swings open, the alarm rings, alerting the entire building to your prescence")
            time.sleep(1)
            print("Your recklessness has jeprodised your adventure.")
            time.sleep(1)
            print("Game over.")
            time.sleep(1)
            print("---------------------------------------------")
            time.sleep(1)
            first_choice()
        elif response == "2":
            print ("You decide to not risk it, as you suspect it could perhaps be a trap. You move back and decide whether to go left or right again.")
            time.sleep(1)
            first_choice()
        time.sleep(1)
        print("---------------------------------------------")
        time.sleep(1)
        first_choice()
    else:
        
        print("I didn't understand that.")
        time.sleep(1)
        print('Please type in either "1" or "2"')
        time.sleep(1)
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
#     choice = int(input('Do you want to: [1] call hackerman to create a distraction? [2] Use an item to distract the guards yourself? or [3] do you want to pick a fight with the guards?'))
#     if choice == 1:
#         print("Your faithful companion Hackerman received your cry for help and through sheer technical skill he was successfully able hack into the walky talkies and drain the batteries.")
#     elif choice == 2:
#         print('You have decided to cause a distraction yourself.')
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

