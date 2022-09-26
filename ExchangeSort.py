def exchangeSort(a, n):
    for i in range(1, n):
        for j in range(i+1, n):
            if a[i] < a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp

a = [-1, 3, 1, 2, 4, 6, 5]
exchangeSort(a, 7)
print(a)