inp = 'uugsqrei'
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

board = []
sol1 = 0
for i in range(128):
    s = inp+'-'+str(i)
    n = f'{knot(s):0>128b}'
    sol1 += n.count('1')
    board.append(n)

seen = set()
def mark_region(i, j):
    if i<0 or j<0 or i>127 or j>127:
        return
    if (i, j) in seen or board[i][j] == '0':
        return
    seen.add((i, j))
    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
        mark_region(i+di, j+dj)

sol2 = 0
for i in range(128):
    for j in range(128):
        if (i, j) not in seen and board[i][j] == '1':
            sol2 += 1
            mark_region(i, j)
print(sol1)
print(sol2)
