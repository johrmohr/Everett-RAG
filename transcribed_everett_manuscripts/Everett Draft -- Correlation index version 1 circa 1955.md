# Everett Draft -- Correlation index version 1 circa 1955.pdf

Correlation index 

Given joint distribution \(F_{ij} = P(X_i = x_i, X_j = x_j, \dots, X_n = x_n)\). 

We wish a measure of the correlation of \(X_i\) with \(X_j\) and \(X_k\) a subset of the remaining variables. 

We shall obtain this measure by integrating
that the random process selects a set of the
random variables \(X_i, X_j, \dots, X_n\) according to the
probability distribution \(P_{ij}\). 

and that we are then
set only the values \(X_i, X_j, \dots, X_n\).
This knowledge
will then generate change our information about
the probability of \(X_i\) achieving a given information
being the greatest. The more strongly are \(X_i\) and \(X_j\) achieving a given information
being the greatest.

---

Corrected: ① However, this information changes
will usually depend upon Earth which transfers 

\(X_j^1, \ldots, X_e\) turn up, so that what we are really
interested in is the expected information change
about it, given that we are to be told
the value \(X_j^1, \ldots, X_e\). We shall denote this
quantity called the correlation index of \(X_i\) with 

\[
\begin{align*}
X_j^1, X_e & \text{ by } C(X_j^1, X_e) \\
X_j^1, X_e & \text{ by } C(X_j^1, \ldots, X_e).
\end{align*}
\]

---

We shall use the definition of Information of a probability distribution \(P\) as 

\[I = \sum_i f_i \ln P_i \quad \text{(as usual in Information theory)}\]

Now since we are only interested in the
Variable \(X^1, X^2, X^3, X^4\) and not in the variables
\(X^5, X^6, X^7, X^8\) 

we define \(D_{F_{ijk...l}} = \sum_{m_1, n_1} P_{ijk...l, m_1, n_1}\) 

so that \(F_{ijk...l}\) is the joint (unconditional) 

Probability distribution on \(X^1, X^2, X^3\) alone (unconditional) 

We further define: 

1. \(N_i = \sum_{j \neq i} F_{ijk...l} = \text{a-priori (uncond) distribution on } X^i\) 

2. \(S_{i...l} = \sum_{j \neq i} F_{ijk...l} = \text{uncond distribution on } X^0, X^1, \ldots, X^l\) 

And finally, the conditional distribution on \(X^2\) given the value of \(X^0, X^1, X^2\) will be identical with \(F_{ijk...l}\) 

\[q_{ijk...l} = \frac{F_{ijk...l}}{\sum_i F_{ijk...l}} = \frac{F_{ijk...l}}{F_{ijk...l}}\]

---

Now, the Apriori information on \(X^i, I^0(X^i)\) is 

\[
\mathfrak{I}(X^i) = \sum_i \mu_{jk..l} \ln \mu_{jk..l}
\]

while the Information on \(X^i\), given the Value of \(X^i \times X^j \times X^p\) (conditional) \(I_{(jk..l)}(X^i)\) is given by 

\[
I_{jk..l}(X^i) = \sum_i \mu_{jk..l} \ln(\mu_{jk..l})
\]

So that the change in information given TOT that the
Value of \(X^i \times X^j \times X^p\) are \(y_{jk..l}\), \(z_{jk..l}\), \((\Delta I)_{jk..l}\) is 

\[
\begin{align*}
(\Delta I)_{jk..l} &= I_{jk..l}(X^i) - I^0(X^i) \\
&= \sum_i \mu_{jk..l} \ln(\mu_{jk..l}) - \sum_i \mu_{jk..l} \ln \mu_{jk..l}
\end{align*}
\]

and now since the values \(y_{jk..l}\) are will in fact
turn up with probabilities \(p_{jk..l}\), we have
the the Expected change, (the correlation value) is: 

\[
\begin{align*}
c(X^i; X^j; X^k; X^l) &= \text{Exp}\{(\Delta I)_{jk..l}\} = \sum_{jk..l} \sum_{jk..l} (\Delta I)_{jk..l} \\
&= \sum_{jk..l} \left[ \sum_{jk..l} \left( \sum_i \mu_{jk..l} \ln(\mu_{jk..l}) \right) - \sum_i \mu_{jk..l} \ln \mu_{jk..l} \right]
\end{align*}
\]

---

\[C(x_i^j x_{jk}^k, x_i^l) = C(x_i^j x_{jk}^k) + C(x_i^j x_{jk}^k) - C(x_j^l x_{jk}^k)\]

