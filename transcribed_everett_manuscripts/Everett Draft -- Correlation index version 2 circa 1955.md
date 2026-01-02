# Everett Draft -- Correlation index version 2 circa 1955.pdf

Correlation Index: 

Given two random variables \(X, Y\) ranges \(\mathbb{E}[X]\), \(\mathbb{E}[Y]\) and their probability distributions \(P_{ij} = \text{the} \text{of} X_i \text{and} Y_j\).
Then Correlation index is defined to be the expected information gain (on \(X\)) given that \(Y\) is itself (according to its a priori distribution): 

\[
C(x, y) = \sum_{ij} P_{ij} \ln \left[ \frac{(\xi_i P_{ij})(\xi_j P_{ij})}{P_{ij}} \right]
\]

More generally, we may have a joint distribution
on \(M\) - random Variables \(X^\alpha, X^\beta, \ldots, X^r\)
ranges \(\mathbb{E}[X^\alpha] \mathbb{E}[X^\beta] \ldots\)
with joint distribution \(P_{ij, k, \ldots, l}\)
= \(\text{not } \{X^\alpha = x_i^\alpha \text{ and } X^\beta = x_j^\beta \text{ and } \ldots \text{ and } X^r = x^r\}\)

---

and again we can define a correlation index for any
Single Variable \(X^\infty\) and any subset of the remaining
Variable 

\(C(X^\infty; X_1, X_2, \ldots, X_5)\) to be the expected
information change about \(X^\infty\) given that we are told
\(X_1, X_2, \ldots, X_5\). 

\[ \text{let } n_i = \sum_{j \leq k \leq l} p_{ijkl} \quad \text{= a-pair distincts on } X^\infty \]

\[ \sum_{j \leq k \leq l} p_{ijkl} = \sum_i p_{ijkl} \quad \text{= a-pair distincts on } X_1, X_2, \ldots, X_5 \]

**Statistical Information** \(I(X^\infty) = \sum_i n_i \ln n_i\) 

**Conditional Information given** \(p_{ijkl, \ldots, l}\) 

\[ I_{ijkl, \ldots, l}(X^\infty) = \sum_i p_{ijkl, \ldots, l} \ln p_{ijkl, \ldots, l} \]

**Information Change** and on \(p_{ijkl, \ldots, l}\) 

\[ \Delta I_{ijkl, \ldots, l}(X^\infty) = \sum_i p'_{ijkl, \ldots, l} \ln p'_{ijkl, \ldots, l} - \sum_i n_i \ln n_i \]

---

Expected inif change 

\[
= \Delta I = \sum_{j_{1}, \ldots, l} \sum_{j_{2}, \ldots, l} \Delta I_{j_{1}, \ldots, l}
\]

\[
= \sum_{j_{1}, \ldots, l} \left( \sum_{j_{2}, \ldots, l} \left( \sum_{j_{3}, \ldots, l} \ldots \sum_{j_{k}, \ldots, l} \ldots \sum_{j_{l}, \ldots, l} \ldots \sum_{j_{l}, \ldots, l}^{N} \ldots \sum_{j_{l}, \ldots, l} \ldots \sum_{\ldots, l} \ldots \sum_{j_{l}, \ldots, l} \right) \right)
\]

Cond proof due 

\[
\frac{\text{on given } j_{k}, \ldots}{\sum_{i} p_{i j_{k}, \ldots} l} = \frac{p_{i j_{k}, \ldots} l}{\sum_{i} p_{i j_{k}, \ldots} l} = \sum_{j_{1}, \ldots, l} \frac{p_{i j_{k}, \ldots} l}{\sum_{j_{1}, \ldots, l} p_{i j_{k}, \ldots} l}
\]

---

**chirotob for perfect Bernoulli variables**

ie
\[
P_{i,j,k,\ldots,m}
\]
in question known remainder

\[
R_i = \sum_{j,m,\ldots,n} P_{i,j,k,\ldots,m,n} = \text{apriori on } i
\]

\[
\hat{y}_{j,k,\ldots,l} = \sum_{j,m,\ldots,n} P_{j,k,\ldots,m,n} = a \text{-priori on } j,k,\ldots
\]

\[
\hat{y}_{j,k,\ldots,l} = \sum_{m,\ldots,n} P_{j,k,\ldots,m,n} \quad \text{condition on } j,k,\ldots
\]