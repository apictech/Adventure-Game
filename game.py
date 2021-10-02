import time
import random

enemy = ["wicked fairie", "troll", "gorgon", "monster"]
demon = random.choice(enemy)
items = []


def print_sleep(message):
    print(message)
    time.sleep(2)


def restart_game():
    if "sword" in items:
        items.remove("sword")
    print_sleep("GAME OVER FOR YOU\n")
    response = input("Would you like to play again? (y/n)")
    print_sleep("\n")
    if response == 'y':
        game()
    elif response == 'n':
        print_sleep("Thanks for playing! See you next time.")
    else:
        restart_game()


def intro():
    print_sleep("You find yourself standing in an open area, "
                "filled with grass and yellow wildflowers.")
    print_sleep(f"Rumor has it that a {demon} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def field():
    # Things that happen when the player runs back to the field
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print("what would you like to do?")
    response = (input("(please enter 1 or 2).\n"))

    if response == '1':
        house()
    elif response == '2':
        cave()
    else:
        field()


def house():
    # Things that happen to the player in the house.
    print_sleep("You approach the door of the house.")
    print_sleep(f"You are about to knock when the "
                "door opens and out steps a {demon}.")
    print_sleep(f"Eep! This is the {demon}'s house!")
    print_sleep(f"The {demon} attacks you!")

    if "sword" in items:
        print_sleep(f"As the {demon} moves to attack, "
                    "you unsheath your new sword.")
        print_sleep("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack.")
        print_sleep(f"But the {demon} takes one look at "
                    "your shiny new toy and runs away!")
        print_sleep(f"You have rid the town of "
                    "the {demon}. You are victorious!")
        restart_game()

    elif "sword" not in items:
        print_sleep("You feel a bit under-prepared for "
                    "this, what with only having a tiny dagger.")
        response = input("Would you like to (1) fight or (2) run away?\n")

        if response == '1':
            print_sleep("You do your best...")
            print_sleep(f"but your dagger is no match for the {demon}.")
            print_sleep("You have been defeated!")
            restart_game()

        elif response == '2':
            print_sleep("You run back into the field. Luckily, "
                        "you don't seem to have been followed.\n")
            field()


def cave():
    # Things that happen to the player goes in the cave
    if "sword" in items:
        print_sleep("You peer cautiously into the cave.Cave is full of darkness")
        print_sleep("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        print_sleep("You walk back out to the field.")
        field()
    else:
        print_sleep("You peer cautiously into the cave.")
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old dagger and "
                    "take the sword with you.")
        print_sleep("You walk back out to the field.\n")
        items.append("sword")
        field()


def game():
    intro()
    field()


game()
