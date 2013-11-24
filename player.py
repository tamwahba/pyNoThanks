class Player:
    """docstring for  Player"""
    def __init__(self, playerName):
        self.__name = playerName
        self.__cardList = []
        self.__chips = 11

    # -------------------------------
    # Accessors

    def getCards(self):
        return self.__cardList
    
    def getChips(self):
        return self.__chips

    def getName(self):
        return self.__playerName

    def getSortedList(self, cardList):
        self.__cardList.sort()
        return self.__cardList

    # -------------------------------
    # 'toString'

    def __str__(self):
        return list(self.__cardList)

