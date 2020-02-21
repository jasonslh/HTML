#print(input("What is your name? > "))
import time

inventory = ['smokebomb', 'taser', 'infrared goggles']
codename = input('Enter your codename ')
local_items = ['hand drill', 'duffle bag', 'banana']
item_selected = 0
# This it for when the code checks the items you currently have

def eventitemcheck():
    print('Your current items are: ')
    for i in inventory:
        print(i)
    time.sleep(2)

# third floor option
def lift_option():
    time.sleep(2)
    print("You go towards the lift and enter it.")
    time.sleep(2)
    print("Once you are inside you see that the buttons for the lower floors are not illuminated.")
    print("You are unable to use the lift.")
    time.sleep(2)
    print("(Please enter B when asked to choose again. This will take you to the door option.)")
    doorlift()

# third floor option
def doorlift():
    choice2 = input("[1] or [2]:")
    if choice2 == "1" or choice2 == "[1]":
        lift_option()
    elif choice2 == "2" or choice2 == "[2]":
        time.sleep(2)
        print("You go towards the door and open it. There is a staircase going downwards. You go down the stairs to Floor 2.")

# REBECCA'S FLOOR

def third_floor():
    time.sleep(1)
    print("You are currently on Floor 3 of the bank.")
    time.sleep(2)
    print("This floor seems quiet however you still need to be alert.")
    time.sleep(2)
    print("You notice a security camera in the corner of the corridoor. What do you do?")
    time.sleep(2)
    print("[1] Text Hackerman to sort it out.")
    time.sleep(1)
    print("[2] Ignore it.")
    time.sleep(2)
    choice = input("[1] or [2]:")
    # NEED A VARIABLE NAME FOR INPUT E.G CHOICE OR CHOICE1, CHOICE2 ETC - NEEDED FOR EVERY INPUT AND IF OPTION
    if choice == "[1]" or choice == "1":
        print("Hackerman recieves your text detailing the location of the camera and uses his skills to make the camera stop working.")
        time.sleep(2)
    elif choice == "[2]" or choice == "2":
        print("You decide to just carry on going down the corridor even though you could be getting recorded. You hope that the camera wasn't working in the first place.")
        time.sleep(2)
    print("You have reached the end of the corridor and noticed there is a lift and a door. Which way do you go?")
    time.sleep(2)
    print("[1] Go to the lift")
    time.sleep(1)
    print("[2] Go to the door")
    time.sleep(2)
    doorlift()

# game start
# JAMES' CODE
print("$$\   $$\$$$$$$$$\$$$$$$\   $$\ $$$$$$$$\ ")
time.sleep(0.2)
print("$$ |  $$ $$  _____\_$$  _|$$$$$$\__$$  __|")
time.sleep(0.2)
print('$$ |  $$ $$ |       $$ | $$  __$$\ $$ |   ')
time.sleep(0.2)
print('$$$$$$$$ $$$$$\     $$ | $$ /  \__|$$ |   ')
time.sleep(0.2)
print('$$  __$$ $$  __|    $$ | \$$$$$$\  $$ |   ')
time.sleep(0.2)
print('$$ |  $$ $$ |       $$ |  \___ $$\ $$ |   ')
time.sleep(0.2)
print('$$ |  $$ $$$$$$$$\$$$$$$\$$\  \$$ |$$ |   ')
time.sleep(0.2)
print('\__|  \__\________\______\$$$$$$  |\__|   ')
time.sleep(0.2)
print('                          \_$$  _/        ')
time.sleep(0.2)
print('                            \ _/          ')
time.sleep(0.2)
print('Welcome to HEI$T, ' + codename + ' you can call me Hackerman')
print("The codes for the security system and the vault are 9745 and 1234.")
time.sleep(1)

def game_intro():
    print("The day has finally arrived.")
    time.sleep(2)
    print("All of the months of preparation has lead up to this moment.")
    time.sleep(2)
    print("You secretly were feeling nervous about undertaking this mission. At least you had Hackerman outside in the van to help out if needed.")
    time.sleep(2)
    print("Currently you are stationed on the building opposite the targeted bank.")
    time.sleep(2)
    print('You are about to zipline down to the bank on the other side of the street. You are hooked up and ready to go but before you go you decide to grab one more item. Your current equipment consists of:')
    time.sleep(2)
    for i in inventory:
        time.sleep(0.2)
        print(i)

