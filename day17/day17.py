inp = 328

l = [0]
curr = 0
for i in range(1, 50000000):
    curr = (curr + inp) % len(l) + 1
    if curr == 1:
        print(i)
    l.insert(curr, i)
