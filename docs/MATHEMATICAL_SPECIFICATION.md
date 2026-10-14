# Mathematical Specification

## Conventions
A table entry in row \(a\), column \(b\) means \(a \circ b\): apply \(b\) first and then \(a\). This convention applies to both permutation and symmetry composition.

## System A — Numbers
\[
\mathbb Z_6=\{0,1,2,3,4,5\},\qquad a+_6b=(a+b)\bmod6.
\]

| \(+_6\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 2 | 3 | 4 | 5 |
| 1 | 1 | 2 | 3 | 4 | 5 | 0 |
| 2 | 2 | 3 | 4 | 5 | 0 | 1 |
| 3 | 3 | 4 | 5 | 0 | 1 | 2 |
| 4 | 4 | 5 | 0 | 1 | 2 | 3 |
| 5 | 5 | 0 | 1 | 2 | 3 | 4 |

Identity: \(0\). Inverse of \(k\): \(-k\bmod6\).  
Orders: \(0:1,1:6,2:3,3:2,4:3,5:6\).  
Generators: \(1,5\).  
Subgroups: \(\{0\}\), \(\{0,3\}\), \(\{0,2,4\}\), \(\mathbb Z_6\).  
It is cyclic and abelian.

## System B — Permutations
\[
C=\langle r\rangle,\qquad r=(1\ 2\ 3\ 4\ 5\ 6).
\]

| \(\circ\) | \(e\) | \(r\) | \(r^2\) | \(r^3\) | \(r^4\) | \(r^5\) |
|---|---|---|---|---|---|---|
| \(e\) | \(e\) | \(r\) | \(r^2\) | \(r^3\) | \(r^4\) | \(r^5\) |
| \(r\) | \(r\) | \(r^2\) | \(r^3\) | \(r^4\) | \(r^5\) | \(e\) |
| \(r^2\) | \(r^2\) | \(r^3\) | \(r^4\) | \(r^5\) | \(e\) | \(r\) |
| \(r^3\) | \(r^3\) | \(r^4\) | \(r^5\) | \(e\) | \(r\) | \(r^2\) |
| \(r^4\) | \(r^4\) | \(r^5\) | \(e\) | \(r\) | \(r^2\) | \(r^3\) |
| \(r^5\) | \(r^5\) | \(e\) | \(r\) | \(r^2\) | \(r^3\) | \(r^4\) |

Identity: \(e\). Inverse: \((r^i)^{-1}=r^{6-i}\).  
Orders: \(e:1,r:6,r^2:3,r^3:2,r^4:3,r^5:6\).  
Generators: \(r,r^5\).  
Subgroups: \(\{e\}\), \(\{e,r^3\}\), \(\{e,r^2,r^4\}\), \(C\).  
It is cyclic and abelian.

## System C — Circular movement
\[
D_3=\{e,r,r^2,s,sr,sr^2\},
\]
where \(r\) is a \(120^\circ\) rotation and \(s\) is a reflection of an equilateral triangle:
\[
r^3=e,\qquad s^2=e,\qquad srs=r^{-1}=r^2.
\]

| \(\cdot\) | \(e\) | \(r\) | \(r^2\) | \(s\) | \(sr\) | \(sr^2\) |
|---|---|---|---|---|---|---|
| \(e\) | \(e\) | \(r\) | \(r^2\) | \(s\) | \(sr\) | \(sr^2\) |
| \(r\) | \(r\) | \(r^2\) | \(e\) | \(sr^2\) | \(s\) | \(sr\) |
| \(r^2\) | \(r^2\) | \(e\) | \(r\) | \(sr\) | \(sr^2\) | \(s\) |
| \(s\) | \(s\) | \(sr\) | \(sr^2\) | \(e\) | \(r\) | \(r^2\) |
| \(sr\) | \(sr\) | \(sr^2\) | \(s\) | \(r^2\) | \(e\) | \(r\) |
| \(sr^2\) | \(sr^2\) | \(s\) | \(sr\) | \(r\) | \(r^2\) | \(e\) |

Derived products:
\[
r^i(sr^j)=sr^{j-i},\quad (sr^i)r^j=sr^{i+j},\quad (sr^i)(sr^j)=r^{j-i}.
\]

Identity: \(e\). Inverses: \(r^{-1}=r^2\), \((r^2)^{-1}=r\), and each reflection is self-inverse.  
Orders: \(e:1,r:3,r^2:3,s:2,sr:2,sr^2:2\).  
Subgroups: \(\{e\}\), \(\{e,r,r^2\}\), \(\{e,s\}\), \(\{e,sr\}\), \(\{e,sr^2\}\), \(D_3\).  
It is non-abelian: \(rs=sr^2\ne sr=sr\).

## Structural conclusions
\[
\phi:\mathbb Z_6\to C,\qquad \phi(k)=r^k
\]
is an isomorphism because it is bijective and:
\[
\phi(a+_6b)=r^{a+b}=r^a\circ r^b.
\]

\(D_3\) is not isomorphic to either \(\mathbb Z_6\) or \(C\): it is non-abelian and has no element of order 6. Lagrange's theorem is illustrated because every listed subgroup order divides 6.
