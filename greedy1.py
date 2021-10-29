size, money = input().split()
size = int(size)
money = int(money)
a = [0] *size
for i in range(0,size):
    a[i] = int(input())

answer = 0
temp = 0
for j in range(size-1,-1,-1):
        if(money>=a[j]):
            temp = j
            break
for i in range(temp,-1, -1):
    while(1):
        if(money < a[i]):
            break
        money -= a[i]
        answer +=1
print(answer)
