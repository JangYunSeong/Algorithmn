size = int(input())
array = [1,1,2,3,5]
answer = []
for i in range(0,size):
    temp = []
    number = int(input())
    while(True):
        if(number > array[-1]):
            array.append(array[-2] + array[-1])
        else:
            break
    for i in range(len(array)-1, -1,-1):
        if(number >= array[i]):
            temp.append(array[i])
            number -= array[i]
    temp.sort()
    for i in temp:
        print(i, end= ' ')
    print()
