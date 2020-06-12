matrix = [] #전역변수 : 3x3틱택토 보드 자료구조
def drawBoard():
    for i in range(3):
        print('----------------')
        for j in range(3):
            print('|', matrix[i][j], ' ', end='')
        print('|')
    print('----------------')
def check():    #3개 연속인 것을 찾으면 X/O를 반환하고, 아니면 빈문자열 반환
    for i in range(3):  #행과 열 가로/세로에 대해서 3개 연속 검사
        player = matrix[i][0]   #i행의 3개 열이 3개 연속인지 검사 (가로검사)
        if player != ' ' and player == matrix[i][1] and player == matrix[i][2]:
            return player
        player = matrix[0][i]  # i열의 3개 행이 3개 연속인지 검사 (세로검사)
        if player != ' ' and player == matrix[1][i] and player == matrix[2][i]:
            return player
    #대각선검사
    player = matrix[0][0]
    if player != ' ' and player == matrix[1][1] and player == matrix[2][2]:
        return player
    player = matrix[0][2]
    if player != ' ' and player == matrix[1][1] and player == matrix[2][0]:
        return player
    return ''
def main():
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(' ') #공란 문자열
    drawBoard()
    isXturn = True #부울 변수 번갈아가면서 X, O 플레이어 차례를 나타냄
    for i in range(9):
        if isXturn:
            row = eval(input('플레이어 X의 행(0,1,2) 입력 : '))
            col = eval(input('플레이어 X의 열(0,1,2) 입력 : '))
            matrix[row][col] = 'X'
        else:
            row = eval(input('플레이어 O의 행(0,1,2) 입력 : '))
            col = eval(input('플레이어 O의 열(0,1,2) 입력 : '))
            matrix[row][col] = 'O'
        drawBoard()
        player = check()
        if player != '':
            print('플레이어', player, '가 이겼습니다.')
            break
        isXturn = not isXturn
    if i == 9:
        print('비겼습니다.')

main()