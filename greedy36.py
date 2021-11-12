temp = input().split()
screen = int(temp[0])
basket = int(temp[1])
size = int(input())
pivot = [1,basket]
answer = 0
for i in range(0,size):
    count = int(input())
    if(pivot[1] < count):
        answer += count - pivot[1]
        pivot = [count-basket + 1, count]
    elif(pivot[0] > count):
        answer += pivot[0] - count
        pivot = [count, count+basket - 1]
    print(pivot,' , ',answer)
print(answer)