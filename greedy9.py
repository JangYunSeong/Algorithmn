size = int(input())
arr = [0] * size
for i in range(0,size):
    arr[i] = int(input())
arr.sort()

temp = 0
answer = 0
while(1):
    temp = arr[0] + arr[1]
    answer += temp
    if(len(arr) == 2):
        break
    arr[1] = temp
    del arr[0]
    arr.sort()
print(answer)