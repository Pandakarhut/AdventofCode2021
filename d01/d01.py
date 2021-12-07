f = open("input.txt", "r")
tmp = 0
count = 0
for x in f:
    if tmp == 0:
        tmp = int(x)
    else:
        if int(x) > tmp:
            count += 1
        tmp = int(x)
print(count)

//part 2
f = open("input.txt", "r")
count = 0
list = []
for x in f:
    list.append(int(x))

for i in range(len(list) - 3):
    if list[i] < list[i+3]:
        count += 1
print(f'Count: {count}')
