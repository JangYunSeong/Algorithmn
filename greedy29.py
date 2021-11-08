size = int(input())
alphabet = []
value = []
answer = 0
for i in range(0,size):
    temp = input()
    for j in range(0,len(temp)):
        if(temp[j] not in alphabet):
            alphabet.append(temp[j])
            value.append(10**(len(temp) - j - 1))
        else:
            value[alphabet.index(temp[j])] += 10**(len(temp) - j - 1)
value.sort(reverse = True)
pivot = 9
for k in range(0,len(value)):
    answer += value[k] * pivot
    pivot -= 1
print(answer)