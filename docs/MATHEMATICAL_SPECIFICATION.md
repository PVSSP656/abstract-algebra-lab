# Mathematical Specification

## Convention
For functions, f composed with g means f(g(x)): apply g first. A transformation group helps explain reversibility but does not establish cipher security.

## Caesar shifts
Encode A=0 through Z=25.
E_k(x)=(x+k) mod 26 and D_k(y)=(y-k) mod 26.
There are 26 shifts: E_k composed with E_l = E_(k+l mod 26), identity E_0, inverse E_(-k mod 26). This is cyclic and abelian. Key 3 maps HELLO to KHOOR through the engine.

## Invertible affine maps
E_(a,b)(x)=(a*x+b) mod 26, where gcd(a,26)=1 and b is in Z_26.
There are phi(26)=12 valid multipliers and 12*26=312 maps.
E_(a,b) composed with E_(c,d)=E_(ac mod 26, ad+b mod 26).
Identity E_(1,0); inverse E_(a^-1, -a^-1*b mod 26).
Reject invalid multipliers. The affine group is non-abelian and not isomorphic to the Caesar group because its order is 312 rather than 26.

## Position permutations
Use S4, with 24 permutations of four positions. A UI key [p1,p2,p3,p4] is one-based: output position i receives input position p_i. Thus [3,1,4,2] maps ABCD to CADB.
Internally, out[i]=in[p[i]], and (p composed with q)[i]=q[p[i]]. The inverse restores the block. Convert letters to uppercase, preserve nonletters at original positions, permute complete alphabetic blocks of four, and leave a final incomplete alphabetic block unchanged. S4 is non-abelian and not isomorphic to C26 by order and commutativity.

## Comparison
Orders are 26, 312, and 24. Different finite orders rule out isomorphism. Caesar shifts embed in the affine group as E_(1,k), but the full groups are not isomorphic.