def eventitemchoose():
    print(local_items)
    item_selected = int(
        input('Which item are you going to take with you [1, 2, 3]: '))
    if item_selected == 1:
        print('You quickly grabbed the {}'.format(local_items[0]))
        inventory.append('{}'.format(local_items[0]))
        eventitemcheck()
    elif item_selected == 2:
        print('You quickly grabbed the {}'.format(local_items[1]))
        inventory.append('{}'.format(local_items[1]))
        eventitemcheck()
    elif item_selected == 3:
        print('You quickly grabbed the {}'.format(local_items[2]))
        inventory.append('{}'.format(local_items[2]))
        eventitemcheck()
    else:
        print('Invalid option try again')

# JACKS CODE

def exit_via_lift_good():
    print("You descend to floor 1 via the lift.")

def exit_via_stairs_good():
    print("You descend to floor 1 via the stairs.")

def floor_2_good_incorrect():
    print("Please choose A or B.")
    floor_2_good_choice = input(
        "Do you: [1] use the lift to go to floor 1. [2] take the stairs to floor 1.")
    if floor_2_good_choice == "1" or floor_2_good_choice == "[1]":
        time.sleep(1)
        exit_via_lift_good()
    elif floor_2_good_choice == "2" or floor_2_good_choice == "[2]":
        time.sleep(1)
        exit_via_stairs_good()
    else:
        floor_2_good_incorrect()

def floor_2_good_leave():
    print("You can now head to Floor 1.")
    floor_2_good_choice = input(
        "Do you: [1] use the lift to go to floor 1. [2] take the stairs to floor 1.")
    if floor_2_good_choice == "1" or floor_2_good_choice == "[1]":
        time.sleep(1)
        exit_via_lift_good()
    elif floor_2_good_choice == "2" or floor_2_good_choice == "[2]":
        time.sleep(1)
        exit_via_stairs_good()
    else:
        floor_2_good_incorrect()

def security_hackerman():
    print("You now have access to the security system thanks to hackerman.")
    floor_2_good_leave()

def security_bad():
    print("You now have security access but people may notice the unconscious guard and rase the alarm.")
    time.sleep(1)
    security_good()

def security_good():
    print("You now have access to the security system.")
    time.sleep(2)
    floor_2_good_leave()

def security_bad_input():
    print("Please choose [1], [2] or [3].")
    print("The security station is a small room with a desk, behind the desk a guard watches over a series of monitors. You can either [1] Knockout the guard, [2] Distract the guard or [3] Call Hackerman to hack the security system for you.")
    time.sleep(2)
    security_station_options = input("Choose [1], [2] or [3]. ")
    if security_station_options == "1" or security_station_options == "[1]":
        print(
            "You attack and knock out the guard, you can now access the security station.")
        time.sleep(1)
        security_bad()
    elif security_station_options == "2" or security_station_options == "[2]":
        print("You distract the guard by telling them they are needed in the main room, causing them to leave the security station, you can now access the security station.")
        time.sleep(1)
        security_good()
    elif security_station_options == "3" or security_station_options == "[3]":
        print("You call up hackerman and get him to hack the security system for you.")
        time.sleep(1)
        security_hackerman()
    else:
        security_bad_input()

def security_station_fn():
    print("The security station is a small room with a desk, behind the desk a guard watches over a series of monitors. You can either [1] Knockout the guard, [2] Distract the guard or [3] Call Hackerman to hack the security system for you.")
    time.sleep(2)
    security_station_options = input("Choose [1], [2] or [3]. ")
    if security_station_options == "1" or security_station_options == "[1]":
        print(
            "You attack and knock out the guard, you can now access the security station.")
        time.sleep(1)
        security_bad()
    elif security_station_options == "2" or security_station_options == "[2]":
        print("You distract the guard by telling them they are needed in the main room, causing them to leave the security station, you can now access the security station.")
        time.sleep(1)
        security_good()
    elif security_station_options == "3" or security_station_options == "[3]":
        print("You call up hackerman and get him to hack the security system for you.")
        time.sleep(1)
        security_hackerman()
    else:
        security_bad_input()

def exit_via_lift_bad():
    print("You descend to floor 1 via the lift.")

def exit_via_stairs_bad():
    print("You descend to floor 1 via the stairs.")

