R = int(input())
p1_total = 0
p2_total = 0
max_lead = 0
winner = 0

for _ in range(R):
    (p1, p2) = map(int, input().split(' '))
    p1_total += p1
    p2_total += p2

    round_lead = abs(p1_total-p2_total)

    if round_lead > max_lead:
        max_lead = round_lead
        winner = 1 if p1_total > p2_total else 2

print(winner, max_lead)
