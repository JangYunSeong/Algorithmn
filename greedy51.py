import queue

size = input().split()
N = int(size[0])
K = int(size[1])
array = []
price = 0
for i in range(0,N):
    tmp = input().split()
    array.append([int(tmp[0]),int(tmp[1])])
for i in range(0,K):
    array.append([int(input()), 2000000])
array.sort()
pq = queue.PriorityQueue(N)
for i in array:
    if i[1] != 2000000:
        pq.put(-i[1])
    else:
        if(not(pq.empty())):
            t = -pq.get()
            price += t
print(price)