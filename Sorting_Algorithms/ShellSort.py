import random, time

def shellSort(a, n):
    h = n // 2
    while h > 0:
        for i in range(h, n):
            tmp = a[i]
            j = i - h
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 2

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
a.reverse()
start_time = time.time()
shellSort(a, N)
end_time = time.time() - start_time
print("Executing time (N = %d) : %0.3f" %(N, end_time))
checkSort(a, N)