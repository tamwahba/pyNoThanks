"""
Analysis

A deck of 33 cards labeled from 3 to 35 is shuffled. Then 9 cards are
removed. Each player starts with 11 chips. On each turn the player has
2 options: to put down one of the chips or take the card. Chips count as
-1 point each while the cards count as positive face value, and unbroken
number sequences are counted as the lowest number of the sequence only.
The winner is the player who has the least points after all cards have
been dealt.
"""
from tkinter import *
from tkinter.ttk import *


class MainWindow(object):
    """docstring for MainWindow"""
    def __init__(self):
        self.__window = Tk()
        self.__window.title("No Thanks")

        self.__window.mainloop()


MainWindow()
