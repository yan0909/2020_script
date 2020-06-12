from tkinter import *
from random import *
from tkinter.simpledialog import *

width = 800
height = 600
barWidth = (width-20) / 20  # 1개의 막대그래프의 너비
class MainGUI:
    def next(self):
        if self.current < 20:
            indexMin = self.current
            for i in range(self.current+1, 20):
                if self.counts[indexMin] > self.counts[i]:
                    indexMin = i
            self.counts[self.current], self.counts[indexMin] = self.counts[indexMin], self.counts[self.current]   # swap

            self.canvas.delete('current_bar')
            self.canvas.delete('histogram')
            for i in range(20):
                self.canvas.create_rectangle(10 + i * barWidth, height - (height - 10) * self.counts[i] / self.maxCount,
                                             10 + (i + 1) * barWidth, height - 10, tags='histogram')

                self.canvas.create_text(10 + i * barWidth + 10, height - (height-10)*self.counts[i] / self.maxCount - 5,
                                        text=str(self.counts[i]), tags='histogram')
            self.canvas.create_rectangle(10 + self.current * barWidth,
                                         height - (height - 10) * self.counts[self.current] / self.maxCount,
                                         10 + (self.current + 1) * barWidth, height - 10, fill='red',
                                         tags='current_bar')
            if (self.counts[self.current] == 20):
                messagebox.showinfo("정렬 끝")
            else:
                self.current += 1
    def reGen(self):
        self.canvas.delete('histogram')
        self.counts = [x for x in range(1,21)]   # [1,2,3,...,20]
        shuffle(self.counts)
        self.current = 0

        self.maxCount = max(self.counts)
        for i in range(20):
            self.canvas.create_rectangle(10+i*barWidth, height - (height-10)*self.counts[i] / self.maxCount,
                                         10+(i+1)*barWidth, height-10, tags='histogram')

            self.canvas.create_text(10 + i * barWidth + 10, height - (height-10)*self.counts[i] / self.maxCount - 5, text=str(self.counts[i]), tags='histogram')
    def __init__(self):
        window = Tk()
        window.title('선택 정렬 애니메이션')
        self.canvas = Canvas(window, bg='white', width=width, height=height)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame, text='다음단계', command=self.next).pack(side=LEFT)
        Button(frame, text='재설정', command=self.reGen).pack(side=LEFT)
        window.mainloop()
MainGUI()