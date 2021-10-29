case = int(input())
size = [0] * case
answer = [0] * case
for i in range(0,case):
    size[i] = int(input())
    test = [0] * size[i]
    answer[i] = size[i]
    for j in range(0,size[i]):
        test[j] = input().split()
    test.sort()
    for t in test:
        for j in test[test.index(t):]:
            if(t[1] < j[1]):
                test.remove(j)
                answer[i]-=1
for i in range(0,len(answer)):
    print(answer[i])