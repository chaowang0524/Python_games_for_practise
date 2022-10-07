"""
In this project you will build a simplified, one-player version of the classic board game Battleship!

In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.

To build this game we will use our knowledge of lists, conditionals and functions in Python.

"""
import random

# Define all the coordinates
location_all = [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
]
time = 10


def print_list():
    for i in location_all:
        print(i, end='\n')


def welcome():
    print("Welcome to Battleship!")
    print("The ship is behind one of the stars below! Make your guess!")
    print(f"You have {time} times left.")
    print_list()
    print("*"*8)


# Generate the ship
location_ship_row = random.randint(0, 4)
location_ship_col = random.randint(0, 4)
location_ship = location_all[location_ship_row][location_ship_col]


# Gameplay
welcome()
while time > 0:
    row = int(input("Please enter the coordinates of the location (row)")) - 1
    column = int(
        input("Please enter the coordinates of the location (column) ")) - 1
    if row == location_ship_row and column == location_ship_col:
        location_all[location_ship_row][location_ship_col] = "@"
        print_list()
        print("Congratulations! You've found the ship!")
        break

    else:
        location_all[row][column] = "X"
        print_list()
        print("Sorry, please try again.")
        time = time - 1
        print(f"You have {time} times left.")
        print("*" * 8)
