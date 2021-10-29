a,b = input().split()
answer = 1
while(1):
    if(a == b):
        break
    if(int(a) > int(b)):
        answer = -1
        break
    if(b[-1] =='1' and len(b) > 1):
        b = b[:-1]
        answer += 1
    else:
        if(int(b) % 2 == 1):
            answer = -1
            break
        else:
            b = int(b) / 2
            b = str(int(b))
            answer += 1
print(answer)
