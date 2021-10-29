count = 0
total = []
while(1):
    l,p,v = input().split()
    l = int(l)
    p = int(p)
    v = int(v)
    if(l==0 and p ==0 and v== 0):
        break
    count += 1
    answer = 0
    quo = v // p
    answer += l * quo
    remain = v % p 
    if(remain < l):
        answer += remain
    else:
        answer += l
    total.append(answer)
for i in range(0,count):
    print("Case "+str(i)+": "+str(total[i]))

