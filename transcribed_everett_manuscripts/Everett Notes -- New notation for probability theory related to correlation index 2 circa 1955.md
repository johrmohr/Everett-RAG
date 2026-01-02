# Everett Notes -- New notation for probability theory related to correlation index 2 circa 1955.pdf

New Notation : 

Original total profit: \(P_{\alpha, \beta, \ldots, \delta, \ldots, \gamma}\) 

Unconditional profit over any Subset: 

\[
\begin{align*}
\text{Total conditional profit} \\
\text{Total profit} \quad P_{\alpha, \beta, \ldots, \delta, \ldots, \gamma} &= \text{Total profit of } \alpha, \beta, \ldots, \delta, \ldots, \gamma \text{ given } \gamma, \ldots, \delta \\
\text{Total conditional profit} \quad P_{\alpha, \beta, \ldots, \delta, \ldots,\gamma} &= \frac{P_{\alpha, \beta, \ldots, \delta, \ldots, \gamma}}{P_{\alpha, \ldots, \delta, \ldots, \gamma}} \\
\text{Total conditional profit} \quad P_{\alpha, \beta, \ldots, 1, \ldots, \gamma} &= \frac{P_{\alpha, \beta, \ldots, 1, \ldots, \gamma}}{P_{\alpha, \ldots, \delta, \ldots,\gamma}} \\
\text{Total conditional profit} \quad P_{\alpha, \beta, \beta, \ldots, \gamma} &= \frac{P_{\alpha, \beta, \ldots,\gamma}}{P_{\alpha, \ldots, \delta, \ldots,\gamma}} \\
\text{(Total conditional profit)} \quad P_{\alpha, \beta, \ldots, \gamma} &= \frac{P_{\alpha, \beta,\ldots,\gamma}}{P_{\alpha, \ldots, \delta, \ldots,\gamma}} \quad \text{(Total conditional profit)} \\
\text{(Total conditional profit)} \quad P_{\alpha, \beta, \ldots, 1, \ldots, \delta} &= \frac{P_{\alpha, \beta, \ldots, 1, \ldots,\delta}}{P_{\alpha, \ldots, \delta, \ldots,\gamma}} \\
\text{(Partial conditional profit)} \quad P_{\alpha, \beta, \ldots, \delta, \ldots, \delta} &= \frac{P_{\alpha, \beta, \ldots,\delta}}{P_{\alpha, \ldots, \delta, \ldots,\delta}} \\
\text{(Partial conditional profit)} \quad P_{\alpha, \beta, \ldots,\delta, \ldots,\delta} &= \frac{P_{\alpha, \beta, \ldots,\delta}}{P_{\beta, \ldots, \delta}} \\
\text{(Partial conditional profit)} \quad P_{\alpha, \beta, \beta, \ldots, \delta} &= \frac{P_{\alpha, \beta, \ldots \delta}}{P_{\alpha, \ldots, \delta}} \\
\text{(Partial conditional profit)} \quad P_{\alpha,\beta,\ldots,\delta} &= \frac{P_{\alpha,\beta,\ldots,\delta}}{P_{\alpha,\ldots,\delta}} \\
\text{(Partial conditional profit)} \quad P_{\alpha,\beta,\ldots,\gamma} &= \frac{P_{\alpha,\beta,\ldots,\gamma}}{P_{\alpha,\ldots,\delta}} \\
\text{(Partial conditional profit)} \quad P_{1,\ldots,\delta} &= \frac{P_{\alpha,\beta,\ldots,\delta}}{P_{1,\ldots,\delta}} \\
\text{(Partial conditional profit)} \quad P_{1,\ldots,1} &= \frac{P_{\alpha,\beta,\ldots,\delta}}{P_{1,\ldots,1}} \\
\text{(Partial conditional profit)} \quad P_{1,\ldots,1} &= P_{\alpha,\ldots,\delta} \\
\text{(Partial conditional profit)} \quad P_{1,\ldots,1} &= P_{1,\ldots,\delta} \\
\text{(Partial conditional profit)} \quad P_{1,\ldots,\delta} &= P_{1,\ldots,\delta} \\
\text{(Partial conditional profit)} \quad \text{Total conditional profit} \quad P_{1,\ldots,\delta} &= P_{1,\ldots,\delta} \quad \text{(Total conditional profit)} \\
\text{(Partial conditional profit)} \quad P_{1,\ldots,\delta} &= P_{\alpha,\ldots,\delta} \\
\text{(Partial conditional profit)} \quad \text{Total conditional} \quad P_{1,\ldots,\delta} &= P_{\alpha,\ldots,\delta} \quad \text{(Total conditional profit)} \\
\text{(Partial conditional} \quad P_{1,\ldots,\delta} &= P_{\alpha,\ldots,\gamma} \\
\text{(Partial conditional} \quad P_{1,\ldots,\delta} &= P_{\gamma,\ldots,\delta} \\
\text{(Partial conditional} \quad P_{1,\ldots,\delta} &= P_{1,\ldots,\delta}
\]

---

By using Theorem 2 

\[
\sum_{\beta \in \mathcal{B}} P_{\beta, \alpha, \beta} P_{\alpha, \beta, \beta} = P_{\alpha, \beta}
\]

by more generally 

\[
\sum_{\beta \in \mathcal{B}} P_{\beta, \beta} P_{\alpha, \beta} P_{\alpha, \beta} = \sum_{\beta \in \mathcal{B}} P_{\beta, \beta} P_{\alpha, 1} P_{\alpha, \beta} = \sum_{\beta \in \mathcal{B}} \frac{P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, \beta}}{P_{\alpha, \beta} P_{\alpha, \beta}} = \sum_{\beta \in \mathcal{B}} \frac{P_{\alpha, \beta}}{P_{\alpha, \beta}} P_{\alpha, \beta} P_{\alpha, \beta} = \sum_{\beta} P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, \beta} = P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, \alpha} P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, 1} P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, \gamma} P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha,} P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, } P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, \delta} P_{\alpha, \beta} P_{\alpha, \beta} P_{\alpha, }
\]

