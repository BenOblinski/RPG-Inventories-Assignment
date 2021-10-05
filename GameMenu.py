# Course: CS 30
# Period: 3
# Date created: 20/9/2021
# Date last modified: 5/10/2021
# Name: Ben Oblinski
# Description: Menu system for a text-based RPG game
import sys


def main_menu():
    # the deafault menu text is a function
    # the menu shows you the options you can choose from
    # this function can be called by typing 'menu'
    print("------Welcome to the Main Menu------")
    print("You can do any of the following actions:")
    print("-> stats   (veiw your characters stats)")
    print("-> charc   (Choose a Character to play)")
    print("-> inv     (View the items in your inventory)")
    print("-> map     (Look at your map to decide were to go)")
    print("-> quit    (Leave the menu loop) ")
    print("")
    print("You can type 'menu' at any time to see the above list")
    print("------------------------------------")

character_stats = ["You have not chosen a Character Yet"]
# list of your charcters stats
# this list can be accsessed by typing 'stats'

charcters = {"John Ruth 💀 ": {"Description": "A grisled bounty hunter with a \
scar on his right eye",
                                 "Health": 120, "Attack": 45, "Defense": 30},
             "Austin Maverick ★":
                                {"Descrpition": "A lawman who deals out justice \
the way he sees fit",
                                 "Health": 100, "Attack": 50, "Defense": 25},
             "Gunner Ace 🦴":
                                {"Description": "An outlaw, framed by a coript \
sheif for murder",
                                 "Health": 110, "Attack": 40, "Defense": 35},
             "Jake \"The Snake\" Calloway 🦴":
                                {"Descrpition": "A dirty outlaw wanted for \
robbery across the state",
                                 "Health": 95, "Attack": 55, "Defense": 25}}
# list of your characters
# this list can be accsessed by typing 'charc'
# subdivisions of the inv dictonary: characters/person/stats

location = {"Tumbleweed":
            {"Description": "A dry, dying town in the \
middle of the desert", "Location": 'South West'},
            "Rattlesnake farm":
            {"Desription": "An old cattle farm turned into a \
gang hideout by Jake \"The Snake\"", "Location": 'NorthWest'},
            "Claymore": {"Desription": "A small, mostly abandoned \
settlment with houses made of clay",
                         "Location": 'SouthWest'},
            "New Highlands":
                        {"Descrpition": "A new, classy town",
                         "Location": 'East'},
            "Great Bear Falls":
                        {"Descrpition": "An enormous water falls that leads into the \
White water river",
                         "Location": 'North'}}
# list of loactions around the world
# list can be accsessed by typing 'map'
# subdivisions of the map dictonary: location/places/about

inventory = {"Primary Weapopn":
             {"6 Shooter":
              {"Description": "A small, \
6 capacity revolver", "Damage": 75, "Range": 50}},
             "Secondary Wepon":
             {"Combat Knife":
              {"Description": "A small, \
versatile knife", "Damage": 45, "Range": "Melee"}},
             "Healing Items": {"Bandages": {"Description": "Sterile bandages \
used to fix wounds",
                                            "Health": 25}}}
# list of items that your character is carrying
# this list can be accsessed by typing 'inv'
# subdivisions of the inv dictonary: inventory/slots/tools/description

# list of main weapons that the player can collect and use
primary_weapons = ["6 shooter", "tommy gun", "mauser", "sawed_off_shotgun",
                   "pump_action_shotgun", "hunting_rifle"]

# list of secondary weapons that the player can collect and use
secondary_weapons = ["Comabt Knife", "Hunting Knife", "Machete",
                     "Bullwhip", "Dynamite"]

# list of healing items the player can collect and use
healing_items = ["Bandages", "Adrealine Shot", "Disinfectant", "Health drink"]

# print test of the main weapons list
print("This is a test of the main weapons list")
print(f"The avalible main weapons are {primary_weapons}")
print(" ")

# print test of the secondary weapons list
print("This is a test of the secondary weapons list")
print(f"The avalible secondary weapons are {secondary_weapons}")
print(" ")

# print test of the healing items list
print("This is a test of the healing items list")
print(f"The avalible secondary weapons are {healing_items}")
print(" ")

main_menu()
# print the main menu text

while True:
    # all the menu options are contained in a loop

    user_input = str(input(""))
    # asks the player to choose what they want to do

    if user_input == "stats":
        # if the player wants to see statistics...
        for x in character_stats:
            print(f"-> {x}")
            # print the list of stats on diffrent lines
        print("")

    elif user_input == "charc":
        print("---------Characters---------")
        # if the player wants to see character traits...
        for person in charcters:
            print(f"-> {person}")
            # print the characters name
            for stats in charcters[person]:
                print(f"{stats} - {charcters[person][stats]}")
                # print the character descriptions next to the name
            print("")
        print("----------------------------")

    elif user_input == "map":
        # if the player wants to see the map...
        print("---------Map---------")
        for places in location:
            print(f"-> {places}")
            # print the list of place names on diffrent lines
            for about in location[places]:
                print(f"{about} - {location[places][about]}")
                # print the descriptions beside these names
            print(" ")
        print("---------------------")

    elif user_input == "inv":
        print("---------Your Inventory---------")
        # if the player wants to see their inventory...
        for slots in inventory:
            print(f"-> {slots}")
            # print the list of item slots on diffrent lines
            for tools in inventory[slots]:
                print(f"{tools}")
                # print the list of items in each slot
                for disc in inventory[slots][tools]:
                    print(f"{disc} - {inventory[slots][tools][disc]}")
                    # print the descriptions of each item on diffrent lines
                print(" ")
        print("--------------------------------")

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
