# Everett Handwritten Draft -- 4 Generalization and further properties of correlation information circa 1955.pdf

§4 Generalization and further properties of correlation information:

On order to arrive at a general definition of correlation, applicable to joint probability distributions we are aiming to establish a certain set of properties of correlation that we have found the effect upon the correlation of two discrete random variables. Now we can implement of the range of one of the variables, say \(X_1\). That is, we initially our joint distribution is

\[
P_{ij} = P(x_i; y_j) \text{ for the event } x_i \text{ and } y_j, \text{ Suppose, however, that one of the events, say } x_1 \text{ is actually the disjunction of two events, } x_1 \text{ and } x_2 \text{ so that we say } x_1 \text{ has occurred if either } x_1 \text{ or } x_2 \text{ occur.} \]

Let \(P_{ij}\) be \(P(x_i; y_j)\), \(P_{12} = P(x_2; y_2)\), then we have the relation that the form probability \(P_{ij}\) are

\[
P_{12} = P_{11} + P_{12} \quad \text{(all } j \text{)}
\]

\[
P_1 = P_{11} + P_{12}
\]

allowing quantities remaining the same. We wish now to investigate how the correlation has changed when we change from our old distribution \(P'_{ij}\) to our new distribution \(P_{ij}\) (i=1,2,3,...) where

\[
P'_{ij} = \begin{cases} P_{ij} & \text{for } i=2,3,\ldots \\ P_{1j} + P_{12j} & i=1 \end{cases} \quad \text{(all } j \text{)}
\]

\[
P'_{1} = P_{1} \quad \text{(all } j \text{)}
\]

\[
P'_{2} = P_{2} \quad \text{(all } j \text{)}
\]

\[
P'_{12} = P_{12} + P_{12}
\]

---

**Theorem 3** Any refinement of a discrete joint probability distribution never decreases the correlation information. 

This is simply the quantitative solution of the intuitive notion that closer analysis of a situation in which quantities \(X\) and \(Y\) are dependent can never learn the knowledge about \(Y\) which can be obtained from \(X\). 

This theorem now allows us to give a rigorous definition of correlation which will apply to joint probability distributions over completely arbitrary sets, i.e. for any probability measure over an arbitrary product space, in the following simple manner:

Given two arbitrary sets \(X\) and \(Y\) and a probability measure on the product space \(M_0(X \times Y)\), let \(P^X\) be a partition of \(X\) into any (infinitesimal) number of measurable subsets, \(X_i\) is that \(X_i \cap X_j = \emptyset\) if \(i \neq j\), and a partition of \(Y\) into sets \(Y_i\). We will say that \(P^Y\) is a refinement of \(P^X\) if \(P^X \subset P^Y\), if \(P^X\) results from further subdivision of the sets \(X_i\) and \(Y_i\). Any such partition results in a discrete joint probability distribution over the subsets, \(P^X = P(X_1, Y_1) = N_0(X_1, Y_1)\) of the probability is defined which denotes by \(\{X_i, Y_i\}^P\) furthermore, by theorem (2) we have

\[
P^X \subset P^Y \implies \{X_i, Y_i\}^P \supseteq \{X_j, Y_j\}^P
\]

this means that for any sequence of partitions, \(P_1, P_2, \ldots\) such that \(j > i \implies P_1 \subset P_i\), a sequence of refinements, the sequence of correlations is monotone increasing, and hence possesses a limit (jointly infinite).

---

Note that the set of all partitions \(P\) forms a directed set, since they are partially ordered under the relation \(\supset\) (refinement), and time further from any pair of partitions \(P\) and \(P'\) there always exists a \(P''\) which is a refinement of both. Furthermore, the function \([X, Y]\) is a monotone function on the directed set, by theorem (1). So that this directed set limit always exists (it may be infinite, but in any case it is always well-defined), and it is this limit which we take as the general definition of the correlation. 

\[ \text{Def: } [X, Y] = \lim_{\to P} [X, Y]^P \]

It is a further consequence of the monotonicity and refinement that this directed set limit is equal to the supremum of \([X, Y]^P\) and so that we can 

\[ (1) \quad [X, Y]^P = \sup_P [X, Y]^P \]

which we could equally well have taken as the limit.

---

We now take as the basic definition of the correlation
\(X, Y^3\) :

\[Def: \{X, Y^3\} = \sup_{P} \{X, Y^3\}^P \quad (range over all partitions)\]

This has the consequence that for any given partition
\(P\), further refinement will always increase the
correlation, and furthermore that there always exists
a refinement of \(P\) for which the correlation is
arbitrarily close to \(\{X, Y^3\}\). This latter statement
is easily established since by definition of
\(\{X, Y^3\}\) as \(\sup \{X, Y^3\}^P\) there always exists a \(P^*\) for
which the correlation is arbitrarily close to \(\{X, Y^3\}\), and
since furthermore there always exists a \(P^*\) which
is both a refinement of \(P\) and of \(P^*\), so that its correlation
is no further from \(\{X, Y^3\}\) than that of \(P^*\). Furthermore
the correlation is approachable by analysis into
finite sets.

We can now prove a very important theorem about
correlation, namely its invariant with respect to change.
Let \(X, Y\) be two with probability measure \(M(X|Y)\) on the
product space. Let \(f(x)\) be a one-to-one mapping of the
set \(X\) onto a set \(U\), \(g(Y)\) onto a one-to-one mapping of \(Y\) onto \(V\).
Then the probability measure induced on the product space \(U \times V\)
is \(M_P^*(U_i, V_j) = M_P(f^{-1}(y), g^{-1}(x))\). Consider any
partition \(\Phi\) of \(X, Y\) into sets \(\{X_1, Y_1\}\) with probability
distribution \(P_1\). Then there is a corresponding partition \(P\)
\(\{X_1, Y_1, X_2, Y_2\}\) in \(U, V\) opposite into sets \(U_1, V_1\) where
\(U_i = f(X_i)\), \(V_j = g(Y_j)\), the partition into the image of \(P\).

---

which has the probability distribution \(P_{ij} = M_{i}(U, V_{j}) = M_{i}(X_{i}, Y_{j})\)
= \(P_{ij}\) which is identical to that of \(P_{in} X, Y\) space,
to that: 

\[4.9 \quad [X, Y]^P = [U, V]^P\]

which obviously implies that 

\[8.10 \quad \sup_{P} [X, Y]^P = \sup_{P} [U, V]^P\]

and we have proved the theorem: 

Theorem ( ) \([X, Y] = [U, V]\) where \(U\) is any
one-to-one image of \(X\), \(V\) any one-to-one image of \(Y\). 

In other words, \([X, Y] = \{f(X), g(Y)\}\) where family
are any arbitrary one-to-one functions. 

This means changing Variable to functionally modified Variable
leaves the condition unchanged. This again is plausible and satisfies generalizes
the special consequence of theorem ( ) in that 

for any continuous joint probability density \(f(x, y)\) 

the correlation between \(t\) and \(y\) is the famous that of
\(f(t)\) and \(g(y)\). 

A special consequence for the partition of two particles,
is that the random variables are two-points coordinates. 

The theorem asserts that the partition correlation is then
the same for all coordinate systems, even if
different coordinate systems are used for each particle. 

Also, for a joint distribution for a pair of events
in space-time, the correlation is invariant to
arbitrary coordinate (spacetime) transformations, again
even allowing different transformations for each
particle. This invariance illustrates the fundamental
nature of the correlation in probability distributions.

---

The preceding results about the behavior of discrete correlation under refinement, the generalizations to arbitrary distributions, and the generalized invariance properties extend immediately from the binary correlation to groups correlations. 

Due to the fact that the correlation is defined as a limit for discrete distributions, it suffices to relate 3.5 to 3.13, which contain only correlation brackets remain true for arbitrary distributions. Only 3.9 and 3.10, which contain in addition information terms, can not be extracted, since as yet information is not defined for arbitrary distributions.

---

## Continuous Distributions: 

So far we have defined information for discrete distributions only, even though we have arrived at a general definition of **correlation**. The definition of **information** for arbitrary distributions can vary, however, the curve at by considering discrete approximations, as was done for correlation, since this process will generally lead to negatively infinite results. 

Suppose that we have a **continuous probability distribution** \(P(x)\). If we divide the bin into equal spaced intervals of length \(h\), we obtain from \(P(x)\) a discrete probability distribution over the intervals, with \(P_i = \int_{a_i}^{a_{i+1}} P(x) dx\) where \(a_i\) is the beginning point of the \(i\)th interval. In the limit as \(h\) becomes sufficiently small so that \(P(x)\) is essentially constant over each interval we have that \(P_i = \int_{a_i}^{a_{i+1}} P(x) d x \sim h P(a_i)\) to that this information is nearly \(I_n = \sum_{i=1}^{n} P_i \ln P_i \approx \sum_{i=1}^{n} \frac{P(x_i)}{h} \ln P(x_i)\) which is \(I_n \approx \int P(x) \ln P(x) dx + \ln h\) which will generally diverge to \(-\infty\) as \(h \to 0\) because of the last term. By taking \(h\) to each choice of interval length \(h\) we redefine the **information** \(I_n = I_n - \ln h\) then as course we have that 

\[ \lim_{h \to 0} I_n = \int P(x) \ln P(x) dx \overset{\text{def}}{=} I_x \]

which we combine as the **information** of the continuous distribution \(P(x)\).

---

This procedure of happy exception content is
pertinent divergence may appear to be unusual
arbitrary, but when we remember that it is not
absolute information but difference of information,
that are of significance we see that the presence
of this constant is immaterial, since it drops out
in any difference. That is for any subdivision of
the line into intervals of length h, the difference
in the direct information resulting from two distributions
\(P(x)\) and \(P(x)\), \(I_h^1 - I_h^2\) is the sum of \(I_h^1 - I_h^2\)
so that in the limit as \(h \to 0\) the difference in the
ordinary direct information is given by: 

\[ \lim_{h \to 0} I_h^1 - I_h^2 = \lim_{h \to 0} I_h^1 - I_h^2 = f(x) \mu_1(x) - f(x) \mu_2(x) dx \]
\[ = I_x^1 - I_x^2 \]

because
for information
difference, this
value is the
limit of the
divergence
divergence. 

so that our definition of the information of a continuous
distribution is justifiable. We can think of the
information no different as the information relative
to the information of the uniform distribution over the
unit interval, which has zero information by our definition.
Information in this defined can range from +∞ for
a S function distribution to -∞ or to distribution tends
toward uniformity over the whole line. 

In similar fashion we define the information
of a continuous joint distribution, \(P(x, y, \ldots)\) to be 

\[ I_{X,Y,\ldots} = \iint P(x, y, \ldots) \ln P(x, y, \ldots) dx dy \]

---

And we find for the correlation, \(\{X, Y\}\) : 

\[
\{X, Y\} = I_{X, Y} - I_X - I_Y = \int P(x, y) \ln \frac{P(x, y)}{P(x) P(y)} dx dy
\]

so long as these quantities are defined. In the event that
these quantities are not defined, the correlation will still
be defined in the previous manner. 

Transformation properties for continuous information: 

If we consider a joint continuous density \(P(x, y, \ldots, z)\) with information \(I_{X, Y, \ldots, Z}\) and transform variables to \(u, v, w\) 

\[
\frac{u = u(x, y, \ldots, z)}{v}
\]

\[
w = w(x, y, \ldots, z)
\]

with information \(I_{X, Y, \ldots, Z}\) 

with transformation \(I_{X, Y, \ldots, Z}\)

---

Concluding remarks upon general definition
of information: 

So far we have defined information for discrete
distributions, and given a special satisfactory definition
for continuous distributions. In actuality, as we have
seen, the definition of information is somewhat arbitrary.
What we can do is give a definition of information
for a probability measure over a direct product, relative
to some other measures upon the basic sets. Thus
other measures that to a product measure on the
product space which we shall refer to, that
basic measures. The probability measure thus leads
to a probability density with respect to the
basic measure and we define the information as
the integral of this probability density times its
logarithm with respect to the basic measure. That is
we define the Information relative to the basic measure
as the expectation of the logarithm of the probability
density with respect to the basic measure.
In this case the correlation \(\mathbb{E}[Y_1 \dots Z]^2\) is still
equal to \(\mathbb{E}[X_1 \dots Z - X_1 - Y_1 - \dots - Y_1 - Z]\), for all
choices of the basic measure where the latter expression
exists and is not indeterminate. That is, we can choose
our basic measure in any manner which makes the
value of \(\mathbb{E}[X_1 \dots Z - X_1 - Y_1 - Y_1 - \dots - Y_1 - Z]\) unambiguous for
the calculation of \(\mathbb{E}[Y_1 \dots Z]^2\).