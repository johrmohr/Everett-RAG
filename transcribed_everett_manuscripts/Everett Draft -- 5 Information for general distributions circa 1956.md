# Everett Draft -- 5 Information for general distributions circa 1956.pdf

(13) Relative information relative to a given information measure.

(5) Formation for general distributions:

Although we have given a definition of correlation
applies for all probability distributions, we have not
yet extended the definition of information, past finite
distributions. In order to make this extension we first
generalize the definition that we gave for discrete
distributions, to a definition of information relative
to a distribution of random variables.

If we assign a
measure to the set of values of a random variable X,
which is simply the argument of a positive
number, it to call value it is in this finite
case, we obtain the information of a probability
distribution \( P(x_i) \) relative to this finite measure to be

\[
I_x = \sum_i P(x_i) \ln \frac{P(x_i)}{a_i} = \text{Exp} \left[ \ln \frac{P(x_i)}{a_i} \right]
\]

(5.1)

If we have a joint distribution of random
variables \( X, Y, \ldots, Z \), with discrete measures on
their values \( \{a_3, \{b_3\}, \ldots, \{c_3\} \) respectively, then
we obtain the total information relative to this measure:

---

\[I_{X,Y,\cdots ,Z} = \sum_{i,j,k}p(x_i,y_j,z_k)\ln \frac{p(x_i,y_j,z_k)}{d_{i,j,k}C_k} = E_{XP}\left[\ln \frac{p(x_i,y_j,z_k)}{d_i,b_j,C_k}\right]\]

so that the **Ep** **ic** **measure** on the **cartesian** **product**
set is always **taken** to be the **product** **measure** of
the **individual** **measure**.
We should **link** **to** **our** **previous** **partition** **slightly** and
always **being** **defined** **relative** **to** **some** **Ep** **ic** **information**
measure, so that our **previous** **definition** **of**

---

of information is to be regarded as the information relative to the measure for which all the \(c_i\) 's
by a n. \(C_i\) 's are taken to be unity, which we
shall interpret as the uniform measure. 

Let we now compute the correlation
\[ [X, Y, \ldots, Z] = \frac{\text{Exp}[\ln \frac{P(X, Y, \ldots, Z)}{P(X) \ldots P(Y) \ldots P(Z)}] - \text{Exp}[\ln \frac{P(X)}{P(X)}] - \text{Exp}[\ln \frac{P(Y)}{P(Y)}] - \ldots - \text{Exp}[\ln \frac{P(Z)}{P(Z)}]}{P(X) \ldots P(Y) \ldots P(Z)}] \] 

\[
\begin{align*}
[X, Y, \ldots, Z] &= I_{X, Y, \ldots, Z} - I_X - I_Y - \ldots - I_Z \\
&= \text{Exp} \left[ \ln \frac{P(X, Y, \ldots, Z)}{P(X) \ldots P(X)} \right] - \text{Exp} \left[ \ln \frac{P(X)}{P(X)} \right] - \text{Exp} \left[ \ln \frac{P(Y)}{P(Y)} \right] - \ldots - \text{Exp} \left[ \ln \frac{P(Z)}{P(Z)} \right] \\
&= \text{Exp} \left[ \ln \frac{P(X, Y, Z)}{P(X) \ldots P(X)} \right] = \{X, Y, \ldots, Z\}
\end{align*}
\]

So that the correlation for discrete distributions,
or defined by (3.4) is independent of the choice of
information measure, and the correlation remains an
absolute, not relative quantity. \(P(Z)\) we now
consider refinements of our distribution, as before,
and make that much a refinement is also a refinement
of the measure, then we can prove a
relation analogous to Theorem 2: 

Theorem 2: The information of a distribution relative
to a finite measure never decreases under refinement.
(proof in appendix) (a) \(P' \in P \Rightarrow I' \geq I^P\) 

Therefore,
the information of a finite measure \(M\) is a probability measure
on the cartesian product of arbitrary sets \(X, Y, \ldots, Z\),
relative to the information measure \(M_X, M_Y, \ldots, M_Z\).

---

by considering, as before, finite partitions \(\mathcal{P}\) into
the sets \(\mathcal{P}_1, \mathcal{P}_2, \ldots, \mathcal{P}_n\), for which we take
as definition of information: 