now, since by (4) \(w_{ijk, l}^e = \frac{g_{ijk, l}^e}{g_{jk, l}^e}\)

\[\Rightarrow \textcircled{1} C(x_i^j x_{jk}^k, x_i^l) = \sum_{jkl} \left[ \sum_{jkl} \left( \sum_{jkl} \frac{g_{ijk, l}^e}{g_{jk, l}^e} \ln \left( \frac{g_{ijk, l}^e}{g_{jk, l}^e} \right) - \sum_{i} M_i \ln M_i \right) \right]\] \[= \sum_{jkl} g_{ijk, l}^e \ln \frac{g_{ijk, l}^e}{g_{jk, l}^e} - \sum_{jkl} M_i g_{jk, l}^e \ln M_i\] 

but since \(\sum_{jkl} g_{ijk, l}^e = 1 \Rightarrow \text{uncountable given 1}\) 

\[\Rightarrow C(x_i^j x_{jk}^k, x_i^l) = \sum_{\text{ijk}} g_{ijk, l}^e \ln \left( \frac{g_{ijk, l}^e}{g_{jk, k}^e} \right) - \sum_{\text{ijk}} M_i \ln M_i\]

---

But \(N_i = \sum_{j \in \mathcal{K}} B_{jik} e\) 

\[
\begin{align*}
\Rightarrow \sum_i N_i \ln N_i &= \sum_i \sum_{j \in \mathcal{K}} B_{jik} e \ln N_i \\
&= \sum_{j \in \mathcal{K}} B_{jik} e \ln N_j
\end{align*}
\]

\[
\Rightarrow C = \sum_{j \in \mathcal{K}} B_{jik} e \left( \ln \left( \frac{B_{jik} e}{B_{ik}} \right) - \ln N_i \right)
\]

\[
\Rightarrow (1) \quad C(x_j; x_{jk}, x_e) = \sum_{j \in \mathcal{K}} B_{jik} e \ln \left( \frac{F_{jik} \cdot l}{F_{jk} \cdot N_i} \right)
\]

---

\[
\begin{align*}
\text{conjecture} & \quad C(X_1^*, X_2^*, \ldots, X_n^*) \\
& \quad + C(X_1^*, X_2^*, \ldots, X_n^*) - C(X_1^*, X_n^*) \\
& \quad = \text{Expected gain on } X_1^* \text{ add } m
\end{align*}
\]

Must really generate a little more to get it

\[
C(X_1^*, X_2^*, \ldots, X_n^*, X_1^*, X_2^*, \ldots, X_n^*) \quad (\text{cumulative gain distribution})
\]

should get formula:

\[
C(X_1^*, X_2^*, \ldots, \hat{X}_n^*, X_1^*, X_2^*, \ldots, X_n^*) = \sum_{\text{all } S \text{ in } S_0} \log \left( \frac{\text{Expected gain on } X_1^* \text{ add } m}{\text{Expected gain on } X_1^* \text{ add } m} \right)
\]

then works out Algebra or C's

---

\[C(x_1, x_2, x_3, \dots, x_d) = \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} \ln \left( \frac{\sum_{k=0}^{\infty} \delta_{i,j} \delta_{k,j}}{\sum_{l=0}^{\infty} \delta_{i,l} \delta_{k,l}} \right)\]

Allometric form 

\[= \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} \frac{\ln g_{i,j} g_{j,i}}{g_{i,j}} - \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} \sum_{k=0}^{\infty} \frac{\ln \xi_{i,j} \ln \eta_{j,k}}{g_{i,j}} - \sum_{i=0}^{\infty} \sum_{k=0}^{\infty} \frac{\ln \eta_{i,k}}{g_{i,j}}\]

\[C = \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} g_{i,j} \ln g_{i,j} - \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} g_i \ln g_i - \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} n_i \ln n_i \\
= \text{Information in Joint distribution} - \text{Information uncorrelated} \times \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} \delta_{i,j} \ln \xi_{i,j} - \text{Information in Joint distribution} - (\text{dim of information in uncorrelated})\]

---

\[
\begin{align*}
\text{Notation: } I(x;x^1, x^2) &= I_{\alpha, \beta, \dots, \gamma} \\
&= \text{unconditional uniform distribution}
\end{align*}
\]

if Total Joint Distribut 

\[
P_{\alpha, \beta, \dots, \omega} = \sum_{g, \dots, \omega} P_{\alpha, \beta, \dots, \omega}
\]

then Unconditional Joint Distribut on \(\alpha, \beta, \dots, \omega\) only 

