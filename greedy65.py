l, r = input().split()
count = 0
if len(l) == len(r):
    for i in range(0,len(l)):
        if(l[i] < r[i]):
            break
        else:
            if(l[i] == '8' and r[i] == '8'):
                count += 1
else:
    count = 0
print(count)