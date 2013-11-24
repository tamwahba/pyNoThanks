FIRST = 1


class Player:
    """docstring for  Player"""
    def __init__(self, playerName):
        self.__name = playerName  # str
        self.__cardList = []  # list<int>
        self.__chips = 11  # int

    # -------------------------------
    # Accessors
    def getCards(self):
        return self.__cardList

    def getChips(self):
        return self.__chips

    def getName(self):
        return self.__playerName

    def getSortedList(self):
        self.__cardList.sort()
        return self.__cardList

    def getScore(self):
        score = 0
        self.__cardList.sort()
        previousCard = self.__cardList[FIRST]

        for card in self.__cardList:
            if not (previousCard == card - 1):
                score += card
            previousCard = card

        score -= self.__chips
        return score

    # ----- Mutators ----- #
    # param card (int)
    def addCard(self, card):
        self.__cardList.append(card)

    # param numchips (int)
    def addChip(self, numchhips=1):
        self.__chips += numchhips

    def removeChip(self):
        self.__chips -= 1

    # -------------------------------
    # 'toString'
    def __str__(self):

        return "%s's Cards:\n%s" % (self.__name,
               "\n".join(str(card) for card in self.__cardList))


# ----- Test ----- #
def main():
    p1 = Player("p1")
    p1.addCard(20)
    p1.addCard(31)
    p1.addCard(33)
    p1.addCard(35)
    p1.addCard(12)
    p1.addCard(11)
    p1.addCard(10)
    p1.addCard(5)
    p1.addCard(7)
    p1.addCard(9)

    print(p1.getCards())

    print(p1.getSortedList())

    p1.removeChip()

    print(p1.getChips())

    print(p1.getScore())

    print(p1)

main()
# ---- End Test ----#
