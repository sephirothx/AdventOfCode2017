inp = tuple(int(x) for x in open('input.txt').read().split())

def sol():
    global inp
    seen = set()
    ret = 0
    while inp not in seen:
        ret += 1
        seen.add(inp)
        n = max(inp)
        i = inp.index(n)
        tmp = list(inp)
        tmp[i] = 0
        for j in range(i+1, i+1+n):
            tmp[j%len(inp)] += 1
        inp = tuple(tmp)
    return ret

print(sol())
print(sol())
