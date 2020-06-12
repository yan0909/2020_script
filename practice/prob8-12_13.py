from tkinter import *
class MainGUI:
    def check(self):  # 4개 연속인 것을 찾으면 X/O를 반환하고, 아니면 빈문자열 반환
        # 가로 4개 체크
        for i in range(6):  # 행과 열 가로/세로에 대해서 4개 연속 검사
            for j in range(4):  # col=0,1,2,3
                player = self.matrix[i][j]['text']  # i행의 4개 열이 연속인지 검사 (가로검사)
                if player != ' ' and player == self.matrix[i][j + 1]['text'] and player == self.matrix[i][j + 2]['text'] and player == self.matrix[i][j + 3]['text']:
                    return player
        # 세로 4개 체크
        for i in range(3):  # row=0,1,2
            for j in range(7):  # col=0,1,2,3
                player = self.matrix[i][j]['text']  # j열의 4개 행이 연속인지 검사 (가로검사)
                if player != ' ' and player == self.matrix[i + 1][j]['text'] and player == self.matrix[i + 2][j]['text'] and player == self.matrix[i + 3][j]['text']:
                    return player
        # 대각선검사 좌에서 우로
        for i in range(3):  # row=0,1,2
            for j in range(4):  # col=0,1,2,3:
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i + 1][j + 1]['text'] and player == self.matrix[i + 2][j + 2]['text'] and player == self.matrix[i + 3][j + 3]['text']:
                    return player
        # 대각선검사 우에서 좌로
        for i in range(3):  # row=0,1,2
            for j in range(4):  # col=3,4,5,6
                player = self.matrix[0][2]['text']
                if player != ' ' and player == self.matrix[i + 1][j - 1]['text'] and player == self.matrix[i + 2][j - 2]['text'] and player == self.matrix[i + 3][j - 3]['text']:
                    return player
        return ''
    def findRow(self, col):
        for row in range(5, -1, -1):  # row=5,4,3,2,1,0
            if self.matrix[row][col]['text'] == ' ':
                return row
        return 6
    def pressed(self, col):
        row = self.findRow(col)
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.isRturn:
                self.matrix[row][col]['image'] = self.imageR
                self.matrix[row][col]['text'] = '빨간색'
            else:
                self.matrix[row][col]['image'] = self.imageY
                self.matrix[row][col]['text'] = '노란색'
            self.isRturn = not self.isRturn
            if self.check() != '':
                self.done = True
                self.explain.set(self.check() + '이 이겼습니다.')
            elif self.isRturn:
                self.explain.set('빨간색 디스크 차례')
            else:
                self.explain.set('노란색 디스크 차례')

    def refresh(self):
        for i in range(6):
            for j in range(7):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.explain.set('빨간색 디스크 차례')
        self.isRturn = True
    def __init__(self):
        window = Tk()
        window.title('사목게임')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageR = PhotoImage(file='image/red.gif')
        self.imageY = PhotoImage(file='image/yellow.gif')
        self.imageE = PhotoImage(file='image/empty.gif')
        self.isRturn =True
        self.done = False
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                self.matrix[i].append(Button(frame, image=self.imageE, text=' ', \
                                             command=lambda col=j : self.pressed(col)))
                self.matrix[i][j].grid(row=i, column=j)
        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set("빨간색 디스크 차례")
        self.label = label = Label(frame1, textvariable=self.explain)
        self.label.pack(side=LEFT)
        Button(frame1, text='다시실행', command=self.refresh).pack(side=LEFT)



        window.mainloop()
MainGUI()