def bad_leave_input():
    print("Please Choose [1] or [2].")
    time.sleep(1)
    print("You need to leave this floor quickly, do you take [1] The stairs or [2] The lift.")
    time.sleep(1)
    floor_2_bad_exit = input("[1] or [2]? ")
    if floor_2_bad_exit == "1" or floor_2_bad_exit == "[1]":
        exit_via_stairs_bad()
    elif floor_2_bad_exit == "2" or floor_2_bad_exit == "[2]":
        exit_via_lift_bad()
    else:
        bad_leave_input()

def floor_2_bad_leave():
    print("----------------------------")
    main_room_fn()

def main_room_bad_input():
    print("Please choose either [1] or [2].")
    time.sleep(1)
    print("Do you [1] Attack the guards or [2] Investigate the area")
    time.sleep(1)
    floor_2_choice_2 = input("[1] or [2] ")
    if floor_2_choice_2 == "1" or floor_2_choice_2 == "[1]":
        print("You begin causing a comotion and draw the attention of the guards, when they approach you attack but you are quickly arrested, your mission ends here.")
        time.sleep(1)
        floor_2_bad_leave()
    elif floor_2_choice_2 == "2" or floor_2_choice_2 == "[2]":
        print("You begin investigating the main room, making sure not to draw attention to yourself, you learn the pattern the guards take and the main exits from this floor, a set of stairs and an elevator both which lead to the first floor.")
        time.sleep(1)
        print("While searching this floor you find A Decorative Horse and decide to take it.")
        time.sleep(1)
        print("PICKED UP THEDECORATIVE HORSE!")
        floor_2_good_leave()
    else:
        main_room_bad_input()

def main_room_fn():
    print("The main room is a large open space with people coming too and throw on their buisness, guards patrol the area, keeping an eye out for potential criminal activity. You can either attack the guards and try to get through the bank as quickly as possible or investigate this floor ofthe bank and find a way around security.")
    time.sleep(2)
    print("Do you [1] Attack the guards or [2] Investigate the area")
    time.sleep(1)
    floor_2_choice_2 = input("[1] or [2] ")
    if floor_2_choice_2 == "1" or floor_2_choice_2 == "[1]":
        print("You begin causing a comotion and draw the attention of the guards, when they approach you attack, but you are quickly cornered and arrested.")
        time.sleep(1)
        print("GAME OVER")
        floor_2_bad_leave()
    elif floor_2_choice_2 == "2" or floor_2_choice_2 == "[2]":
        print("You begin investigating the main room, making sure not to draw attention to yourself, you learn the pattern the guards take and the main exits from this floor, a set of stairs and an elevator both which lead to the first floor.")
        time.sleep(1)
        print("While searching this floor you find A Decorative Horse and decide to take it.")
        time.sleep(1)
        print("PICKED UP A DECORATIVE HORSE!")
        floor_2_good_leave()
    else:
        main_room_bad_input()

def door_incorrect_input():
    print("Please choose either [1] or [2].")
    time.sleep(1)
    floor_2_choice_1 = input(
        " [1] The main room of the bank or [2] Security Station? ")
    if floor_2_choice_1 == "1" or floor_2_choice_1 == "[1]":
        main_room_fn()
    elif floor_2_choice_1 == "2" or floor_2_choice_1 == "[2]":
        security_station_fn()
    else:
        door_incorrect_input()

def floor_2_enter():
    floor_3_exit = "the stairs"
    print("You enter the 2nd floor from {}".format(floor_3_exit))
    time.sleep(2)
    print("You see a door leading to [1] The main room of the bank and [2] The Security Station.")
    time.sleep(1)
    print("Which door do you go through?")
    time.sleep(1)
    floor_2_choice_1 = input(" [1] or [2] ")
    if floor_2_choice_1 == "1" or floor_2_choice_1 == "[1]":
        main_room_fn()
    elif floor_2_choice_1 == "2" or floor_2_choice_1 == "[2]":
        security_station_fn()
    else:
        door_incorrect_input()

# runs game
game_intro()
eventitemchoose()
# Use this to get the floors to be linked
print('------Next sequence------')
third_floor()
# This is to run the third floor
print('------Next sequence------')
floor_2_enter()
# This is to run the second floor
print('------Next sequence------')
# Start_of_floor_1
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
        print("'------Next sequence------'")
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
    print("[1] Do you attack the guards?")
    time.sleep(1)
    print("[2] Do you call upon Hackerman to cause a distraction?")
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
    print("[1] Do you go left")
    time.sleep(1)
    print("[2] Do you go right?")
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
        print("[1] Do you want to kick the door open?")
        time.sleep(1)
        print("[2] Do you decide not to risk it and go back?")
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
    else:
        
        print("I didn't understand that.")
        time.sleep(1)
        print('Please type in either "1" or "2"')
        time.sleep(1)
        print("---------------------------------------------")
        first_choice()
