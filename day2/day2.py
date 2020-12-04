inp = open('./input.txt').read().splitlines()

checksum1 = 0
checksum2 = 0
for l in inp:
    nums = [int(x) for x in l.split()]
    hi, lo = max(nums), min(nums)
    checksum1 += hi - lo
    for n, m in [(n,m) for n in nums for m in nums]:
        if n == m:
            continue
        if n % m == 0:
            checksum2 += n // m

print(checksum1)
print(checksum2)
