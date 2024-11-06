l = int(input())
tests=[]
for _ in range(l):
    t = list(map(int, input().split()))
    stack=[t.pop(1)]
    for i in range(2, t.pop(0)):
        new = t.pop(0)
        if new - stack.pop(0) != 1:
            print(i)
            break
        stack.append(new)