\[
F_{\alpha, \beta, \dots, \gamma} = \sum_{g, \dots, \omega} P_{\alpha, \beta \dots, \omega}
\]

\[
\begin{align*}
I_{\alpha, \beta, \dots, \gamma} &= \sum_{g, \dots, \omega} f_{g, \dots, \omega} \ln f_{g, \dots, \omega} \\
&= \sum_{g, \dots, \omega} \left( \sum_{g, \dots, \omega} P_{\alpha, \beta, \omega} \right) \ln \left( \sum_{g, \dots, \omega} P_{\alpha, \gamma, \omega} \right) \\
&= \sum_{g, \dots, \omega} \beta_{\alpha, \beta, \omega} \ln \left( \sum_{g, \dots, \omega} P_{\alpha \beta, \omega} \right)
\end{align*}
\]

\[
\begin{align*}
& \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \sum_{\alpha \beta \gamma \delta \omega} \ln \left( \sum_{\alpha \beta \gamma \delta \omega} P_{\alpha \beta \gamma \delta \omega} \right) \\
& = \sum_{\alpha \beta \gamma \delta \omega} P_{\alpha \beta \delta \omega} \ln \left( \sum_{\alpha \beta \gamma \gamma \delta \omega} P_{\alpha \beta \gamma \delta \omega} P_{\alpha \beta \gamma \gamma \delta \omega} \right) \\
& = I_{\alpha \beta \gamma \delta \omega} - \sum_{\alpha \beta \gamma \delta \omega} \ln \left( \frac{P_{\alpha \beta \gamma \delta \omega}}{\sum_{\alpha \beta \gamma \delta \omega} P_{\alpha \beta \gamma} \delta \omega} \right)
\end{align*}
\]

---

\[ \frac{P_{\alpha \beta \gamma \delta \omega}}{\sum_{\delta \omega} P_{\alpha \beta \gamma \delta \omega}} = \text{cond: } P_{\delta \omega \alpha \beta \gamma} \]

\[ I_{\alpha \beta \gamma} = I_{\alpha \beta \gamma \delta \omega} - \sum_{\delta \omega} P_{\alpha \beta \gamma \delta \omega} \ln P_{\delta \omega \alpha \beta \gamma} \]

\[ = \frac{\sum_{\delta \omega} \left( \sum_{\delta \omega} P_{\alpha \beta \gamma \delta \omega} / \ln P_{\delta \omega \alpha \beta \gamma} \right)}{\sum_{\delta \omega} P_{\alpha \beta \gamma \delta \omega} / P_{\delta \omega \alpha \beta \gamma}} \]

\[ \text{new: } \sum_{\alpha \beta \gamma \delta \omega} P_{\alpha \beta \gamma \delta \omega} \ln P_{ \delta \omega \alpha \beta \gamma} \]

General Formula \(C(\alpha \beta; \delta \omega) = I_{\alpha \beta \gamma \delta \omega} - I_{\alpha \gamma \delta} - I_{\delta \omega}\) 

\[ \Rightarrow C(\alpha \beta; \delta \omega) = I_{\alpha \beta \gamma \gamma \delta} - I_{\alpha} - I_{\beta \gamma \delta} \]

\[ \Rightarrow \mathcal{H} I_{\alpha \beta \gamma \delta} = I_{\alpha \beta \gamma \delta} - I_{\alpha} - C(\alpha \beta; \delta \omega) \]

---

\[C(\alpha, \beta) = I_{\alpha \beta} - I_{\alpha} - I_{\beta}\]

\[C(\beta, \gamma) = I_{\beta \gamma} - I_{\beta} - I_{\gamma}\]

\[C(\alpha, \beta) = I_{\alpha \gamma} - I_{\alpha} - I_{\gamma}\]

Conditional uniform \(I_{\alpha \beta \gamma \ldots \delta}\) 

\[\text{lett } I_{\alpha \beta \ldots \delta}^{\gamma \ldots \delta} = \sum_{\alpha \beta} P_{\alpha \beta \ldots \delta} \ln P_{\alpha \beta \ldots \delta}\]

\(\sigma\) let \(P_{\alpha \beta \ldots \delta}^{\gamma \ldots \delta}\) be conditional probability on \(\alpha, \beta\)
given \(\gamma, \ldots, \delta\) 

\[\Rightarrow \text{orig distr. } P_{\alpha \beta \ldots \delta} u \ldots \gamma\]

\[\Rightarrow P_{\alpha \beta \ldots \delta} = \sum_{u \ldots \gamma} P_{\alpha \beta \ldots \delta} u \ldots \gamma\]