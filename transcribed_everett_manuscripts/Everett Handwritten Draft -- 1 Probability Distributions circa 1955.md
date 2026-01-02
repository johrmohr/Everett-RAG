# Everett Handwritten Draft -- 1 Probability Distributions circa 1955.pdf

## 5. Probability distributions 

Let \(P(xy, \ldots, z)\) represent a joint probability density for the random variables \(X, Y, \ldots, Z\), where values are real numbers, so that \(P(xy, \ldots, z) dx dy \ldots dz\) is interpreted to mean the probability that \(X\) will take a value in the interval \([x, x+dx]\) and \(Y\) will take a value in \([y, y+dy]\) and \(\ldots\) and \(Z\) will take a value in \([z, z+dz]\). 

We now define a marginal probability for any subset of the original random variables, say \(X, Y\) to be the integral of the total joint density with respect to the remaining variables, i.e. 

\[P(x, y) = \int_{x, y} P(x, y, z, \ldots, w) dz \ldots dw\]

Which represents the density for the joint events \(X \in [x, x+dx]\) and \(Y \in [y, y+dy]\), with no restriction on the remaining variables. This the relative density over \(X, \ldots, Y\) when we have no information about the other variables. 

Finally, we define a conditional density for any subset \(X_1, \ldots, X_n\) conditioned on any remaining variables having prescribed values, say \(Z = z_1, \ldots, W = w_n\) denoted by \(P_{X_1, \ldots, X_n|Z=z_1, \ldots, W=w_n}\). 

\[P_{X_1, \ldots, X_n|Z=z_1, \dots, W=w_n} = \frac{P_{X_1, \ldots, X_n, Z=z_1, \ldots, W=w_n}}{P_{Z=z_1, \ldots, W=w_n}}\]

which represents the density for \(X_1, \ldots, X_n\) relative to the likelihood that \(Z = z_1, \ldots, W\) have the definite values \(z_1, \ldots, w\).

---

We shall say that the Variables \(X\) and \(Y\) are **independent** if and only if \(P(x,y) = P(x)P(y)\) except for a set of measure zero, and more generally we shall say that the Groups \(S_1, S_2, \ldots, S_n\) are mutually independent if and only if the group-wise independence of \(P(x_1, x_2, \ldots, x_n, y_1, y_2, \ldots, y_n) = P(x_1, y_1) P(x_2, y_2) \ldots P(x_n, y_n)\) except for a set of measure zero. **Independence** then implies that the conditional distribution for a group conditioned on values in another independent group, is the same as the marginal for the group, i.e. \(X\) is indepe- 

\[ \Rightarrow P_y^x = P_x \quad \text{or} \quad S_1, S_2, \ldots, S_n \text{ mutually independent} \Rightarrow P_{w_1, w_2, \ldots, w_n} = P_{w_1, w_2, \ldots, w_n} \text{ always converges.} \]

That is, we learn nothing about \(W_1, \ldots, X\) by using the
Volumes of Variables in groups independent of \(W_1, \ldots, X\). 

\(\Rightarrow\) **Indicate Exp** and **Exp** (and and exp Exp) 

## §2 Information 

We now define a functional for probability distribution,
\(I_{x, \ldots, y} = I[x, \ldots, y] = \int \ldots \int P_{x, \ldots, y} \ln P_{x, \ldots, y} dx \ldots dy\) 

\[ \begin{aligned} I_{x, \ldots, y} &= \iint P_{x, \ldots, y} \ln P_{x, \ldots, \hat{y}} dx \ldots dy \\ &= \exp[\ln P_{x, \ldots, y}] \end{aligned} \]

i.e. we define the **Information** of a probability distribution
to be the **Expected** logarithm of the probability density.

---

we can now define Marginal Prob. measures 

over the product space of subclasses of \(X, Y, Z, \ldots\) 

\[
P_M(X, Y) = P(X, Y, Z, \ldots)
\]

and similarly from this Marginal Measure we derive 

\[
\text{Marginal Densities } P(x, y) = \int P(x, y, z, \ldots) \, dy \ldots \, dz
\]

We further define conditional measures \(M_P\{X, Y, \ldots | Z, \ldots, W\}\) 

\[
\text{to be} \quad M_P \{X, Y, Z, \ldots | Z, \ldots, W\} = \frac{M_P \{X, Y, Z, \ldots, W\} \cap Z, \ldots, W\}}{M_P \{Z, \ldots, W\}}
\]

\[
\text{which leads to conditional densities } P_{X, Y, \ldots}^{Z, \ldots, W} = \frac{P(X, Y, Z, \ldots, W)}{P(Z, \ldots, W)}
\]

\[
\text{briefly, we define } I_{X, Y, \ldots}^{Z, \ldots, W} = \text{Exp}\{ \ln P_{X, Y, \ldots}^{Z, \ldots, W} \}
\]

with respect to the conditional measure \(M_P\{X, Y, Z, \ldots, W\}\)

---

## 5 Probability distributions: 

We shall assume that we have a collection of sets \(X, Y, Z, \ldots, \ldots, \ldots\) each with a measure assigned \(M(X)\). \(M(Z)\) 

(ie a non-negative, countably additive set function over some of the subsets \(X, Y, Z, \ldots, \ldots\))

and furthermore we assign the product measure to the direct product of these sets. 

We further assume that we have a probability measure over this direct product, which we shall denote by \(P(X, Y, \ldots)\). 

is now a function of \(n\) tuples of sets one in \(X\), one in \(Y\), etc. and which we think of as being the Probability that a selection of one element from each set will result in the event that \(x_i \in X_i, y_j \in Y_j\). To know if a person that this always results in the existence of a Probability density function \(P(x, y, 3, \ldots)\) which is a point (or element) function rather than a set function, such that the integral of \(P(x, y, 3, \ldots)\) over any set of the product space, with respect to some original product measure, is the Probability measure of that set.