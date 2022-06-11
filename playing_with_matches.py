T = int(input())

for _ in range(T):
    r = 0
    n = 0
    count = 0
    matches_list = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    a, b = [int(i) for i in input().split()]
    n = a + b

    while n > 0:
        r = n % 10
        n = n//10
        count += matches_list[r]
    print(count)
