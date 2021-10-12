# Recursive Types

## Warmup / Exercise

<script
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-chtml.min.js"
    integrity="sha512-93xLZnNMlYI6xaQPf/cSdXoBZ23DThX7VehiGJJXB76HTTalQKPC5CIHuFX8dlQ5yzt6baBQRJ4sDXhzpojRJA=="
    crossorigin="anonymous" referrerpolicy="no-referrer">
</script>

$$ \sum_i^{n=10} i^2 $$

1. Typescript playground: Covariance / Contravariance of function types
  * https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgIIEZkG8BQOC+eoksiKqATNnoTsdPEsgEKa4FHgNktXu0AbCGGQwAXMgAUcdBIwBKZAF4AfGgoBuHEJEBzCZIBGslukWreWoA
  * Input type: "what we must be able to expect" => upper bound
  * Output type: "what our result must satisfy" => lower bound

2. Typescript playground: Recursive interface types
  * https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgJIDEoHsC2BlMKUAc2QG8AoZa5GACgGcAuZBwkgShY233ZGIBuCgF8KFUJFiIUPXASICATOSo0A9OuQALaCmANayAEQBXEDCwAbACYQbxtdXrNW-Yl3K1GTNoo-cmPLuKiLCYlYQYEYAvMg+fpzIMQB88WTMDAA0tEwwIhzCFJHRcMmqNKxMxpZYxllOuT5u-hzJaXQZLNm0BaJFJcgARkxyfP7lcMKDQ0qBvAokKnFTFEPls8KzG4JAA
  * Intuitively, IFromString and IFromString2 are the "same type" (not
      nominally)
  * How to express this mathematically?  Verify algorithmically? (We focus on
      the first question).

## Preliminaries
### Types in Lambda Calculus
* T = Top | T x T | T -> T
* Examples

### Types as trees
* Tree as a partial function
* t: {1,2}\* -> {Top, ->, x}
* TreeOf(T): Types -> Trees, Tp(t): Trees -> Types (bijection)
* Recursive types as infinite trees...
  * Want to show Existence / Uniqueness
  * We define a metric on the space of trees _T_...

### Metric Spaces
* Definition: metric, Example: metric on trees
* Given a metric space, what do we want to know?
* Definition: Complete (cauchy-sequences converge), Example: _T_ is complete
  (approximations stabilize trees)
* Definition: Compact... Theorem, compact iff exist finite epsilon-nets.
  Example: _T_ is compact.
* Theorem: Banach Fixpoint Theorem, Proof: iterated function

## Recursive Types in _T_
* Regular Trees
* Trees with variables
* Substitution on _T_: (Observe contractiveness, under which conditions?)
* Recursive types as recursive formulas, Existence/ Uniqueness given by Banach

### Mu-Types and relation to recursive formulas
* T = X | Top | T x T | T -> T | \mu X.T
* Substitution in mu-types (free / bound variables)
* Fold / Unfold: \mu X.T = T[X -> \mu X.T]
* Observation: \mu contraction
* From \mu types to tree-types (intuitive / formalization)

**How should subtyping be defined?**

## Lattice-Based Approach
* Basic idea: Subtype is a relation on _T_ x _T_
* Given a set of Types and their relations, we can create new types and
  **infer** new Subtype relationships
* We define a function mapping P(_T_ x _T_) -> P(_T_ x _T_), and "iterate it
  until its closed"

### Preliminaries
* Definition: F: P(U) -> P(U) monotone | X \subseteq Y => F(X) \subseteq F(Y)
* Definition: Let X \subseteq U
  * F-closed: F(X) \subseteq X
  * F-consistent: X \subseteq F(X)
  * Fixed point: F(X) = X
* Intuition: suppose F takes X (assumptions) to all conclusions you can draw
  from X.  Then:
  * Closed: anything you can conclude is already in X - you can't learn more
      from drawing conclusions - its possible you've assumed more than you can
      conclude.
  * Consistent: if its in X, then you can conclude it from X - you can prove
      all your assumptions - it's possible that you can prove some things that
      you haven't assumed.
