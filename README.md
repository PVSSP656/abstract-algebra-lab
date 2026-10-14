# Cryptography Through Abstract Algebra

**An Interactive Study of Three Transformation Systems** — TMAT302L, VIT Vellore.

## Purpose
An educational cryptography laboratory showing how groups, composition, identities, inverses, orders, cyclicity, commutativity, and structural comparison explain reversible classical transformations. It does not claim a new cipher or real-world security.

## Official systems
1. Caesar shifts modulo 26 — cyclic group of order 26.
2. Invertible affine maps modulo 26 — group of order 312.
3. Position permutations on four-letter blocks — S4, group of order 24.

The groups share the axioms but are not all isomorphic. Group structure is not the same as cryptographic security.

## Current stage
Scope migration and mathematical verification. No website UI has been implemented.

## Verify
```bash
python scripts/verify_math.py
```

- [Project Charter](docs/PROJECT_CHARTER.md)
- [Mathematical Specification](docs/MATHEMATICAL_SPECIFICATION.md)
- [Implementation Plan](docs/IMPLEMENTATION_PLAN.md)
- [Independent Verification](scripts/verify_math.py)

The prior six-element comparison is preserved in Git history as a legacy example, not active scope.
