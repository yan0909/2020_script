from functools import *
def intersect(*ar):
    return reduce(__intersectSC,ar)
def __intersectSC(listX,listY):
    setList =[]
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    setList = []
    intersectSet = intersect(*ar) #ar 가변인자리스트를 튜플 (A,B,C) => *ar : A,B,C로 풀어줌
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList