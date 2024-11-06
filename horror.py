import sys
import math
from collections import deque

'''
data = []
for line in sys.stdin:
    data.append(line)
'''

data = ["6 3 5",
        "0 5 2",
        "0 1",
        "1 2",
        "4 5",
        "3 5",
        "0 2"
        ]



data = ["6 2 3",
        "5 2",
        "0 5",
        "0 1",
        "3 4"
        ]



N, H, L = list(map(int, data[0].split()))

horrorList = list(map(int, data[1].split()))

edges = [list(map(int, line)) for line in list(map(str.split, data[2:]))]

similarities = {}
for n in range(N):
    similarities[n] = []

for a, b in edges:
    similarities[a].append(b)
    similarities[b].append(a)

HI = {}
for horror in horrorList:
    HI[horror] = 0
    for h in horrorList:
        similarities[horror].append(h)


def bfs(roots, graph, f):
    queue = deque(roots)  
    visited = set(roots) 

    while queue:
        current = queue.popleft()
        current_distance = f[current]

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                f[neighbor] = current_distance + 1
                queue.append(neighbor)

    return f


bfs(horrorList, similarities, HI)


presenceInfinity = False
for n in range(N):
    if n not in HI:
        presenceInfinity = True
        print(n)
        break

if not presenceInfinity:
    max_HI_value = max(HI.values())
    answer = [key for key, value in HI.items() if value == max_HI_value]
    print(min(answer))