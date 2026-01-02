# Everett Handwritten Fragments -- Discrete approximations to continuous distributions circa 1955.pdf

1
Discret approximations to continuous distributions
Rigorous of car, Existence guaranteed 

Given continuous \(P(x, y)\) 

divide into small intervals \(\Delta x_i\) and \(\Delta y_j\),
where \(x_i \in \mathbb{R}\) and \(y_j \in \mathbb{R}\). 

Proof of \(P(\Delta x_i \Delta y_j) = P_{i,j} = P(x_i, y_j) \Delta x_i \Delta y_j\) 

\[C^* = \sum_{i,j} P_{i,j} \frac{P_{i,j}}{P_{i,j}}\]

\[= \frac{\sum_{i,j} P(x_i, y_j) \Delta x_i \Delta y_j}{\sum_{K} P(x_i, y_j) \Delta x_i \Delta y_j} \ln \frac{P(x_i, y_j) \Delta x_i \Delta y_j}{\sum_{K} \frac{P(x_i, y_j) \Delta x_i \Delta y_j}{\sum K P(x_i, y_j) \Delta x_i \Delta y_j}}\]

---

\[= \sum_{i,j} P(x_i, y_j) \triangle x_i \triangle y_j \cdot \ln \frac{P(x_i, y_j)}{\sum_k P(x_k, y_j) \triangle x_k} \cdot \sum_k P(x_i, y_j) \triangle y_k\]

\(P(x_i, y_j) \triangle x_i \triangle y_j\)

\(= \sum_{i,j} P(x_i, y_j) \triangle x_i \triangledown y_j \cdot \ln \frac{P(x_i, y_j)}{\sum_k P(x_i, y_j) \triangle x_k} \cdot \sum_k P(x_i, y_i) \triangle y_k\)

\(\text {let } \text {any other } \text {support is } \leq 1\)

**let**

\(\lim_{x \to 0} \text {lim }\)

as \(x \to 0\)

= \(\int P(x, y) \ln \frac{P(x, y)}{P(x) P(y)} \text {deby } = C(x, y)\)

as \(\partial K\)

\[\text {Take } \lim \text {bail of } \text {Correlation as } \text {lim of } \text {process, then}\]

\[\]

\[\]

---

**Cumulative Distribution :** 

\[A(x'_1, y') = \text{Prob } x < x' \text{ and } y < y'\]

