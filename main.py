# Monty Hall Problem
# Done in stupid way in purpose... Wanted to make it "Real"
# Made by mvaario

import time
import random

class settings:
    def __init__(self):

        # rounds
        self.f = 500000

        self.stay_win = 0
        self.switch_win = 0

        # better switch
        self.better_switch_win = 0

        return

    # Stay
    def stay(win, choise):
        # stay
        if win == choise:
            game.stay_win = game.stay_win + 1
        return

    # Switch
    def switch(win, choise):
        if win == 1:
            if choise == 1:
                choise = random.randint(2,3)
            else:
                choise = 1
        elif win == 2:
            if choise == 2:
                choise = random.randint(2,3)
                if choise == 2:
                    choise = 1
            else:
                choise = 2
        else:
            if choise == 3:
                choise = random.randint(1, 2)
            else:
                choise = 3

        if choise == win:
            game.switch_win = game.switch_win + 1
        return

    # Better switch..
    def better_switch(win, choise):
        # switch wins when stay doesn't
        if win != choise:
            game.better_switch_win = game.better_switch_win + 1
        return

    # Printing result
    def print():
        print("Stay wins - Switch wins")
        print(game.stay_win, " / ", game.switch_win)
        print("percentages")
        print(round(game.stay_win / game.f * 100,2), "%  / ", round(game.switch_win / game.f * 100,2), "% ")
        print("---------------")

        if game.better_switch_win != 0:
            print("Easier way", round(game.switch_win / game.f * 100, 2), "% ")

        return

if __name__ == '__main__':

    game = settings()
    last_time = time.time()

    print("")
    print("Starting", game.f, "Rounds")
    print("---------------")

    F = game.f
    for i in range(game.f):
        win = random.randint(1, 3)
        choise = random.randint(1, 3)

        settings.stay(win, choise)
        settings.switch(win, choise)

        settings.better_switch(win, choise)

    settings.print()









