"""Independent verification for Cryptography Through Abstract Algebra."""
from itertools import permutations, product
from math import gcd
M = 26
UNITS = tuple(a for a in range(M) if gcd(a, M) == 1)
AFFINE = tuple((a, b) for a in UNITS for b in range(M))
def shift(k, x): return (x + k) % M
def affine(key, x):
    a, b = key
    if gcd(a, M) != 1: raise ValueError("invalid affine multiplier")
    return (a * x + b) % M
def affine_compose(f, g):
    a, b = f; c, d = g
    return ((a * c) % M, (a * d + b) % M)
def affine_inverse(f):
    a, b = f; inv = pow(a, -1, M)
    return (inv, (-inv * b) % M)
def perm_apply(p, block): return tuple(block[i] for i in p)
def perm_compose(p, q): return tuple(q[p[i]] for i in range(len(p)))
def perm_inverse(p):
    out = [0] * len(p)
    for i, x in enumerate(p): out[x] = i
    return tuple(out)
S4 = tuple(permutations(range(4)))
assert len({shift(k, 0) for k in range(M)}) == 26
assert all(shift(k, shift(l, x)) == shift((k+l) % M, x) for k,l,x in product(range(M), repeat=3))
assert all(shift((-k) % M, shift(k, x)) == x for k,x in product(range(M), repeat=2))
assert len(UNITS) == 12 and len(AFFINE) == 312
assert all(affine_compose(f,g) in AFFINE for f,g in product(AFFINE, repeat=2))
assert all(affine(affine_compose(f,g),x) == affine(f,affine(g,x)) for f,g in product(AFFINE, repeat=2) for x in range(M))
assert all(affine(affine_inverse(f),affine(f,x)) == x for f in AFFINE for x in range(M))
assert len(S4) == 24 and all(perm_compose(p,q) in S4 for p,q in product(S4, repeat=2))
assert all(perm_apply(perm_compose(p,q),x) == perm_apply(p,perm_apply(q,x)) for p,q in product(S4, repeat=2) for x in permutations(range(4)))
assert all(perm_apply(perm_inverse(p),perm_apply(p,x)) == x for p in S4 for x in permutations(range(4)))
assert perm_apply((2,0,3,1),tuple("ABCD")) == tuple("CADB")
assert perm_compose((1,0,2,3),(0,2,1,3)) != perm_compose((0,2,1,3),(1,0,2,3))
print("Caesar: 26 shifts, composition and inverses verified.")
print("Affine: 12 valid multipliers, 312 maps, composition and inverses verified.")
print("S4: 24 permutations, convention, composition, inverses and noncommutativity verified.")
print("All cryptography mathematical verification checks passed.")
