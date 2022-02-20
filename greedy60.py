n = int(input())
array = input().split()
count = 1
position = [0] * (n + 1)
max = -1
for i in range(0,n):
    array[i] = int(array[i])
    position[array[i]] = i
for i in range(1,n-1):
    if(position[i] < position[i+1]):
        count+=1
        if(count > max):
            max = count
    else:
        count = 1
print(n-max)