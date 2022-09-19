import random, time

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

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("Sorted!")
    else:
        print("Error!")

N = 987
a = []

for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
quickSort(a, 1, N-1)
end_time = time.time() - start_time
print("Executing time (N = %d) : %0.3f" %(N, end_time))
checkSort(a, N)