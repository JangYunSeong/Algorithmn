size = int(input())
array = []
answer  = 0
for i in range(0,size):
    temp = int(input())
    array.append(temp)
for i in range(size - 1, -1, -1):
    for j in range(i-1,-1, -1):
        if(array[i] <= array[j]):
            temp = array[j] - array[i] + 1
            answer += temp
            array[j] -= temp
print(answer)