import sys
import math

data = []
for line in sys.stdin:
    data.append(line)

'''
data = [    "PAUL_ERDOS HARVEY_ABBOTT JANOS_ACZEL TAKASHI_AGOH RON_AHARONI MARTIN_AIGNER MIKLOS_AJTAI",
            "HARVEY_ABBOTT CHARLES_AULL EZRA_BROWN PAUL_DIERKER",
            "PAUL_DIERKER MATTS_ESSEN",
            "FRANK_BROWN CHARLES_ROGERS"
        ]
'''

d = {}

for l in data:
    l = l.split()
    d[l[0]] = (set(x for x in l[1:]))

n = {}
for a in d:
    for c in d[a]:
        if c in d:
            d[c].add(a)
        else:

            if c in n:
                n[c].add(a)
                
            else:
                n[c] = set()
                n[c].add(a)

d = d | n

def bfs(authors, dict):
    
    visited = {}
    queue = ["PAUL_ERDOS"]    
    depth = {"PAUL_ERDOS": 0}
    answers = {}

    while len(queue) != 0:
        current = queue.pop(0)
        for c in dict[current]:
            depth[current] = min(depth.get(current, math.inf), 1 + depth.get(c, math.inf))

        if current in authors:
            answers[current] = depth[current]
        
        visited[current] = True
        for coauthor in dict[current]:
            if not visited.get(coauthor, False):
                queue.append(coauthor)
                
    return answers

queries = []
for q in data:
    queries.append(q.split()[0])

a = bfs(queries, d)
for q in queries:
    print(q, a.get(q, "no-connection"))