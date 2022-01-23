str = input()
array = []
index = []
answer = ''
for i in range(0,len(str)):
    if(str[i] in array):
        index[array.index(str[i])]+=1
    else:
        array.append(str[i])
        index.append(1)
count = 0
middle = ''
new = []
tmp = ''
for i in index:
    if(i % 2 == 1):
        middle = array[index.index(i)]
        count +=1
if(count > 1):
    answer = "I'm Sorry Hansoo"
    print(answer)
else:
    for i in range(0,len(index)):
        index[i] = index[i] // 2
    for j in range(0,len(array)):
        tmp += array[j] * index[j]
    for k in tmp:
        new.append(k)
    new.sort()
    for m in new:
        answer += m
    print(answer + middle + "".join(reversed(answer)))
    