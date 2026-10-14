"""Independent verification of the approved mathematical specification.

A product a * b means: apply b first, then a.
Run: python scripts/verify_math.py
"""
from itertools import combinations, product

Z6 = tuple(range(6))
D3 = ("e", "r", "r2", "s", "sr", "sr2")


def add_mod_6(a, b):
    return (a + b) % 6


# Permutations are tuples giving the images of 1,...,6.
IDENTITY_PERM = (1, 2, 3, 4, 5, 6)
R_PERM = (2, 3, 4, 5, 6, 1)


def compose(p, q):
    """Return p after q."""
    return tuple(p[q[i] - 1] for i in range(6))


def power(op, identity, element, n):
    value = identity
    for _ in range(n):
        value = op(value, element)
    return value


C6 = tuple(power(compose, IDENTITY_PERM, R_PERM, k) for k in range(6))


def d3_product(x, y):
    """Return x after y in D3, with elements written r^i or s r^i."""
    encode = {
        "e": ("R", 0), "r": ("R", 1), "r2": ("R", 2),
        "s": ("S", 0), "sr": ("S", 1), "sr2": ("S", 2),
    }
    decode = {value: key for key, value in encode.items()}
    left_kind, i = encode[x]
    right_kind, j = encode[y]

    if left_kind == "R" and right_kind == "R":
        result = ("R", (i + j) % 3)
    elif left_kind == "R" and right_kind == "S":
        result = ("S", (j - i) % 3)
    elif left_kind == "S" and right_kind == "R":
        result = ("S", (i + j) % 3)
    else:
        result = ("R", (j - i) % 3)

    return decode[result]


def group_checks(elements, operation, identity):
    return {
        "closure": all(operation(a, b) in elements for a, b in product(elements, repeat=2)),
        "associativity": all(
            operation(operation(a, b), c) == operation(a, operation(b, c))
            for a, b, c in product(elements, repeat=3)
        ),
        "identity": all(
            operation(identity, a) == a and operation(a, identity) == a
            for a in elements
        ),
        "inverses": all(
            any(operation(a, b) == identity and operation(b, a) == identity for b in elements)
            for a in elements
        ),
        "commutativity": all(
            operation(a, b) == operation(b, a) for a, b in product(elements, repeat=2)
        ),
    }


def element_order(elements, operation, identity, element):
    value = identity
    for n in range(1, len(elements) + 1):
        value = operation(value, element)
        if value == identity:
            return n
    raise AssertionError("No order found")


def generated_subgroup(elements, operation, identity, generator):
    values = []
    current = identity
    while current not in values:
        values.append(current)
        current = operation(current, generator)
    return frozenset(values)


def all_subgroups(elements, operation, identity):
    result = set()
    for size in range(1, len(elements) + 1):
        for members in combinations(elements, size):
            subgroup = frozenset(members)
            if identity not in subgroup:
                continue
            if all(operation(a, b) in subgroup for a, b in product(subgroup, repeat=2)):
                if all(
                    any(operation(a, b) == identity and operation(b, a) == identity for b in subgroup)
                    for a in subgroup
                ):
                    result.add(subgroup)
    return result


EXPECTED_D3_TABLE = [
    ["e", "r", "r2", "s", "sr", "sr2"],
    ["r", "r2", "e", "sr2", "s", "sr"],
    ["r2", "e", "r", "sr", "sr2", "s"],
    ["s", "sr", "sr2", "e", "r", "r2"],
    ["sr", "sr2", "s", "r2", "e", "r"],
    ["sr2", "s", "sr", "r", "r2", "e"],
]

EXPECTED_Z6_SUBGROUPS = {
    frozenset({0}),
    frozenset({0, 3}),
    frozenset({0, 2, 4}),
    frozenset(Z6),
}

EXPECTED_D3_SUBGROUPS = {
    frozenset({"e"}),
    frozenset({"e", "r", "r2"}),
    frozenset({"e", "s"}),
    frozenset({"e", "sr"}),
    frozenset({"e", "sr2"}),
    frozenset(D3),
}

assert [[d3_product(a, b) for b in D3] for a in D3] == EXPECTED_D3_TABLE

assert group_checks(Z6, add_mod_6, 0) == {
    "closure": True, "associativity": True, "identity": True,
    "inverses": True, "commutativity": True,
}
assert group_checks(C6, compose, IDENTITY_PERM) == {
    "closure": True, "associativity": True, "identity": True,
    "inverses": True, "commutativity": True,
}
assert group_checks(D3, d3_product, "e") == {
    "closure": True, "associativity": True, "identity": True,
    "inverses": True, "commutativity": False,
}

assert len(set(C6)) == 6
assert all(compose(C6[a], C6[b]) == C6[(a + b) % 6] for a, b in product(Z6, repeat=2))
assert all_subgroups(Z6, add_mod_6, 0) == EXPECTED_Z6_SUBGROUPS
assert all_subgroups(D3, d3_product, "e") == EXPECTED_D3_SUBGROUPS
assert generated_subgroup(Z6, add_mod_6, 0, 1) == frozenset(Z6)
assert generated_subgroup(Z6, add_mod_6, 0, 5) == frozenset(Z6)
assert not any(len(generated_subgroup(D3, d3_product, "e", x)) == 6 for x in D3)

z6_orders = [element_order(Z6, add_mod_6, 0, x) for x in Z6]
permutation_orders = [element_order(C6, compose, IDENTITY_PERM, x) for x in C6]
d3_orders = [element_order(D3, d3_product, "e", x) for x in D3]
assert z6_orders == [1, 6, 3, 2, 3, 6]
assert permutation_orders == [1, 6, 3, 2, 3, 6]
assert d3_orders == [1, 3, 3, 2, 2, 2]

print("All approved mathematical verification checks passed.")
print("D3 table: exact 36-entry match.")
print("Permutation powers: 6 distinct powers; all 36 products verified.")
print("Z6 subgroups: exact approved list verified.")
print("D3 subgroups: exact approved list verified.")
print("Z6 orders:", z6_orders)
print("Permutation orders:", permutation_orders)
print("D3 orders:", d3_orders)
print("Isomorphism k -> r^k: all 36 operation-preservation pairs verified.")
print("D3 noncommuting witness: r*s =", d3_product("r", "s"), "; s*r =", d3_product("s", "r"))
