size = int(input())
array = input().split()
for i in range(0,size):
    array[i] = int(array[i])
answer = 0
pos = 0
for k in array:
    if(pos % 3 == k):
        pos += 1
        answer += 1
print(answer)