\[(5.9) \quad I_{\mathcal{X} \times \mathcal{Y} \cdot \mathcal{Z}}^{\mathcal{P}} = \sum_{i,j,k} M_{\mathcal{P}}(Q_i, Y_j, \ldots, Z_k) \ln \frac{M_{\mathcal{P}}(Q_i, Y_j, \ldots, Z_k)}{M_{\mathcal{P}}(Q_i) M_{\mathcal{P}}(Y_j) \ldots M_{\mathcal{P}}(Z_k)}.\]

\(I_{\mathcal{X} \times \mathcal{Y} \cdot \mathcal{Z}}^{\mathcal{P}}\) is then, as before, a monotone function
upon the directed set of partitions (by item 4) and
as before, we take the directed set limit for each level
definition: 

\[(5.5) \quad I_{\mathcal{X} \times \mathcal{Y} \cdot \mathcal{Z}} = \lim_{\mathcal{P} \to \mathcal{P}} I_{\mathcal{X} \times \mathcal{Y} \cdot \mathcal{Z}}^{\mathcal{P} \to \mathcal{P}} = \sup_{\mathcal{P}} I_{\mathcal{X} \times \mathcal{Y} \cdot \mathcal{Z}}^{\mathcal{P}}\]

Which is then the information relative to the finite union
measure \(M_1, M_2, \ldots, M_n\). 

Now, for function \(f\) on a directed set, the
existence of limit and being is a sufficient condition
for the existence of \(\lim(f+g)\), which is then limit + lim(g)
provided that this is not indeterminate (a → ∞). Therefore 

\[ \begin{aligned} \text{Theorem 5} \quad [X_1, \ldots, X_n] = \lim_{i \to \infty} [X_{i,1}, X_{i,2}]^p = \lim_{i \to \infty} [I_{X_{i,1}, \ldots, X_{i, n}} - I_{X_{i, n}}]^p \\ = I_{X_{i,1}, \ldots, X_{i, n}} - I_{i, n} \end{aligned} \]

where the information is then relative to
systematic
any finite measure for which the expression
is not indeterminate. It is sufficient
for the validity of that that the finite
measures \(M_1, \ldots, M_n\) be such that the marginal
information \(I_{X_1, \ldots, X_n}\) is positive infinite.

---

(Guilty) by a man of my own
No. 1

---

The latter statement holds, because of the
general relation \(I_{x_1, \ldots, x_n} \geq I_x + \ldots + I_y\), the determinants of \(I_{x_1, \ldots, x_n}\) are
in general no long as all of the \(I_{x_i}\) are \(L + \infty\). 

Henceforth, unless otherwise noted, we shall
understand that information is to be computed with
respect to the uniform measure for discrete distributions
and Lebesgue measure for continuous distributions
over real variables. In case of a mixed
distribution with a continuous density \(P(x, y, \ldots, z)\)
plus discrete "lumps" \(P'(x_i, y_j, \ldots, z_k)\) we shall
understand the lumps drawn to be the uniform
one over the discrete range, and Lebesgue measure over
the continuous range. Three conventions thus lead
us to the expressions: 

\[
(5.6) \quad I_{x_1, \ldots, x_n} = \frac{\sum_{i,j,k} P(x_i, y_j, z_k) \ln P(x_i, y_j, z_k)}{P(x, y, z) \ln P(x, y, z)} \quad \text{(discrete case)} \\
\qquad + \frac{\sum_{i,j,k} P(x_i, y_j, z_k) (\ln P(x_i, y_j, z_k) - \ln P(x, y, z))}{P(x, y, z) (\ln P(x, y, z) - \ln P(x, y, z))} \quad \text{(multiscale case)} \\
\qquad \text{(unless otherwise noted)}
\]

The mixed case occurs again in quantum mechanics,
for quantities have both a discrete and continuous spectrum.

---

D. In introduction, we Feller
13. Influence on the article and edited
Bollinger, Rie and Ryle (1954 - 55
article in the period magazine. 

§1. Early Information in Scholastic Proceedings
§2. Convention of Information in Class Meetings
(Contribution to the Proceedings)