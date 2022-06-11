T = int(input())

for _ in range(T):
    (N, X, P) = map(int, input().split())

    if X * 3 - (N-X) >= P:
        print("Pass")
    else:
        print("Fail")
