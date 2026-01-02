# Everett Handwritten Draft -- II Probability Information and Correlation circa 1955.pdf

# Probability, Information, and Correlation 

§1 

distributive 

Joint distribution, marginal & conditional: (marginal & conditional)
We assume that we have a collection of sets, \(X, Y, \ldots, Z\)
where elements we denote by \(x_i \in X, y_i \in Y, \ldots, z_k \in Z\)
and that we have a joint probability distribution, 

\[P(x_i, y_i, \ldots, z_k) \text{ which represents the occurrence of the}
\text{combined event } x_i, y_i, \ldots \text{ and } z_k. \text{ We write this, for}
\text{briefly, } P(x_i, y_i, \ldots, z_k). \text{ We may then}
\text{think of } X, Y, \ldots, Z \text{ as random variables whose values}
\text{are the elements of this joint.} \]

For any subset \(Y, \ldots, Z\) of a set of random
variables \(W, X, Y, \ldots, Z\) we define the Marginal
distribution \(P_{X, Y, \ldots, Z}\) :

---

\[P(y_k \dots z) = \sum_{j_1 \dots j_k} P(w_j \dots y_j, y_{k+1} \dots z)\]

which represents the probability of the joint occurrence of
\(y_k \dots y_{k+1} \dots z\) with no restriction upon the remaining variables. 

**Not, for any subset** \(Y_1 \dots Z\) **of the random variable**
we define the conditional distribution \(P(w_1 \dots y_j \dots z)\) conditioned
upon the values \(W = w_1 \dots X = x_j\) **for** \(j = 1 \dots k\) 

\[P(w_1 \dots y_j \dots z) (y_k \dots z) = \frac{P(w_1 \dots y_j \dots z, y_{k+1} \dots z)}{P(w_1 \dots y_j)}\]

which represents the probability of the joint event
\(Y = y_{k+1} \dots z = z\) conditioned by the fact that \(W_1 \dots X\) are
known to have taken the values \(W_1 \dots W_k\).

---

Finally, for any set function \(F(y_1, \ldots, y_n)\) we define the expectation \(Exp[F]\) as: 

\[(1(3) \quad Exp[F] = \sum_{k=1}^{n} P(y_1, \ldots, y_n) F(y_1, \ldots, y_n)\]

and we note that is \(P(y_1, \ldots, y_n)\) is a marginal distribution of some larger distribution \(P(w_1, \ldots, w_n, y_1, \ldots, y_n)\). 

\[Exp[F] = \sum_{k=1}^{n} \left( \sum_{i,j} P(w_1, \ldots, w_n, y_1, \ldots, y_n) F(y_1, \ldots, y_n) \right) = \sum_{i,j,k} P(w_1, \ldots, w_n, y_1, \ldots, w_n, y_2, \ldots, y_n) F(y_1, \ldots, y_n)\]

\[= \sum_{i,j,k} P(w_1, \ldots, w_n, y_i, \ldots, y_n) F(y_1, \ldots, y_n) \quad \text{so that is we wish to compute } Exp[F] \text{ with respect to some joint distribution, it suffices to use any marginal distribution of the original distribution which contains at least these variables which occur in } F.\]

We may also be interested in Conditional Expectation \(Exp(w_1, \ldots, w_n | F)\) which we define as: 

\[(1(4) \quad Exp(w_1, \ldots, w_n | F) = \sum_{k=1}^{n} P(w_1, \ldots, w_n) F(y_1, \ldots, y_n) \quad \text{and we note, the following rules:} \quad Exp[Exp(B)] = Exp[F] \quad (Def of Independence) \quad Exp[Exp(w_1, \ldots, w_n | F)] = Exp[F] \quad \text{and} \quad Exp[F+G] = Exp[F] + Exp[G]\]

---

## 57 Information: 

Suppose that we have a single random \(X\) with distribution \(P(x_i)\). Then we define a number, \(I_X\), called the information of \(X\) to be: 

\[(2.1) \quad I_X = \sum_i P(x_i) \ln P(x_i) = \exp \left[ \ln P(x_i) \right]\] 

The information is essentially a measure of the
period of a probability distribution as well as the
more clear shortly. That is, any change in the distribution
\(P(x_i)\) which leads out of the probabilities decreases the
information. \(I\) is zero for a perfectly sharp distribution
as form \(P(x_i) = S_i\), and strictly negative for all others.
Many arguments can be given to show that this definition
corresponds clearly to our intuitive notion of what
sometimess information. 

In a similar fashion, we define the Information
of a group of random variables \(X_1, \ldots, X_n\) with joint
distribution \(P(x_1, y_1, \ldots, x_n)\) and \(I_{X_1, \ldots, X_n}\) to be: 

\[(2.2) \quad I_{X_1, \ldots, X_n} = \sum_{i,j,\ldots,k} P(x_1, y_1, \ldots, x_n) \ln P(x_1, y_1, \ldots, x_n) = \exp I_n\] 

Finally, we define a conditional Information \(I_{X_1, \ldots, X_n | Z}\) 

\[(2.3) \quad I_{X_1, \ldots, X_n | Z} = \sum_{i,j,\ldots,k} P(x_1, y_1) \ln P(x_1, y_1, \ldots, x_n | z) \ln P(x_1, y_1, \ldots, x_n | z)\] 

a quantity which measures our information about \(X_1, \ldots, X_n\)
given that we know that \(V = v_1, \ldots, W = w_m\).

---

Some further properties of information are: 

(a) Information is a function only of the probabilities themselves, and in any way depends upon numerical values of the random variables, so that it can be defined for probability distributions, our arbitrary sets, and not restricted to distributions upon numerical values, as are the usual measures of spread, such as variance, etc. 

(2) For independent random variables \(X, Y, Z\):
\[ I_{X, Y, Z} = I_X + I_Y + I_Z \] so that the information about \(X, Y, Z\) is the sum of the individual information, which is in accord with our intuitive feeling that if we are given information about independent events then our total information is simply the sum of the individual information. Also, this requirement of reliability for independent events is akin to the principle of information is essentially only the one given here, a fact that leads great plausibility to our definition (Feschmann). 

Finally, we shall also assume useful Factor Theorem: 

a) \(f\) is convex, Gaussian random variable, 

\[ \Rightarrow f\left(\mathbb{E}[P(G)]\right) \leq \mathbb{E}[P(f(G))] \]

b) \(g\) is not a convex (or a concave) function 

