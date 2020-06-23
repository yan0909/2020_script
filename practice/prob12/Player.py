class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.betMoney = 0

    def GetCards(self):
        return self.cards

    def AddCard(self, card):
        self.cards.append(card)
    
    def AddBetMoney(self, bet):
        self.betMoney += bet

    def GetBetMoney(self):
        return self.betMoney

    def SetBetMoney(self, bet):
        self.betMoney = bet