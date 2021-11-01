#15093
temp = input().split()
size = int(temp[0])
choice = int(temp[1])
k = input().split()
card = []
for i in range(0,size):
    card.append(int(k[i]))
card.sort()
for j in range(0,choice):
    box = card[0]
    card[0] += card[1]
    card[1] += box
    card.sort()
answer = sum(card)
print(answer)