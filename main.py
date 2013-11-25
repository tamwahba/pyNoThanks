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
DEFAULT_PLAYERS = 3


class MainWindow(object):
    """docstring for MainWindow"""
    def __init__(self):
        self.__window = Tk()
        self.__window.title("No Thanks")
        self.__window.minsize(width=400, height=350)

        self.__currentPage = self.page1()

        self.__window.mainloop()

    def page1(self):
        self.__numPlayersVar = IntVar(value=DEFAULT_PLAYERS)

        self.__pageFrame = Frame(self.__window)
        self.__numPlayerLabel = Label(self.__pageFrame,
                                      text="Select number of players")

        self.__menuBtn = Menubutton(self.__pageFrame,
                                    textvariable=self.__numPlayersVar)
        # create menu widget, disallow it to be removed from it's position
        self.__menu = Menu(self.__menuBtn, tearoff=0)

        # populate drop down menu with number choices, don't allow checkmark
        #  to appear next to selected entry
        self.__menu.add_radiobutton(label="3", variable=self.__numPlayersVar,
                                    value=3, indicatoron=0)
        self.__menu.add_radiobutton(label="4", variable=self.__numPlayersVar,
                                    value=4, indicatoron=0)
        self.__menu.add_radiobutton(label="5", variable=self.__numPlayersVar,
                                    value=5, indicatoron=0)
        self.__menu.add_radiobutton(label="6", variable=self.__numPlayersVar,
                                    value=6, indicatoron=0)

        self.__menuBtn.config(menu=self.__menu)

        self.__nextButton = Button(self.__pageFrame, text="Next",
                                   command=self.goToPage2)

        self.__numPlayerLabel.pack(side="left")
        self.__menuBtn.pack(side="left")
        self.__nextButton.pack(side="left")
        self.__pageFrame.pack(side="top")

    def goToPage2(self):
        self.__pageFrame.pack_forget()
        del self.__pageFrame
        self.__currentPage = self.page2()

    def page2(self):
        print(self.__numPlayersVar.get())

        self.__pageFrame = Frame(self.__window)
        self.__playerNames = []

        for player in range(self.__numPlayersVar.get()):
            self.__playerNames.append(StringVar())

        for player in range(self.__numPlayersVar.get()):
            self.__nameFrame = Frame(self.__pageFrame)
            Label(self.__nameFrame,
                  text="Enter player %i name" % (player + 1)).pack(side="left")
            Entry(self.__nameFrame,
                  textvariable=self.__playerNames[player]).pack(side="top")
            self.__nameFrame.pack()

        self.__pageFrame.pack()

        self.__goButton = Button(self.__pageFrame,
                                 text="Go", command=self.goToPage3)
        self.__goButton.pack()

    def goToPage3(self):
        self.__pageFrame.pack_forget()
        del self.__pageFrame
        # -- test
        for player in self.__playerNames:
            print(player.get())

MainWindow()
