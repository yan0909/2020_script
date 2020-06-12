import random
from tkinter import *
class MainGUI:
    def toString(self, guessWord):
        result =''
        for ch in guessWord:
            result += ch
        return result
    def drawHangman(self):
        self.canvas.delete('hangman')
        self.canvas.create_arc(20, 200, 20+80, 200+40, start=0, extent=180) #아크 베이스
        self.canvas.create_line(20+40, 200, 20+40, 20)                      #폴대
        self.canvas.create_line(20+40, 20, 20+40+100, 20)                   #행거

        if self.doneWithWrong:  #7번 틀린 경우
            self.canvas.create_text(200, 250, text='정답' + self.toString(self.hiddenWord), font='Times 14', tag='hangman')
            self.canvas.create_text(200, 270, text='계속하려면 ENTER', font='Times 14', tags='hangman')
        elif self.doneWithCorrect:  #정답을 맞춘 경우
            self.canvas.create_text(200, 250, text='맞았습니다.' + self.toString(self.hiddenWord), font='Times 14', tag='hangman')
            self.canvas.create_text(200, 270, text='계속하려면 ENTER', font='Times 14', tags='hangman')
        else:
            self.canvas.create_text(200, 250, text='단어 추측'+self.toString(self.guessWord), font='Times 14', tag='hangman')
            if self.NumOfMiss > 0:
                self.canvas.create_text(200, 270, text='틀린 글자'+self.toString(self.missChars), font='Times 14', tags='hangman')
        if self.NumOfMiss < 1:
            return
        x1 = 20 + 40 + 100
        y1 = 20
        x2 = x1
        y2 = y1 + 20
        self.canvas.create_line(x1 ,y1, x2, y2, tags='hangman')             #행거

        if self.NumOfMiss < 2:
            return
        x3 = x2
        y3 = y2 + 20
        self.canvas.create_oval(x3-20, y3-20, x3+20, y3+20, tags='hangman') #머리

        if self.NumOfMiss < 3:
            return
        self.canvas.create_line(x3-15, y3+15, x3-50, y3+60, tags='hangman')       #왼팔

        if self.NumOfMiss < 4:
            return
        self.canvas.create_line(x3+15, y3+15, x3+50, y3+60, tags='hangman')       #오른팔

        if self.NumOfMiss < 5:
            return
        x4 = x3
        y4 = y3 + 100
        self.canvas.create_line(x3, y3+20, x4, y4, tags='hangman')       #몸통

        if self.NumOfMiss < 6:
            return
        self.canvas.create_line(x4, y4, x4-50, y4+70, tags='hangman')       #왼발

        if self.NumOfMiss < 7:
            return
        self.canvas.create_line(x4, y4, x4+50, y4+70, tags='hangman')       #왼발


    def setWord(self):
        index = random.randint(0, len(self.words)-1)
        self.hiddenWord = self.words[index]
        self.guessWord = ['*']*len(self.hiddenWord)
        self.NumOfCorrectChar = 0
        self.NumOfMiss = 0
        self.missChars = []
        self.doneWithWrong = False
        self.doneWithCorrect = False
    def KeyEvent(self, Key):
        if 'a' <= Key.char <= 'z':
            if Key.char in self.guessWord:
                print('\t', Key.char, '은/는 이미 포함되어 있습니다.')
            elif self.hiddenWord.find(Key.char) == -1:  # 리스트의 find 함수는 검색해서 찾으면 인덱스를 반환g
                print('\t', Key.char, '은/는 포함되어 있지 않습니다.')  # 못찾으면 -1 반환
                self.NumOfMiss += 1
                if not Key.char in self.missChars:
                    self.missChars.append(Key.char)
                if self.NumOfMiss == 7:
                    self.doneWithWrong = True   #7번 틀리고 못맞추고 종료
            else:
                k = self.hiddenWord.find(Key.char)
                while k >= 0:
                    self.guessWord[k] = Key.char
                    self.NumOfCorrectChar += 1
                    k = self.hiddenWord.find(Key.char, k + 1)
                if self.NumOfCorrectChar == len(self.hiddenWord):
                    self.doneWithCorrect = True #다 찾고 종료
        elif Key.keycode == 13:    #ENTER 입력 key cod == 13
            if self.doneWithCorrect or self.doneWithWrong:
                self.setWord()
                self.drawHangman()
        self.drawHangman()
    def __init__(self):
        fp = open('hangman.txt')
        self.words = fp.read().split()
        window = Tk()
        window.title('행맨 게임')
        self.canvas = Canvas(window, bg='white', width=400, height=300)
        self.canvas.pack()
        self.setWord()
        self.drawHangman()

        #Canvas key 입력에 대한 이벤트 bind
        self.canvas.bind('<Key>', self.KeyEvent)
        self.canvas.focus_set()

        window.mainloop()
MainGUI()