from tkinter import *
from tkinter import font
import tkinter.ttk
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import requests
from xml.etree.ElementTree import parse
import xml.etree.ElementTree as elemTree
import os
import os.path
import folium
import webbrowser
import spam
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import telepot

def Pressd():
    map_osm = folium.Map(location=[], zoom_start=13)
    folium.Marker([], popup='').add_to(map_osm)
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

def OpenWeb(url):
    print('https://map.naver.com/v5/search/' + url)
    webbrowser.open('https://map.naver.com/v5/search/' + url)

def DownloadImage(url, width = None, height = None):
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))

    if(width != None):
        im  = im.resize((width, height), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(im)
    # Label(window, image=image, height=400, width=400).pack()
    # print(image)

    return image

def RequestInfo(startDt, endDt, org_cd = None, kind_cd = None, numOfRows = 16):
    # bgnde 시작일 20150601
    # endde 종료일 20140630
    # upr_cd 시도코드
    # org_cd 시군구코드
    # numOfRows 개수 4

    # startDt = '20140601'
    # endDt = '20140630'

    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic"
    url = url + "?bgnde=" + str(startDt) + "&endde=" + str(endDt)

    if( org_cd != None ):
        url = url + "&org_cd=" + str(org_cd)

    if( kind_cd != None ):
        url = url + "&upkind=" + str(kind_cd)

    url = url + "&pageNo=1"
    url = url + "&numOfRows=" + str(numOfRows)
    
    url = spam.GetAuthorize(url) # spam 이용해서 API Key 받기
    responseText = requests.get(url).text
    fp = open("data.xml", "w", encoding="utf8")
    fp.write(responseText)
    fp.close()
    return responseText

def ParseXML(text):
    a = elemTree.fromstring(text)
    return a

def LoadBookMark(fileName):
    # 없으면 새로 생성
    if( os.path.isfile(fileName) == False ):
        root = elemTree.Element('response')
        root.append( elemTree.Element('body') )
        root.find('body').append( elemTree.Element('items') )
        return root

    f = open(fileName, 'r', encoding='utf8')
    s = f.read()
    return ParseXML(s)

def SaveBookMark(tree, fileName):
    root = elemTree.ElementTree(tree)
    root.write(fileName, encoding='utf8')

def AddBookMark(elem):
    root = LoadBookMark('bookmark.xml')
    root.find('body').find('items').append(elem)
    SaveBookMark(root, 'bookmark.xml')

def GetSexString(sexCd):
    if( sexCd == 'M' ):
        return '수컷'
    if ( sexCd == 'F' ):
        return '암컷'
    return '성별 미상'

def ShowData(root, isBookMark):
    global curTab
    # 데이터 정리
    items = root.find('body').find('items').findall('item')
    datas = []
    for item in items:
        data = {}
        # data['desertionNo'] = item.find('desertionNo').text
        data['popfile'] = item.find("popfile").text
        data['happenDt'] = item.find("happenDt").text
        data['happenPlace'] = item.find("happenPlace").text
        data['kindCd'] = item.find("kindCd").text
        data['colorCd'] = item.find("colorCd").text
        data['age'] = item.find("age").text
        data['sexCd'] = item.find("sexCd").text
        data['specialMark'] = item.find("specialMark").text
        data['careNm'] = item.find("careNm").text
        data['careTel'] = item.find("careTel").text
        data['processState'] = item.find("processState").text
        data['orgNm'] = item.find("orgNm").text
        datas.append(data)

    # GUI 세팅
    for i in range( frameCount ):
        if(i >= len(datas)):
            guiDic[frames[i]]['popfile'].pack_forget()
            guiDic[frames[i]]['orgNm'].pack_forget()
            guiDic[frames[i]]['happenDt'].pack_forget()
            guiDic[frames[i]]['happenPlace'].pack_forget()
            guiDic[frames[i]]['kindCd'].pack_forget()
            guiDic[frames[i]]['specialMark'].pack_forget()
            guiDic[frames[i]]['careNm'].pack_forget()
            guiDic[frames[i]]['processState'].pack_forget()
            guiDic[frames[i]]['map'].pack_forget()
            guiDic[frames[i]]['bookmarkSep'].pack_forget()
            guiDic[frames[i]]['bookmark'].pack_forget()
            continue

        img = DownloadImage(datas[i]['popfile'], 330, 330)
        guiDic[frames[i]]['popfile'].configure(image=img, width=330, height= 330)
        guiDic[frames[i]]['popfile'].image=img
        guiDic[frames[i]]['popfile'].pack()
        guiDic[frames[i]]['orgNm'].configure(text = "지역 : " + datas[i]['orgNm'])
        guiDic[frames[i]]['orgNm'].pack()
        guiDic[frames[i]]['happenDt'].configure(text = "접수일 : " + datas[i]['happenDt'])
        guiDic[frames[i]]['happenDt'].pack()
        guiDic[frames[i]]['happenPlace'].configure(text = "발견 장소 : " + datas[i]['happenPlace'])
        guiDic[frames[i]]['happenPlace'].pack()
        guiDic[frames[i]]['kindCd'].configure(text = datas[i]['kindCd'] + " " +  datas[i]['colorCd'] + " " + datas[i]['age'] + " " + GetSexString(datas[i]['sexCd']))
        guiDic[frames[i]]['kindCd'].pack()
        guiDic[frames[i]]['specialMark'].configure(text = "특징 : " + datas[i]['specialMark'])
        guiDic[frames[i]]['specialMark'].pack()
        guiDic[frames[i]]['careNm'].configure(text = "보호소 : " + datas[i]['careNm'] + " (" + datas[i]['careTel'] + ")")
        guiDic[frames[i]]['careNm'].pack()
        guiDic[frames[i]]['processState'].configure(text = "상태 : " + datas[i]['processState'])
        guiDic[frames[i]]['processState'].pack()
        guiDic[frames[i]]['map'].configure(command = lambda : OpenWeb(datas[curTab]['careNm']))
        guiDic[frames[i]]['map'].pack()
        guiDic[frames[i]]['bookmarkSep'].pack()
        guiDic[frames[i]]['bookmark'].configure(command = lambda : AddBookMark(items[curTab]) )
        guiDic[frames[i]]['bookmark'].pack()

        if(isBookMark):
            guiDic[frames[i]]['bookmark'].pack_forget()

    i = 0

def OnClickedBtnSearch():
    global orgCdMap, kindCdMap, cbstr1, cbstr2
    bgnde = e1.get()
    endde = e2.get()
    # upr_cd = e3.get() if len(e3.get()) > 0 else None
    org_cd = orgCdMap[cbstr1.get()] #e4.get() if len(e4.get()) > 0 else None
    kind_cd = kindCdMap[cbstr2.get()]

    response = RequestInfo(bgnde, endde, org_cd, kind_cd)
    root = ParseXML(response)
    ShowData(root, isBookMark= False)

def OnClickedBtnShowBookMark():
    root = LoadBookMark('bookmark.xml')
    ShowData(root, isBookMark= True)

def OnClickedBtnSendBookMark():
    msg = MIMEMultipart()

    ID = 'silverk0909@gmail.com'
    PW = 'a7621718'
    SEND = 'silverk0909@gmail.com'

    msg['From'] = ID
    msg['To'] = SEND
    msg['Subject'] = '유기동물 조회 서비스 북마크 정보'


    root = LoadBookMark('bookmark.xml')
    items = root.find('body').find('items').findall('item')
    body = '북마크 파일입니다. \n\n'
    for item in items:
        body += "이미지 링크 : " + item.find('popfile').text + '\n'
        body += "지역 : " + item.find('orgNm').text + '\n'
        body += "접수일 : " + item.find('happenDt').text + '\n'
        body += "발견 장소 : " + item.find('happenPlace').text + '\n'
        body += item.find('kindCd').text + " " + item.find('colorCd').text + " " + item.find('age').text + '\n'
        body += "특징 : " + item.find('specialMark').text + '\n'
        body += "보호소 : " + item.find('careNm').text + " (" + item.find('careTel').text + ")" + '\n'
        body += "상태 : " + item.find('processState').text + '\n'
        body += '\n\n\n\n'

    msg.attach(MIMEText(body,'plain'))

    # 첨부
    filename='bookmark.xml'  
    attachment = open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)

    # 보내기
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(ID,PW)

    server.sendmail(ID,SEND,text)
    server.quit()




