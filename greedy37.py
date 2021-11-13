testsize = int(input())
answerarray = [0] * testsize
for j in range(0,testsize):
    size = int(input())
    array = input().split()
    for i in range(0,size):
        array[i] = int(array[i])
    stock = 0
    price = 0
    answer = 0
    for k in range(0,size):
        if(array[k] < max(array[k:])):
            stock += 1
            price += array[k]
        else:
            answer += stock * array[k] - price
            stock = 0
            price = 0
    answerarray[j]=answer
for i in range(0,testsize):
    print(answerarray[i])
