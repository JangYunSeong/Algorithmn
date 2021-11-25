size = int(input())
array = []
answer = 0
for i in range(0,size):
    array.append(int(input()))
array.sort(reverse = True)
for i in range(0,size):
    if(i % 3 == 2):
         pass
    else:
        answer += array[i]
print(answer)