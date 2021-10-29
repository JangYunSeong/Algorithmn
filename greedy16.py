plugSize, size = input().split()
plugSize = int(plugSize)
size = int(size)
plug = [0] * plugSize
step = [0] * size
step = input().split()
answer = 0
index = 1
index_p = 0
for i in range(0,size):
    step[i] = int(step[i])
plug[0] = step[0]
while(1):
    if(index_p == plugSize - 1):
        break
    if step[index] == plug[index_p]:
        index += 1
    else:
        index_p+=1
        plug[index_p] = step[index]
        index+=1
for i in range(index ,size):
    if step[i] in plug:
        pass
    else:
        flag = 0
        for j in range(0,plugSize):
            if plug[j] not in step[i + 1:]:
                plug[j] = step[i]
                answer += 1
                flag = 1
                break
        if(flag == 0):
            answer+=1
print(answer)
        

