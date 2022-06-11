T = int(input())

for _ in range(T):
    (m, h) = map(int, input().split())
    BMI = m/(h**2)
    if BMI <= 18:
        print(1)
    elif 19 <= BMI <= 24:
        print(2)
    elif 25 <= BMI <= 29:
        print(3)
    elif BMI >= 30:
        print(4)

