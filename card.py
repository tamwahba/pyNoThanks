""""
Michael Mones
mmones@binghamton.edu

Class for card object has variables self.__value,
 self.__chips, and self.__picPath
"""


class Card:

    def __init__(self, cardValue):
        self.__value = cardValue
        self.__chips = 0
        self.__picPath = "cards/card%i.gif" % self.__value

    # ----------------------------
    # Mutators

    def addChip(self):
        self.__chips += 1

    # ----------------------------
    # Accessors

    def getChips(self):
        return self.__chips

    def getValue(self):
        return self.__value

    def getPicPath(self):
        return self.__picPath

# ----- Test ----- #
# from tkinter import *


# def main():
#     win = Tk()

#     c = Card(1)
#     im1 = PhotoImage(file=c.getPicPath())
#     pic = Label(win, image=im1)
#     pic.pack()

#     c2 = Card(2)
#     im2 = PhotoImage(file=c2.getPicPath())
#     pic2 = Label(win, image=im2)
#     pic2.pack()

#     c3 = Card(4)
#     im3 = PhotoImage(file=c3.getPicPath())
#     pic3 = Label(win, image=im3)
#     pic3.pack()

#     print(c3.getPicPath())

#     win.mainloop()

#     del c
# main()
# --- End Test --- #
