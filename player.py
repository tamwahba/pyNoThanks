FIRST = 0


class Player:
    """Player class for handling the player hand"""
    def __init__(self, playerName):
        self.__name = playerName  # str
        self.__cardList = []  # list<int>
        self.__chips = 11  # int

    # ----- Mutators ----- #
    # param card (int)
    def addCard(self, card):
        self.__cardList.append(card)

    # param numchips (int)
    def addChip(self, numchhips=1):
        self.__chips += numchhips

    def removeChip(self):
        self.__chips -= 1

    def getScore(self):
        score = 0
        self.__cardList.sort()
        currentCard = self.__cardList[FIRST]
        for card in self.__cardList:
            if not (currentCard == card - 1):
                score = card
            currentCard = card

        score -= self.__chips
        return score


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

main()
# ---- End Test ----#
