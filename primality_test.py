import random

def power(a, k):
    res = 1
    while (k > 0):
        if (k & 1) == 1:
            res = res * a
        k = k // 2
        a = a * a
    return res


def is_prime(n, k):
    if n <= 1:
        return False

    if n <= 3:
        return True

    while k > 0:
        a = random.randint(2, n - 1)
        if (power(a, n - 1) % n) != 1:
            return False
        k -= 1

    return True


if __name__ == '__main__':
    t = int(input())
    k = 5
    for i in range(t):
        m, n = map(int, input().split())
        for x in range(m, n + 1):
            if is_prime(x, k):
                print(x)
        print()