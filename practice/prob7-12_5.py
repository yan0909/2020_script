from tkinter import *
class MainGUI:
    def check(self):  # 3개 연속인 것을 찾으면 X/O를 반환하고, 아니면 빈문자열 반환
        for i in range(3):  # 행과 열 가로/세로에 대해서 3개 연속 검사
            player = self.matrix[i][0]['text']  # i행의 3개 열이 3개 연속인지 검사 (가로검사)
            if player != ' ' and player == self.matrix[i][1]['text'] and player == self.matrix[i][2]['text']:
                return player
            player = self.matrix[0][i]['text']  # i열의 3개 행이 3개 연속인지 검사 (세로검사)
            if player != ' ' and player == self.matrix[1][i]['text'] and player == self.matrix[2][i]['text']:
                return player
        # 대각선검사
        player = self.matrix[0][0]['text']
        if player != ' ' and player == self.matrix[1][1]['text'] and player == self.matrix[2][2]['text']:
            return player
        player = self.matrix[2][2]['text']
        if player != ' ' and player == self.matrix[1][1]['text'] and player == self.matrix[2][0]['text']:
            return player
        return ''
    def pressed(self, row, col):
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.isXturn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'X'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'O'
            self.isXturn = not self.isXturn
            if self.check() != '':
                self.done = True
                self.explain.set('플레이어' + self.check() + '가 이겼습니다.')
            elif self.isXturn:
                self.explain.set('플레이어 X 차례')
            else:
                self.explain.set('플레이어 O 차례')

    def refresh(self):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.explain.set('플레이어 X 차례')
        self.isXturn = True
    def __init__(self):
        window = Tk()
        window.title('틱택토')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='image/x.gif')
        self.imageO = PhotoImage(file='image/o.gif')
        self.imageE = PhotoImage(file='image/empty.gif')
        self.isXturn =True
        self.done = False
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append(Button(frame, image=self.imageE, text=' ', \
                                             command=lambda row=i,col=j : self.pressed(row,col)))
                self.matrix[i][j].grid(row=i, column=j)
        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set("플레이어 X 차례")
        self.label = Label(frame1, textvariable=self.explain)
        self.label.pack(side=LEFT)
        Button(frame1, text='다시실행', command=self.refresh).pack(side=LEFT)



        window.mainloop()
MainGUI()