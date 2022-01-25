size = int(input())
load = input().split()
city = input().split()
for i in range(0,size - 1):
    load[i] = int(load[i])
    city[i] = int(city[i])
city[size-1] = int(city[size-1])
oil = city[0]
answer = load[0] * city[0]
for i in range(1,size-1):
    oil = min(oil,city[i])
    answer += oil * load[i]
print(answer)
