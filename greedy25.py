string = input()
check = 0
newStr = ""
answer = 0
for i in range(0,len(string)):
    if(string[i] == "X"):
        check += 1
    else:
        if(check % 2 == 1):
            answer = -1
            break
        else:
            a = check // 4
            for j in range(0,a):
                newStr += "AAAA"
            for k in range(0,check - 4*a):
                newStr += "B"
            check = 0
            newStr += "."
if(check % 2 == 1):
    answer = -1
t = check // 4
for j in range(0,t):
    newStr += "AAAA"
for k in range(0,check - 4*t):
    newStr += "B"
if(answer == -1):
    print(answer)
else:
    print(newStr)

        