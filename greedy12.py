size = int(input())
weight = [0] * size
weight = input().split()
for i in range(0, size):
    weight[i] = int(weight[i])

weight.sort(reverse = 1)
answer = 1
while(1):
    flag = 0
    temp = answer
    for i in weight:
        if(temp > i):
            temp -= i
        elif(temp < i):
            pass
        else:
            answer+=1
            flag = 1
            break
    if(flag == 0):
        break
print(answer)