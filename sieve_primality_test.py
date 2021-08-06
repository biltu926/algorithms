t = int(input())

max_ = 1000000000
prime = [True] * max_


def sieve():
    p = 2
    while p * p <= max_:
        if prime[p * p]:
            for i in range(p * p, max_ - 1, p):
                prime[i] = False
        p += 1


while (t > 0):
    m, n = map(int, input().split())
    for i in range(m, n):
        if prime[i]:
            print(i)

    t -= 1