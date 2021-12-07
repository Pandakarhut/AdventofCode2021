from functools import reduce
# my code
f = open("input.txt", "r")
gamma = ""
epsilon = ""
count_one = 0
list = []
for x in f:
    list.append(x)
for i in range(12):
    for item in list:
        if item[i] == "1":
            count_one += 1
    if count_one > (len(list) / 2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    count_one = 0
print(int(gamma, 2) * int(epsilon, 2))

# part 1+2
N = [*open('input.txt')]
a, b, c, d = [int(reduce(lambda x, y:x+'01'[t([int(l[y])for l in N if x == l[:len(x)] or m])], range(len(N[0])-1), ''), 2)
              for t in (lambda x:2*sum(x) >= len(x), lambda x:0 < 2*sum(x) < len(x) or all(x))for m in (0, 1)]
print(b*d, a*c)
