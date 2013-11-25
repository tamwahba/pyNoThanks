from player import *
from card import *
import random

REMOVE_CARDS = 9
FIRST = 0


class Game:
    """docstring for  Game"""
    def __init__(self, playerNameList):
        self.__playerDict = {}

        for playerName in playerNameList:
            self.__playerDict[playerName] = Player(playerName)

        self.__playerOrderList = playerNameList
        random.shuffle(self.__playerOrderList)

        self.__currentPlayerName = playerNameList[FIRST]

        self.__deck = []

        # populate card deck
        for num in range(3, 36):
            self.__deck.append(Card(num))

        random.shuffle(self.__deck)

        # remove 9 cards from the deck
        self.__deck = self.__deck[: len(self.__deck) - REMOVE_CARDS]

        self.__currentCard = self.__deck[FIRST]

    # ----- Mutators ----- #
    def playerAddCard(self, playerName, card):
        self.__playerDict[playerName].addCard(card.getValue())
        self.__playerDict[playerName].addChip(card.getChips())

    def playerRemoveChip(self, playerName):
        self.__playerDict[playerName].removeChip()

    def currentCardAddChip(self):
        self.__currentCard.addChip()

    # ----- Accessors ----- #
    # param playerName (str)
    def getPlayerCards(self, playerName):
        return self.__playerDict[playerName].getCards()

    def getDeck(self):
        return self.__deck

    def getNextPlayerName(self):
        self.__currentPlayerName = self.__playerOrderList[
            self.__playerOrderList.index(self.__currentPlayerName) + 1]
        return self.__currentPlayerName


# ---- Test ---- #
# def main():
#     g = Game(["p1", "p2", "p3", "p4"])
#     print(len(g.getDeck()))

#     g.playerAddCard("p1", g.getDeck()[1])

#     print(g.getPlayerCards("p1"))

#     print(g.getNextPlayerName())

# main()
# ----- End Game ----- #
