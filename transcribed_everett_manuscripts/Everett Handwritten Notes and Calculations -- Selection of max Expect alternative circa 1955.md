# Everett Handwritten Notes and Calculations -- Selection of max Expect alternative circa 1955.pdf

Selection of Max. Expect, alternative.
cost 1
Payoff \(\frac{1}{Q}\) on Q distributed
independently

\[
\exp_i \left( \frac{p_i Q}{Q} \right)
\]

Given that chooses at best on

\[
= \frac{p_i}{Q} - 1 \quad \text{(Simpler, omit the payment of $1$)}
\]

\[
\text{thus} = \frac{p_i}{Q_i} \quad Q_i \text{ is indep. and uniformly distributed on } [E, 1]
\]

Assume choose always max \(p_i / Q_i\) on course

\[
\text{So Payoff of } \left\{ p_i \right\} \left\{ Q_i \right\} = \max_i \frac{p_i}{Q_i}
\]

Now wish to
compute \(E \exp \left( H \left( \frac{p_i}{Q_i} \right) \right)\) under assumption that \(Q_i\) chosen on \([E, 1]\)

---

S. Considér
\[
\text{Prof } \left\{ \frac{P_i}{Q_i} \in \text{s.t.} \text{ and } \frac{P_i}{Q_j} \notin \text{s.t.} \text{ all } y \neq x \right\}
\]

\[
\text{Prof } \frac{P_i}{Q_i} \in \{\text{s.t.} \text{ and } \frac{P_i}{Q_i} \in \text{s.t.} \text{ all } y \neq x \}
\]

