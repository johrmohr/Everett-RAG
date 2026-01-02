# Everett Draft -- II Probability Information and Correlation circa 1956.pdf

which represents the probability of the joint occurrence of \(y_1, \ldots, y_n\) and \(z\) with no restrictions upon the remaining variables. 

For any subset \(Y, \ldots, Z\) of a set of random variables, we define the conditional distribution, conditional upon the value \(W = w_1, \ldots, X = x_j\) for any remaining subset \(W, \ldots, X\) and denoted by \(p(w_1, \ldots, x_j | y_1, \ldots, y_n, z) = \frac{p(w_1, \ldots, x_j, y_1, \ldots, y_n, z)}{p(w_1, \ldots, x_j)}\). 

\[p(w_1, \ldots, x_j | y_1, \ldots, y_2, z) = \frac{P(w_1, \ldots, x_j, y_1, y_2, \ldots, z)}{P(w_1, \ldots, x_j)}\]

(1.2) 

which represents the probability of the joint event \(Y = y_1, \ldots, y_n, Z = z\), conditional upon the fact that

---

W...X are known to have taken the values 

\(w_1, \ldots, w_k\). 

For any numerical valued function \(F(y_1, \ldots, y_k)\), defined on the elements of the direct product of \(Y_1, \ldots, Y_k\), we define the expectation, denoted by \(\text{Exp}[F]\) as follows: 

\[(1.3) \quad \text{Exp}[F] = \sum_{y_1, \ldots, y_k} P(y_1, \ldots, y_k) F(y_1, \ldots, y_k)\]

Recall we note that if \(P(y_1, \ldots, y_k)\) is a marginal distribution of some larger distribution \(P(w_1, \ldots, w_k, y_1, \ldots, y_k)\), then 

\[(1.4) \quad \text{Exp}[F] = \sum_{k, \ldots, k} \left( \sum_{i, j} P(w_i, \ldots, w_j, y_k) F(y_i, \ldots, y_k) \right) = \sum_{i, j, k, \ldots} P(w_i, \ldots, w_j, y_k) F(y_i, \cdots, y_k) \quad (1.4)\]

so that if we wish to compute \(\text{Exp}[F]\) with respect to some joint distribution, it suffices to use any marginal distribution of the original distribution which contains at least those variables which occur in \(F\). 

We shall also occasionally be interested in conditional expectations, which we define as: 

\[(1.5) \quad \text{Exp}^{w_1, \ldots, w_k}[F] = \sum_{k, \ldots, k} P^{w_1, \ldots, w_k}(y_k, \ldots, y_k) F(y_k, \ldots, y_k)\]

and we note the following easily verifiable for expectations: 

\[(1.6) \quad \text{Exp}[\text{Exp}[F]] = \text{Exp}[F] \quad (1.6)\]

---

We should also finally to comment upon the notion of independency. Two random variables \(X\) and \(Y\) with point distribution \(P(x_i, y_j)\) will be said to be independant if and only if \(P(x_i, y_j) = P(x_i)P(y_j)\) for all \(i, j\). 

Similarly, the groups of random variables
\((U, V), (W, X), \ldots, (Y, Z)\) will be called mutually independant groups if and only if 

\[P(u, v, w, x, \ldots, y, z, \ldots, z_n) = P(u, v, y, z, \ldots, z_n) \cdot P(w, x, \ldots, z_n) \cdot \ldots \cdot P(y, z, \ldots, z_n).\]

Independance means that the random variables
takes on values which are not influenced by the values
of other variables with respect to which they are independant.
That is, the conditional distribution of one of two independant
variables, conditional upon the value \(x_i\) for the other, is
independant of \(x_i\); no that independance about one
variable tells nothing of the other.

---

§7. Information for finite distributions 

questions
one response
to historical
best published
reports 

Suppose that we have a single random variable \(X\) with distribution \(P(x_i)\). We then define a number, \(I_{X_i}\), called the information of \(X\), to be: 

\[ (2.1) \quad I_X = \sum_i P(x_i) \ln P(x_i) = \exp \left[ \ln P(x_i) \right] \]

which is a function of the probabilities alone and not of
any possible numerical values of the \(x_i\)'s. This makes
the information is essentially a measure of the
sharpness of a probability distribution that is, an

---

New
barypt

\[\text{New} \quad \text{New} \quad \text{New} \quad \text{New} \text{New} \text{New} \text{New} \text{New}\]

