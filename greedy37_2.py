testsize = int(input())
answerarray = [0] * testsize
for j in range(0,testsize):
    size = int(input())
    array = input().split()
    for i in range(0,size):
        array[i] = int(array[i])
    answer = 0
    pivot = 0
    for k in range(size-1,-1,-1):
        if(pivot < array[k]):
            pivot = array[k]
        else:
            answer += pivot - array[k]
    answerarray[j]=answer
for i in range(0,testsize):
    print(answerarray[i])
