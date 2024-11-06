import sys
import math


data = []
for line in sys.stdin:
    data.append(line[:-1])


def kmp_search(s, w):
    P = []
    np = 0
    j = 0
    k = 0
    T = kmp_table(w)

    while j < len(s):
        if w[k] == s[j]:
            j += 1
            k += 1
            if k == len(w):
                P.append(j-k)
                np += 1
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1
    return P
                
def kmp_table(w):
    pos = 1
    cnd = 0
    T = {}
    T[0] = -1
    while pos < len(w):
        if w[pos] == w[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


queries = []
for i in range(int(len(data)/2)):
    queries.append((data[i*2], data[(i*2)+1]))

for w, s in queries:
    answer = list(map(str, kmp_search(s, w)))
    print(' '.join(answer))