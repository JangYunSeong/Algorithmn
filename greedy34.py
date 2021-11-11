size = int(input())
array = input()
count = 0
answer = 0
for i in range(0,size):
    if(array[i] == 'L'):
        count += 1
if(count % 2 == 1):
    answer = -1
else:
    if(count == 0):
        answer = size
    else:
        answer = size - (count // 2) + 1
print(answer)