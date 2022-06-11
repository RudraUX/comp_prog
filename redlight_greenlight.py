T = int(input())
count = 0
for _ in range(T):
    in_between_players, height_of_alihu = [
        int(i) for i in input().split()]

    in_between_players_h = list(map(int, input().split()))
    for i in range(in_between_players):
        if (in_between_players_h[i] > height_of_alihu):
            count += 1

    print(count)
    count = 0
