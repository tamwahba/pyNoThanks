FIRST = 1


class Player:
    '''docstring for  Player'''
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

    def getSortedCards(self):
        self.__cardList.sort()
        return self.__cardList

    # ----- Mutators ----- #
    # param card (int)
    def addCard(self, card):
        self.__cardList.append(card)

    # param numchips (int)
    def addChip(self, numchips=1):
        self.__chips += numchips

    def removeChip(self):
        self.__chips -= 1

    def getScore(self):
        score = 0
        self.__cardList.sort()
        currentCard = self.__cardList[FIRST]
        for card in self.__cardList:
            if not (currentCard == card - 1):
                score += card
            currentCard = card

        score -= self.__chips
        return score

    # -------------------------------
    # 'toString'
    def __str__(self):
        currentCard = self.__cardList[FIRST]
        cardSets = ""
        for card in self.getSortedCards():
            if not (currentCard == card - 1):
                cardSets += "\n"
            cardSets += str(card) + " "
            currentCard = card
        return cardSets
    
    
        


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
    p1.addChip()
    print(p1)
    print(p1.getScore())
main()
# ---- End Test ----#
