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
        self.__window.minsize(width=400, height=350)

        self.__currentPage = self.page1()

        self.__window.mainloop()

    def page1(self):
        self.__pageFrame = Frame(self.__window)
        self.__numPlayerLabel = Label(self.__pageFrame,
                                      text="Enter number of players")

        self.__numPlayers = IntVar(value=3)

        self.__menuBtn = Menubutton(self.__pageFrame,
                                    textvariable=self.__numPlayers)
        self.__menu = Menu(self.__menuBtn, tearoff=0)

        self.__menu.add_radiobutton(label="3", variable=self.__numPlayers,
                                    value=3, indicatoron=0)
        self.__menu.add_radiobutton(label="4", variable=self.__numPlayers,
                                    value=4, indicatoron=0)
        self.__menu.add_radiobutton(label="5", variable=self.__numPlayers,
                                    value=5, indicatoron=0)
        self.__menu.add_radiobutton(label="6", variable=self.__numPlayers,
                                    value=6, indicatoron=0)

        self.__menuBtn.config(menu=self.__menu)

        self.__numPlayerLabel.pack(side="left")
        self.__menuBtn.pack(side="left")
        self.__pageFrame.pack(side="top")

    def page2(self):
        a=1

MainWindow()