first_choice()

def eventitemcheck():
    print('your current items are: ')
    for i in inventory:
        print(i)
    time.sleep(0.2)
    
def eventitemchoose():
    print(local_items)
    item_selected = int(input('which item are you going to take with you[1, 2, 3]: '))
    if item_selected == 1:
        print('you quickly grabbed the {}'.format(local_items[0]))
        inventory.append('{}'.format(local_items[0]))
        eventitemcheck()
    elif item_selected == 2:
        print('you quickly grabbed the {}'.format(local_items[1]))
        inventory.append('{}'.format(local_items[1]))
        eventitemcheck()
    elif item_selected == 3:
        print('you quickly grabbed the {}'.format(local_items[2]))
        inventory.append('{}'.format(local_items[2]))
        eventitemcheck()
    else:
        print('invalid option try again')
        eventitemchoose()

def event_basement_left():
    print('you spot a door at the end of left hallway and quickly dart back round the corner, hoping the security camera above the door didnt see you. SECURITY ROOM is printed on the door. you get the idea that you might be able to shut off the whole banks security system if you manage to get into that room.')
    choice = int(input('what do you want to do? [1] get hackerman to disable the security camera tempoarily so you can get in, or [2] use a tool to try and somehow make it inside the door?'))
    if choice == 1:
        print('hackerman manages to disable the camera and you breeze right through upto the door and enter it.')
        event_basement_security()
    elif choice == 2:
        eventitemcheck()
        item_used = str(input('which item are you going to use?'))
        if item_used == 'smokebomb':
            print('you pull the ring out of your smokebomb, rolling it down the hallway fills it with smoke and you quickly rush to the door and enter it')
            print('item smokebomb removed from inventory')
            inventory.remove('smokebomb')
            eventitemcheck()
            event_basement_security()
        elif item_used == 'taser':
            print('you used the taser, activating it made a loud noise and alerted the guards to your position')
            print('YOU FAILED')
            event_basement_left()
        elif item_used == 'infrared goggles':
            print('you used infrared goggles to try and walk upto the door, they didnt help but atleast it seems the camera isnt being opperated right now.')
            print('item infrared googles removed from inventory')
            inventory.remove('infrared goggles')
            eventitemcheck()
            event_basement_security()
        elif item_used == 'hand drill':
            print('you tried using the hand drill to do drill into the wall and by pure chance you hit the routing for the security camera cutting it off however the drill is now stuck in the wall. You freely walk upto the door after cutting the camera off.')
            print('item hand drill removed from inventory')
            inventory.remove('hand drill')
            eventitemcheck()
            event_basement_security()
        elif item_used == 'duffle bag':
            print('you attempted to use the duffle bag for whatever reason, you slipped while fumbling with the bag and died')
            print('YOU FAILED')
            event_basement_left()
        elif item_used == 'banana':
            print('you ate the banana and it gave you the power of invisibility for a short amount of time. You managed to make it inside the room before the invisibility.')
            print('item banana removed from inventory')
            inventory.remove('banana')
            event_basement_security()
    else:
        print('YOU FAILED')
        event_basement_left()

