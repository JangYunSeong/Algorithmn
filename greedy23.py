import sys
input=sys.stdin.readline
size=int(input())
hw=[tuple(map(int,input().split())) for _ in range(size)]
hw.sort(key=lambda x:[-x[1]])
date=[0]*max(hw[0])

for day,w in hw:
    if date[day]==0: date[day]=w
    else:
        for i in range(day,0,-1):
            if date[i]==0:
                date[i]=w
                break
print(sum(date))