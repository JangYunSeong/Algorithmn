temp = input().split()
book = int(temp[0])
size = int(temp[1])
array = input().split()
pos_pos = [0]
pos_neg = [0]
answer = 0
for i in range(0,book):
    if(int(array[i]) > 0):
        pos_pos.append(int(array[i]))
    else:
        pos_neg.append(-int(array[i]))
pos_pos.sort(reverse = True)
pos_neg.sort(reverse = True)
pivot = max(pos_pos[0], pos_neg[0])
for i in range(0,len(pos_pos), size):
    answer += pos_pos[i] * 2
for i in range(0,len(pos_neg), size):
    answer += pos_neg[i] * 2
answer -= pivot
print(answer)
