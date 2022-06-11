T = int(input())

for _ in range(T):
    list_of_days = list(map(int, input().split()))
    sunny = 0
    rainy = 0
    for i in range(7):
        if list_of_days[i] == 1:
            sunny += 1
        else:
            rainy += 1

    if sunny > rainy:
        print("Yes")
    else:
        print("No")
