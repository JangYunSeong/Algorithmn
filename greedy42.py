size = int(input())
array = []
answer = 0
for i in range(0,size):
    array.append(int(input()))
array.sort(reverse = True)
for i in range(0,size):
    if(array[i] - i <= 0):
        break
    answer += array[i] - i
print(answer)