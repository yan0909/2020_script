from tkinter import *
class MainGUI:
    def up(self):   #window 좌표계는 좌측상단이 (0,0)
        self.canvas.move('ball', 0, -5)
    def down(self):
        self.canvas.move('ball', 0, 5)
    def left(self):
        self.canvas.move('ball', -5, 0)
    def right(self):
        self.canvas.move('ball', 5, 0)
    def __init__(self):
        window = Tk()
        window.title("공 옮기기")
        width = 200
        height = 100
        self.canvas = Canvas(window, bg='white', width=width, height=height)
        self.canvas.pack()
        self.canvas.create_oval(10, 10, 20, 20, fill='red', tags='ball')

        frame = Frame(window)
        frame.pack()
        #bUp = Button(frame, text='상', command=self.up)
        #bUp.pack(side=LEFT)
        Button(frame, text='상', command=self.up).pack(side=LEFT)
        Button(frame, text='하', command=self.down).pack(side=LEFT)
        Button(frame, text='좌', command=self.left).pack(side=LEFT)
        Button(frame, text='우', command=self.right).pack(side=LEFT)

        window.mainloop()
MainGUI()
