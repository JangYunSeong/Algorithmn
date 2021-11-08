#11399
size = int(input())
temp = input().split()
array = [0] * size
for i in range(0,size):
    array[i] = int(temp[i])
array.sort()
answer = 0
for i in range(0,size):
    answer += (array[i]) * (size - i)
print(answer)
