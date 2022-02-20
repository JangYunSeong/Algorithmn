n = int(input())
k = int(input())
array = input().split()
new = [0] * (n - 1) 
for i in range(0,n):
    array[i] = int(array[i])
array.sort()
for i in range(0,n-1):
    new[i] = array[i+1] - array[i]
# print(array)
# print(new)
if(k >= n):
    print(0)
else:
    start = 0
    result = []
    tmp = 0
    for i in range(0,n-1):
        if(tmp + new[i] >= max(new)):
            result.append(array[start:i+1])
            tmp = 0
            k -= 1
            start = i+1
        else:
            tmp += new[i]
        if(k == 1):
            result.append(array[start:])
            break
    ans = 0
    for i in range(0,len(result)):
        ans += max(result[i]) - min(result[i])
    print(ans)