window = Tk()
window.geometry("700x800")
window.title("유기동물 조회 서비스")

f0 = Frame(window, width=100, height=300)
f0.pack(side=LEFT, fill='both', padx=20, pady=50, expand=True)

label_title = Label(f0, text="유기동물 조회 서비스", fg='blue')
label_title.grid(row=0, column=1)

l1 = Label(f0, text="검색시작일")
l2 = Label(f0, text="검색종료일")
l3 = Label(f0, text="시도")
l4 = Label(f0, text="종류")

l1.place(x=0, y=30)
l2.place(x=0, y=60)
l3.place(x=0, y=90)
l4.place(x=0, y=120)

e1 = Entry(f0)
e2 = Entry(f0)
e1.place(x=120, y=30)
e2.place(x=120, y=60)


orgCdMap = {}
orgCdMap['전체'] = None
orgCdMap['서울특별시'] = '6110000'
orgCdMap['부산광역시'] = '6260000'
orgCdMap['대구광역시'] = '6270000'
orgCdMap['인천광역시'] = '6280000'
orgCdMap['광주광역시'] = '6290000'
orgCdMap['세종특별자치시'] = '5690000'
orgCdMap['대전광역시'] = '6300000'
orgCdMap['울산광역시'] = '6310000'
orgCdMap['경기도'] = '6410000'
orgCdMap['강원도'] = '6420000'

