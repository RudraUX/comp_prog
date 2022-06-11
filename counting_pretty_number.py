T = int(input())
count = 0

for _ in range(T):
    [start_num, end_num] = [int(i) for i in input().split()]
    for i in range(start_num, end_num+1):
        last_num = i % 10
        if last_num == 2 or last_num == 3 or last_num == 9:
            count += 1
    print(count)
    count = 0