def event_vault_codepad(enteredcode):
    codepad_code = 1234
    if enteredcode == codepad_code:
        print('After the bank vault opens, you rush into the vault. Stacks and Stacks of COLD, HARD, CASH piled high sit on the table infront of you.')
        time.sleep(3)
        print('You stuff your bags full of the ill gotten gains, and make you way back through the bank using the elevator to get to the roof before abseiling down the building to meet hackerman.')
        time.sleep(3)
        print('You make your way to the van parked at the back of the bank. Chucking your bags filled to the brim with cash into the van before hopping in the passengers seat and driving away.')
        time.sleep(3)
        print("$$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\  $$$$$$\  $$\   $$\       $$\   $$\ $$$$$$$$\ $$$$$$\    $$\  $$$$$$$$\ ")
        time.sleep(0.2)
        print("\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |$$  __$$\ $$$\  $$ |      $$ |  $$ |$$  _____|\_$$  _| $$$$$$\\__$$  __|")
        time.sleep(0.2)
        print(' \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |$$ /  $$ |$$$$\ $$ |      $$ |  $$ |$$ |        $$ |  $$  __$$\  $$ |   ')
        time.sleep(0.2)
        print('  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |$$ |  $$ |$$ $$\$$ |      $$$$$$$$ |$$$$$\      $$ |  $$ /  \__| $$ |   ')
        time.sleep(0.2)
        print('   \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ |  $$ |$$ \$$$$ |      $$  __$$ |$$  __|     $$ |  \$$$$$$\   $$ |   ')
        time.sleep(0.2)
        print('    $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |  $$ |$$ |\$$$ |      $$ |  $$ |$$ |        $$ |   \___ $$\  $$ |   ')
        time.sleep(0.2)
        print('    $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ | $$$$$$  |$$ | \$$ |      $$ |  $$ |$$$$$$$$\ $$$$$$\ $$\  \$$ | $$ |   ')
        time.sleep(0.2)
        print('    \__|     \______/  \______/       \__/     \__| \______/ \__|  \__|      \__|  \__|\________|\______|\$$$$$$  | \__|   ')
        time.sleep(0.2)
        print('                                                                                                          \_$$  _/         ')
        time.sleep(0.2)
        print('                                                                                                            \ _/           ')
        time.sleep(0.2)
        print('Created by Team JJJR: Tolkien')
        time.sleep(.2)
        print('James')
        time.sleep(.2)
        print('Jack')
        time.sleep(.2)
        print('Jason')
        time.sleep(.2)
        print('Rebecca')
        time.sleep(1)
        print('-----------------------------------------------------------')
        print('*6 months later on a small island off the coast of Morocco*')
        time.sleep(2)
        print('      .                         .                             .')
        time.sleep(1)
        print('                      .     *          .')
        time.sleep(1)
        print('                .')
        time.sleep(1)
        print('                               .')
        time.sleep(1)
        print('   *              .                                    .')
        time.sleep(1)
        print('                                      .           ''`                   .')
        time.sleep(1)
        print('      .                                         ''`')
        time.sleep(1)
        print('                  //////')
        time.sleep(1)
        print('                  //////                                    ######')
        time.sleep(1)
        print('                 (//////)                                  ########')
        time.sleep(1)
        print('... ..  ..  ... . ////// . ... .())((() .. . . . .... . . . ..   . . ...  . . .')
        time.sleep(1)
        print('             _____|____|_____  ((()(()))                   /   /  /')
        time.sleep(1)
        print('            /                \ (((((((()                     /  /')
        time.sleep(1)
        print('           |                  |()(()(())_')
        time.sleep(1)
        print('           |                  |(((()()() |')
        time.sleep(1)
        print('           \                  ''\()))))(  |')
        time.sleep(1)
        print('            \                   \(((((  /')
        time.sleep(1)
        print('             \              .    \___. (')
        time.sleep(1)
        print('              \            / \    |:| ) \'')
        time.sleep(1)
        print('              |            | |`------'   '|''')
        time.sleep(1)
        print('              \____________/  \_________/                      Hackerman x {}, Forever '.format(codename))
        time.sleep(1)
        print(' ..........................................................................')
    elif enteredcode != codepad_code:
        print('incorrect code, the alarms have been sounded. Try Again')
        print('YOU FAILED')
        print('you approach the codepad and try and remember the code, what was it again?:')
        event_basement_security_codepad(int(input()))

#security room
def event_basement_security_codepad(enteredcode):
    security_system_code = 9745
    if enteredcode == security_system_code:
        print('you quickly punched the code into the codepad before flipping the switch. the code was right and the security system for the whole bank has been shutdown')
        print('getting into the vault should be a breeze')
        event_basement_right()
    elif enteredcode != security_system_code:
        print('incorrect code, the alarms have been sounded. Try Again')
        print('YOU FAILED')
        print('you approach the codepad and try and remember the code, what was it again?:')
        event_basement_security_codepad(int(input()))

