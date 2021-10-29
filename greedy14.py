size, length = input().split()
size = int(size)
length = int(length)
answer = 0
pipe = [0] * size
check = [0] * size
pipe = input().split()
for i in range(0,size):
    pipe[i] = int(pipe[i])
pipe.sort()
pipe.append(-10)
index = 0
while(1):
    if(index == size):
        if(check[-1] == 0):
            answer += 1
        break
    temp = index
    for i in pipe[index+1:]:
        if(pipe[index] + length > i):
            check[temp] = 1
            temp +=1
        else:
            check[temp] = 1
            temp += 1
            break
    answer += 1
    index = temp
print(answer)