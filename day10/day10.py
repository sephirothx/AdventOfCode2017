inp = open('input.txt').read()

RANGE = 256

def knot(s):
    s = [ord(c) for c in s] + [17,31,73,47,23]
    pos = 0
    skip = 0
    l = [x for x in range(RANGE)]
    for _ in range(64):
        for i in s:
            tmp = l[pos:]+l[:pos]
            tmp[:i] = tmp[:i][::-1]
            l = tmp[(RANGE-pos):]+tmp[:(RANGE-pos)]
            pos += (i + skip)
            pos %= RANGE
            skip += 1
    k = 0
    curr = 0
    for i in range(RANGE):
        curr ^= l[i]
        if (i+1) % 16 == 0:
            k = (k << 8) + curr
            curr = 0
    return k

print(f'{knot(inp):x}')
