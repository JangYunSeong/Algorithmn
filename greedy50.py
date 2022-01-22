tmp = input().split()
line = int(tmp[0])
shop = int(tmp[1])
temp = input().split()
minSet = int(temp[0])
minOne = int(temp[1])
price = 0
for i in range(1,shop):
    temp = input().split()
    minSet = min(minSet,int(temp[0]))
    minOne = min(minOne,int(temp[1]))
while(True):
    if(line == 0):
        break
    if(line >=6):
        if(minSet <= minOne * 6):
            price += minSet
            line -=6
        else:
            price += minOne * 6
            line -=6
    else:
        if(minSet < minOne * line):
            price += minSet
            line = 0
        else:
            price += minOne * line
            line = 0
print(price)