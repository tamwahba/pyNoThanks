from player import *
import random

REMOVE_CARDS = 9
FIRST = 0


class Game:
    """docstring for  Game"""
    def __init__(self, playerNameList):
        self.__playerDict = {}
        self.__playerOrderList = playerNameList
        random.shuffle(self.__playerOrderList)
        self.__deck = []

        # populate card deck
        for num in range(3, 36):
            self.__deck.append(Card(num))

        random.shuffle(self.__deck)

        # remove 9 cards from the deck
        self.__deck = self.__deck[: len(self.__deck) - REMOVE_CARDS - 1]

        self.__currentCard = self.__deck[FIRST]

        for playerName in playerNameList:
            self.__playerDict[playerName] = Player(playerName)

    # ----- Mutators ----- #
    def playerAddCard(self, playerName, card):
        self.__playerDict[playerName].addCard(card.getValue())
        self.__playerDict[playerName].addChip(card.getChips())

    def playerRemoveChip(self, playerName):
        self.__playerDict[playerName].removeChip()

    # ----- Accessors ----- #
    def getPlayerCards(self, playerName):
        return self.__playerDict[playerName].getCards()

    def getDeck(self):
        return self.__deck


# ---- Test ---- #
def main():
    g = Game(["p1", "p2", "p3", "p4"])
    print(g.getDeck())

main()
# ----- End Game ----- #
