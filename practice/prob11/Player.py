class Player: 
    
    def __init__(self, name): 
        self.name = name 
        self.cards = [] 
        self.N = 0 
    
    def inHand(self): 
        return self.N 
        
    def addCard(self,c): 
        self.cards.append(c) 
        self.N += 1 
        
    def reset(self): 
        self.N = 0 
        self.cards.clear() 
        
    def value(self):    # ace 는 1 혹은 11 로 모두 사용 가능 
                        # 일단 11 로 계산한 후 21 이 넘어가면 1 로 정정
        sum = 0
        for card in self.cards:
            sum += card.getValue()
        return sum