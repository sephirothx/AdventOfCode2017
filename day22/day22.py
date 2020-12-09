from collections import defaultdict
inp = open('input.txt').read().splitlines()

CLEAN = '.'
INFECTED = '#'
WEAKENED = 'W'
FLAGGED = 'F'

pos = (len(inp)//2, len(inp)//2)
d = [0, -1]
board = defaultdict(lambda: CLEAN)
for i in range(len(inp)):
    for j in range(len(inp[i])):
        board[(j, i)] = inp[i][j]

sol = 0
for i in range(10000000):
    if board[pos] == CLEAN:
        d[0], d[1] = d[1], -d[0]
        board[pos] = WEAKENED
    elif board[pos] == INFECTED:
        d[0], d[1] = -d[1], d[0]
        board[pos] = FLAGGED
    elif board[pos] == WEAKENED:
        sol += 1
        board[pos] = INFECTED
    elif board[pos] == FLAGGED:
        d[0], d[1] = -d[0], -d[1]
        board[pos] = CLEAN
    pos = (pos[0]+d[0], pos[1]+d[1])
print(sol)
