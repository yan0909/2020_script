class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def GetCards(self):
        return self.cards

    def AddCard(self, card):
        self.cards.append(card)