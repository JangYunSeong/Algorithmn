start = input()
complete = input()
size = len(complete)
newArray = ""
answer = 0
while(1):
    k = len(complete) - 1
    print(complete)
    print(k)
    if(start == complete):
        answer = 1
        break
    if(k <= 0):
        break
    if(complete[k] == "A"):
        complete = complete[0:k -1]
    elif(complete[k] == "B"):
        complete = complete[0:k -1]
        for i in range(len(complete)-1, -1, -1):
            newArray += complete[i]
        complete = ""
        complete += newArray
        print(newArray)
        newArray = ""
print(answer)
    