\[A(x'_2, \infty) = \text{Prob } x < x' \quad \text{(marginal cumulative)}\]

\[A(\infty, y') = \text{other marginal}\]

**Proof that** 

\[P(\text{origin 1}) = A(x'_1, x_1)\]

\[P(\text{origin 2}) = A(x'_2, y_2) - A(x'_1, y_1)\]

\[P(\text{origin 3}) = A(x'_2, y_2) - (1) - (2) - (1)\]

\[= A(x'_2, y_2) - A(x'_1, y_1) + A(x'_1, y_1) - A(x'_2, y_1) + A(x'_2, y_2) - A(x'_1, y_2) - A(x'_1, y_1) + A(x'_2, y_1) - A(x'_2, y_2)\]

---

\[ \dot{x} = A(x_1, y_1) - A(x_1, y_2) - A(x_2, y_1) + A(x_2, y_2) \]

\[ \dot{y} = \dot{x} \text{ divided by its ordered sequence } \dot{x}_i \text{ into } \dot{y}_i \]

and integral \( P_{i,j} \) as proof of sequence \( \dot{x}_i \leq \dot{x}_{i+1} \) and \( \dot{y}_i \leq \dot{y}_{i+1} \)

\[ P_{i,j} = A(x_{i+1}, y_{j+1}) - A(x_i, y_{j+1}) - A(x_i, y_i) + A(x_i, y_i) \]

\[ P_j = A(\infty, y_{j+1}) - A(\infty, y_j) \]

---

1. Das Maximum always exists C ? 

also really nice \(P_{i,j} \to P_{i,j}\) and \(P_{i+j}\) such that 

\[P_{i+j} + P_{i+j} = P_{i,j}\]

\[P = \sum_{i} P_{i,j} \quad \text{and} \quad P_{i,j} = \sum_{j} P_{i,j+j}\]

\[I' = \sum_{i,j} P_{i,j} \ln \frac{P_{i,j}}{P_{i,j} P_{j}} = \sum_{i,j} P_{i,j} \ln \frac{P_{i-j}}{P_{i-j} P_{j}} + \sum_{i,j} P_{i-j} \ln \frac{P_{i-j}}{P_{i-j} P_{j}} \]

\[= \sum_{i,j} P_{i,j} \ln \frac{P_{i,j} P_{i-j}}{P_{i-j} P_{j}} + \sum_{i,j, k} P_{i-j} \ln \frac{P_{i-j}}{P_{i-j}} \sum_{j} P_{i-j} \ln \frac{P_{i-j}}{P_{i-j}}\]

\[\text{converge to } \sum_{i,j} P_{i,j} \ln \frac{P_{i,j}'}{P_{i,j} P_{j}} + \sum_{i,j} P_{i-j} \ln P_{i-j} \ln \frac{P_{i-j}'}{P_{i-j} P_{j}}\]

---

fun is be
compared = 

\[
\sum_j \frac{p_{ij}}{p_{ij}} \ln \frac{p_{ij}}{p_i p_j} \quad i = 1 \\
\sum_j \frac{p_{ij} + p_{2j}}{(p_i + p_2) p_j} \ln \frac{p_{ij} + p_{2j}}{(p_i + p_2)} \quad i = 2
\]

\[
= \sum_j (p_{ij} + p_{2j}) \ln \frac{p_{ij} + p_{2j}}{(p_i + p_{2}) p_j}
\]

\[
\begin{align*}
\text{compared to} \quad & \sum_j p_{ij} \ln \frac{p_{ij}}{p_i p_j} + \sum_j p_{2j} \ln \frac{p_{2j}}{p_i p_j} \\
= & \sum_j (p_{ij} + p_{2j}) \ln \left( \frac{p_{ij}}{p_{ij} + p_{2j}} \right) + \sum_j (p_{ij} + p_{2j}) \ln \frac{p}{p_{ij} + p_{2j}}
\end{align*}
\]

in particular
need this 

\[
(p_{ij} + p_{2j}) \ln \frac{p_{ij} + p_2j}{(p_i + p_2)p_j} \le p_{ij} \ln \frac{p_{ij}}{p_ip_j} + p_{2j} \ln \frac{p_{2j}}{p_ip_j}
\]

---

Now, \((P_1 + P_2) \ln \frac{P_1 + P_2}{(P_1 + P_2)P_2} \leq (P_1 + P_2) \ln \frac{P_1 + P_2}{P_1 P_2}\) and \(\leq 11\) 

\[ \text{ie} \quad (\alpha_1 + \alpha_2) \ln \frac{\alpha_1 + \alpha_2}{(P_1 + P_2)P_3} \leq (\alpha_1 \ln \frac{\alpha_1}{P_1} + \alpha_2 \ln \frac{\alpha_2}{P_2})\]

\[ = (\alpha_1 + \alpha_2) \ln \left( \frac{\alpha_1 + \alpha_2}{P_1 + P_2} \right) - (\alpha_1 \ln \frac{\alpha_1}{P_1} + \frac{\alpha_2}{P_2}) \leq \alpha_1 \ln \frac{\alpha_1}{P_1} + \alpha \ln \frac{\alpha_2}{P_2} - \alpha \ln \frac{\alpha_1}{P_1} - \alpha \ln \frac{\alpha_2}{P_2} \]

need only prove: 

\[ (\alpha_1 + \alpha_2) \ln \frac{\alpha_1 + 2}{P_1 + P_2} \leq \alpha_1 \ln \frac{\alpha_1}{P_1} \quad + \quad \alpha_2 \ln \frac{\alpha_2}{P_2} \]

\[ = (\alpha_1 + \alpha_2) \ln (\alpha_1 + \alpha_2) - (\alpha_1 + \alpha_2) \ln P_1 + P_2 \]

True by #119 of Hardy, without Hardy, only
\(x \ln x + y \ln y > (x+y) \ln \frac{x+y}{2}\)

---

So draw a Theorem 

given discrete joint distribution, distribution
of any blocks above, never increases.
condition. 

Then reverse to prove that 

Condition is always defined for any 

and prior distribution simply as limit of approximations
by discrete distributions. Since each refinement
does not decrease correlation, the sequence of
opportunity correlation is monotone ↑, hence
approaches a limit (which may of course be infinite). Negative
correlation always defined. Moreover this is independent
of the relative sizes of the patches, hence invariant
to every Scale change. (Normalized measure of joint
is product measure of merging) 

hence given joint distribution with sphere approximation by patches
gives in limit C for the continuous part
+ C for the discrete part

---

Inelastic Sache, negative \(\alpha\) 

\[ \text{Contributive} \propto \ln \frac{\infty}{\infty} = \infty \ln \frac{1}{\infty} = -\infty \ln \infty \]

Correlation 

Note since inequality 

\[ \frac{\ln x}{a} + \frac{\ln y}{b} > \frac{(x+y)\ln \frac{x+y}{a+b}}{a+b} \]

\[ = \frac{\ln x}{a} + \frac{\ln y}{b} + \frac{\ln z}{c} \geq \frac{(x+y)}{c} \ln \frac{(x+y)}{a+b} + \frac{3 \ln z}{c} \]

\[ \Rightarrow \text{by induction} \sum_{i} x_i \ln x_i \geq \left( \sum_{i} \ln \frac{x_i}{x_i} \right) \sum_{i} x_i \]

\[ \text{no this difference for group correlation} \]

---

## 5. Probability distributions 

Let \(P(xy, \ldots, z)\) represent a joint probability density for the random variables \(X, Y, \ldots, Z\), where values are real numbers, so that \(P(xy, \ldots, z) dx dy \ldots dz\) is interpreted to mean the probability that \(X\) will take a value in the interval \([x, x+dx]\) and \(Y\) will take a value in \([y, y+dy]\) and \(\ldots\) and \(Z\) will take a value in \([z, z+dz]\). 

We now define a marginal probability for any subset of the original random variables, say \(X, Y\) to be the integral of the total joint density with respect to the remaining variables, i.e. 

\[P(x, y) = \int_{x, y} P(x, y, z, \ldots, w) dz \ldots dw\]

Which represents the density for the joint events \(X \in [x, x+dx]\) and \(Y \in [y, y+dy]\), with no restriction on the remaining variables. This the relative density over \(X, \ldots, Y\) when we have no information about the other variables. 

Finally, we define a conditional density for any subset \(X_1, \ldots, X_n\) conditioned on any remaining variables having prescribed values, say \(Z = z_1, \ldots, W = w_n\) denoted by \(P_{X_1, \ldots, X_n|Z=z_1, \ldots, W=w_n}\). 

\[P_{X_1, \ldots, X_n|Z=z_1, \dots, W=w_n} = \frac{P_{X_1, \ldots, X_n, Z=z_1, \ldots, W=w_n}}{P_{Z=z_1, \ldots, W=w_n}}\]

which represents the density for \(X_1, \ldots, X_n\) relative to the likelihood that \(Z = z_1, \ldots, W\) have the definite values \(z_1, \ldots, w\).