* Observation: F-monotone + C-consistent => F(C) is also consistent
* Theorem: _C_ = Union { C : C F-consistent } = greatest fixed point of F
* Proof:
  * Union of consistent sets is consistent (therefore _C_ is consistent)
  * _C_ consistent => F(_C_) consistent => F(_C_) \in _C_ 
  * By definition of _C_, F(_C_) \subseteq _C_ => _C_ closed
  * _C_ closed and consistent => Fixed Point
  * Greatest? (a greater one would have been in { C : C F-consistent })

### Back to Subtyping
* Consider S: P(_T_ x _T_) -> P(_T_ x _T_) | S(R) = union of
  * {(T, Top) | T \in _T_}
  * {(S1 x S2, T1 x T2) | (S1, T1), (S2, T2) \in R (covariance)}
  * {(S1 -> S2, T1 -> T2) | (T1, S1), (S2, T2) \in R (contra/covariance)}
* Is S Monotone? (Obvious).  Take greatest fixpoint nS to be Subtype relation.
* How do these trees relate to mu-Types?  They are "the same," proof is a
  boring structural induction (show if there's time)

## Other Topics
### Regular Languages and Contractive Grammars
* Relationship between regular trees and regular languages

* Definition: Contractive Grammar: All rules are of the form N -> tN | N -> t

* Theorem: A language is Regular iff it has a Contractive Grammar
* Proof (=>):
  * Suppose L is regular, consider DFA of L
  * Introduce non-terminal Q for each state q, S is start-state
  * for each transition \delta(p,t) -> q add rule P -> tQ
  * for each transition \delta(p,t) -> f (f \in F) add rule P -> t
  * Check: DFA(w) \in F iff S --> w (chase the graph)
* Proof (<=):
  * Suppose G is contractive.
  * Create DFA with states = NonTerminals(G), unique finishing state F
  * If there are two rules { P -> tQ, P -> t }, then
    * add new state P'
    * for each rule { R -> tP }, add rule { R -> tP' }
    * replace { P -> t } with { P' -> t }
  * For each rule P -> tQ, add transition \delta(p,t) = Q
  * For each rule P -> t, add transition \delta(p,t) = F
  * Check: S --> w iff DFA(w) = F (chase the grammar)

* Definition (language of tree):
  * p \in Labels, A tree, Occ(p,A) = { \pi | A(\pi) = p }
  * L(A) = { \pi p | \pi \in Occ(p,A) }

* Claim: If A is regular, then L(A) is regular
* Proof:
  * Consider the Subtree-labled tree
  * Every path length >= |Sub(A)| either terminates or has an infinite
      subtree occuring at position > 1
  * Truncate the tree to first occurence of infinite subtree
  * Create grammar from leaves:
    * All infinite sub-trees get a non-terminal T_i, terminals = {0,1,Top,x,->}
      example: suppose l_i = 0 1 0 T_i, then add production rules:
       A     -> 0 l_i_1
       l_i_1 -> 1 l_i_2
       l_i_2 -> 0 T_i
  * Obviously creates a finite number of rules, all of them contractive
  * Repeat this procedure for all infinite-subtrees: results in finite number
      of rules, all of them contractive.

* Claim: if L(A) is regular, then A is regular
* Proof:
  * Consider a DFA for L(A).
  * Note that every state has outward edges labled 0 or 1 (or no edges)
  * Every state defines a new tree - consider DFA' with start(DFA') = state
      (some states may be unreachable)
  * Need to show that every subtree of A is represented by a state in DFA
  * say T(\sigma) = A(\pi \sigma), then T is represented by DFA(\pi)

### Misc
* Algorithm / Machine to determine recursive subtype relationship: http://web.cs.ucla.edu/~palsberg/paper/mscs95-kps.pdf
* ([F-Bounded] Polymorphism) Java Generics are Turing Complete: https://arxiv.org/pdf/1605.05274.pdf
