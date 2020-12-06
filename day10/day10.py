inp = [ord(c) for c in open('input.txt').read()]
inp.extend([17, 31, 73, 47, 23])

RANGE = 256

pos = 0
skip = 0
l = [x for x in range(RANGE)]

for _ in range(64):
    for i in inp:
        tmp = l[pos:]+l[:pos]
        tmp[:i] = tmp[:i][::-1]
        l = tmp[(RANGE-pos):]+tmp[:(RANGE-pos)]
        pos += (i + skip)
        pos %= RANGE
        skip += 1

knot = []
curr = 0
for i in range(RANGE):
    curr ^= l[i]
    if (i+1) % 16 == 0:
        knot.append(curr)
        curr = 0

for i in knot:
    print(f'{i:0>2x}', end='')
