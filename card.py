class Card:

    def __init__(self, cardValue):
        self.__value = cardValue
        self.__chips = 0

    # ----------------------------
    # Mutators

    def addChip(self):
        return self.__chips + 1

    # ----------------------------
    # Accessors

    def getChips(self):
        return self.__chips

    def getValue(self):
        return self.__value
