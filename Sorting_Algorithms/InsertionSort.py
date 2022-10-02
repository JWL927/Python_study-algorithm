def insertionSort(a, n):
    for i in range(2, n):
        if a[0] > a[i]:
            j = 1
            while j < i:
                if a[j] > a[i]:
                    tmp = a[i]
                    for k in range(i-1, j-1, -1):
                        a[k+1] = a[k]
                    a[j] = tmp
                j = j+1
            
a = [5, 3, 1, 2, 4, 0]
insertionSort(a, 6)
print(a)
