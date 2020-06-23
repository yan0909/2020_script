class Card:
    삼팔광땡 = 1
    일팔광땡 = 2
    일삼광땡 = 3
    장땡 = 4
    구땡 = 5
    팔땡 = 6
    칠땡 = 7
    육땡 = 8
    오땡 = 9
    사땡 = 10
    삼땡 = 11
    이땡 = 12
    삥땡 = 13
    알리 = 14
    독사 = 15
    구삥 = 16
    장삥 = 17
    장사 = 18
    세륙 = 19
    갑오 = 20
    여덟끗 = 21
    일곱끗 = 22
    여섯끗 = 23
    다섯끗 = 24
    네끗 = 25
    세끗 = 26
    두끗 = 27
    한끗 = 28
    망통 = 29

    # 특수 족보 #
    땡잡이 = 30
    구사 = 31
    멍텅구리구사 = 32
    
    노메이드 = 100


    def __init__(self, cardIndex, isVisible = False):
        self.month = cardIndex % 10 + 1
        self.index = cardIndex // 10 + 1
        self.isVisible = isVisible

    def GetMonth(self):
        return self.month

    def GetIndex(self):
        return self.index

    def GetCardIndex(self):
        return (self.index - 1) * 10 + self.month - 1

    def SetVisible(self, isVisible):
        self.isVisible = isVisible

    def GetCardName(self):
        if( not self.isVisible ):
            return 'back'
        return str(self.month) + '.' + str(self.index)

    def __eq__(self, other):
        if( other == None ):
            return False
        return self.GetCardIndex() == other.GetCardIndex()

    def __str__(self):
        return str(self.month) + '월_' + str(self.index)

    def __repr__(self):
        return str(self)