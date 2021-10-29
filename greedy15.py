string = input()
sample = input()

answer = 0
while(1):
    if sample in string:
        string = string[:string.index(sample)] +"0"+ string[string.index(sample)+len(sample):]
        answer += 1
    else:
        break
print(answer)