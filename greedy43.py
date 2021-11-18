size = int(input())
array = []
answer = 0
for i in range(0,size):
    array.append(int(input()))
array.sort()
for i in range(0,size):
    if(array[i]< i + 1):
        answer += i + 1 -array[i]
    else:
        answer += array[i] - (i + 1)
print(answer)