def event_basement_security():
    print('theres one guard sat with his legs up in the chair asleep, you probably could have made it without being notice just by walking upto to the door. You see a codepad that says emergency shutdown above it you remember in your plan that you must enter a code into it to completly shut down the security system. but first you must take out the guard so he doesnt alert anyone else.')
    choice = int(input('[1] Use hands to try and choke him out, or [2] use a item'))
    if choice == 1:
        print('You sneak up behind the sleeping guard and get him in a headlock, holding him in it until he stops struggling.')
        print('you approach the codepad and try and remember the code, what was it again?: ')
        event_basement_security_codepad(int(input()))
    elif choice == 2:
        eventitemcheck()
        item_used = str(input('which item are you going to use?'))
        if item_used == 'smokebomb':
            print('you pull the ring out of your smokebomb, planting it under the guys seat and it fills the room with smoke. While the guard is confused you approach the codepad')
            print('item smokebomb removed from inventory')
            inventory.remove('smokebomb')
            print('you approach the codepad and try and remember the code, what was it again?: ')
            event_basement_security_codepad(int(input()))
        elif item_used == 'taser':
            print('you used the taser, activating it made a loud noise and alerted the guard but it does not matter as you make contact with the guards neck')
            print('item taser removed from inventory')
            inventory.remove('taser')
            print('you approach the codepad and try and remember the code, what was it again?: ')
            event_basement_security_codepad(int(input()))
        elif item_used == 'infrared goggles':
            print('you used infrared goggles they did nothing')
            print('YOU FAILED')
        elif item_used == 'hand drill':
            print('you thought about using the hand drill to take out the guard but it would be too gruesome')
            print('YOU FAILED')
        elif item_used == 'duffle bag':
            print('you use the duffle bag for whatever reason, you slipped while fumbling with the bag and died')
            print('YOU FAILED')
            event_basement_security()
        elif item_used == 'banana':
            print('you ate the banana and it gave you the power of invisibility for a short amount of time. You managed to approach the codepad with ease while the guard sleeps.')
            print('item banana removed from inventory')
            inventory.remove('banana')
            print('you approach the codepad and try and remember the code, what was it again?: ')
            event_basement_security_codepad(int(input()))
    else:
        event_basement_security()

def event_basement_right():
    print('you come upon a long hallway with the vault at the end, you cautiously approach what seems to be a plain hallway however there is something awry your gut feeling is kicking in.')
    choice = int(input('[1] walk ahead or [2] use item? '))
    if choice == 1:
        print('you cautiously walk ahead knowing that the security system included a high power laser system that could be activated at any time')
        print('after carefully shuffling across the hallway you make it to the vault, you see a lit up code pad, what code do you enter?')
        event_vault_codepad(int(input()))
    elif choice == 2:
        eventitemcheck()
        item_used = str(input('which item are you going to use? '))
        if item_used == 'smokebomb':
            print('you pull the ring out of your smokebomb, using it fills the room with a faint smoke. you can clearly see the effects of high powered lasers at work')
            print('you carefully dip and bob beneath the lasers and make it to the vault door')
            print('item smokebomb removed from inventory')
            inventory.remove('smokebomb')
            eventitemcheck()
            print('you approach the codepad for the vault, what code do you enter?')
            event_vault_codepad(int(input()))
        elif item_used == 'taser':
            print('you used the taser, activating it made a loud noise and alerted the guards to your position')
            print('YOU FAILED')
            event_basement_right()
        elif item_used == 'infrared goggles':
            print('you used infrared goggles and can clearly see the infrared lasers covering the hallway in a thick spiderweb of deadly beams')
            print('as you bob and weave between the lasers you make it to the other side without a scratch')
            print('item infrared goggles removed from inventory')
            inventory.remove('infrared goggles')
            eventitemcheck()
            print('you approach the codepad for the vault, what code do you enter?')
            event_vault_codepad(int(input()))
        elif item_used == 'hand drill':
            print('you tried using the hand drill for some reason, nothing happens except you waste time and get caught by a passing guard')
            print('YOU FAILED')
            event_basement_right()
        elif item_used == 'duffle bag':
            print('you attempted to use the duffle bag for whatever reason, you slipped while fumbling with the bag and died')
            event_basement_right()
        elif item_used == 'banana':
            print('you ate the banana and it gave you the power of invisibility for a short amount of time. The would be laser beams pass right through you like nothing was there.')
            print('you make it to the other side without a hitch')
            print('item banana removed from inventory')
            inventory.remove('banana')
            eventitemcheck()
            print('you approach the codepad for the vault, what code do you enter?')
            event_vault_codepad(int(input()))
        else:
            event_basement_right()
    else:
        event_basement_right()

def event_basement_start():
    print("after entering the basement you come across a hallway that splits into two path, you can either go left or right. ")
    time.sleep(1)
    floor_2_choice_1 = int(input(" [1] Go Left [2]. Go Right "))
    if floor_2_choice_1 == 1:
        event_basement_left()
    elif floor_2_choice_1 == 2:
        event_basement_right()
    else:
        event_basement_start()

event_basement_start()