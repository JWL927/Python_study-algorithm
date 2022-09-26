def cocktailShakerSort(a, n):
    d = True
    i = 1
    k = n
    while i < k:
        if d == True:
            for l in range(i, k-1):
                if a[l] > a[l+1]:
                    tmp = a[l]
                    a[l] = a[l+1]
                    a[l+1] = tmp
            k = k-1
        else:
            for l in range(k, i, -1):
                if a[l] < a[l-1]:
                    tmp = a[l]
                    a[l] = a[l-1]
                    a[l-1] = tmp
            i = i+1
        d = not d

a = [-1, 6, 5, 4, 3, 2, 1]
cocktailShakerSort(a, 7)
print(a)