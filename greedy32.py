size = int(input())
array = input().split()
for i in range(0,size):
    array[i] = int(array[i])
answer = []
pivot = array[0]
count = 0
for i in range(1,size):
    if(pivot < array[i]):
        answer.append(count)
        pivot = array[i]
        count = 0
    else:
        count += 1
answer.append(count)
print(max(answer))