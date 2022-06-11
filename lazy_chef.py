T = int(input())

for _ in range(T):
    (X, M, D) = map(int, input().split())

    t1 = X*M
    t2 = X+D

    print(min(t1, t2))
