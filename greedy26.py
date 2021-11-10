start = input()
complete = input()
size = len(complete)
array = []
answer = -1
for i in range(0,size):
    array.append(complete[i])
while(1):
    pivot = len(array) - 1
    if(pivot < 0):
        answer = 0
        break
    if(array[pivot] == 'A'):
        del array[pivot]
    else:
        del array[pivot]
        array.reverse()
    test = ""
    for j in range(0,len(array)):
        test += array[j]
    if(test == start):
        answer = 1
        break
print(answer)
