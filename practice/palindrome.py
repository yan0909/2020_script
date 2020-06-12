def check_palindrome(n):
    n_length = get_length(n)
    for i in range(n_length // 2):
        if (get_nth_num(n, n_length - i) != get_nth_num(n, i + 1)):
            return False
    return True

def get_length(n):
    n_length = 0
    while (n > 0):
        n_length += 1
        n //= 10
    return n_length


def get_nth_num(n, nth):
    for i in range(1, nth):
        n //= 10
    return n % 10


def check_prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

N = eval(input())
for i in range(N+1, 1000000):
    if check_prime(i):
        if check_palindrome(i):
            M = i
            break
print(M)
