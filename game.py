"""
Tamer Wahba
twahba1@binghamton.edu

Class for game object has variables self.__playerDict, self.__playerOrderList,
 self.__currentPlayerName, self.__currentCard, and self.__deck
"""
from player import *
from card import *
import random

REMOVE_CARDS = 9
FIRST = 0


class Game:
    # constructor
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

        self.__deck.append(Card(0))

        self.__currentCard = self.__deck[FIRST]

    # ----- Mutators ----- #
    def currentPlayerTakeCurrentCard(self):
        self.__playerDict[self.__currentPlayerName].addCard(
            self.__currentCard.getValue())
        self.__playerDict[self.__currentPlayerName].addChip(
            self.__currentCard.getChips())
        if self.cardsLeftInDeck():
            self.nextCard()
        elif self.lastCardInDeck():
            self.__currentCard = Card(0)
            self.__deck.append(self.__currentCard)

    def currentPlayerAddChipToCurrentCard(self):
        self.__playerDict[self.__currentPlayerName].removeChip()
        self.__currentCard.addChip()

    def nextCard(self):
        if self.cardsLeftInDeck():
            self.__currentCard = self.__deck[
                self.__deck.index(self.__currentCard) + 1]

    def nextPlayer(self):
        self.__currentPlayerName = self.__playerOrderList[
            self.__playerOrderList.index(self.__currentPlayerName) - 1]

    # ----- Accessors ----- #
    # param playerName (str)
    def getCurrentPlayerCards(self, playerName):
        return self.__playerDict[playerName].getCards()

    def getDeck(self):
        return self.__deck

    def getCurrentPlayerName(self):
        return self.__currentPlayerName

    def getCurrentPlayerChips(self):
        return self.__playerDict[self.__currentPlayerName].getChips()

    def getCurrentPlayerChipsStr(self):
        chips = self.getCurrentPlayerChips()
        return "%s chip%s" % (str(chips) if chips > 0 else "no",
                              "" if chips == 1 else "s")

    def getCurrnetPlayerCards(self):
        return self.__playerDict[self.__currentPlayerName].getCards()

    def getCurrentPlayerCardsStr(self):
        return self.__playerDict[self.__currentPlayerName].getOrderedCardStr()

    def getPlayerNames(self):
        return self.__playerOrderList

    def getCurrentCard(self):
        return self.__currentCard

    def getCurrentCardPath(self):
        return self.__currentCard.getPicPath()

    def getPlayerScoreList(self):
        scorelist = []
        for player in self.__playerDict.values():
            scorelist.append(player.getName() + ': ' + str(player.getScore()))
        return scorelist

    def getWinnerName(self):
        winner = ""
        currentPlayerScore = 1000
        for player in self.__playerDict.values():
            if player.getScore() < currentPlayerScore:
                winner = player.getName()
                currentPlayerScore = player.getScore()
        return winner

    def getCardsRemainingInDeck(self):
        return 24 - self.__deck.index(self.__currentCard)

    # ----- Predicates ----- #
    def cardsLeftInDeck(self):
        return self.__deck.index(self.__currentCard) < 23

    def currentPlayerHasChips(self):
        return self.getCurrentPlayerChips() > 0

    def lastCardInDeck(self):
        return self.__deck.index(self.__currentCard) == 23


# ---- Test ---- #
# def main():
#     g = Game(["p1", "p2", "p3", "p4"])
#     print("deck size:")
#     print(len(g.getDeck()))

#     print("player order:")
#     print(g.getPlayerNames())

#     print("deck:")
#     for card in g.getDeck():
#         print(card.getValue())

#     print("current card:")
#     cc = g.getCurrentCard()
#     print(cc.getValue())

#     g.CurrentPlayerAddCurrentCard()

#     print("next card:")
#     print(g.getCurrentCard().getValue())

#     print("current player has:")
#     print(g.getPlayerCards(g.getCurrentPlayerName()))

#     print("next player:")
#     print(g.getNextPlayerName())

# main()
# ----- End Test ----- #
