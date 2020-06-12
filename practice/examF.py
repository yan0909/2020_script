def scoreSmallStraight(dice):
    numList = [i for i in dice]
    if 1 in numList and 2 in numList and 3 in numList and 4 in numList:
        return True
    if 2 in numList and 3 in numList and 4 in numList and 5 in numList:
        return True
    if 3 in numList and 4 in numList and 5 in numList and 6 in numList:
        return True
    return False

dice = map(eval, input().split())
if(scoreSmallStraight(dice)):
    print('YES')
else:
    print('NO')