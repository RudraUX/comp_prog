T = int(input())

for _ in range(T):
    (X, Y, Z) = map(int, input().split())

    if (Z * 2) + X >= Y:
      print("Yes")
    else:
      print("No")


