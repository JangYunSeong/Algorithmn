temp = input().split()
fruit = int(temp[0])
size = int(temp[1])
array = input().split()
for i in range(0,fruit):
    array[i] = int(array[i])
array.sort()
for i in range(0,fruit):
    if(size >= array[i]):
        size += 1
print(size)
