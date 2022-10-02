import time, random

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

N = 5000
a = []

for i in range(N):
    a.append(i)
start_time = time.time()
cocktailShakerSort(a, N)
end_time = time.time() - start_time
print("Executing time (N = %d) : %0.3f" %(N, end_time))
checkSort(a, N)