c) Theorem:
\[ P'_e = \sum_j Q_{ij} \cdot \beta_j \]
\[ \sum_j Q_{ij} = \sum_j Q_{ij} = 1, \text{ so } Q_{ij} = 1 \]
\[ \Rightarrow I' \leq I \] (so any leveling out decrease into \(I\)) 

(d) \(I \geq I'\). \(T \leq T' \leq T\)

---

§3 Correlation 

Suppose that we have a pair of discrete random variables \(X\) and \(Y\) with joint distribution \(P(x, y)\). If one makes the statement that \(X\) and \(Y\) are correlated, what is generally meant is that one has something about one variable when he is told the value of the other. Let us focus our attention upon the variable \(X\). If we are not informed of the value of \(Y\) then our information about \(X\) given by the marginal distribution \(P(x)\). However, if we are now told that \(Y\) has the value \(y\), then our information about \(X\) changes to the information of the conditional distribution \(P(Y|x)\). Accordingly to what has been said we wish the degree of correlation to measure how much we learn about \(X\) by being informed of the value of \(Y\). However, since this change of information, \(I_{X|Y} = I_{X} - I_{X|Y}\) may depend upon the particular value \(y\), or \(Y\) which we are told the natural thing to do, in order to arrive at a single number for a measure of the degree of correlation, is to consider the expected change in information about \(X\) given that we are to be told the value of \(Y\). This quantity we shall call the correlation information, or correlation coefficient, and denote by \(I_{X,Y}\) thus: 

\[(3.1) \quad \{X, Y\} = \text{Exp} \left[ I_{X|Y} - I_{X} \right] = \text{Exp} \left[ I_{X|Y} - I_{X|Y} \right]\]

---

Expanding the quantity \(\mathbb{E} \exp \left[ \sum_{i} Y_i^2 \right]\) using rules (1.4) 

\[
\begin{align*}
(3.2) \quad & \mathbb{E} \exp \left[ \sum_{i} \frac{Y_i^2}{X} \right] = \mathbb{E} \exp \left[ \mathbb{E} \exp^2 \left( \ln P(x_i) \right) \right] \\
&= \mathbb{E} \exp \left[ \ln \frac{P(x_i, y_i)}{P(y_i)} \right] = \mathbb{E} \exp \left[ \ln P(x_i, y_i) - \ln P(y_i) \right] \\
&= \mathbb{E} \exp \left[ \ln P(x_i, y_i) \right] - \mathbb{E} \exp \left[ \ln P(y_i) \right] = \mathbb{E}_{X_Y} - \mathbb{E}_Y
\end{align*}
\]

and combining with (3.2) we have: 

\[
\{X, Y\} = \mathbb{E}_{X_Y} - \mathbb{E}_X - \mathbb{E}_Y
\]

So that it is symmetric in X and Y, and hence
equal to the expected change in information about Y
given that we wish to test the value of X. Furthermore, by
(3.3) corresponds precisely to the amount of missing
information "if we process only the marginal distribution
for X and Y." 

Theorem 1. \(\{X, Y\} = 0\) is and only if X and Y
are independent, and its alternative strictly positive. 

Proof: write \(P_{ij} = P(x_i, y_i)\), \(P(x_i) = P_i\), \(P(y_i) = P_j\) 

and let \(P_{ij} = \frac{P_{ij}}{P_j}\) (\(1\) is \(P_j = 0\)) hold \(P_{ij} = Q_{ij} P_j\) 

\[
\lim_{n \to \infty} \mathbb{E} \{Y_i^2\} = \mathbb{E} P \left[ \ln P_{ij} \right] - \mathbb{E} P \left[ \ln P_j \right] - \mathbb{E} P \left[ \ln P_0 \right]
\]

\[
= \mathbb{E} P \left[ \ln P_{ij} | P_{ij} \right] = \mathbb{E} P \left[ \ln Q_{ij} \right] = \sum_{i,j} P_{ij} Q_{ij} \ln Q_{ij}
\]

making use of the inequality \(\ln x \geq 1 - x\) unless \(x = 1\)
we have

---

\[
\begin{align*}
P_i P_j Q_{ij} \ln Q_{ij} > P_i P_j (1 - Q_{ij}) \quad \text{unless } Q_{ij} = 1 \\
\Rightarrow \sum_{ij} P_i P_j Q_{ij} \ln Q_{ij} > \sum_{ij} P_i P_j - \sum_{ij} Q_{ij} P_i P_j = 0 \quad \text{unless finally } Q_{ij} = 1 \text{ or } P_i P_j = 0 \\
\Rightarrow \{X, Y\} > 0 \quad \text{unless } P_{ij} = P_i P_j \text{ all } i, j \text{ (independently)}
\end{align*}
\]

In this regard the correlation is defined in
support to the usual correlation coefficients of statistics,
such as covariance, which can be given even when
the variables are not independent, and which can assume
both positive and negative values. A negative correlation is often
quite as useful as a positive correlation. 

We can generalize (3.3) to define a group
correlation for the groups of random variables
\((U_1, V_1), (U_2, V_2), \ldots, (U_n, V_n)\) defined by \((U_i, V_i, X_{ij}, Z_i)\), to be: 

\[
\{U_i, V_i, X_{ij}, Z_i\} \in \mathbb{R}^{n \times n} \times \mathbb{R}^{n \times n}, \quad T = \prod_{i=1}^n \prod_{j=1}^n \ldots \prod_{i=1}^n \prod_{j=1}^n \ldots \ldots \prod_{i=1}^n \prod_{j=1}^n \prod_{k=1}^n \ldots \ldots \prod_{i=1}^n \prod_{k=1}^n \ldots \ldots \ldots \prod_{i=1}^n \prod_{k=1}^m \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \dots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \cdots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ddots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \vdots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \text{and} \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \quad \text{and} \ldots \ldots \ldots \ldots \ldots \ldots \ldots
\]

Again measuring the information defining of the variable.
Theorem 1 is also satisfied by the group correlation, so
that it is 0 if and only if the group are mutually indep.
And, of course, we can define conditional correlations if
we wish, in the above manner.

---

we list some easily proved relations: 

3.5 Commutator: 

\[
\begin{align*}
\{x, y, z\} &= \{y, z, x\} + \{z, x, y\} \\
\{x, y, z\} &= \{y, z, x\} + \{z, y, x\}
\end{align*}
\]

3.6 Commutator: 

\[
\{x, y, z\} = \{y, z, x\} + \{z, x, y\} = \{y, z\} - \{z, x, y\}
\]

3.7 \(\{X\} = 0\) (definition of brach with no commutator) 

3.8 \(\{x, x, x\} = \{x, x, x\}\) (variably repeated within commas) may be omitted 

3.9 \(\{y, y, y\} = \{y, y, y\}\) - \(I_V - \{y, y\}\) 

(implicitly over a comma) 

3.10 \(\{X, X\} = -I_X\) 

3.11 \(\{y, y, x\} = \{y, x, x\}\) 

3.12 \(\{y, y, x\} = \{y, x, x\}\) (conditional variables may be omitted) 

3.13 \(\{X, Y, Z\} \equiv \{X, Z, Y\}\) \(\{X, Y, Z\} \equiv \{X, Y\} + \{X, Z\} - \{Y, Z\}\) 

Note in above formulae, any random
variable, W may be replaced by a group X#...Z
and the notation remains true.

---

Note that we are now able to compute correlations for distributions which have both discrete and continuous parts, by simply choosing as measure difference measure for the continuous part and uniform measure for the discrete part, to that if our distribution is \(P(x)\) density, with discrete lumps \(P(x_i)\), we define the info to be 

\[I_x = \int P(x) \frac{dP(x)}{dx} + \sum_i P(x_i) \ln P(x_i)\]

on \(x\) \(P(x, y)\) and lumps \(P(x_i, y_i)\) 

\[\Rightarrow P(x) = \int P(x, y) dy \quad \text{and} \quad P(x_i) = \sum_j P(x_i, y_j)\]

\[I_{xy} - I_x - I_y = \int P(x, y) \ln P(x, y) dy + \sum_{i,j} P_i \ln P_i - \sum_i P_i \ln P_i\]

\[= \int P(x, y) \frac{P(x, y)}{P(x) P(y)} dx dy + \sum_{i,j} P_i \ln \frac{P_i}{P_j}\]

\[= \int \int x_i y_j \quad \text{conditions}\]

This result is useful for quantum mechanics where spectra can be mixed discrete and continuous.

---

Thorem 1.8 divided set, \(f, g\) functions
on divided set.

3. \(\lim f = a\) \(\lim g = b\)

\[\Rightarrow \lim (f+g) = a+b\]

so that if the individual limits exist
then the limit of the sum exists and is
equal to the sum of the limits.

Therefore, Defining Information 

\[I_{x_1, \ldots, z} \quad I_x \quad I_z \quad \text{as divided}\]
set limits

We have that: \(I_x \ldots I_z \ldots I_{x_1, \ldots, z}\) exist
(they always do)
by monotonicity 

\[ \Rightarrow \lim (I_{x_1, \ldots, z} - I_x - I_y - I_z) \]
\[ = \lim I_{x_1, \ldots, z} - \lim I_x - \ldots - \lim I_z \]
\[ \therefore I_3 = I_{x_1, \ldots, z} - I_x - I_z \]

so that the formula holds as long as right hand
side not identitminates 

Moreover, Since for each partition marked
so is red

---

We now consider the effects decomposition of the
values of random variables. For example, we may discuss
that the sum \(X_i\) is actually the disjunction of
several events \(X_i^1, X_i^2, \ldots, X_i^n\), so that \(X_i\) occurs if
any of the \(X_i^1\) occurs. If the probabilities for the \(X_i^1\) are
\(P(X_i^1) = 1\), then \(P(X_i) = \sum P(X_i^1)\). Similarly, if we had
a joint distribution \(P(X_i^1, X_i^2, \ldots, X_i^n) = \sum P(X_i^1, X_i^2, \ldots, X_i^n) = \)
\(P(X_i^1, X_i^2, \ldots, X_i^n)\). 

On general, we shall say that a distribution
\(P = P(X_1, \ldots, X_n)\) is a refinement of the distribution \(P(X_1, \ldots, X_n)\) 

\[P(X_i, \ldots, Y_j) = \sum_{X_i, \ldots, Y_j} P'(X_i, \ldots, Y_j)\]

This is a refinement of a probability distribution we
mean the ability to distinguish between events which
were previously considered to be a single event. For example,
if we had a continuous probability density \(P(x, y)\), then
by definition of the area-intervals we arrive at
a finite total probability distribution over the rectangles
in \(x-y\) space by integrality \(P(x, y)\) on each rectangle,
which represents the probability that \(X, Y\) is contained in that
rectangle. If we now subdivide the intervals, and hence the rectangles,
the new joint distribution is a refinement of the old one. 

We now state an important theorem concerning the behavior
of correlations under a refinement of a joint distribution: 

**Theorem 2** No correlation product decreases
under refinement of a joint probability distribution. 

\[P'(\text{refinement of } P) \Rightarrow \{X_1, \ldots, X_i\} \cong \{X_1, \ldots, X_i\}\]