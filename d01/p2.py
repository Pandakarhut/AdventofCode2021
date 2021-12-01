f = open("input.txt", "r")
count = 0
list = []
for x in f:
    list.append(int(x))

for i in range(len(list) - 3):
    if list[i] < list[i+3]:
        count += 1
print(f'Count: {count}')

# 0	1 A
# 1	2 A B
# 2	3 A B C
# 3	4 D B C
# 4	5 D E C
# 5	6 D E F
# 6	7	E F
