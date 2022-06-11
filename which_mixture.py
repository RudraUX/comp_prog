T = int(input())

for _ in range(T):
    (A, B) = map(int, input().split())

    if A > 0 and B > 0:
        print("Solution")
    elif A == 0:
        print("Liquid")
    else:
        print("Solid")
