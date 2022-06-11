T = int(input())

for _ in range(T):
    (A, B, C) = map(int, input().split())

    if C < B and C < A:
        print("Alice")
    elif B < A:
        print("Bob")
    else:
        print("Draw")
