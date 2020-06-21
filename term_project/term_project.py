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
import folium
import webbrowser
import spam

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

def RequestInfo(startDt, endDt, upr_cd = None, org_cd = None, numOfRows = 16):
    # bgnde 시작일 20150601
    # endde 종료일 20140630
    # upr_cd 시도코드
    # org_cd 시군구코드
    # numOfRows 개수 4

    # startDt = '20140601'
    # endDt = '20140630'

    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic"
    url = url + "?bgnde=" + str(startDt) + "&endde=" + str(endDt)

    if( upr_cd != None ):
        url = url + "&upr_cd=" + str(upr_cd)

    if( org_cd != None ):
        url = url + "&org_cd=" + str(org_cd)

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

def GetSexString(sexCd):
    if( sexCd == 'M' ):
        return '수컷'
    if ( sexCd == 'F' ):
        return '암컷'
    return '성별 미상'

def OnClickedBtnSearch():
    bgnde = e1.get()
    endde = e2.get()
    upr_cd = e3.get() if len(e3.get()) > 0 else None
    org_cd = e4.get() if len(e4.get()) > 0 else None

    response = RequestInfo(bgnde, endde, upr_cd, org_cd)
    root = ParseXML(response)

    # 데이터 정리
    items = root.find('body').find('items').findall('item')
    datas = []
    for item in items:
        data = {}
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
    for i in range(frameCount):
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
        guiDic[frames[i]]['map'].configure(command = lambda : OpenWeb(datas[i]['careNm']))
        guiDic[frames[i]]['map'].pack()





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
l4 = Label(f0, text="군/구")
l1.place(x=0, y=30)
l2.place(x=0, y=60)
l3.place(x=0, y=90)
l4.place(x=0, y=120)

e1 = Entry(f0)
e2 = Entry(f0)
e3 = Entry(f0)
e4 = Entry(f0)
e1.place(x=120, y=30)
e2.place(x=120, y=60)
e3.place(x=120, y=90)
e4.place(x=120, y=120)

b1 = Button(f0, text="검색", width=10, command=OnClickedBtnSearch)
b1.place(x=120, y=150)

notebook = tkinter.ttk.Notebook(window, width=350, height=700)
notebook.pack(side=RIGHT, padx=20)


f1 = Frame(window, bg='white smoke')
notebook.add(f1, text='1')
f2 = Frame(window, bg='white smoke')
notebook.add(f2, text='2')
f3 = Frame(window, bg='white smoke')
notebook.add(f3, text='3')
f4 = Frame(window, bg='white smoke')
notebook.add(f4, text='4')
f5 = Frame(window, bg='white smoke')
notebook.add(f5, text='5')
f6 = Frame(window, bg='white smoke')
notebook.add(f6, text='6')
f7 = Frame(window, bg='white smoke')
notebook.add(f7, text='7')
f8 = Frame(window, bg='white smoke')
notebook.add(f8, text='8')
f9 = Frame(window, bg='white smoke')
notebook.add(f9, text='9')
f10 = Frame(window, bg='white smoke')
notebook.add(f10, text='10')
f11 = Frame(window, bg='white smoke')
notebook.add(f11, text='11')
f12 = Frame(window, bg='white smoke')
notebook.add(f12, text='12')
f13 = Frame(window, bg='white smoke')
notebook.add(f13, text='13')
f14 = Frame(window, bg='white smoke')
notebook.add(f14, text='14')
f15 = Frame(window, bg='white smoke')
notebook.add(f15, text='15')
f16 = Frame(window, bg='white smoke')
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


# image1 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091206924_s.jpg")
# Label(f1, image=image1, width=200, height=200).pack()

# image2 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091206772_s.jpg")
# Label(f2, image=image2, width=200, height=200).pack()

# image3 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091106743_s.jpg")
# Label(f3, image=image3, width=200, height=200).pack()

# image4 = DownloadImage("http://www.animal.go.kr/files/shelter/2020/06/202006091206843_s.jpg")
# Label(f4, image=image4, width=200, height=200).pack()

window.mainloop()
