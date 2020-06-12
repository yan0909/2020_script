matrix = [] #전역변수 : 6x7 사목게임 보드 자료구조
def drawBoard():
    for i in range(6):
        for j in range(7):
            print('|', matrix[i][j], ' ', end='')
        print('|')
    print('------------------------------------')
def check():    #4개 연속인 것을 찾으면 X/O를 반환하고, 아니면 빈문자열 반환
    #가로 4개 체크
    for i in range(6):  #행과 열 가로/세로에 대해서 4개 연속 검사
        for j in range(4): #col=0,1,2,3
            player = matrix[i][j]   #i행의 4개 열이 연속인지 검사 (가로검사)
            if player != ' ' and player == matrix[i][j+1] and player == matrix[i][j+2] and player == matrix[i][j+3]:
                return player
    #세로 4개 체크
    for i in range(3):  #row=0,1,2
        for j in range(7):  # col=0,1,2,3
            player = matrix[i][j]  #j열의 4개 행이 연속인지 검사 (가로검사)
            if player != ' ' and player == matrix[i+1][j] and player == matrix[i+2][j] and player == matrix[i+3][j]:
                return player
    #대각선검사 좌에서 우로
    for i in range(3):  #row=0,1,2
        for j in range(4):  #col=0,1,2,3:
            player = matrix[i][j]
            if player != ' ' and player == matrix[i+1][j+1] and player == matrix[i+2][j+2] and player == matrix[i+3][j+3]:
                return player
    #대각선검사 우에서 좌로
    for i in range(3):  #row=0,1,2
        for j in range(4):  #col=3,4,5,6
            player = matrix[0][2]
            if player != ' ' and player == matrix[i+1][j-1] and player == matrix[i+2][j-2] and player == matrix[i+3][j-3]:
                return player
    return ''
def findRow(col):
    for row in range(5, -1, -1):  #row=5,4,3,2,1,0
        if matrix[row][col] == ' ':
            return row
    return 6
def main():
    for i in range(6):
        matrix.append([])
        for j in range(7):
            matrix[i].append(' ') #공란 문자열
    drawBoard()
    isRturn = True #부울 변수 번갈아가면서 빨간색R, 노란색Y 플레이어 차례를 나타냄
    while True:
        if isRturn:
            col = eval(input('열 0-6에 빨간색 디스크를 떨어뜨리세요 : '))
        else:
            col = eval(input('열 0-6에 노란색 디스크를 떨어뜨리세요 : '))

        row = findRow(col)  #디스크가 들어갈 최하단 행을 구함
        while True:
            if row != 6:
                if isRturn:
                    matrix[row][col] = 'R'
                else:
                    matrix[row][col] = 'Y'
                break
            else:
                print('꽉찬 열입니다. 다시 떨어뜨리세요.')
        drawBoard()
        player = check()
        if player != '':
            if player == 'R':
                print('빨간색 플레이어가 이겼습니다.')
            else:
                print('노란색 플레이어가 이겼습니다.')
            break
        isRturn = not isRturn

main()