complete = [1, 1, 2, 2, 2, 8]
num_list = list(map(int, input().split()))

for i in range(0, 6):
    num_list[i] = complete[i] - num_list[i]
    
for j in range(0, 6):
    print(num_list[j], end=' ')