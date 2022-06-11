T = int(input())

for _ in range(T):
    (A, B) = map(int, input().split())

    if A + B < 3:
        print(1)
    elif 3 <= A + B <= 10:
        print(2)
    elif 11 <= A + B <= 60:
        print(3)
    elif 60 < A+B:
        print(4)
