size = int(input())
array = []
money = [25,10,5,1]
for i in range(0,size):
    temp = int(input())
    array.append(temp)
for j in range(0,size):
    temp = []
    for k in money:
        count = 0
        while(1):
            if(array[j] < k):
                temp.append(count)
                break
            else:
                array[j] -= k
                count += 1
    print(temp[0], temp[1], temp[2], temp[3])
    