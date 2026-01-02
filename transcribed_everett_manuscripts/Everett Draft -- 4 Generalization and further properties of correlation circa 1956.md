# Everett Draft -- 4 Generalization and further properties of correlation circa 1956.pdf

§4. Generalization and further properties of correlation. 

Up to now we have been concerned only with finite
probability distributions, for which we have defined information
and correlation. We shall now generalize this definition of
correlation so as to be applicable to joint probability
distributions over arbitrary sets of unrestricted cardinality. 

We first consider the effects of refinement of a
finite distribution. For example, we may discover that
the event \(X_i\) is actually the disjunction of several
exclusive events \(\tilde{X}_i^1, \tilde{X}_i^2, \ldots, \tilde{X}_i^m\), so that \(X_i\) occurs if any
one of the \(\tilde{X}_i^j\) occurs, i.e., the single event \(X_i\) results from
one failing to distinguish between the \(\tilde{X}_i^j\). The probability
distribution which distinguishes between the \(\tilde{X}_i^j\) will be
called a refinement of the distribution which does not. In
general, we shall say that a distribution \(P' = P'(\tilde{X}_i^1, \tilde{X}_i^2, \ldots, \)
is a refinement of \(P = P(X_i, \ldots, Y_i)\) if 

\[ (4.1) \quad P(X_i, \ldots, Y_i) = \sum_{j=1}^{m} P'(\tilde{X}_i^j, \ldots, \tilde{Y}_i^j) \quad (\text{all } i, \ldots, j) \]

We now state an important theorem concerning the
behavior of correlation under a refinement of a joint
probability distribution: (Proof in Appendix) 

**Theorem 2:** \(P'\) is a refinement of \(P \Rightarrow \{X_i, \ldots, Y_i\} \subseteq \{X_1, \ldots, Y_1\}\) 

So that correlations never decrease upon refinement
of a joint probability distribution. (Proof in Appendix)

As an example, suppose that we have a continuous
probability density \(P(x, y)\). By division of the data into a
finite number of intervals, \(A_i \ni Y_i\), we arrive at

---

11. Definition of measure = quantitative
  calculation of profit and loss
  measurement of value of asset 4.

---

a finite joint distribution \(P_{ij}\) by integration of \(P(y|y)\) over the rectangle whose sides are the intervals \(T_i\) and \(T_j\) and which represents the probability that \(X \in T_i\) and \(Y \in T_j\). If we now subdivide the intervals, the new distribution \(P'\) will be a refinement of \(P\), and by theorem 2 the correlator \(X \times Y\) computed by \(P'\) will never be less than the computed by \(P\). Theorem 2 is seen to be simply the mathematical verification of the intuitive notion that closer analysis of a situation in which quantities \(X\) and \(Y\) are disjoint can never lessen the knowledge about \(Y\) which can be obtained from \(X\). 

This theorem allows all our to give a definition of correlation which will apply to joint distributions over completely arbitrary sets, for any probability measure \(B\) on an arbitrary product space, in the following manner: assume that we have two arbitrary sets \(X\) and \(Y\). \(Z\) and a probability measure on the product, \(M(X \times Y)\). Let \(P^M\) be any finite partition of \(X\) into subsets \(X_i\) and \(Y_i\) into subsets \(Y_i\), such that the products of the \(X_i \times Y_i\) are measurable in the probability measure \(M\). A partition \(P^M\) is a refinement of \(P^X\), \(P^Y \subset P^X\), is \(P^M\) results from \(P^X\) by further subdivision of the subsets \(X_i\) and \(Y_i\). Each partition results in a finite probability distribution, for which the correlation always defined and furthermore a refinement of a partition leads to a refinement of the probability distribution, so that by theorem 2: 

\(P^X \subset P^M \implies \{X_i, Y_i\} \cong \{X_j, Y_j\}_{i,j}\)

---

-

-

-

-

-

-

-

<|det|>[-0, 0, 1000, 0]-

- 

-

The text of the text is not clear. The text is not clear. The text is not clear. The text is not clear. The text of the text is not clear. The text is not clear. The text is not clear.

-

0

-

-

---

Now the set of all partitions is partially ordered under the refinement relation. Moreover, because for any pair of partitions \(P, P'\) there is always a partition \(P''\) which is a refinement of both (common lower bound), the set of all partitions forms a directed set. For functions \(f, g\) on a directed set \(B\), one defines a directed set \(G\) as a directed set, \(\lim f = a \iff \forall \epsilon > 0 \exists \text{ such that } \lim g \text{ exists and is equal to } a \text{ for every } \epsilon > 0 \text{ such that } \lim g \text{ exists and is equal to } a. \text{ which is } \epsilon \text{ such that for every } \beta \in B, \text{ which is } \epsilon \text{ such that for every } \beta \text{ exists and is equal to } a. \text{ which is } \epsilon. \text{ which is } \epsilon \text{ such that for every } \beta. \text{ which is } \epsilon \text{ such that for every } \beta, \text{ which is } \epsilon \text{ such that for every } \beta. 

**Def:** \(\lim f = a \iff \forall \epsilon > 0 \exists \text{such that } \lim g \text{ exists and is equal to } a \text{ for any } \epsilon > 0 \text{ such that } \lim g \text{ exists.}\) 

**Not for:** \(\lim f = \infty \iff \forall \epsilon > 0 \exists \text{such that } \lim f = \infty \text{ exists and is equal to } \infty \text{ for any } \epsilon > 0 \text{ such that } \lim f = \infty \text{ exists.}\) 

**New for:** 

New for: 

For:

---

**Input**  
7.5  

We can now prove a very important theorem about correlation which concerns its invariant nature. Let \(X\) and \(Y\) be arbitrary sets with probability measure \(M_P(X|Y)\) on the product. Let \(f \in \mathcal{B}\) be any one-to-one mapping of \(X\) onto a set \(V\), \(g\) a one-to-one mapping of \(Y\) onto \(V\). Then the probability measure induced on the product \(U \times V\) is simply the measure which assigns to each subset \(V_j \times V_j\) the measure of the image set, \(M_P'(V_j \times V_j) = M_P(f(g_j^{-1}(x_j)))\). Consider any partition \(P\) of \(X \times Y\) into the subsets \(\mathcal{B}(x_j)\), \(\mathcal{B}(y_j)\) with probability distribution \(P_{ij}\). Then there is a corresponding partition \(P'\) of \(U \times V\) into the sets \(\mathcal{B}(x_j)\), \(\mathcal{B}(y_j)\) where \(V_j = f(X_j)\) and \(V_j = g(Y_j)\), the partition of the image sets of \(P_j\) which has the probability distribution \(P_{ij} = M_P'(V_j \times V_j) = M_P(X_j \times Y_j) = P_{ij}\) which is identical to the distribution for \(P\) in \(X \times Y\), so that:  

\[\{X, Y\}^P = \{U, V\}^{P'}\]

---

Let the to its corresponding between the \(P_0\) and \(P_1\) be
we have that
\[
\sup_{P} \{x, y\} = \sup_{P} \{y, x\}^{P^{-1}} \quad \text{and by virtue of (4.9) we have proved the theorem:}
\]

\[
\text{Theorem 3: } \{x, r\} = \{y, v\} \text{ where } U \text{ is any}
\]

\[
\text{on to one image of } X, \text{ } V \text{ any one to one image of } Y.
\]

\[
\text{In atomization: } \{x, r\} = \{f(x), g(r)\} \text{ where } f \text{ and }
\]

\[
g \text{ are arbitrary one to one functions.}
\]

---

This means changing variables to functionally related variables preserves the correlation. Again this is plausible on intuitive grounds, since a knowledge of \(f(x)\) is just as good as knowledge of \(x\), provided that \(f\) is on to one. 

A special consequence of theorem 3 is that for any continuous probability density \(P(x, y)\) over real numbers, the correlation between \(f(x)\) and \(g(y)\) is the same as between \(f\) and \(g\), where \(f\) and \(g\) are any real valued one-to-one functions. As an example consider a probability distribution for the position of two particles, so that the position coordinate random variables are the position coordinates. Theorem 3 then asserts that the position correlation is independent of the coordinates setting, even if different coordinate systems are used for each particle! Also for a joint distribution over a pair of events in space, time the correlation is invariant to arbitrary projective coordinate transformations, again even allowing different transformations for the coordinates of each particle. 

The general variance of correlation expressed in theorem 3 indicates the fundamental nature of this quantity for probability distributions. If \(p\) is to be understood that all of the preceding results hold equally well for group correlations. Due to the fact that the correlation is defined as a limit for discrete distributions, all of the relations 3.7 to 3.15 which contain only correlation products remain true for arbitrary distributions. Only 3.11 and 3.12, which contain information terms, cannot be extended (yet).

---

Assume that we have a collection of arbitrary sets \(X, Y, \ldots, Z\) and a probability measure \(M_p(x, y, z)\) on their cartesian product. Let \(P^u\) be any finite partition of \(X\) into subsets \(X_i^u, Y\) into subsets \(Y_i^u\) and \(Z\) into subsets \(Z_i^u\), such that the sets \((X_i^u, Y_i^u, Z_i^u)\) of the cartesian product are measurable in the probability measure \(M_p\). Another partition \(P^v\) is a refinement of \(P^u, P^v \subseteq P^u\) if \(P^v\) results from \(P^u\) by putting subdivision of the subsets \(X_i^u, Y_i^u, Z_i^u\). Each partition \(P^u\) results in a finite probability distribution for which the correlation \([X, Y, \ldots, Z]^p\) is always defined through (3.3). Furthermore a refinement of a partition leads to a refinement of the probability distribution, so that by theorem 2: 

\[(9.8) \quad P^v \subseteq P^u \implies \{X, Y, Z\}^p \subseteq \{X, Y, Z\}^{p^v}\]

**Remark.** For a directed set \(B\), one defines a directed set limit \(\lim f\), 

**Def.:** \(\lim f\) exists and is equal to \(a\) \(\iff\) for every \(\varepsilon > 0\) there exists an \(\alpha \in B\) such that \(|f(p) - a| < \varepsilon\) for every \(p \in B\) for which \(p \leq \alpha\).

---

Inver
1

By (9.8) the correlation \([X, Y, Z]\) is a monotone function on the directed set of all partitions. Consequently the directed set limit which we shall take as the basic definition of the correlation \(E[X, Y, Z]\) always exists. (It may be infinite, but is in every case well-defined.) Thus:

\[
Def: \{X, Y, Z\} = \lim_{n} [X, Y, Z]^n
\]

---

Smart 1.5) 

P Due to the fact that the correlation
is defined as a limit for discrete distributions,
Theorem 1 and all of the relations (3.1) (3.15),
which contain only correlation brackets, remain
true for arbitrary distributions. Only 3.11 and
3.12, which contain information terms, cannot
be extended yet.

---

We can now prove an important theorem about correlation which concerns its invariance nature. Let \(X, Y, \theta, \gamma\) be arbitrary sets with probability measure \(M_P\) on their cartesian product. It is the any one-to-one mapping of \(X\) onto a set \(U\), a one-to-one map of \(Y\) onto \(V\), ..., and has a map of \(Y\) onto \(W\). Then a joint probability distribution over \(X \times Y \times \ldots \times Y\) leads also to one over \(U \times V \times \ldots \times U\) where the probability measure \(M_P\) is included on the product \(U \times V \times \ldots \times U\) is simply the measure which assigns to each subset of \(U \times V \times \ldots \times U\) the measure which is the image set in \(X \times Y \times \ldots \times Y\) for the original measure \(M_P\). (We have simply transformed to a new set of random variables: \(U = g(X)\), \(V = g(Y)\), ..., \(W = h(Z)\).) Consider any partition \(P\) of \(X \times Y \times \ldots \times Y\) into the subsets \(\{X_1, Y_1, \ldots, Y_k\}\) with probability distribution \(P_{i,j,k} = M_P(X_i \times Y_j \times \ldots \times Y_k)\). Then there is a corresponding partition \(Q^P\) of \(U \times V \times \ldots \times U\) into the image sets of the sets of \(P\), \(\{X_1, Y_1, \ldots, Y_k\}\); \(\{X_2, Y_2, \ldots, Y_k\}\); ..., \(\{X_k, Y_k, \ldots, Y_k\}\), where \(U_i = f(X_i)\), \(V_j = g(Y_j)\), ..., \(W_k = h(Y_k)\). But the probability distribution for \(Q^P\) is the same as that for \(P\), since \(P_{i,j,k} = M_P(U_i \times V_j \times \ldots \times U_k) = M_P(X_i \times Y_j \times \ldots \times Y_k) = P_{i,j,k}\). No that \(\{X, Y, \ldots, Z\}^Q = \{U, V, \ldots, W\}^Q\).

---

Theorem 3: \(\{x, y, z\} = \{y, z, w\}\) where \(\mathcal{U}\) is any one image of \(x, y, z\) on one image of \(y, z, w\) on another image of \(z\). In other notation: \(\{x, y, z\} = \{x(k), y(l), z(h)\}\) for all one-one function \(f, g, h\).

\[
W, V, W \text{ are the images of } xy, z
\]

naturally.

---

The
examples illustrate clearly the
intrinsic nature of the correlation of various groups
probability distributions, which is simplified
by its invariance against arbitrary (one-one)
transformations of the random variables.
These correlation quantities are thus fundamental
properties of probability distributions.

A correlation is an absolute rather than
relative quantity, in the sense that the
correlation between (numerical values) random
variables is completely independent of the
scale of measurement chosen for its variables.

end of Section 4