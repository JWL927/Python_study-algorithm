import random, time

def exchangeSort(a, n):
    for i in range(1, n):
        for j in range(i+1, n):
            if a[i] < a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i] < a[i+1]:
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
exchangeSort(a, N)
end_time = time.time() - start_time
print("Executing time (N = %d) : %0.3f" %(N, end_time))
checkSort(a, N)