\[\text{New} \quad \text{New} \quad \text{New}  \quad \text{New} \quad \text{New} \quad \text{new} \quad \text{new} \quad \text{new} \quad \text{\textbf{new}} \quad \text{\textbf{new}} \quad \text{\textbf{new}} \text{\textbf{new}} \quad \text{\textbf{new}} \quad \textbf{new} \quad \textbf{new} \quad \textbf{new} \quad \textbf{New} \quad \textbf{new} \quad \textbf{new} \quad \textbf{\textbf{new}} \quad \textbf{\textbf{new}} \quad \textbf{\textbf{new}} \text{\textbf{new}} \quad \textbf{\textbf{new}} \quad \textbf{\text{new}} \quad \textbf{\text{new}} \quad \textbf{\text{New}} \quad \textbf{\text{new}} \quad \textbf{\text{new}}  \quad \textbf{\text{new}} \quad \textbf{\text{new}} \text{\textbf{new}} \quad \textbf{\text{new}} \quad \textbf{\textbf{new}} \quad \textbf{\textbf{New}} \quad \textbf{\textbf{new}} \quad \textbf{\textbf{new}}  \quad \textbf{\textbf{new}} \quad \textbf{\textbf{new}} \textbf{\textbf{new}} \quad \textbf{\textbf{new}} \quad \text{\textbf{new}} \quad \textbf{\textbf{new}} \quad \text{\text{new}} \quad \textbf{\textbf{new}} \quad \text{\textbf{New}} \quad \textbf{\textbf{new}} \quad \textbf{\text{new}}  \quad \textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{new}} \quad \textbf{new}} \quad \textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{new}}} \quad \textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{new}} \quad  \textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{new}} \text{\textbf{new}} \quad \textbf{\textbf{\textbf{new}} \quad \text{\textbf{new}} \quad \textbf{New}} \quad \textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{new}}  \quad \textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{new}} \quad  \textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{New}} \quad \textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\text{new}} \quad \textbf{New}} \quad \textbf{\textbf{\textbf{\textbf{new}} \quad  \textbf{\textbf{\textbf{\textbf{new}}}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{\text{new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{new}} \text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\text{new}} \quad \textbf{\textbf{\textbf{\text{new}} \quad \text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\text{New}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{New}} \quad \textbf{\textbf{\textbf{\text{New}} \quad \textbf{\textbf{\textbf{\text{New}} \quad \text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{New}} \quad  \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad  \textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \text{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{new}}  \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}}}} \quad \textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{New}} \quad \textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{new}}  \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \text{new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad  new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf\new}}}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\text{\textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}}  \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{new}} \quad \textbf{ new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\text{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{\textbf{new}}  \textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\text{\textbf{new}} \quad \textbf{new}} \quad \textbf{\textbf{\text{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{\textbf{\textbf{\text{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\text{\textbf{\text{\textbf{\textbf{\textbf{new}} \quad \textbf{\textbf{new}} \text{\textbf{\textbf{\textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{new}} \quad  \textbf{\textbf{\textbf{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\text{new}} \quad \textbf{new}} \quad \textbf{\textbf{\textbf{\text{\textbf{\textbf{\text{\textbf{\textbf{\textbf{new}} \quad  \text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textit{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textit{\text{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textbf{\textit}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

---

\[(2.3) \quad \begin{aligned} \prod_{X,Y,\dots,Z} & = \sum_{i,j,\dots,k} P^{i,j,\dots,k} P^{i,j,\dots,k} \ln P^{i,j,\dots,k} (k_i, y_j, \dots, y_k) \\ & = E_X P^{i,j,\dots,k} \left[ \ln P^{i,j,\dots,k} (k_i, y_j, \dots y_k) \right] \end{aligned}\]

a quantity which measures our information about \(X, Y, \dots, Z\)
given that we know that \(V, \dots, W\) have taken the values \(v_1, \dots, v_m\). 

For independent random variables \(X, Y, \dots, Z\),
the following relationship is easily proved: 

\[(2.4) \quad \prod_{X,Y,\dots,Z} = \prod_X + \prod_Y + \dots + \prod_Z \quad (X, Y, \dots, Z \text{ independent})\]

so that the information of \(X, Y, \dots, Z\) is the sum of the individual quantities of information, which is in
accord with our intuitive feeling that if we are given
information about unrelated events, our total
knowledge is the sum of the separate amounts of
information. Furthermore, this requirement of
solubility for independent events limits the possible
definition of information to essentially only the one
given here, so that these kinds of generalizability to
our definition. We shall generalize this definition later
in section 55.

---

Suppose that we have a pair of random variables,
\(X\) and \(Y\), with joint distribution \(P(x_i, y_i)\). If both
\(X\) and \(Y\) are correlated, what
we are looking for is the one that is
about one variable when he is told the value of the other.
Let us focus on attention upon the variable \(X\). If
we are not informed of the value of \(Y\), then our
information concerning \(X\), \(I_{X-Y}\) is calculated from
the marginal distribution \(P(x_i)\). However if we are
now told that \(Y\) has the value \(y_i\), then our
information about \(X\) changes to the information
of the conditional distribution \(P(y_i | x_i)\), \(I_{X-Y}^{y_i}\). According
to what we have said, we wish the degree of
correlation to measure how much we learn
about \(X\) by being informed of \(Y\)'s value. However,
since the change of information, \(I_{X-Y}^{y_i} - I_{X}\), may depend
upon the particular value \(y_i\), of \(Y\) which we are told,
the natural thing to do to arrive at a single number
to measure the strength of correlation is to consider
the expected change in information about \(X\), given
that we are to be told the value of \(Y\). This quantity
we call the correlation information, or for brevity,
the correlation of \(X\) and \(Y\), and denote it by \([X, Y]\). Thus: 

\[[X, Y] = \text{Exp}[\prod_{X}^{y_i} - I_X] = \text{Exp}[\prod_{X}^{y_i}] - I_X\]

Expanding the quantity \(\text{Exp}[\prod_{X}^{y_i}]\) using (2.3) and the
rules for expectation (1.6-1.8) we find

---

\[
\begin{align*}
\exp\left[I_x^{y_j}\right] &= \exp\left[\exp^{y_j}\left[\ln p^{y_j}(k_i)\right]\right] \\
&= \exp\left[\ln \frac{p(k_i, y_j)}{p(y_j)}\right] = \exp\left[\ln p(k_i, y_j) - \exp\left[\ln p(y_j)\right]\right] \\
&= I_{xr} - I_r
\end{align*}
\]

and combining with (3.1) we have: 

\[
\{X, Y\} = I_{Xr} - I_X - I_Y
\]

Thus the correlation 

is symmetric between X and Y, and hence
equal also to its expected change of information about
Y given that we will be told the value of X. Furthermore,
according to (3.3), the correlation corresponds precisely
to the amount of missing information if we proceed
only the marginal distribution, i.e. the loss of
information is due to regard the variables as
independent. 

Theorem 1: \(\{X, Y\} = 0\) if and only if
X and Y are independent, and is otherwise
strictly positive. (Proof in appendix) 

In this report the correlation is defined is
superior to the usual correlation coefficients of statistics,
such as covariance, etc, which can be zero even when
the variables are not independent, and which can
assume both positive and negative values. A positive
correlation is, after all, quite as useful as a negative
correlation. Furthermore, it has the great advantage of
depending upon the probabilities alone, and not

---

upon any numerical value of the \(k_i\) and \(y_j\) so that it is defined for distributions over sets whose elements are of an arbitrary nature, and not only for distributions over numerical properties. (Note: the definition of \(k_i\) is not given here.) 

Invert
4 

4 

<|det|>[[0, 0, 0, 0]] figure
Figure 4 

<|det|>[[0, 0, 0, 0]] figure

<|det|>[[0, 0, 0, 0]] figure

<|det|>[[0, 0, 0, 0]] figure

math
We can generalize (3.3) to define a group
carculation for the groups of random variables
\((U, \cdots, V), (W, \cdots, X), \cdots, (Y, \cdots, Z)\), denoted by \(\{U, \cdots, V, W, \cdots, X, \cdots, Y, \cdots, Z\}\) (where the groups are separated by commas) to be:

<|det|>[[0, 0, 0, 0]] figure

math
(3.4) \[\{U, \cdots, V, W, \cdots, X, \cdots, Y, Z\} = I_{U, V, W, \cdots, X, \cdots, Y, \cdots, Z} - I_{U, V} - I_{W, X} - \cdots - I_{Y, Z}\]

math
again, measuring the information efficiency for the
group marginals. Theorem 1 is also satisfied by
the group correlation, so that it is zero if and only if
the groups are mutually independent. We can, of course,
extend to the definition of conditional correlation
as follows in the above manner, denoting thus
quantities by applying the conditional value as
superintegrals, as before.

math
We conclude this section by listing some useful
formulas and inequalities which are easily proved:

<|det|>[[0, 0, 0, 0]] figure

equation
(3.5) \[\{U, V, \cdots, W\} = \exp \left[ \ln \frac{P(U, V, \cdots, W)}{P(U)P(V) \cdots P(W)} \right]\]

<|det|>[[0, 0, 0, 0]] figure

equation

equation
(3.6) \[\{U, V, \cdots, W\} = \exp \left[ \int \ln \frac{P^{k_1, \cdots, k_s}(U, V, \cdots, W)}{P^{k_1, \cdots, k_s}(U)P^{k_1, \cdots, k_s}(V) \cdots P^{k_s}(W)} \right] \]

<|det|>[[0, 0, 0, 0]] figure

<|det|>[[0, 0, 0, 0]] figure

m
(conditional correlation)

---

(3.2) (Comma Removal) \(\{ \dots , y, y, \dots \} = \{ \dots , y, y, \dots \} + \{ y, y \}\) 

\[
\begin{align*}
\{ \dots , y, y, y, \dots \} &= \{ \dots , y, y, \dots \} + \{ y, y, \dots \} \\
&= \{ \dots , y, y, \dots \} + \{ y, y, \cdots \}
\end{align*}
\]

(3.3) (Commutator) 

\[
\{ \dots , y, y, y, \dots \} - \{ \dots , y, y, y, \dots \} = \{ y, y \} - \{ y, y \}
\]

(3.9) \(\{ x \} = 0 \) (definition of bracket with no covering) 

(3.10) \(\{ \dots , x, x, y, \dots \} = \{ \dots , x, y, \dots \} \) (a repeated variable within a comma may be omitted) 

(3.11) \(\{ \dots , y, y, y, y, \dots \} = \{ \dots , y, y, y, \dots \} - \{ y, y \} - I_x \) 

(3.12) \(\{ x, x \} = -I_x \) 

(3.13) \(\{ y, y, y, y, \dots \} = \{ y, y, y, \dots \} \) (conditioned variables may be removed.) 

(3.14) \(\{ x, y, z \} \ge \{ x, z \} \) , \(\{ x, y, z \} \ge \{ x, y, z \} + \{ x, z \} - \{ y, z \} \) 

(3.15) \(\{ x, y, z \} \ge \{ x, y, z \} + x, z \} \) 

Not that in this above formulae, any random
variable W may be replaced by any group XY...Z
and the relation holds true, irrespective X,Y,Z may be
regarded as the single random variable W, with the its values
in the cartesian product X x Y x ... x Z.

---

## §1 Finite joint distribution 

Point 2 

We assume that we have a collection of finite sets \(X, Y, Z\) whose elements are denoted by \(x_i \in X, y_i \in Y, z_i \in Z\), etc., and that we have a joint probability distribution \(p = P(x_1, y_1, \ldots, z_n)\) defined on the cartesian product of the sets, which represents the probability of the combined event \(x_1, y_1, \ldots, z_n\) and \(z_k\). We then denote by \(X, Y, \ldots, Z\) as the random variables whose values are the elements of the sets \(X, Y, Z\), with probabilities given by \(P\). 

Point 3 

<|det|>[[0, 0, 1000, 1005]]

---

Page 7 

(For example, we might have a joint probability distribution for the political party and religious affiliation of individuals, for which our correlation coefficient, such which specifies nothing here, assumes an extreme, since no numerical value is involved.) 

Also, just for the sake of this justo
discussion about variance. 

No New Paragraph 

Page 4 

Page 4 

<|det|>[[0.5, 0.5, 0.5, 0.5, 0.5,

---

The present chapter is devoted to the mathematical development of the concepts of information and correlation. As mentioned in the introduction we shall use the language of probability theory throughout this chapter to facilitate the exposition, as in later chapters we shall apply the mathematical definitions and formulas without reference to probability models. We shall develop our definitions and theorems in full generality, for probability distributions over arbitrary sets, rather than merely for distributions over real numbers, with which we are mainly interested. We take this course because it is just as easy as the restricted development, and because it gives a better insight into the subject. The first three sections develop definitions and properties of information and correlation for probability distributions over finite sets. In section four the definition of correlation is extended to distributions over arbitrary sets, and the general invariance of the correlation is proved. Section five generalizes the definition of information to distributions over arbitrary sets. Finally, multivariate examples given are called to illustrate applications to stochastic processes and causal machines, respectively.