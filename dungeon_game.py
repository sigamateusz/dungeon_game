import sys
import os
import time
import gameboard
import random
import collections
import sfinx_graphic
from termcolor import colored, cprint

os.system('clear')  # clear screen


def sfinx(life):
    global num_gameb
    # global life
    global inv
    sfinx_graphic.print_sfinx()
    print("If you answer my riddle I will give you a ruby. If not I will attack you!")
    print("\nWhat creature walks on four legs in the morning, on two in the midday and on three in the evening?")
    answer_sfinx = input("\nWhat is your answer?: ")
    while answer_sfinx != "human":
        os.system('clear')  # clear screen
        life -= 1
        sfinx_graphic.print_sfinx()
        print("\nWhat creature walks on four legs in the morning, on two in the midday and on three in the evening?")
        print("lifes:", life)
        answer_sfinx = input("What is your answer?: ")
    else:
        print("You are correct. Here is your ruby. You can move on with your journey.")
        loot = ['ruby']
        inv = add_to_inventory(inv, loot)
        num_gameb += 1
        return life


def merchant():
    global gold_coins
    global inv
    global num_gameb
    loot =['life_potions']
    life_potions = 5
    print("Welcome in my shop.")
    print("\nI sell potions that restore your life.")
    print("\nOne costs 30 gold coins")
    amount = int(input("\nHow much do you want?: "))
    if life_potions >= amount:
        if gold_coins >= amount * 30:
            life_potions = life_potions * amount
            gold_coins = gold_coins - 30 * amount
            print(inv)
            print("\nThank you for purchase.")
            print(life_potions)
            loot = ['life_potions']*amount
            add_to_inventory(loot)
            num_gameb += 1
            num_gameb -= 1
        else:
            print("You don't have enough gold.")
    elif ValueError:
        print("You need to give me some gold.")
    else:
        print("I do not have that many.")


def add_to_inventory(loot):
    """it adding loot to current inventory"""
    global inv
    inv = collections.Counter(inv)
    # collections module helps to add dictionaries value
    loot = collections.Counter(loot)
    inv = inv+loot
    return inv


def choice_gameboard(number, wide_gameboard, height_gameboard, user_coordinates):
    tab = []
    if number == 1:
        tab = gameboard.gameboard(wide_gameboard, height_gameboard, user_coordinates)
    elif number == 3:
        tab = gameboard.gameboard1(wide_gameboard, height_gameboard, user_coordinates)
    elif number == 5:
        tab = gameboard.gameboard2(wide_gameboard, height_gameboard, user_coordinates)
    return tab


def getch():
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def option():
    """starting menu about inventory"""
    cprint("\t  ...:::CHOOSE AN OPTION:::...\t\t", 'green', 'on_grey')
    cprint("{:>9}{:>16}{:>11}{:>8}\t".format('START', 'INSTRUCTIONS', 'CREDITS', 'EXIT'), 'green', 'on_grey')
    cprint("{:>7}{:>13}{:>13}{:>10}\t".format('1', '2', '3', 'X'), 'blue', 'on_grey')
    option1 = getch()
    if option1 == '1':
            start()
    elif option1 == '2':
        os.system('clear')  # clear screen
        instructions()
    elif option1 == '3':
        os.system('clear')  # clear screen
        credits()
    elif option1 == 'x':
        sys.exit()


def credits():
    cprint("Made by Maria Steinmec, Mateusz Siga and Marek Stopka", 'green', 'on_grey')
    cprint("Press <q> to go back to menu: ", 'red', 'on_grey')
    exit = getch()
    if exit == 'q':
        os.system('clear')
        option()
    else:
        cprint("Are you ready to go on?", attrs=['bold'])
        credits()


def instructions():
    """it shows how to move in a dungeon game"""
    cprint("Use WSAD to move up/down/left/right in DUNGEON GAME", 'green', 'on_grey')
    cprint("And x to exit the game.", 'green', 'on_grey')
    cprint("Press <q> to go back to menu: ", 'red', 'on_grey')
    exit = getch()
    if exit == 'q':
        os.system('clear')  # clear screen
        option()
    else:
        cprint("Are you ready to go on?", attrs=['bold'])
        instructions()


