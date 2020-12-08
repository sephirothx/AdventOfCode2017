inp = open('input.txt').read().split(',')

s = list('abcdefghijklmnop')

def dance():
    global s
    for l in inp:
        i, v = l[0], l[1:]
        if i == 's':
            v = int(v)
            s = s[-v:]+s[:-v]
        elif i == 'x':
            a, b = v.split('/')
            a, b = int(a), int(b)
            s[a], s[b] = s[b], s[a]
        elif i == 'p':
            a, b = v.split('/')
            a, b = s.index(a), s.index(b)
            s[a], s[b] = s[b], s[a]

seen = set()
rep = 0
while True:
    if str(s) in seen:
        break
    rep += 1
    seen.add(str(s))
    dance()

for i in range(1000000000%rep):
    dance()

print(''.join(s))
