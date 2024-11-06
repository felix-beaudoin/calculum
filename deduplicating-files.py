
def hashishe(x):
    h = 0
    for c in x:
        h = h^ord(c)
    return h

print(hashishe("abc"))