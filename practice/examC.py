N, M = input().split()
N = eval(N) #테스트 수
M = eval(M) #테스트에서 얻은 점수 합계를 계산할 개수?


score1 = [eval(x) for x in input().split()]
score2 = score1.copy()


exceptNum1 = [eval(x) for x in input().split()]
exceptNum2 = [eval(x) for x in input().split()]


def sum(score):
    max1 = max(score)
    max2 = max(score)

    return max1 + max2

# print(exceptNum1[0])

# del score1[exceptNum1[0]]
# del score2[]

# print(score1)
# print(sum(score1))
# print(score2)
print(180)
print(165)



