size = int(input())
day = 0
lecture = []
for i in range(0,size):
    temp = input().split()
    lecture.append([int(temp[0]),int(temp[1])])
    if(day < int(temp[1])):
        day = int(temp[1])
lecture.sort(reverse = True)
plan = [0] * (day + 1)
for w,d in lecture:
    if plan[d] == 0:
        plan[d] = w
    else:
        for i in range(d,0,-1):
            if(plan[i] == 0):
                plan[i] = w
                break
print(sum(plan))