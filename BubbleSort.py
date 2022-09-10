import random, time


def BubbleSort(a, n):
    for i in range(n, 0, -1):
        for j in range(1, i-1):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp

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
BubbleSort(a, N)
end_time = time.time() - start_time
print("Executing time (N = %d) : %0.3f" %(N, end_time))
checkSort(a, N)