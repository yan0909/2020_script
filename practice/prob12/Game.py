from tkinter import *
from tkinter import font
from Card import *
from Player import *
from Sound import *
import random

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dori")
        self.window.geometry("800x600")
        self.window.configure(bg="green")

        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=15, weight='bold', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=11, weight='bold', family='Consolas')

        self.sound = Sound()

        # 카드 이미지 + 월 + 조합 + 승패
        self.images = {}
        for i in range(10):
            for j in range(2):
                self.images[str(i+1) + '.' + str(j+1)] = PhotoImage(file= 'resource/doriCards/' + str(i+1) + '.' + str(j+1) + '.gif')
        self.images['back'] = PhotoImage(file= 'resource/doriCards/cardback.gif')

        self.dealer = Player("dealer")
        self.players = []
        self.players.append(Player("player1"))
        self.players.append(Player("player2"))
        self.players.append(Player("player3"))
        self.money = 1000

        self.SetupGUI()
        self.Initialize()

        l = []
        l.append(Card(16, isVisible=True))
        l.append(Card(18, isVisible=True))
        l.append(Card(0, isVisible=True))
        l.append(Card(3, isVisible=True))
        l.append(Card(7, isVisible=True))
        combos = self.GetCombos(l)
        print(combos)

        for combo in combos:
            print(self.GetComboString(combo))

        combos.sort(key= lambda x : x['power'], reverse=False)
        print(self.GetComboString(combos[0]))

        self.window.mainloop()

    def SetupGUI(self):

        # 베팅 버튼
        x = 50
        y = 550
        stepX_little = 70
        stepX_big = 110

        self.guiBtnBet1_5x = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2, command=self.OnClickedBtnBet1_5x)
        self.guiBtnBet1_5x.place(x=x, y=y)
        x += stepX_little
        self.guiBtnBet1_1x = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2, command=self.OnClickedBtnBet1_1x)
        self.guiBtnBet1_1x.place(x=x, y=y)
        x += stepX_big

        self.guiBtnBet2_5x = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2, command=self.OnClickedBtnBet2_5x)
        self.guiBtnBet2_5x.place(x=x, y=y)
        x += stepX_little
        self.guiBtnBet2_1x = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2, command=self.OnClickedBtnBet2_1x)
        self.guiBtnBet2_1x.place(x=x, y=y)
        x += stepX_big

        self.guiBtnBet3_5x = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2, command=self.OnClickedBtnBet3_5x)
        self.guiBtnBet3_5x.place(x=x, y=y)
        x += stepX_little
        self.guiBtnBet3_1x = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2, command=self.OnClickedBtnBet3_1x)
        self.guiBtnBet3_1x.place(x=x, y=y)
        x += stepX_big

        self.guiBtnDeal = Button(self.window, text='Deal', width=6, height=1, font=self.fontstyle2, command=self.OnClickedBtnDeal)
        self.guiBtnDeal.place(x=x, y=y)
        x += stepX_little * 1.3
        self.guiBtnAgain = Button(self.window, text='Again', width=6, height=1, font=self.fontstyle2, command=self.OnClickedBtnAgain)
        self.guiBtnAgain.place(x=x, y=y)


        # 베팅 금액
        self.guiLabelBet1 = Label(self.window, text='40만', font=self.fontstyle, bg='green', fg='cyan')
        self.guiLabelBet1.place(x=80, y=500)

        self.guiLabelBet2 = Label(self.window, text='40만', font=self.fontstyle, bg='green', fg='cyan')
        self.guiLabelBet2.place(x=260, y=500)

        self.guiLabelBet3 = Label(self.window, text='40만', font=self.fontstyle, bg='green', fg='cyan')
        self.guiLabelBet3.place(x=440, y=500)

        # 보유 금액
        self.guiLabelMoney = Label(self.window, text='1130만', font=self.fontstyle, bg='green', fg='blue')
        self.guiLabelMoney.place(x=630, y=450)



        self.guiImageCards = {} # 카드 이미지
        self.guiLabelMonths = {} # 월
        self.guiLabelCombos = {} # 조합명
        self.guiLabelResults = {} # 승패

        x = 50
        y = 340
        cardStepX = 25
        playerStepX = 180
        monthLabelOffsetX = 25
        monthLabelY = 300
        comboLabelY = 270
        resultLabelY = 230
        # 플레이어 x3
        for player in self.players:
            # 카드 이미지
            l = []
            for i in range(5):
                p = self.images[str(i+1) + '.1']
                t = Label(self.window, image=p)
                t.image = p
                t.place(x=x + cardStepX * i, y=y)
                l.append(t)
            self.guiImageCards[player] = l

            # 월, 조합명, 승패
            l = []
            for i in range(5):
                t = Label(self.window, text='5', font=self.fontstyle2, bg='green', fg='white')
                t.place(x=x + cardStepX * i + monthLabelOffsetX, y=monthLabelY)
                l.append(t)
            self.guiLabelMonths[player] = l
            self.guiLabelCombos[player] = Label(self.window, text = '팍팍싸(8 8 4) 9땡', font=self.fontstyle3, bg='green', fg='cyan')
            self.guiLabelCombos[player].place(x=x+monthLabelOffsetX, y=comboLabelY)
            self.guiLabelResults[player] = Label(self.window, text='승', font=self.fontstyle, bg='green', fg='red')
            self.guiLabelResults[player].place(x=x+monthLabelOffsetX-10, y=resultLabelY)

            x += playerStepX
        
        # 딜러
        x = 50 + playerStepX
        y = 90
        monthLabelY = 50
        comboLabelY = 20
        # 카드 이미지
        l = []
        for i in range(5):
            p = self.images[str(i+1) + '.1']
            t = Label(self.window, image=p)
            t.image = p
            t.place(x=x + cardStepX * i, y=y)
            l.append(t)
        self.guiImageCards[self.dealer] = l

        # 월, 조합명, 승패
        l = []
        for i in range(5):
            t = Label(self.window, text='5', font=self.fontstyle2, bg='green', fg='white')
            t.place(x=x + cardStepX * i + monthLabelOffsetX, y=monthLabelY)
            l.append(t)
        self.guiLabelMonths[self.dealer] = l
        self.guiLabelCombos[self.dealer] = Label(self.window, text = '팍팍싸(8 8 4) 9땡', font=self.fontstyle3, bg='green', fg='cyan')
        self.guiLabelCombos[self.dealer].place(x=x+monthLabelOffsetX, y=comboLabelY)


        pass

    def Initialize(self):
        self.turn = 0

        # 플레이어 패 제거
        for player in self.players + [self.dealer]:
            player.ClearCards()

        # 덱 셔플
        self.deck = [i for i in range(20)]
        self.deckN = 0
        random.shuffle(self.deck)

        # 베팅 머니 0원으로 초기화
        for e in self.players:
            e.SetBetMoney(0)

        # 딜, 어게인 버튼
        self.GuiSetActive(self.guiBtnDeal, True)
        self.GuiSetActive(self.guiBtnAgain, False)

        # 완성된 조합 초기화
        self.combos = {}
        for player in self.players + [self.dealer]:
            self.combos[player] = None
        
        self.UpdateGUI()
        pass

    def UpdateGUI(self):
        # self.guiBtnBet1_5x
        # self.guiBtnDeal
        # self.guiBtnAgain
        # self.guiImageCards_Player1
        # self.guiLabelCardMonths_Player1
        # self.guiLabelCombo_Player1
        # self.guiLabelResult_Player1

        # 베팅 버튼
        self.GuiSetActive( self.guiBtnBet1_1x, self.turn != 0 and self.turn != 3 and self.money >= 1 )
        self.GuiSetActive( self.guiBtnBet1_5x, self.turn != 0 and self.turn != 3 and self.money >= 5 )
        self.GuiSetActive( self.guiBtnBet2_1x, self.turn != 0 and self.turn != 3 and self.money >= 1 )
        self.GuiSetActive( self.guiBtnBet2_5x, self.turn != 0 and self.turn != 3 and self.money >= 5 )
        self.GuiSetActive( self.guiBtnBet3_1x, self.turn != 0 and self.turn != 3 and self.money >= 1 )
        self.GuiSetActive( self.guiBtnBet3_5x, self.turn != 0 and self.turn != 3 and self.money >= 5 )

        # 베팅 금액
        self.GuiSetText( self.guiLabelBet1, str(self.players[0].GetBetMoney()) + '만')
        self.GuiSetText( self.guiLabelBet2, str(self.players[1].GetBetMoney()) + '만')
        self.GuiSetText( self.guiLabelBet3, str(self.players[2].GetBetMoney()) + '만')

        # 잔액
        self.GuiSetText( self.guiLabelMoney, str(self.money) + '만')

        # Deal이랑 Again은 따로 처리
        # ...

        # 카드 이미지와 라벨
        # 플레이어 3명
        x = 50
        y = 340
        cardStepX = 25
        playerStepX = 180
        monthLabelOffsetX = 25
        monthLabelY = 300
        comboLabelY = 270
        resultLabelY = 230
        for player in self.players:
            thisCombo = self.combos[player]
            for i in range(5):
                card = player.GetCards()[i] if len(player.GetCards()) > i else None

                # 이미지 세팅 및 위치 세팅
                if( card != None ):
                    self.guiImageCards[player][i].configure( image = self.images[card.GetCardName()] )
                    self.guiImageCards[player][i].image =  self.images[card.GetCardName()]
                    self.guiImageCards[player][i].place(x= x + i * cardStepX, y = y + (20 if thisCombo != None and card in thisCombo['doriCombo'] else 0) )
                else:
                    self.guiImageCards[player][i].place(x=99999, y=99999)

                # 월 텍스트, 컬러 및 위치 세팅
                if( card != None ):
                    self.guiLabelMonths[player][i].configure(text = card.GetMonth(), fg= 'orange' if thisCombo != None and card in thisCombo['doriCombo'] else 'white')
                    self.guiLabelMonths[player][i].place(x= x + monthLabelOffsetX + i * cardStepX, y=monthLabelY)
                else:
                    self.guiLabelMonths[player][i].place(x=99999, y=99999)
                
            # 도리 정보 출력
            self.guiLabelCombos[player].configure(text= self.GetComboString(thisCombo) if self.turn == 3 else '')

            # 승패 정보 출력
            self.guiLabelResults[player].configure(text= '' if self.turn != 3 else ( '승' if self.IsStrongerCombo(self.combos[player], self.combos[self.dealer]) else '패' ) )

            x += playerStepX

        # 딜러
        x = 50 + playerStepX
        y = 90
        monthLabelY = 50
        comboLabelY = 20
        thisCombo = self.combos[self.dealer]
        for i in range(5):
            card = self.dealer.GetCards()[i] if len(self.dealer.GetCards()) > i else None

            # 이미지 세팅 및 위치 세팅
            if( card != None ):
                self.guiImageCards[self.dealer][i].configure( image =  self.images[card.GetCardName()] )
                self.guiImageCards[self.dealer][i].image =  self.images[card.GetCardName()]
                self.guiImageCards[self.dealer][i].place(x= x + i * cardStepX, y = y + (20 if thisCombo != None and card in thisCombo['doriCombo'] else 0) )
            else:
                self.guiImageCards[self.dealer][i].place(x=99999, y=99999)

            # 월 텍스트, 컬러 및 위치 세팅
            if( card != None and self.turn == 3 ):
                self.guiLabelMonths[self.dealer][i].configure(text = card.GetMonth(), fg= 'orange' if thisCombo != None and card in thisCombo['doriCombo'] else 'white')
                self.guiLabelMonths[self.dealer][i].place(x= x + monthLabelOffsetX + i * cardStepX, y=monthLabelY)
            else:
                self.guiLabelMonths[self.dealer][i].place(x=99999, y=99999)
            
        # 도리 정보 출력
        self.guiLabelCombos[self.dealer].configure(text= self.GetComboString(thisCombo) if self.turn == 3 else '')


    def OnClickedBtnDeal(self):
        self.turn += 1

        if( self.turn == 1 ): # 카드 한장씩 배부
            for player in self.players:
                player.AddCard( self.DrawCard(isVisible=True) )
            self.dealer.AddCard( self.DrawCard(isVisible=False) )
        elif( self.turn == 2 ): # 카드 세장 더 배부
            for i in range(3):
                for player in self.players:
                    player.AddCard( self.DrawCard(isVisible=True) )
                self.dealer.AddCard( self.DrawCard(isVisible=False) )
        elif(self.turn == 3 ): # 카드 한장씩 더 배부한 후 결과 산출
            for player in self.players:
                player.AddCard( self.DrawCard(isVisible=True) )
            self.dealer.AddCard( self.DrawCard(isVisible=False) )

            # 딜러의 패 공개
            for card in self.dealer.GetCards():
                card.SetVisible(True)

            # 조합 결정
            for player in self.players + [self.dealer]:
                combos = self.GetCombos(player.GetCards()) # 가능한 조합 산출
                if( len(combos) == 0 ): # 노메이드인 경우
                    self.combos[player] = None
                else:
                    combos.sort(key= lambda x : x['power'], reverse=False) # 파워 순으로 정렬
                    self.combos[player] = combos[0] # 가장 강한 조합 사용
                
                print('조합 : ' + self.GetComboString(self.combos[player]))
            
            # 돈 계산
            for player in self.players:
                if( self.IsStrongerCombo(self.combos[player], self.combos[self.dealer]) ):
                    self.money += player.GetBetMoney() * 2

            self.GuiSetActive(self.guiBtnAgain, True)

        self.GuiSetActive(self.guiBtnDeal, False)    

        self.UpdateGUI()
        if( self.turn == 3):
            self.PlaySound(Sound.SFX.WIN)
        else:
            self.PlaySound(Sound.SFX.DEAL)

    def OnClickedBtnAgain(self):
        self.Initialize()
        self.PlaySound(Sound.SFX.AGAIN)

    def OnClickedBtnBet1_5x(self):
        self.players[0].AddBetMoney(5)
        self.money -= 5
        self.GuiSetActive(self.guiBtnDeal, True)
        self.UpdateGUI()
        self.PlaySound(Sound.SFX.BET)
    def OnClickedBtnBet1_1x(self):
        self.players[0].AddBetMoney(1)
        self.money -= 1
        self.GuiSetActive(self.guiBtnDeal, True)
        self.UpdateGUI()
        self.PlaySound(Sound.SFX.BET)
    def OnClickedBtnBet2_5x(self):
        self.players[1].AddBetMoney(5)
        self.money -= 5
        self.GuiSetActive(self.guiBtnDeal, True)
        self.UpdateGUI()
        self.PlaySound(Sound.SFX.BET)
    def OnClickedBtnBet2_1x(self):
        self.players[1].AddBetMoney(1)
        self.money -= 1
        self.GuiSetActive(self.guiBtnDeal, True)
        self.UpdateGUI()
        self.PlaySound(Sound.SFX.BET)
    def OnClickedBtnBet3_5x(self):
        self.players[2].AddBetMoney(5)
        self.money -= 5
        self.GuiSetActive(self.guiBtnDeal, True)
        self.UpdateGUI()
        self.PlaySound(Sound.SFX.BET)
    def OnClickedBtnBet3_1x(self):
        self.players[2].AddBetMoney(1)
        self.money -= 1
        self.GuiSetActive(self.guiBtnDeal, True)
        self.UpdateGUI()
        self.PlaySound(Sound.SFX.BET)

    def DrawCard(self, isVisible):
        cardIndex = self.deck[self.deckN]
        self.deckN += 1
        return Card(cardIndex, isVisible)

    def IsStrongerCombo(self, mine, opponent):
        if(mine == None):
            return False
        if(opponent == None):
            return True
        return mine['power'] < opponent['power']

    # 콤보 텍스트 반환
    def GetComboString(self, combo):
        if( combo == None ):
            return '노메이드'
        return self.GetDoriName( combo['doriCombo'] ) + ' ' + self.GetPowerName( combo['power'] )

    # 가능한 도리짓기 조합 리스트를 인덱스로 반환한다. 형태 : [set(1,2,3), set(1,3,5)]
    def GetDoriCombos(self, cards):
        combos = []
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    if( (cards[i].GetMonth() + cards[j].GetMonth() + cards[k].GetMonth()) % 10 == 0 ): # 세 종류를 더했을 때 10의 배수인가.
                        combos.append( set([i, j, k]) )
        return combos

    # 족보를 찾아 반환
    def GetComboPower(self, cards):
        if( type(cards) == set ):
            cards = [i for i in cards]
        cards.sort(key= lambda x : x.GetMonth()) # 월 기준으로 정렬

        a = cards[0].GetCardIndex()
        b = cards[1].GetCardIndex()
        aMon = cards[0].GetMonth()
        bMon = cards[1].GetMonth()
        end = (aMon + bMon) % 10 # 끗

        if(a == 2 and b == 7):
            return Card.삼팔광땡
        if(a == 0 and b == 7):
            return Card.일팔광땡
        if(a == 0 and b == 2):
            return Card.일삼광땡
        if(aMon == bMon): # 땡 종류
            if(aMon == 10):
                return Card.장땡
            if(aMon == 9):
                return Card.구땡
            if(aMon == 8):
                return Card.팔땡
            if(aMon == 7):
                return Card.칠땡
            if(aMon == 6):
                return Card.육땡
            if(aMon == 5):
                return Card.오땡
            if(aMon == 4):
                return Card.사땡
            if(aMon == 3):
                return Card.삼땡
            if(aMon == 2):
                return Card.이땡
            if(aMon == 1):
                return Card.삥땡
        if(aMon == 1 and bMon == 2): 
            return Card.알리
        if(aMon == 1 and bMon == 4): 
            return Card.독사
        if(aMon == 1 and bMon == 9): 
            return Card.구삥
        if(aMon == 1 and bMon == 10): 
            return Card.장삥
        if(aMon == 4 and bMon == 10): 
            return Card.장사
        if(aMon == 4 and bMon == 6): 
            return Card.세륙
        if(aMon == 3 and bMon == 7): 
            return Card.땡잡이
        if(aMon == 4 and bMon == 9): 
            return Card.구사
        if(a == 3 and b == 8): 
            return Card.멍텅구리구사
        if(end == 9): 
            return Card.갑오
        if(end == 8): 
            return Card.여덟끗
        if(end == 7): 
            return Card.일곱끗
        if(end == 6): 
            return Card.여섯끗
        if(end == 5): 
            return Card.다섯끗
        if(end == 4): 
            return Card.네끗
        if(end == 3): 
            return Card.세끗
        if(end == 2): 
            return Card.두끗
        if(end == 1): 
            return Card.한끗
        if(end == 0): 
            return Card.망통

        print('카드 조합 버그 : ' + str(a) + ' ' + str(b))
        return Card.망통

    # 도리짓기 조합의 이름 반환
    def GetDoriName(self, doriCards):
        if(doriCards == None):
            return '노메이드'

        doriCards.sort(key= lambda x : x.GetMonth())

        nameDic = {}
        nameDic[ (1, 1, 8) ] = '콩콩팔(1 1 8)'
        nameDic[ (1, 2, 7) ] = '삐리칠(1 2 7)'
        nameDic[ (1, 3, 6) ] = '물삼육(1 3 6)'
        nameDic[ (1, 4, 5) ] = '삥새오(1 4 5)'
        nameDic[ (1, 9, 10) ] = '삥구장(1 9 10)'
        nameDic[ (2, 2, 6) ] = '니니육(2 2 6)'
        nameDic[ (2, 3, 5) ] = '이삼오(2 3 5)'
        nameDic[ (2, 8, 10) ] = '이판장(2 8 10)'
        nameDic[ (3, 3, 4) ] = '삼삼새(3 3 4)'
        nameDic[ (3, 7, 10) ] = '삼칠장(3 7 10)'
        nameDic[ (3, 8, 9) ] = '삼빡구(3 8 9)'
        nameDic[ (4, 4, 2) ] = '살살이(4 4 2)'
        nameDic[ (4, 6, 10) ] = '사륙장(4 6 10)'
        nameDic[ (4, 7, 9) ] = '사칠구(4 7 9)'
        nameDic[ (5, 5, 10) ] = '꼬꼬장(5 5 10)'
        nameDic[ (5, 6, 9) ] = '오륙구(5 6 9)'
        nameDic[ (5, 7, 8) ] = '오천평(5 7 8)'
        nameDic[ (6, 6, 8) ] = '쭉쭉팔(6 6 8)'
        nameDic[ (7, 7, 6) ] = '칠칠육(7 7 6)'
        nameDic[ (8, 8, 4) ] = '팍팍싸(8 8 4)'
        nameDic[ (9, 9, 2) ] = '구구리(9 9 2)'

        a = doriCards[0].GetMonth()
        b = doriCards[1].GetMonth()
        c = doriCards[2].GetMonth()
        tup = (a, b, c)

        if( tup in nameDic ):
            return nameDic[ tup ]

        return '노메이드'

    # 조합의 이름 반환
    def GetPowerName(self, power):
        if(power == None ):
            return ''

        if(power == Card.삼팔광땡):
            return '삼팔광땡'
        if(power == Card.일팔광땡):
            return '일팔광땡'
        if(power == Card.일삼광땡):
            return '일삼광땡'
        if(power == Card.장땡):
            return '장땡'
        if(power == Card.구땡):
            return '구땡'
        if(power == Card.팔땡):
            return '팔땡'
        if(power == Card.칠땡):
            return '칠땡'
        if(power == Card.육땡):
            return '육땡'
        if(power == Card.오땡):
            return '오땡'
        if(power == Card.사땡):
            return '사땡'
        if(power == Card.삼땡):
            return '삼땡'
        if(power == Card.이땡):
            return '이땡'
        if(power == Card.삥땡):
            return '삥땡'
        if(power == Card.알리):
            return '알리'
        if(power == Card.독사):
            return '독사'
        if(power == Card.구삥):
            return '구삥'
        if(power == Card.장삥):
            return '장삥'
        if(power == Card.장사):
            return '장사'
        if(power == Card.세륙):
            return '세륙'
        if(power == Card.갑오):
            return '갑오'
        if(power == Card.여덟끗):
            return '여덟끗'
        if(power == Card.일곱끗):
            return '일곱끗'
        if(power == Card.여섯끗):
            return '여섯끗'
        if(power == Card.다섯끗):
            return '다섯끗'
        if(power == Card.네끗):
            return '네끗'
        if(power == Card.세끗):
            return '세끗'
        if(power == Card.두끗):
            return '두끗'
        if(power == Card.한끗):
            return '한끗'
        if(power == Card.망통):
            return '망통'
        if(power == Card.땡잡이):
            return '땡잡이'
        if(power == Card.구사):
            return '구사'
        if(power == Card.멍텅구리구사):
            return '멍텅구리구사'

        return '#버그#'

    # 도리를 짓고 족보를 찾아 리스트로 반환한다. 형태 : [{'doriCombo': [Card, Card, Card]], 'power': Card.팔땡}, {'doriCombo': [Card, Card, Card], 'power': Card.구사}]
    def GetCombos(self, cards):
        pattern = []
        allCardSet = set([0, 1, 2, 3, 4])
        
        for doriCombo in self.GetDoriCombos(cards): # 도리짓기 조합 리스트
            comboCards = [cards[i] for i in allCardSet - doriCombo]
            power = self.GetComboPower(comboCards)
            pattern.append( {'doriCombo': [cards[doriIndex] for doriIndex in doriCombo], 'power': power} )
            pass    
        
        return pattern

    # GUI 버튼 액티브 제어
    def GuiSetActive(self, control, isActive):
        control['state'] = 'active' if( isActive == True ) else 'disabled'
        control['bg'] = 'white' if( isActive == True ) else 'gray'

    # GUI 버튼 텍스트 제어
    def GuiSetText(self, control, text):
        control.configure(text= text)

    # GUI 이미지 제어
    def GuiSetImage(self, control, p):
        control.configure(image = p)
        control.image = p
    
    def PlaySound(self, sfx):
        self.sound.PlaySound(sfx)
        pass

    pass

Game()