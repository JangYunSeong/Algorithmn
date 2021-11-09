size= int(input())
temp = input().split()
array = []
day = []
answer = []
for i in range(0,size):
    array.append(int(temp[i]))
    day.append(i + 1)
array.sort(reverse = True)
for i in range(0,size):
    answer.append(array[i] + day[i])
print(max(answer) + 1)