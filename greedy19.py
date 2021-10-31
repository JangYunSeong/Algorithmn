testing = int(input())
for i in range(0, testing):
    size = input().split()
    book = int(size[0])
    student = int(size[1])
    array = []
    start = []
    end = []
    answer = 0
    for k in range(1,book + 1):
        array.append(k)
    for i in range(0,student):
        case = input().split()
        start.append(int(case[0]))
        end.append(int(case[1]))
    for j in range(0,student):
        k = end.index(min(end))
        print("(" + str(start[k])+"," + str(end[k])+")")
        for i in range(start[k], end[k] + 1):
            if i in array:
                array.remove(i)
                answer += 1
                break
        del start[k]
        del end[k]
    print(answer)

