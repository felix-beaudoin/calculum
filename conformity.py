l = int(input())
dees = {}
for _ in range(l):
    t = list(map(int, input().split()))
    t.sort()
    tu = tuple((n for n in t))
    dees[tu] = 1 + dees.get(tu, 0)
maks = -1
score = -1
for v in dees.values():
    if v > maks:
        score = v
        maks = v
    elif v == maks:
        score += v
print(score)