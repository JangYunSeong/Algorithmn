size = int(input())
count=0
array = [0] * size
for i in range(0,size):
    array[i] = int(input())
    if array[i]<0:
        count += 1
array.sort(reverse=1)
index = 0
answer = 0
while(1):
    if(index == size):
        break
    if(index == size - 1):
        if size == 1:
            answer += array[-1]
            break
        if array[-2] == 0:
            pass
        else:
            answer += array[-1]
        break
    if(array[index] * array[index+1]) > 0:
        if array[index] == 1 or array[index + 1] == 1:
            answer += array[index]
            index+=1
        else:
            if(count % 2 == 1 and array[index] < 0):
                if 0 in array:
                    count = 0
                    index += 1
                else:
                    answer += array[index]
                    count = 0
                    index += 1
            else:
                answer += (array[index] * array[index + 1])
                index += 2
    else:
        answer += array[index]
        index += 1
print(answer)