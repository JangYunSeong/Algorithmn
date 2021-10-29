size = int(input())
array = [0] * size
max = 0
answer = 0
for i in range(0, size):
    array[i] = input().split()
    array[i][0] = int(array[i][0])
    array[i][1] = int(array[i][1])
    array[i].append(array[i][1] - array[i][0])
    if(max < array[i][1]):
        max = array[i][1]
time = [1] * (max + 1)
array.sort(key = lambda x:x[2])

for i in array:
    flag = 0
    if(time[i[0]] != 0 and time[i[1]] != 0):
        if flag in time[i[0]:i[1]]:
            pass
        else:
            for k in range(i[0] + 1, i[1]):
                time[k] = 0
            answer += 1
    else:
        pass

print(answer)
    