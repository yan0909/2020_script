from tkinter import *
from tkinter import font
from Card import *
from Player import *
import inspect

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dori")
        self.window.geometry("800x600")
        self.window.configure(bg="green")

        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=11, weight='bold', family='Consolas')
        self.dealer = Player("dealer")
        self.player1 = Player("player1")
        self.player2 = Player("player2")
        self.player3 = Player("player3")

        self.SetupGUI()


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

        guiBtnBet1_5x = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2)
        guiBtnBet1_5x.place(x=x, y=y)
        x += stepX_little
        guiBtnBet1_1x = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2)
        guiBtnBet1_1x.place(x=x, y=y)
        x += stepX_big

        guiBtnBet2_5x = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2)
        guiBtnBet2_5x.place(x=x, y=y)
        x += stepX_little
        guiBtnBet2_1x = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2)
        guiBtnBet2_1x.place(x=x, y=y)
        x += stepX_big

        guiBtnBet3_5x = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2)
        guiBtnBet3_5x.place(x=x, y=y)
        x += stepX_little
        guiBtnBet3_1x = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2)
        guiBtnBet3_1x.place(x=x, y=y)
        x += stepX_big

        guiBtnDeal = Button(self.window, text='Deal', width=6, height=1, font=self.fontstyle2)
        guiBtnDeal.place(x=x, y=y)
        x += stepX_little * 1.3
        guiBtnAgain = Button(self.window, text='Again', width=6, height=1, font=self.fontstyle2)
        guiBtnAgain.place(x=x, y=y)


        # 베팅 금액
        guiLabelBet1 = Label(self.window, text='40만', font=self.fontstyle, bg='green', fg='cyan')
        guiLabelBet1.place(x=80, y=500)

        guiLabelBet2 = Label(self.window, text='40만', font=self.fontstyle, bg='green', fg='cyan')
        guiLabelBet2.place(x=260, y=500)

        guiLabelBet3 = Label(self.window, text='40만', font=self.fontstyle, bg='green', fg='cyan')
        guiLabelBet3.place(x=440, y=500)

        # 보유 금액
        guiLabelBet2 = Label(self.window, text='1130만', font=self.fontstyle, bg='green', fg='blue')
        guiLabelBet2.place(x=630, y=450)

        # 카드 이미지
        self.images = {}
        for i in range(10):
            for j in range(2):
                self.images[str(i+1) + '.' + str(j+1)] = PhotoImage(file= 'resource/doriCards/' + str(i+1) + '.' + str(j+1) + '.gif')
        self.images['back'] = PhotoImage(file= 'resource/doriCards/cardback.gif')

        x = 50
        y = 340
        cardStepX = 25

        guiImageCards_Player1 = []
        for i in range(5):
            p = self.images[str(i+1) + '.1']
            t = Label(self.window, image=p)
            t.image = p
            t.place(x=x + cardStepX * i, y=y)
            guiImageCards_Player1.append(t)
        x += 180

        guiImageCards_Player1[0].image=None

        guiImageCards_Player2 = []  
        for i in range(5):
            p = self.images[str(i+1) + '.1']
            t = Label(self.window, image=p)
            t.image = p
            t.place(x=x + cardStepX * i, y=y)
            guiImageCards_Player2.append(t)
        x += 180

        guiImageCards_Player3 = []
        for i in range(5):
            p = self.images[str(i+1) + '.1']
            t = Label(self.window, image=p)
            t.image = p
            t.place(x=x + cardStepX * i, y=y)
            guiImageCards_Player3.append(t)

        x = 230
        y = 90
        guiImageCards_Dealer = []
        for i in range(5):
            p = self.images[str(i+1) + '.1']
            t = Label(self.window, image=p)
            t.image = p
            t.place(x=x + cardStepX * i, y=y)
            guiImageCards_Dealer.append(t)


        # 카드 라벨
        x = 50 + 25
        y = 300
        stepX = 25
        guiLabelCardMonths_Player1 = []
        for i in range(5):
            t = Label(self.window, text='5', font=self.fontstyle2, bg='green', fg='white')
            t.place(x=x + stepX * i, y=y)
            guiLabelCardMonths_Player1.append(t)
        guiLabelCombo_Player1 = Label(self.window, text = '팍팍싸(8 8 4) 9땡', font=self.fontstyle3, bg='green', fg='cyan')
        guiLabelCombo_Player1.place(x=x, y=y-30)
        guiLabelResult_Player1 = Label(self.window, text='승', font=self.fontstyle, bg='green', fg='red')
        guiLabelResult_Player1.place(x=x-10, y=y-80)

        x = 50 + 25 + 180
        y = 300
        stepX = 25
        guiLabelCardMonths_Player2 = []
        for i in range(5):
            t = Label(self.window, text='5', font=self.fontstyle2, bg='green', fg='white')
            t.place(x=x + stepX * i, y=y)
            guiLabelCardMonths_Player2.append(t)
        guiLabelCombo_Player2 = Label(self.window, text = '팍팍싸(8 8 4) 9땡', font=self.fontstyle3, bg='green', fg='cyan')
        guiLabelCombo_Player2.place(x=x, y=y-30)
        guiLabelResult_Player2 = Label(self.window, text='승', font=self.fontstyle, bg='green', fg='red')
        guiLabelResult_Player2.place(x=x-10, y=y-80)

        x = 50 + 25 + 180 + 180
        y = 300
        stepX = 25
        guiLabelCardMonths_Player3 = []
        for i in range(5):
            t = Label(self.window, text='5', font=self.fontstyle2, bg='green', fg='white')
            t.place(x=x + stepX * i, y=y)
            guiLabelCardMonths_Player3.append(t)
        guiLabelCombo_Player3 = Label(self.window, text = '팍팍싸(8 8 4) 9땡', font=self.fontstyle3, bg='green', fg='cyan')
        guiLabelCombo_Player3.place(x=x, y=y-30)
        guiLabelResult_Player3 = Label(self.window, text='승', font=self.fontstyle, bg='green', fg='red')
        guiLabelResult_Player3.place(x=x-10, y=y-80)

        x = 50 + 25 + 180
        y = 50
        stepX = 25
        guiLabelCardMonths_Dealer = []
        for i in range(5):
            t = Label(self.window, text='5', font=self.fontstyle2, bg='green', fg='white')
            t.place(x=x + stepX * i, y=y)
            guiLabelCardMonths_Dealer.append(t)
        guiLabelCombo_Dealer = Label(self.window, text = '팍팍싸(8 8 4) 9땡', font=self.fontstyle3, bg='green', fg='cyan')
        guiLabelCombo_Dealer.place(x=x, y=y-30)



        pass

    # 콤보 텍스트 반환
    def GetComboString(self, combo):
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

        return '노메이드'

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

    pass

Game()