def display_gameboard(x, y, table, life, gold_coins):
    os.system('clear')  # clear screen
    for i in range(x):
        if i == 2:
            cprint("{:^15}".format("MONEY"), 'green', attrs=['bold'], end='')
        elif i == 3:
            cprint("{:^15}".format(gold_coins), 'green', attrs=['bold'], end='')
        elif i == 6:
            cprint("{:^15}".format("LIFES"), 'green', attrs=['bold'], end='')
        elif i == 7:
            cprint("{:^15}".format(life), 'green', attrs=['bold'], end='')
        else:
            print('{:>15}'.format(''), end='')
        for j in range(y):
            if table[i][j] == '#':
                cprint(table[i][j], 'yellow', attrs=['bold'], end=' ')
            elif table[i][j] == '?':
                cprint(table[i][j], 'red', attrs=['bold'], end=' ')
            elif table[i][j] == '$' or table[i][j] == '%':
                cprint(table[i][j], 'blue', attrs=['bold'], end=' ')
            elif table[i][j] == '^':
                cprint(table[i][j], 'magenta', attrs=['bold'], end=' ')
            elif table[i][j] == '&' or table[i][j] == '!':
                cprint(table[i][j], 'green', attrs=['bold'], end=' ')
            elif table[i][j] == '@':
                cprint(table[i][j], 'white', attrs=['bold'], end=' ')
            elif table[i][j] == '.':
                print('\033[1;30;1m' + "{}".format(table[i][j]) + '\033[0m', end=' ')
        print('')


def user_move(table, user_position):
    """
    Moves user and clears previous position
    Returns new table with new position with user
    When touch '?' going to boss level
    """
    global num_gameb
    x_user = user_position[0]
    y_user = user_position[1]
    move = getch()
    if move == 'd':
        x_user += 1
        # checks new position
        if table[y_user][x_user] == '#':
            x_user -= 1
        # removes @ from previous position
        table[y_user][x_user - 1] = '.'
    elif move == 'a':
        x_user -= 1
        if table[y_user][x_user] == '#':
            x_user += 1
        table[y_user][x_user + 1] = '.'
    elif move == 'w':
        y_user -= 1
        if table[y_user][x_user] == '#':
            y_user += 1
        table[y_user + 1][x_user] = '.'
    elif move == 's':
        y_user += 1
        if table[y_user][x_user] == '#':
            y_user -= 1
        table[y_user - 1][x_user] = '.'
    elif move == 'x':
        sys.exit()
    user_position[0] = x_user
    user_position[1] = y_user
    check_touch(table, user_position)
    # sets @ on current position of user
    table[y_user][x_user] = '@'


def check_touch(table, user_position):
    """Checks if the user touches any item"""
    global num_gameb
    global gold_coins
    x_user = user_position[0]
    y_user = user_position[1]
    if table[y_user][x_user] == '?':
        num_gameb += 1
    elif table[y_user][x_user] == '!':
        pass
    elif table[y_user][x_user] == '$':
        gold_coins += random.randint(20, 50)
    elif table[y_user][x_user] == '%':
        pass
    elif table[y_user][x_user] == '^':
        merchant()
        pass
    elif table[y_user][x_user] == '&':
        pass


def random_elements(tab, *args):
    """randoms items to gameboard"""
    elements = ('!', '$', '%', '^', '&', '?')
    for i in range(6):
        x = random.randint(2, len(tab)-1)
        y = random.randint(2, len(tab[0])-1)
        while tab[y][x] != '.':
            x = random.randint(2, len(tab)-1)
            y = random.randint(2, len(tab[0])-1)
        tab[y][x] = elements[i]
    return tab


def start():
    """
    Starts game
    num_gameb checks wich gameboard should be displayed
    if num_gameb ==
        #1 first gameboard
        #2 sfinx
        #3 create second gameboard
        #4 run second gameboard
        #5 ...
    """
    global gold_coins
    global num_gameb
    global inv
    life = 3
    gold_coins = 1009
    inv = {'ruby': 1}
    num_gameb = 1
    user_coordinates = [1, 1]
    wide_gameboard = 40
    height_gameboard = 40
    gameboard_table = choice_gameboard(num_gameb, wide_gameboard, height_gameboard, user_coordinates)
    gameboard_table = random_elements(gameboard_table)
    while True:
        os.system('clear')
        if num_gameb == 1:
            display_gameboard(wide_gameboard, height_gameboard, gameboard_table, life, gold_coins)
            print('{}'.format(num_gameb))
            user_move(gameboard_table, user_coordinates)
            time.sleep(0.1)
        elif num_gameb == 2:
            # move to first boss
            life = sfinx(inv, life)
        elif num_gameb == 3:
            # creates new gameboard
            user_coordinates = [1, 1]
            gameboard_table = choice_gameboard(num_gameb, wide_gameboard, height_gameboard, user_coordinates)
            gameboard_table = random_elements(gameboard_table)
            num_gameb += 1
        elif num_gameb == 4:
            # run next level
            display_gameboard(wide_gameboard, height_gameboard, gameboard_table, life, gold_coins)
            print('{}'.format(num_gameb))
            user_move(gameboard_table, user_coordinates)
            time.sleep(0.1)
        elif num_gameb == 5:
            print('\n\n\tI wait for function!\n\n')
            sys.exit()


def main():
    cprint("{:^48}".format("Welcome stranger in DUNGEON GAME!"), 'red', 'on_grey')
    option()


main()


if __name__ == '__main__':
    main()
