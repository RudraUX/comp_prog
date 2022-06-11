T = int(input())

for _ in range(T):
    A, B, C, D = [int(i) for i in input().split()]

    if A < B:
        A = A + C
    else:
        B = B + C

    if A < B:
        A = A + D
    else:
        B = B + D

    if A < B:
        print("S")
    elif A == B:
        print("N")
    else:
        print("N")
