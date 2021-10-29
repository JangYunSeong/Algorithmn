size = int(input())
dice = input().split()
for i in range(0,6):
    dice[i] = int(dice[i])
answer = 0
if(size == 1):
    for i in range(0,6):
        answer += dice[i]
    answer -= max(dice)
elif size > 1:
    array = []
    array.append(min(dice[0],dice[5]))
    array.append(min(dice[1],dice[4]))
    array.append(min(dice[2],dice[3]))
    array.sort(reverse=0)
    sum2 = array[0] + array[1]
    sum3 = array[0] + array[1] + array[2]
    answer = 4 * sum3 + (8*size - 12) * sum2 + ((size - 2) ** 2) * array[0] + 4*(size - 1) * (size - 2) * array[0]
print(answer)