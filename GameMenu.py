# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 22/9/2021
# Name: Ben Oblinski
# Description: Menu system for a text-based RPG game
import sys


def main_menu():
    # the deafault menu text is a function
    # the menu shows you the options you can choose from
    # this function can be called by typing 'menu'
    print("Welcome to the Main Menu")
    print("You can do any of the following actions:")
    print("-stats   (veiw your characters stats)")
    print("-charc   (View your character)")
    print("-inv     (View the items in your inventory)")
    print("-store   (purchase weapons and equipment)")
    print("-lvl     (Select the level you wish to play)")
    print("-quit    (Leave the menu loop) ")
    print("")
    print("You can type 'menu' at any time to see the above list")
    print("")

character_stats = ["HEALTH:     120", "ATTACK:     20",
                   "DEFENSE:    8", "EXPERIENCE: 50"]
# list of your charcters stats
# this list can be accsessed by typing 'stats'

charcter_traits = ["Name:  John", "Race:  Human", "Class: Cowboy"]
# list of your characters traits
# this list can be accsessed by typing 'charc'

inventory = ["MAIN WEAPON:      Long Sword", "SECONDARY WEAPON: Pocket Knife",
             "Healing Items:    Bandages x 2", "Gold Peices:      100"]
# list of items that your character is carrying
# this list can be accsessed by typing 'inv'

store_items = ["Shortsword    - +3 to attack  - 75 gold",
               "Combat Knife  - +1 to attack  - 45 gold",
               "Shogun        - +4 to attack  - 250 gold",
               "Sheild        - +2 to defense - 80 gold"]
# list of items that can be bought from the store
# this list can be accsessed by typing 'store'

levels = ["Level 1| HERO", "Level 2| HERO", "Level 3| HERO", "Level 4| HERO",
          "Level 1| Villain", "Level 2| Villain", "Level 3| Villain", "Level 4| Villain"]
# list of levels that the player can play
# this list can be accsessed by typing 'lvl'

main_menu()
# print the main menu text

while True:
    # all the menu options are contained in a loop
    # when the user types an input, varios if statments decide what to do
    # if the input does not match with an if statment the progam responds 'invalid response'

    user_input = str(input(""))
    # asks the player to choose what they want to do

    if user_input == "stats":
        # if the player wants to see statistics...
        for x in character_stats:
            print(f"-> {x}")
            # print the list of stats on diffrent lines
        print("")

    elif user_input == "charc":
        # if the player wants to see character traits...
        for y in charcter_traits:
            print(f"-> {y}")
            # print the list of charcater traits on diffrent lines
        print("")

    elif user_input == "inv":
        # if the player wants to see their inventory...
        for z in inventory:
            print(f"-> {z}")
            # print the list of items on diffrent lines
        print("")

    elif user_input == "store":
        # if the player wants to see the shop...
        print("Welcome to the Store")
        print("You have 100 gold peices to spend")
        print("Items for Sale:")
        for a in store_items:
            print(f"-> {a}")
            # print the list of shop items on diffrent lines
        print("")

    elif user_input == "lvl":
        # if the player wants to see playable levels...
        print("Select a level you wish to play:")
        for b in levels:
            print(f"-> {b}")
            # print the list of levels on diffrent lines
        print("")

    elif user_input == "menu":
        # if the player wants to see the main menu
        main_menu()
        # run the main_menu function

    elif user_input == "quit":
        # if the play want to quit
        print("are you sure you want to quit?")
        print("type 'y' to confrim")
        print("type any key to stay in the game")
        choose_to_quit = input("")
        # ask the player to confirm quitting

        if choose_to_quit == "y":
            # if the play wants to quit
            print("You have left the menu")
            # shut down the code
            sys.exit()

        else:
            print("You have choosen not to quit")
            print("")
            main_menu()
            # return the player to the main menu

    else:
        # the player has typed somthing that is not a command
        print("Invalid response. Please type again.")
        print("")
