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
