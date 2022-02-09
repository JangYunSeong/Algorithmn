n = int(input())
array = input().split()
for i in range(0,n):
    array[i] = int(array[i])
array.sort()
sum = 0
if(n % 2 ==0):
    sum1 = 0
    sum2 = 0
    pivot1 = array[n//2]
    pivot2 = array[n//2+1]
    for i in range(0,n):
        sum1 += abs(pivot1 -array[i])
        sum2 += abs(pivot2 - array[i])
    print(min(sum1, sum2))
else:
    pivot = array[n//2]
    for i in range(0,n):
        sum += abs(pivot-array[i])
    print(sum)