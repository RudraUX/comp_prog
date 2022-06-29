def solution():
    N = int(input())
    A = [int(i) for i in input().split()]

    freq = {}
    for a in A:
        if a in freq.keys():
            freq[a] += 1
        else:
            freq[a] = 1
    # print(freq)
    max_count = 0
    for a in freq.keys():
        max_count = max(max_count, freq[a])
    print(N - max_count)


T = int(input())
while (T > 0):
    T = T - 1
    solution()