\[
\Rightarrow Q_i \in \left[ \frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{s.t.}}}}}, \frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_{i}}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}}}}}}}}}} \right] \quad \text{and} \quad \frac{d\left(\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_{1}}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_1}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_2}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_{2}}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_{\frac{1}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{1}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{s.t.\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i} \frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_3}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_{\infty}}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_\infty}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_\frac{1}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i} \frac{1}{\frac{P_i}{\frac{P_i}{\frac{P_i}{\frac{P_i}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\right)
\]

\[
\text{but } \text{Prof } \left( \frac{dQ}{d\xi} \right) \text{ is } Q \text{ from } \text{ all } \xi \in \text{s.t.} \text{ and } \frac{dQ}{d\xi} \in \text{s.t.} \text{ all } y \neq x
\]

\[
\text{but } \text{Prof } \left( \frac{P_i}{\xi} \right) = \frac{P_i}{\xi^2 (1-\xi)} d\xi
\]

\[
\text{not} \forall \xi \text{ from } \xi \in \text{s.t.}
\]

\[
\Rightarrow \text{Prof } \frac{P_i}{Q_i} \text{ from } \frac{P_i}{\xi} \text{ to } P_i \quad (\xi \in \text{ from } P_i \text{ to } P_i)
\]

---

as check is \(\int_{P_i} P_i(\xi) d\xi = 1\) 

\[
\begin{align*}
L &= \int_{P_i} P_i \xi \frac{P_i}{\xi (1-\epsilon)} d\xi = \frac{P_i}{1-\epsilon} \left( -\frac{1}{\xi} \int_{P_i} P_i \xi \right) \\
&= \frac{P_i}{1-\epsilon} \left( -\frac{\epsilon}{P_i} + \frac{1}{P_i} \right) \\
&= \left( \frac{P_i}{1-\epsilon} \right) \left( \frac{1-\epsilon}{P_i} \right) = 1 < 0
\end{align*}
\]

and establish that \(P_i(\xi) d\xi = \frac{P_i}{\xi^2 (1-\epsilon)} d\xi = \int_{P_i} P_i \xi \in [\xi, \xi + \epsilon]\)

with \(P_i \leq \xi \leq \frac{P_i}{\epsilon}\)

define \(R_j(n) = \text{Prob} \frac{P_i}{Q_j} \leq n\) (i.e cumulative function)

---

\[ \begin{align*} \text{Then } R_j(n) &= \int_{\xi_3}^{n} \int_{\xi_3}^{n} p_j(\xi_1) d\xi_1 d\xi_2 \\ &= 0 \end{align*} \qquad \begin{align*} \text{and } n \le \frac{\xi_2}{\xi_1} \\ \text{and } n \le \frac{\xi_2}{\xi_1} \end{align*} \]

\[ \begin{align*} \int_{\xi_3}^{n} p_j(\xi_1) d\xi_2 &= \int_{\xi_3}^{n} \frac{p_j}{\xi_1^2(1-\xi)} d\xi_1 \\ &= \frac{p_j}{(1-\xi)} \left[ -\frac{1}{\xi} \right]_{\xi_3}^{n} = \frac{p_j}{(1-\xi)} \left[ -\frac{1}{n} + \frac{1}{p_j} \right] \\ &= \frac{p_j}{(1-\xi)} \left[ \frac{n-p_j}{n p_j} \right] \\ &= \frac{n-p_j}{n(1-\xi)} \end{align*} \]

---

So we have that 

\[R_j(n) = \begin{cases} \frac{1}{N - P_j} & \text{for } n \geq \frac{P_j}{\varepsilon} \\ \frac{N - P_j}{N(1 - \varepsilon)} & \text{for } P_j \leq n \leq \frac{P_j}{\varepsilon} \\ 0 & \text{for } n \leq P_j \end{cases}\]

which is the probability that \(\frac{P_j}{Q_j}\) shall be \(\leq N\) (note \(P_j\) feed \(Q_j\) uniform over \([E]\))

and Finally define \(S_k(u) = P_{\text{rob}} \left\{ \frac{P_k}{Q_k} \in [u, u+du] \right\}\) and \(\frac{P_j}{Q_j} \leq u\) all \(j\)

so that \(S_k(u) = P_k(u) du \times \prod_{j \neq k} R_j(u)\)

---

\[ \begin{aligned} \text{Then define } E_k &= \int_{\mathcal{C}_k(u)} u \, du \\ &= \text{Expectation from the } \epsilon \text{th alternative} \end{aligned} \]

\[ \text{is the total expectation for the process} \]

\[ \text{and hope it looks like } \sum P_k u_k P_k \]

\[ \begin{aligned} \text{so: } E_k P &= \sum_k \int_0^\infty u P_k(u) \prod_{j \neq k} R_j(u) \, du \\ &= \sum_k \left( \int_0^\infty u \left[ \frac{P_k}{u^2(1-\epsilon)} \right]_{P_k \leq u \leq \frac{P_k}{\epsilon}} \right) \left[ \prod_{j \neq k} \frac{1}{u - \frac{P_j}{u(1-\epsilon)}} \right]_{P_j \leq u \leq \frac{P_j}{\epsilon}} \times du \end{aligned} \]

---

\[
\sum_{K} \left( \int_{0}^{\infty} \left( \frac{P_{K}}{u(1-\epsilon)} \right) \frac{P_{K} \leq u \leq \frac{P_{K}}{\epsilon}}{0} \right) \prod_{j \neq K} \left[ \frac{1}{1-\epsilon} - \frac{P_{j}}{u(1-\epsilon)} \right] \frac{P_{j} \leq u \leq \frac{P_{j}}{\epsilon}}{0} \frac{P_{j} \leq u \leq \frac{P_{j}}{\epsilon}}{u \leq P_{j}} \right) d\epsilon
\]

\[
\text{Whittaker } \frac{P_K}{u} \prod_{j \neq K} \left(1 - \frac{P_j}{u}\right)
\]

\[
\begin{align*}
\text{ie } \frac{P_K}{u(1-\epsilon)} \prod_{j \neq K} \left( \frac{u-P_j}{u(1-\epsilon)} \right) \\
&= \frac{1}{u(1-\epsilon)}^N \prod_{j \neq K} (u-P_j) \\
&= \frac{1}{u(1-\epsilon)}^N \frac{P_K}{u-P_K} \prod_{\text{all } j} (u-P_j) \\
\text{now } \sum_K \frac{1}{u(1-\epsilon)}^N \frac{P_K}{u(1-\epsilon)} \prod_{j \neq K} (u-P_j) \\
&= \frac{1}{\prod_{j \neq K} (u-P_j)} \sum_K \frac{P_K}{u-P_K}
\end{align*}
\]

---

\[ \text{now} \sum_k \frac{p_k}{u - p_k} = \frac{\sum_k p_k \prod_{j \neq k} (u - p_j)}{\prod_k (u - p_k)} \]

each is
where before 

\[ \text{which is} \int \frac{\prod_j (u - p_j)}{[u(1 - \epsilon)]^n} \sum_k \frac{p_k}{u - p_k} \quad du? \]

\[ \begin{aligned} \text{except for} & \quad \sum_k \ln (u - p_k) \bigg|_p^{p_k \in} = \ln \left( \frac{p_k}{\epsilon} - p_k \right) \\ & \quad \sum_k p_k \ln \left( \frac{1}{\epsilon} - 1 \right) \\ & \quad \text{would appear to give logarithm} \\ & \quad \text{ie} \quad \sum_k \int \frac{p_k}{u - p_k} \quad \text{and} \quad \text{and} \quad \text{and} \quad \text{wrong} \end{aligned} \]

---

try again, method: 

Actual Exp on t'hat guess chosen is 

\[
= \int_{\Sigma} \frac{p_i}{Q_i} dQ = p_i \ln\left(\frac{1}{\epsilon}\right)
\]

Absolute 

Proof that i'th act will be chosen 

\[
= \int_{0}^{\infty} p_i(\xi) R_i(\xi) d\xi
\]

(is this a log P_i?)
(mystery) 

\[
\log \frac{p_i}{Q_i} = \log p_i - \log Q_i.
\]

if distinct on Q is uniform, 

\[
d \ln Q = \frac{1}{Q} dQ \quad \Rightarrow \quad dQ = Q d\ln Q
\]

---

What is Prob
\[
[ \log P_i - \log Q_i ] \leq \xi \quad \text{?}
\]
u 

\[
\text{let } u_i = \log Q_i
\]

\[
\Rightarrow P(u) du = \frac{e^u}{1-\epsilon} du \quad \text{and} \quad \epsilon dQ = e^u du
\]

\[
u \text{ from } 0 \text{ to } \ln \epsilon
\]

\[
\text{which } \frac{1}{\epsilon} \int_0^\epsilon e^u du
\]

\[
\begin{align*}
u &= \ln Q \\
du &= \frac{dQ}{Q} \\
\Rightarrow dQ &= e^u du
\end{align*}
\]

\[
\text{Proof: } dQ = dQ = e^u du
\]

\[
\text{Proof: } du = \text{Proof} \left[ \frac{dQ}{e^u} \right]
\]

\[
\begin{align*}
&= \frac{1}{e^u} dQ \\
&= e^{-u}
\end{align*}
\]

---

is Q uniform [E, I] subset bQ ? 

\[ \frac{u}{u} \quad Q = e^u \]

\[ \text{Proof} \left\{ \frac{dQ}{Q} \right\} = \frac{dQ}{1 - E} \quad du = \frac{1}{Q} dQ = e^{-u} dQ \]

\[ \text{so that} \quad P(u) du = \frac{1}{1 - E} e^u du \quad \text{Q} \{E, I\} \quad \text{so} \quad u \left[ \ln E, 0 \right] \]

\[ \text{Correct} \quad P(u) du = \frac{1}{1 - E} e^udu \quad \text{check} \int_{\ln E}^0 \frac{1}{1 - E} e^u du = \frac{1}{1 - E} e^{u \left[ \ln E, 0 \right]} \quad \text{so} \quad P(u_i) = \frac{1}{1 - E} e^u du \quad \text{from} \left[ \ln E, 0 \right] \]

---

Direction, Given N random variables \(X_i\) uniformly over individual (joint) distribution of \(X_i\)?

do \(\text{Prob} \{ \ln P_i - \ln Q_i \leq n \} \)

\[= \text{Prob} \{ \ln Q_i \geq \ln P_i - n \} \]

\[= \text{Prob} \{ u_i \geq \ln P_i - n \} \]

\[= \int_{\ln P_i - n}^{0} \frac{1}{1 - \epsilon} e^{u_i} du \quad \text{is } \ln P_i - n \leq 0\]

\[= \frac{1}{(1 - \epsilon)} \left[ 1 - P_i e^{-n} \right]\]