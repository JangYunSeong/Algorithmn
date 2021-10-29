sum = int(input())
temp = 0
answer = 1
while(1):
    if((temp + answer)>sum):
        answer-=1
        break
    else:
        temp += answer
        answer += 1
print(answer)