\[

---

\[ \text{conditio} \quad P_{\text{su}, \beta} P_{\text{su}, \gamma} P_{\text{su}, \gamma} \cdots P_{\text{su}, \gamma} \]

\[ = P_{\text{su}, \beta} \frac{P_{\text{su}, \beta, \gamma, \delta, \cdots, \nu}}{P_{\text{su}, \gamma, \cdots, \nu}} \]

\[ \text{but by} \quad \text{⑤} \quad P_{\text{su}, \beta, \gamma, \delta, \cdots, \nu} = P_{\text{su}, \gamma, \delta, \cdots, \nu} P_{\text{su}, \gamma, \cdots, \nu} \]

\[ \alpha = \frac{P_{\text{su}, \beta, \gamma, \delta, \cdots,\nu}}{P_{\text{su}, \gamma, \delta, \cdots, \nu}} \frac{P_{\text{su}, \beta, \gamma, \delta, \cdots , \nu}}{P_{\text{su}, \gamma, \delta, \cdots, \nu} P_{\nu, \gamma, \delta, \cdots, \nu}} \]

\[ = \frac{P_{\text{su}, \beta, \gamma, \delta, \nu}}{P_{\text{su}, \gamma, \delta, \nu}} \]

\[ \sum_{\delta} P_{\delta} P_{\delta} = \frac{\sum_{\delta} P_{\delta} P_{\delta}}{\sum_{\delta} P_{\delta}} = \frac{1}{\sum_{\delta}} \sum_{\delta} P_{\delta} P_{\delta} \]

\[ \text{in} \quad P_{\text{su}, \delta} = \sum_{\gamma} \frac{P_{\text{su}, \gamma} P_{\delta}}{\sum_{\gamma} P_{\delta}} \quad \text{?} \]

\[ P_{\text{su}, \gamma} P_{\delta} = \frac{P_{\text{su}, \gamma} P_{\delta}}{\sum_{\delta} P_{\delta}} \]

---

\[ \frac{P_{ur}P_{\delta}^r}{P_r} = \frac{P_{ur}P_{\delta}}{\bar{P}_r} = P_{ur}^r P_{\delta} \]

S. Conna: 

\[ \frac{P_{ur}P_{\delta}^r}{P_r} = P_{ur}^r P_{\delta} \quad \text{(on supplée, l'ouverture peut être interchangée)} \]

Now 

\[ \frac{P_{\delta}^r P_{\delta}^r}{P_{\delta}} = P_{\delta} \quad \text{avec } P_{\delta}^r = \frac{P_{\delta}}{P_{\delta}} \]

\[ \Rightarrow \sum_{\delta} P_{\delta}^r P_{\delta} = \sum_{\delta} P_{\delta} = P_{\delta} \]

\[ \begin{aligned} \text{algo} \quad & P_{\delta}^r P_{\delta}^{\infty} = P_{\delta}^r \frac{P_{\delta}^{\infty}}{P_{\delta}} \\ &= \frac{P_{\delta}}{P_{\delta}} \frac{P_{\delta}^{\infty}}{P_{\delta}} = \frac{P_{\delta}}{P_{\delta}} \frac{P_{\delta}^{\infty}}{P_r P_{\delta}} = \frac{P_{\delta}^{\infty}}{P_{\delta}} \end{aligned} \]

\[ \text{aut } \frac{P_{\delta}}{P_{\delta}} = P_{\delta}^r \]

---

Define Partial Correlation Coefficient: 

\[I_{(\alpha, \beta)}^{r, s} = \sum_{\alpha, \beta} p_{\alpha, \beta}^{r, s} \ln p_{\alpha, \beta}^{r, s}\]

Define 

Partial 

Correlation indices 

Correlation index \(C_{(\alpha, \beta, r, s)}\) = \(I_{(\alpha, \beta, r, s)}\) - \(I_{(\alpha, \beta, r, s)}\) - \(I_{r, s}\) 

Define Conditional
Correlation
\(C_{(\alpha, \beta, r, s)}^{u, v}\) = \(I_{(\alpha, \beta, r, s)}^{u, v}\) - \(I_{(\alpha, \beta, r, s)}^{u, v}\) - 
\(I_{(\alpha, \beta, r, s)}^{u, v}\) 

Try to show \(\sum_{\alpha, \beta} C_{(\alpha, \beta, r, s)}^{u, v} = C_{(\alpha, \beta, r, s)}^{u, v}\)

---

\[ \sum_{r, \dots, s} p_{r, \dots, s} I_{(\alpha, \dots, \beta)}^{r, \dots, s} = \sum_{r, \dots, s} p_{r, \dots, s} \sum_{\alpha, \dots, \beta} p_{r, \dots, \beta}^{r, \dots, s} \ln p_{r, \dots, \beta}^{r, \dots, s} \]

\[ \sum_{\alpha, \dots, \beta} I_{(\alpha, \dots, \beta)}^{r, \dots, s}\ln p_{r, \dots, \beta}^{r, \dots, s} \]
\[ = \sum_{\alpha, \dots, \beta} \frac{p_{r, \dots, \beta}^{r, \dots, s}}{p_{r, \dots, \beta}^{r, \dots, s}} \ln \left( \frac{p_{r, \dots, \beta}^{r, \dots, s}}{q_{r, \dots, \beta}^{r, \dots, s}} \right) \]

\[ = \frac{1}{r_{r, \dots, s}} \sum_{\alpha, \dots, \beta} p_{r, \dots, \alpha}^{r, \dots, s} \ln p_{r, \dots, \beta} \]

\[ = \frac{1}{r_{r, \dots, s}} I_{(\alpha, \dots, \beta)}^{r, \dots, s} \ln p_{r, \dots, \beta}^{\alpha} \]

\[ = \frac{1}{r_{r, \dots, s}}I_{(\alpha, \dots, \beta)}^{r, \dots, s} \left( \ln p_{r, \dots, \beta}^{\alpha} \right) - \ln r_{r, \dots, \beta} \]

\[ \Rightarrow p_{r, \dots, s} I_{(\alpha, \dots, \beta)} = \sum_{\alpha, \dots, \beta} p_{r, \dots, \gamma} \ln p_{r, \dots, \beta} - p_{r, \dots, \beta} \ln p_{r, \dots, \gamma} \]

\[ \sum_{r, \dots, s} p_{r, \cdots, s} I_{(\alpha, \cdots, \beta)}^{r, \cdots, s} = \sum_{\alpha, \cdots, \beta} p_{r, \cdots, \gamma} \ln p_{r, \cdots, \beta} - \sum_{r, \cdots, s} p_{r, \cdots, \gamma} \ln p_{r, \cdots,\beta} \]

\[ = I_{(\alpha, \cdots, \beta)} - I_{r, \cdots, \beta} \]

---

As that 

\[
\begin{align*}
\sum_{u \sim v} p_{u \sim v} C_{u \sim v, \dots, \delta}^{u \sim v} &= \sum_{u \sim v} p_{u \sim v} I_{\alpha, \beta, \dots, \delta}^{u \sim v} \\
&\quad - \sum_{u \sim v} p_{u \sim v} I_{\alpha, u, \dots, \delta}^{u \sim v} - \sum_{u \sim v} p_{u \sim v} I_{\gamma, \dots, \delta}^{u \sim v}
\end{align*}
\]

\[
\begin{align*}
&= I_{\alpha, \beta, \gamma, \dots, \delta} - I_{u, \dots, v} \\
&\quad - \left[ I_{\alpha, \beta, u, \dots, v} - I_{u, \dots, v} \right] \\
&\quad - \left[ I_{\gamma, \dots, \delta, u, \dots, v} - I_{u, \dots, v} \middle] \right]
\end{align*}
\]

\[
= I_{\alpha, \beta, \gamma, \dots, \delta} + I_{u, \dots, v} - I_{\alpha, \beta, u, \dots, v} - I_{\gamma, \dots, \delta, u, \dots, v}
\]

\[
\text{but } C_{\alpha, \beta, \gamma, \dots, \delta} = I_{\alpha, \beta, \gamma, \dots, \delta} - I_{\alpha, \beta, u, \dots, v} - I_{\alpha, \beta, \gamma, \dots, \delta}
\]

---

Digestion: 

\[
\text{Expected information change upon knowing } \beta = I_\alpha^\beta - I_\alpha
\]

\[
\begin{align*}
\text{Expected change} &= \sum_{\beta} I_\alpha^\beta - I_\alpha \\
&= I_{\alpha\beta} - I_\beta - I_\alpha \quad \text{or,}
\end{align*}
\]

More generally 

\[
\begin{align*}
\text{uniform change of } \alpha, \beta \text{ knowing } \gamma, \dots \delta \\
&= I_{\alpha, \dots, \beta}^{\gamma, \dots, \delta} - I_{\alpha, \dots, \beta}^{\gamma}
\end{align*}
\]

\[
\begin{align*}
E_{\text{expected}} &= \sum_{\gamma, \dots, \delta} I_{\gamma, \dots, \delta}^{\gamma, \dots, \delta} - I_{\gamma, \dots, \delta} \\
&= I_{\alpha, \dots, \beta} \gamma, \dots, \delta - I_{\gamma, \dots, \delta} - I_{\alpha, \dots, \beta} \quad \text{or} \\
&= I_{\alpha, \dots, \beta} \gamma, \dots, 1 - I_{\gamma, \dots, \delta} - I_{\alpha, \dots, 1} \quad \text{or} \\
&= I_{\alpha, \dots, \beta \gamma, \dots, 1} - I_{\gamma, \dots, \delta} - I_{\alpha, \dots,1} \quad \text{or} \\
&= I_{\alpha, \dots, \gamma, \dots, 1} - I_{\gamma, \dots, \delta}
\end{align*}
\]

(Proof: Bernoulli change) 

\[
\begin{align*}
\text{Wemust have } I_{\alpha, \beta, \gamma, \dots, \delta} - I_{\gamma, \delta} &= I_{\alpha, \dots, \beta} \\
\text{Consequently false!} \\
C_{\alpha \beta, \gamma, \delta} &= I_{\alpha \beta, \delta} - I_{\alpha \beta} - I_{\gamma \delta}
\end{align*}
\]

---

Back to formula 

\[ \sum_{u \sim v} C_{\alpha \beta; \gamma \delta}^{(u, v)} = I_{\alpha \beta; \gamma \delta} + I_{\alpha \gamma} - I_{\beta \gamma} - I_{\beta \delta} \]

\[ \text{not } I_{\alpha \beta; \gamma \delta} - I_{\alpha \gamma} - I_{\beta \delta} = C_{\alpha \beta; \gamma \delta} \]

\[ \text{first } C_{\alpha \beta; \gamma \delta} = I_{\alpha \beta; \gamma \delta} - I_{\alpha \gamma} - \frac{I_{\alpha \gamma}}{I_{\alpha \beta}} - I_{\alpha \gamma} \Rightarrow I_{\alpha \gamma} = I \]

\[ \begin{aligned} & \text{factoring further} \\ &= I_{\alpha \beta; \gamma \delta} - I_{\alpha \gamma} \\ & \qquad - (I_{\alpha \beta; \gamma \delta} - I_{\alpha \gamma}) \qquad (C_{\alpha \beta; \gamma \delta} + I_{\alpha \beta}) \\ & \qquad (I_{\beta \gamma; \alpha \delta} - I_{\alpha \gamma}) \qquad (C_{\beta \gamma; \alpha \delta} + I_{\beta \delta}) \\ &= C_{\alpha \beta; \gamma \delta} + I_{\alpha \gamma} - (C_{\alpha \beta; \gamma \delta} + I_{\alpha \gamma}) - (C_{\beta \gamma; \alpha \delta} - I_{\beta \delta}) \\ &= (C_{\alpha \beta; \gamma \delta} - C_{\alpha \beta; \gamma \delta}) - C_{\beta \gamma; \alpha \delta} + I_{\alpha \gamma} - I_{\alpha \beta} - I_{\beta \delta} \end{aligned} \]

\[ = (C_{\alpha \beta; \gamma \delta} - C_{\alpha \beta; y \delta}) - C_{\beta \gamma; \alpha \delta} + I_{\alpha y} - I_{\alpha \beta} - I_{\beta \delta} \]

---

Ao that 

\[
\sum_{u, y} P_{u, y} \left( \sum_{\alpha, \beta, \gamma, \delta} C_{\alpha \beta \gamma \delta} u^{\alpha} v^{\beta} s \right) = C_{\alpha \beta \gamma \delta} u^{\alpha} v^{\beta} - C_{\alpha \beta \gamma \delta} u^{\alpha} v^{\beta} + C_{\alpha \beta \gamma \delta} s
\]

Nourned to share that 

\[
C_{\alpha \beta \gamma \delta} u^{\alpha} v^{\beta} = C_{\alpha \beta \gamma} u^{\alpha} v^{\beta} + C_{\gamma \delta} u^{\alpha} v^{\beta}
\]

\[
\Rightarrow I_{\alpha \beta \gamma \delta} u^{\alpha} v^{\beta} - I_{\alpha \beta \gamma} s - I_{\alpha \gamma} u^{\alpha} v^{\beta} = I_{\alpha \beta \gamma} u^{\alpha} v^{\beta} - I_{\alpha \beta} s - I_{\alpha \gamma} u^{\alpha} v^{\beta} + I_{\gamma \delta} u^{\alpha} v^{\beta} - I_{\gamma \beta} s - I_{\alpha \gamma} u^{\alpha} v^{\beta}
\]

→
\[
C_{\alpha \beta \gamma \delta} = I_{\alpha \beta \gamma} - I_{\alpha} - I_{\beta \gamma}
\] 

\[
C_{\alpha \beta \gamma \delta} = I_{\alpha \beta} - I_{\alpha} - I_{\beta \gamma}
\]

\[
C = I_{\alpha} + I_{\beta} = I_{\alpha \beta} + I_{\gamma}
\]

\[
\begin{align*}
I_{\alpha} + I_{\beta} &= \sum_{\alpha} P_{\alpha} \ln P_{\alpha} + \sum_{\beta} P_{\beta} \ln P_{\beta} \\
&= \sum_{\alpha \beta} P_{\alpha \beta} \ln P_{\alpha \beta} + \sum_{\alpha \beta} P_{\alpha \beta} \ln P_{\alpha \gamma} \\
&= \sum_{\alpha \beta \gamma} P_{\alpha \beta \gamma} \ln (P_{\alpha \beta \gamma}) \tag{20, without}
\end{align*}
\]