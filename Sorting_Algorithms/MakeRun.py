def makeRun(a, n):
    i = 1
    r = []
    while i <= n:
        t = []
        while i < n and a[i] < a[i+1]:
            t.append(a[i])
            i += 1
        t.append(a[i])
        r.append(t)
        i += 1
    return r

a = [0, 6, 7, 8, 3, 4, 1, 5, 9, 10, 2]
print(makeRun(a, 10))