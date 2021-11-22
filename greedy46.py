temp = input().split()
ball  = int(temp[0])
basket = int(temp[1])
array = [0] * basket
answer = 0
for i in range(0,basket):
    array[i] = basket - i
if(sum(array) > ball):
    answer = -1
else:
    for i in range(0,(ball-sum(array))):
        array[i % basket] += 1
    answer = array[0] - array[basket-1]
print(answer)