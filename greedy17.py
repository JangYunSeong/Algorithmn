def sum2(dice):
    min = max(dice)
    index = 0
    sum = 0
    array = []
    array_r = []
    for j in range(0,2):
        for i in range(0,6):
            if(min >= dice[i]):
                if i not in array and i not in array_r:
                    index = i
                    min = dice[i]
        array.append(index)
        array_r.append(5-index)
        sum += min
        index = 0
        min = max(dice)
    return sum
def sum3(dice):
    min = max(dice)
    index = 0
    sum = 0
    array = []
    array_r = []
    for j in range(0,3):
        for i in range(0,6):
            if(min >=dice[i]):
                if i not in array and i not in array_r:
                    index = i
                    min = dice[i]
        array.append(index)
        array_r.append(5-index)
        sum += min
        index = 0
        min = max(dice)
    return sum
size = int(input())
dice = input().split()
answer = 0
for i in range(0,6):
    dice[i] = int(dice[i])
if(size == 1):
    answer = dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5] - max(dice)
elif(size > 1):
    answer = (8 * size - 12) * sum2(dice) + 4 * sum3(dice) + min(dice) * ((size-2)**2) + 4 * min(dice) * (size - 2) * (size - 1)
print(answer)
     