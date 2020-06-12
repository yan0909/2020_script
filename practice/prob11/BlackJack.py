from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random

class BlackJack: 
    def __init__(self): 
        self.window = Tk() 
        self.window.title("Black Jack") 
        self.window.geometry("800x600") 
        self.window.configure(bg="green")        
        
        bgP = PhotoImage(file="cards/table.gif")
        bgImage = Label(self.window, image=bgP)
        bgImage.pack()

        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas') 
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas') 
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.playerMoney = 1000 
        self.initialize()
        
        self.window.mainloop()

    def setupButton(self): 
        self.B50 = Button(self.window,text="Bet 50", width=6,height=1, font=self.fontstyle2,command=self.pressedB50) 
        self.B50.place(x=50,y=500)
        self.B10 = Button(self.window,text="Bet 10", width=6,height=1, font=self.fontstyle2,command=self.pressedB10) 
        self.B10.place(x=150,y=500) 
        self.B1 = Button(self.window,text="Bet 1", width=6,height=1, font=self.fontstyle2,command=self.pressedB1) 
        self.B1.place(x=250,y=500) 
        self.Hit = Button(self.window,text="Hit", width=6,height=1, font=self.fontstyle2,command=self.pressedHit) 
        self.Hit.place(x=400,y=500) 
        self.Stay = Button(self.window,text="Stay", width=6,height=1, font=self.fontstyle2,command=self.pressedStay) 
        self.Stay.place(x=500,y=500) 
        self.Deal = Button(self.window,text="Deal", width=6,height=1, font=self.fontstyle2,command=self.pressedDeal) 
        self.Deal.place(x=600,y=500) 
        self.Again = Button(self.window,text="Again", width=6,height=1, font=self.fontstyle2,command=self.pressedAgain) 
        self.Again.place(x=700,y=500)
        self.Hit['state'] = 'disabled' 
        self.Hit['bg'] = 'gray' 
        self.Stay['state'] = 'disabled' 
        self.Stay['bg'] = 'gray' 
        self.Deal['state'] = 'disabled' 
        self.Deal['bg'] = 'gray' 
        self.Again['state'] = 'disabled' 
        self.Again['bg'] = 'gray'

    def initialize(self):        
        self.betMoney = 0 
        self.nCardsDealer = 0 
        self.nCardsPlayer = 0 
        self.LcardsPlayer = [] 
        self.LcardsDealer = [] 
        self.deckN = 0
        self.player.reset()
        self.dealer.reset()
        self.setupButton() 
        self.setupLabel()

    def pressedStay(self):
        self.checkWinner()

    def pressedDeal(self):
        self.deal()

    def pressedAgain(self):
        for Lcard in self.LcardsPlayer + self.LcardsDealer:
            Lcard.destroy()
        self.initialize()


    def setupLabel(self): 
        self.LbetMoney = Label(text="$0",width=4,height=1,font=self.fontstyle,bg="green",fg="cyan") 
        self.LbetMoney.place(x=200,y=450) 
        self.LplayerMoney = Label(text="You have $" + str(self.playerMoney),width=15,height=1,font=self.fontstyle,bg="green",fg="cyan") 
        self.LplayerMoney.place(x=500,y=450) 
        self.LplayerPts = Label(text="",width=2,height=1,font=self.fontstyle2,bg="green",fg="white") 
        self.LplayerPts.place(x=300,y=300) 
        self.LdealerPts = Label(text="",width=2,height=1,font=self.fontstyle2,bg="green",fg="white") 
        self.LdealerPts.place(x=300,y=100) 
        self.Lstatus = Label(text="",width=15,height=1,font=self.fontstyle,bg="green",fg="white") 
        self.Lstatus.place(x=500,y=300)

    def pressedB50(self): 
        self.betMoney += 50 
        if self.betMoney <= self.playerMoney: 
            self.LbetMoney.configure(text="$"+str(self.betMoney)) 
            self.playerMoney -=50 
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney)) 
            self.Deal["state"] = "active" 
            self.Deal["bg"] = "white" 
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else: 
            self.betMoney -= 50

    def pressedB10(self): 
        self.betMoney += 10 
        if self.betMoney <= self.playerMoney: 
            self.LbetMoney.configure(text="$"+str(self.betMoney)) 
            self.playerMoney -=10 
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney)) 
            self.Deal["state"] = "active" 
            self.Deal["bg"] = "white" 
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else: 
            self.betMoney -= 10

    def pressedB1(self): 
        self.betMoney += 1 
        if self.betMoney <= self.playerMoney: 
            self.LbetMoney.configure(text="$"+str(self.betMoney)) 
            self.playerMoney -=1 
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney)) 
            self.Deal["state"] = "active" 
            self.Deal["bg"] = "white" 
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else: 
            self.betMoney -= 1
    
    def deal(self): 
        self.player.reset() 
        self.dealer.reset() # 카드 덱 52 장 셔플링 0,1,,.51 
        self.cardDeck = [i for i in range(52)] 
        random.shuffle(self.cardDeck) 
        self.deckN = 0
        self.hitPlayer(0) 
        self.hitDealerDown() 
        self.hitPlayer(1) 
        self.hitDealer(1) 
        self.nCardsPlayer = 1 
        self.nCardsDealer = 1
        self.B50['state'] = 'disabled' 
        self.B50['bg'] = 'gray' 
        self.B10['state'] = 'disabled' 
        self.B10['bg'] = 'gray' 
        self.B1['state'] = 'disabled' 
        self.B1['bg'] = 'gray'

        self.Hit['state'] = 'active' 
        self.Hit['bg'] = 'white' 
        self.Stay['state'] = 'active' 
        self.Stay['bg'] = 'white' 
        self.Deal['state'] = 'disabled' 
        self.Deal['bg'] = 'gray' 
        self.Again['state'] = 'disabled' 
        self.Again['bg'] = 'gray'

    def hitPlayer(self, n): 
        newCard = Card(self.cardDeck[self.deckN]) 
        self.deckN += 1 
        self.player.addCard(newCard) 
        p = PhotoImage(file="cards/"+newCard.filename()) 
        self.LcardsPlayer.append(Label(self.window,image=p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임 
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=250+n*30,y=350)
        self.LplayerPts.configure(text=str(self.player.value())) 
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealer(self, n, isVisible = True): 
        newCard = Card(self.cardDeck[self.deckN], isVisible=isVisible) 
        self.deckN += 1 
        self.dealer.addCard(newCard)
        if(isVisible):
            p = PhotoImage(file="cards/"+newCard.filename()) 
        else:
            p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window,image=p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임 
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250+n*30,y=150)
        # self.LdealerPts.configure(text=str(self.dealer.value())) 
        # PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealerDown(self):
        self.hitDealer(self.dealer.inHand(), isVisible=False)

    def pressedHit(self): 
        self.nCardsPlayer += 1 
        self.hitPlayer(self.nCardsPlayer) 
        if self.player.value() > 21: 
            self.checkWinner()

    def checkWinner(self): 
        # 뒤집힌 카드를 다시 그린다 . 
        p = PhotoImage(file="cards/"+self.dealer.cards[0].filename()) 
        self.LcardsDealer[0].configure(image = p) # 이미지 레퍼런스 변경 
        self.LcardsDealer[0].image=p # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        while(self.dealer.value() < 17):
            self.hitDealer(self.dealer.inHand())

        self.LdealerPts.configure(text=str(self.dealer.value()))
        if self.player.value() > 21: 
            self.Lstatus.configure(text="Player Busts") 
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        elif self.dealer.value() > 21: 
            self.Lstatus.configure(text="Dealer Busts") 
            self.playerMoney += self.betMoney*2 
            PlaySound('sounds/win.wav', SND_FILENAME) 
        elif self.dealer.value() == self.player.value(): 
            self.Lstatus.configure(text="Push") 
            self.playerMoney += self.betMoney 
        elif self.dealer.value() < self.player.value(): 
            self.Lstatus.configure(text="You won!!") 
            self.playerMoney += self.betMoney*2 
            PlaySound('sounds/win.wav', SND_FILENAME) 
        else: 
            self.Lstatus.configure(text="Sorry you lost!") 
            PlaySound('sounds/wrong.wav', SND_FILENAME)

        self.betMoney = 0 
        self.LplayerMoney.configure(text="You have $"+str(self.playerMoney)) 
        self.LbetMoney.configure(text="$"+str(self.betMoney))
        self.B50['state'] = 'disabled' 
        self.B50['bg'] = 'gray' 
        self.B10['state'] = 'disabled' 
        self.B10['bg'] = 'gray' 
        self.B1['state'] = 'disabled' 
        self.B1['bg'] = 'gray' 
        self.Hit['state'] = 'disabled' 
        self.Hit['bg'] = 'gray' 
        self.Stay['state'] = 'disabled' 
        self.Stay['bg'] = 'gray' 
        self.Deal['state'] = 'disabled' 
        self.Deal['bg'] = 'gray' 
        self.Again['state'] = 'active' 
        self.Again['bg'] = 'white'






BlackJack()

