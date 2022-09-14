def quickSort(a, l, r):
    if r > l:
        i = partition(a, l, r)
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

def partition(a, l, r):
    v = a[r]
    i = l-1
    j = r
    while True:
        while True:
            i = i+1
            if a[i] >= v:
                break
        while True:
            j = j-1
            if a[j] <= v:
                break
        if i >= j:
            break
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
    tmp = a[i]
    a[i] = a[r]
    a[r] = tmp

    return i

a = [-1, 5, 2, 4, 1, 3]
quickSort(a, 1, 5)
print(a)