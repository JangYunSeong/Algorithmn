inputing = input()
answer = 0
if "-" in inputing:
    temp = inputing.split("-")
    if '+' in temp[0]:
        k = temp[0].split("+")
        for t in k:
            answer += int(t)
    else:
        answer = int(temp[0])
    for i in temp[1:]:
        if '+' in i:
            k = i.split("+")
            for t in k:
                answer -= int(t)
        else:
            answer -= int(i)
else:
    k = inputing.split("+")
    for t in k:
        answer += int(t)
print(answer)