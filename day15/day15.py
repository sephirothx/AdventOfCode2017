fa = 16807
fb = 48271

mod1 = 2147483647
mod2 = 1 << 16
sol1 = 0
sol2 = 0

def generate(x, fx, mod=1):
    x = (x*fx)%mod1
    while x%mod != 0:
        x = (x*fx)%mod1
    return x

a = 873
b = 583
for i in range(40000000):
    a = generate(a,fa)
    b = generate(b,fb)
    if a%mod2 == b%mod2:
        sol1 += 1
print(sol1)

a = 873
b = 583
for i in range(5000000):
    a = generate(a,fa,4)
    b = generate(b,fb,8)
    if a%mod2 == b%mod2:
        sol2 += 1
print(sol2)
