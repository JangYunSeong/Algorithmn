size = int(input())
array = input().split()
start = 0
answer = 0
for i in range(0,size):
    array[i] = int(array[i])
array.sort()
for i in range(0,size):
    if(start + 1 < array[i]):
        break
    else:
        start += array[i]
answer = start + 1
print(answer)