kindCdMap = {}
kindCdMap['전체'] = None
kindCdMap['개'] = '417000'
kindCdMap['고양이'] = '422400'
kindCdMap['기타'] = '429900'

cbstr1 = StringVar()
cb1 = tkinter.ttk.Combobox(f0, width = 12 , textvariable = cbstr1 )
cb1['values'] = ['전체', '서울특별시' , '부산광역시' , '대구광역시', '인천광역시', '광주광역시', '세종특별자치시', '대전광역시', '울산광역시', '경기도', '강원도']
cb1.current(0)
cb1.place(x=120, y=90)

cbstr2 = StringVar()
cb2 = tkinter.ttk.Combobox(f0, width = 12 , textvariable = cbstr2 )
cb2['values'] = ['전체', '개' , '고양이' , '기타']
cb2.current(0)
cb2.place(x=120, y=120)

b1 = Button(f0, text="검색", width=14, command=OnClickedBtnSearch)
b1.place(x=120, y=150)

b2 = Button(f0, text="북마크 보기", width=14, command=OnClickedBtnShowBookMark)
b2.place(x=120, y=195)

b3 = Button(f0, text="메일 보내기", width=14, command=OnClickedBtnSendBookMark)
b3.place(x=120, y=195+45)

notebook = tkinter.ttk.Notebook(window, width=350, height=700)
notebook.pack(side=RIGHT, padx=20)

curTab = 0

def SetCurrentTab(index):
    global curTab
    curTab = index

f1 = Frame(window, bg='white smoke')
f1.bind("<Visibility>", func= (lambda e : SetCurrentTab(0)))
notebook.add(f1, text='1')
f2 = Frame(window, bg='white smoke')
f2.bind("<Visibility>", func= (lambda e : SetCurrentTab(1)))
notebook.add(f2, text='2')
f3 = Frame(window, bg='white smoke')
f3.bind("<Visibility>", func= (lambda e : SetCurrentTab(2)))
notebook.add(f3, text='3')
f4 = Frame(window, bg='white smoke')
f4.bind("<Visibility>", func= (lambda e : SetCurrentTab(3)))
notebook.add(f4, text='4')
f5 = Frame(window, bg='white smoke')
f5.bind("<Visibility>", func= (lambda e : SetCurrentTab(4)))
notebook.add(f5, text='5')
f6 = Frame(window, bg='white smoke')
f6.bind("<Visibility>", func= (lambda e : SetCurrentTab(5)))
notebook.add(f6, text='6')
f7 = Frame(window, bg='white smoke')
f7.bind("<Visibility>", func= (lambda e : SetCurrentTab(6)))
notebook.add(f7, text='7')
f8 = Frame(window, bg='white smoke')
f8.bind("<Visibility>", func= (lambda e : SetCurrentTab(7)))
notebook.add(f8, text='8')
f9 = Frame(window, bg='white smoke')
f9.bind("<Visibility>", func= (lambda e : SetCurrentTab(8)))
notebook.add(f9, text='9')
f10 = Frame(window, bg='white smoke')
f10.bind("<Visibility>", func= (lambda e : SetCurrentTab(9)))
notebook.add(f10, text='10')
f11 = Frame(window, bg='white smoke')
f11.bind("<Visibility>", func= (lambda e : SetCurrentTab(10)))
notebook.add(f11, text='11')
f12 = Frame(window, bg='white smoke')
f12.bind("<Visibility>", func= (lambda e : SetCurrentTab(11)))
notebook.add(f12, text='12')
f13 = Frame(window, bg='white smoke')
f13.bind("<Visibility>", func= (lambda e : SetCurrentTab(12)))
notebook.add(f13, text='13')
f14 = Frame(window, bg='white smoke')
f14.bind("<Visibility>", func= (lambda e : SetCurrentTab(13)))
notebook.add(f14, text='14')
f15 = Frame(window, bg='white smoke')
f15.bind("<Visibility>", func= (lambda e : SetCurrentTab(14)))
notebook.add(f15, text='15')
f16 = Frame(window, bg='white smoke')
f16.bind("<Visibility>", func= (lambda e : SetCurrentTab(15)))
notebook.add(f16, text='16')


