from tkinter import *
import tkinter.messagebox #에러메세지 출력하는 모듈
from tkinter.filedialog import askopenfilename #파일오픈 대화상자
def openFile():
    fn = askopenfilename()
    filename.set(fn)

def showResult2():
    fn = filename.get()  # 중요
    try:
        infile = open(fn, "r")
        counts = [0] * 26  # [0,0,...]
        for line in infile:
            lowerLine = line.lower()
            for ch in line:
                if ch.isalpha():  # a,b,c,d,...,z 97,87,99,... ord('a'), chr(97)를 활용
                    counts[ord(ch) - ord('a')] += 1
        width = int(canvas['width'])
        height = int(canvas['height'])
        maxCounts = max(counts) #빈도수가 높은 최대 값
        heightBar = height*0.75 #canvas 크기의 75%가 최대 막대 바의 높이
        widthBar = width - 20 #canvas 전체 너비에서 좌 10 우 10을 뺀 값
        for i in range(26):  # i=0,1,2,...,25
            canvas.create_rectangle(i*widthBar/26 + 10, height - heightBar*counts[i]/maxCounts - 20, (i+1)*widthBar/26, height-20) #막대가 길수록 y좌표는 작아진다
            canvas.create_text(i*widthBar/26 + 10 + 0.5*widthBar/26, height-10, text=chr(i+ord('a')))
        infile.close()
    except IOError:
        tkinter.messagebox.showwarning(filename + "파일이 존재하지 않습니다.")

window = Tk()
window.title("문자의 출현 빈도수")
frame1 = Frame(window)
frame1.pack()

canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()
Label(frame2, text="파일명을 입력하세요 : ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="열기", command=openFile).pack(side=LEFT) ##openFile에서 ()쓰면 실행한다는 의미이므로 쓰면 안됨
Button(frame2, text="결과보기", command=showResult2).pack(side=LEFT)
window.mainloop()
