import random
def main():
    fp = open('hangman.txt')
    words = fp.read().split()
    while True:
        index = random.randint(0, len(words)-1)
        hiddenWord = words[index]   #숨긴 단어 랜덤하게 생성
        guessWord = ['*']*len(hiddenWord)
        NumOfCorrectChar = 0 #맞힌 문자의 개수
        NumOfMiss = 0        #틀린 횟수
        while NumOfCorrectChar < len(hiddenWord):
            ch = input ('(추측) 단어' + toString(guessWord) + '에 포함되는 문자를 입력 >')
            if ch in guessWord:
                print('\t', ch, '은/는 이미 포함되어 있습니다.')
            elif hiddenWord.find(ch) == -1:   #리스트의 find 함수는 검색해서 찾으면 인덱스를 반환g
                print('\t', ch, '은/는 포함되어 있지 않습니다.')    # 못찾으면 -1 반환
                NumOfMiss += 1
            else:
                k = hiddenWord.find(ch)
                while k >= 0:
                    guessWord[k] = ch
                    NumOfCorrectChar += 1
                    k = hiddenWord.find(ch, k+1)
        print('정답은', hiddenWord, '입니다.', NumOfMiss, '번 실패했습니다.')
        YesNo = input('다른 단어 맞추기를 하시겠습니까? y/n >')
        if YesNo == 'n':
            break


def toString(guessWord):
    result = ''
    for c in guessWord:
        result += c
    return result

main()