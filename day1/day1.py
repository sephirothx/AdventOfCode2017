f = open('./input.txt')
INPUT = f.read()

sol = 0
l = len(INPUT)
for i in range(l):
    if INPUT[i] == INPUT[int(i + l/2) % l]:
        sol += int(INPUT[i])
print(sol)