frames = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16]
frameCount = len(frames)

guiDic = {}
for frame in frames:
    guiDic[frame] = {}
    guiDic[frame]['popfile'] = Label(frame)
    guiDic[frame]['orgNm'] = Label(frame)
    guiDic[frame]['happenDt'] = Label(frame)
    guiDic[frame]['happenPlace'] = Label(frame)
    guiDic[frame]['kindCd'] = Label(frame)
    guiDic[frame]['specialMark'] = Label(frame)
    guiDic[frame]['careNm'] = Label(frame)
    guiDic[frame]['processState'] = Label(frame)
    guiDic[frame]['map'] = Button(frame, text='지도에서 보호소 찾기')
    guiDic[frame]['bookmarkSep'] = Label(frame, text='   ')
    guiDic[frame]['bookmark'] = Button(frame, text='북마크에 추가')


# image1 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091206924_s.jpg")
# Label(f1, image=image1, width=200, height=200).pack()

# image2 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091206772_s.jpg")
# Label(f2, image=image2, width=200, height=200).pack()

# image3 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091106743_s.jpg")
# Label(f3, image=image3, width=200, height=200).pack()

# image4 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091206843_s.jpg")
# Label(f4, image=image4, width=200, height=200).pack()


class TeleBot:
    bot = None
    KEY = '1195857579:AAE5Lnon-hLeUxb1CvRPc1OjLLFWsGFgzFo'

    @staticmethod
    def RepresentsInt(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    @classmethod
    def handle(cls, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if(content_type != 'text'):
            return

        text = msg['text']
        args = text.split(' ')

        if(len(args) != 2 and len(args) != 3):
            cls.bot.sendMessage(chat_id, '(검색시작일) (검색종료일) [결과 수]   형태로 입력해주세요.')
            return

        startDt = args[0]
        endDt = args[1]
        if(len(args) == 2):
            searchCount = 1
        else:
            searchCount = args[2]

        # args 검증
        if(len(startDt) != 8 or len(endDt) != 8 or not TeleBot.RepresentsInt(searchCount)):
            cls.bot.sendMessage(chat_id, '(검색시작일) (검색종료일) [결과 수]   형태로 입력해주세요.')
            return

        searchCount = int(searchCount)

        responseText = RequestInfo(startDt, endDt, org_cd=None, kind_cd=None, numOfRows=searchCount)
        root = ParseXML(responseText)
        items = root.find('body').find('items').findall('item')
        for item in items:
            body = '# ' + str(items.index(item) + 1) + '/' +  str(len(items)) + '\n'
            body += "지역 : " + item.find('orgNm').text + '\n'
            body += "접수일 : " + item.find('happenDt').text + '\n'
            body += "발견 장소 : " + item.find('happenPlace').text + '\n'
            body += item.find('kindCd').text + " " + item.find('colorCd').text + " " + item.find('age').text + '\n'
            body += "특징 : " + item.find('specialMark').text + '\n'
            body += "보호소 : " + item.find('careNm').text + " (" + item.find('careTel').text + ")" + '\n'
            body += "상태 : " + item.find('processState').text + '\n'
            body += "(이미지 : " + item.find('popfile').text + ')'

            cls.bot.sendMessage(chat_id, body)

    def __init__(self):
        TeleBot.bot = telepot.Bot(TeleBot.KEY)
        TeleBot.bot.message_loop(TeleBot.handle)
        



telebot = TeleBot()

window.mainloop()
