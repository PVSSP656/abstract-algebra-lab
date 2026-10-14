# Implementation Plan

## P0
- src/math/caesar.ts: shifts, composition, inverse.
- src/math/affine.ts: validation, modular inverse, maps, composition, inverse.
- src/math/permutation.ts: S4 keys, documented block policy, composition, inverse.
- tests/math/: engine assertions mirrored by scripts/verify_math.py.
- src/ui/: playground, visualiser, algebra laboratory, comparison dashboard.

## Milestones
| Date | Evidence |
|---|---|
| Oct 14–15 | Migration and independent verification |
| Oct 16–18 | Typed engines and unit tests |
| Oct 19–22 | P0 playground and visualiser |
| Oct 23–25 | Algebra/comparison views and integration tests |
| Oct 26 | Deployment rehearsal |
| Oct 27–29 | Paper, figures, slides, rehearsal |
| Oct 30–31 | Freeze, final checks, submission |

## Team
Project Lead: engine, integration, deployment. Dotto: paired engine/tests. Varun: test cases and mathematical examples. Pavani: sources, paper, acceptance checklist. Ananya: explanations, usability, slides and rehearsal.

## Acceptance
Every cipher round-trips; invalid keys are explained; displayed calculations use the engine; independent verification passes; comparison states structural facts and security limits accurately.
