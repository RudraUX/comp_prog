T = int(input())

for _ in range(T):
    n = int(input())
    r = 1
    while n > 0:
        r = r * n
        n -= 1
    print(r)
