size = int(input())
tempA = input().split()
tempB = input().split()
a = [0] * size
b = [0] * size
answer = 0

for i in range(0,size):
    a[i] = int(tempA[i])
    b[i] = int(tempB[i])
a.sort(reverse = False)
b.sort(reverse = True)
for i in range(0,size):
    answer += a[i] * b[i]
print(answer)

