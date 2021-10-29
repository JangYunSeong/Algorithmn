cook = [300,60,10]
count =[0] * 3
time = int(input())
for i in range(0,3):
    if(time<cook[i]):
        pass
    else:
        while(1):
            time -=cook[i]
            count[i] += 1
            if(time < cook[i]):
                break
if(time != 0):
    print(-1)
else:
    print(str(count[0])+' ' + str(count[1])+' ' + str(count[2]))