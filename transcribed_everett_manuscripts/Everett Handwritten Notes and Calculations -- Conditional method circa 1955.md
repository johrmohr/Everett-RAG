# Everett Handwritten Notes and Calculations -- Conditional method circa 1955.pdf

(containingNeumann type Neumann) 

Convolution Method 

System card distributed \(a_r a_r^* = r\) 

\(A_r = d\) 

\[Total \ n_f = \sum_r a_r f_r (y, x)\]

\[\Rightarrow \text{condprog} \quad P_y^{r \oplus} = f_r (y, t) f_r^*\]

\[\Rightarrow \quad I_y^r = \iint y \ln y^r dy\] \[= \int f_r f_r^* \ln f_r f_r^* dy\]

---

\[C_{r,y} = \sum_r r T_y^r - I_y\]

\[Now \text{ is in } \frac{\partial F_r(y,t)}{\partial t} = H_r(y) F_r(y,t) \text{ writing as } H_r(y)\]

\[\Rightarrow \frac{\partial F_r(y,t)}{\partial t} = \frac{1}{i\hbar} H_r(y) F_r(y,t)\]

\[F = e^{\frac{iH_0 t}{\hbar}} F_0^* \quad F_r^* = e^{\frac{-iH_0 t}{\hbar}} F_0^*\]

If now \(H_r(y)\) is simply multi-functorial, nothing happens to change weights of \(y\), only phase change.
So must be operator. (?)

---

Work out what happens for Separate
coupling in uncoupling of several otherwise
System uncoupled, couples to A through
couples to B then uncouple, finally A+B couples compare.
\[
A \xrightarrow{\text{no total}} \sum c_r v_r(x)
\]
System in \(\sum c_r v_r(x)\)
Apparatus in \(f_0(y)\) (Impulsive)
no total \(t=0 \quad \frac{v_0}{v_0} = f_0(y) \sum c_r v_r(x)\)
also can write \(\psi(x,y,t) = \sum f_r(y,t) v_r(x)\)
\(\Rightarrow\) it \(\frac{\partial f_r}{\partial t} = H_r(y)f_r(y,t)\)
since H is a thin thin thin thin thin thin thin thin thin thin thin thin thin thin thin thin thin thin thin thin
\(f_r(y,t) = c_r f_0(y)e^{-iH_r(y)t/\hbar}\)
\(\Rightarrow \psi(x,y,t) = \sum c_r f_0(y)e^{-iH_r(y)t/\hbar} v_r(x)\)

---

y momentum in \(\frac{\partial}{\partial y}\) kinetic energy 

\[ \frac{\text{cond } W_f}{\text{cond momentum}} \quad \psi_r(k) = f_0(y) e^{-iH_f(y)t/\hbar} \]

\[ \frac{\text{cond momentum}}{\phi_r(k)} = \int e^{iky} \psi_r(y) dy \]

\[ = \int e^{iky} f_0(y) e^{-iH_f(y)t/\hbar} dy \]

\[ \phi_r(k)^\dagger = \int f_0(y) e^{i[k y - H_f(y)t/\hbar]} dy \]

---

\[ \mathcal{H}(r, y, t) = \frac{\sum_{r} c_{r} f_{0}(y) e^{-i H(r, y) t / \hbar}}{\sqrt{\mathcal{H}}} \]

\[ \Rightarrow \mathcal{P}(r, y, t) = \mathcal{H} \mathcal{H} = \left( \sum_{r} c_{r} f_{0}^{*}(y) e^{-i H(r, y) t / \hbar} \right) \left( \sum_{r} c_{r} f_{0}(y) e^{-i H(r,y) t / \hbar} \right) \]

\[ = f_{0}^{*}(y) \sum_{r} c_{r} f_{0}^{*}(y) e^{i \frac{t}{\hbar} [H(r, y) - H(r, y)]} \]

\[ \mathcal{H}(r, y) = \mathcal{H} f_{0}(y) e^{-i H(r, y) t / \hbar} \]

---

Von Neumann Measurement 

\[ \mathcal{F} = \text{Systin} \quad \mathcal{F} = \text{apparato} \quad \mathcal{W} \in \mathcal{S} \mathcal{V}(g) \quad \mathcal{H}(r) \]

assume masso solare, che K.E., portato d'energia abneg. 

then Heinitz's definition 

\[ \text{Choose } H_{\Sigma} = -\text{in } g \frac{\partial}{\partial r} \]

then -in \(\frac{\partial}{\partial t} \psi_t(g; r) = + \text{in } g \frac{\partial}{\partial r} \psi_t(g; r)\) 

\[ \Rightarrow \left( \frac{\partial}{\partial t} + g \frac{\partial}{\partial r} \right) \psi_t(g; r) = 0 \]

\[ \Rightarrow \psi_t(g; r) = f(g; r - t g) \]

\[ \left[ \text{time } \frac{\partial}{\partial t} \psi_t = f_2(-g) \quad \frac{\partial}{\partial r} \psi_t = f_2 \right] \]

\[ \Rightarrow \left( \frac{\partial}{\partial t} + g_2 \frac{\partial}{\partial r} \right) \psi_t = 0 \]

if for \(t=0\) \(\psi_0(g; r) = \Phi(g; r)\) 

\[ \text{then } \psi_t(g; r) = \Phi(g; r - t g) \\ \text{in part } \mathcal{G} := \Phi(g) \mathcal{G}(r) \]

\[ \Rightarrow \psi_t(g; r) = \Phi(g) \mathcal{G}(r - t g) \]

---

\[ \alpha_1: P(g|r) = P_1(g)P_2(r-t_g) \]

\[ \begin{cases} P_1 = \phi^* \phi \\ P_2 = \xi^* \xi \end{cases} \quad (r-t_g) \]

\[ \Rightarrow C_{r,g} = \int P(g|r) h \left( \frac{P(g|r)}{\int P(g|r) P(g|r) P(g|r)} \right) dg dr \quad \text{not: } \int P_1 dg = 1 \quad \int P_2 dr = 1 \]

\[ = \int P_1(g)P_2(r-t_g) h \left[ \frac{P_1(g)P_2(r-t_g)}{\int P_1(g)P_2(r-t_g) dg} \right] dr dg \]

\[ = \int P_1(g)P_2(r-t_g) \left[ h_1 P_1(g) + h_2 P_2(r-t_g) - h_1 \int P_1(g)P_2(r-t_g) dg \right] dr \]

\[ = \int P_1(g) \ln P_1(g) + \int P_1(g) P_2(r-t_g) \ln P_2(r-t_g) - \int P_1(g) P_2(r-g) \left[ \frac{\ln S_1(g)P_2(r-t_g)}{P_1(g)} \right] dr \]

---

\[P_r = \int P(r)dr = P_1(z)\]

\[P_r^r = \frac{P(zr)}{P(z)} = P_2(r-tz) \quad P_r = \int_{tmin}^{tmax} P_1(z) P_2(r-tz) dz\]

\[I_r^r = \int P_r^r \ln P_r^r dr = \int P_2(r-tz) \ln P_2(r-tz) dr\]

\[\int_{r_1}^{r_2} I_2(r) \ln I_2(r) dr\]

\[P(r) = \int P_1(z) P_2(r-tz) dz\]

\[C_{r_1}^{r_2} = P_2 I_2^{r_2} - I_2^{r_1} = \int P_1(z) I_2(z) dz - (I_2^{r_2} - I_2^{r_1})\]

---

\[I_{gr} = \int \int \rho_1(q) \rho_2(r-gt) [h \rho_1(q) + h \rho_2(r-gt)] dr dg\]

\[= \int \int \rho_1(q) \rho_2(r-gt) h \rho_1(q) dg dr + \int \int \rho_1(q) \rho_2(r-gt) h\rho_2(r-gt) dg dr\]

\[= \int \int \rho_1(q) \left[ \int \rho_2(r-gt) h \rho_1(q) dg \right] dr\]

\[I = \int \int \rho_1(q) \rho_2(r-gt) h(\rho_1(q) + \rho_2(r-gt)) dr dg\]

\[5 = \int \int \rho_1(q) \rho_2(r-gt) \frac{h(\rho_1(q) + \rho_2(r-gt))}{r} dr dg\]

\[5 = 2 \cos \theta \cos \theta = 8 \cos^2 \theta\]

---

govermed by \(I_r\) 

\[P_r = \int P_1(g) P_2(r-gt) dg = f(5t)\]

\[I_r = \int P_r \ln P_r \, dr \quad \text{this spreads out} \quad \text{in time}\]

\[I_r^{(j)} = \left[ \int P_1(g) P_2(r-gt) dg \right] \ln \left[ \int P_1(g) P_2(r-gt) dg\right] \, dr\]

\[P_r = \int P_1(g) P_2'(r-gt)(-g) \, dg \quad \text{in this} \quad \text{is} \quad 0 \quad P_1\]

---

\[P_r^g = P_2(r-gt) \quad \text{(troubles with according to } g)}\]

\[P_r(r) = \int P_1(g) P_2(r-gt) dg\]

\[I_r^g = \int P_r^g \ln P_r^g dr \\
= \int P_2(r-gt) \ln P_2(r-gt) dr \\
\text{change to } \omega = r-gt \\
d\omega = dr \quad (g \text{ cont.})\\
= \int P_2(\omega) \ln P_2(\omega) d\omega \quad \text{cont.}\\
\Rightarrow \int P_2 I_r^g dg \quad \text{also cont.} \\
\text{(expected confidence interval)}\]

only the error is known, is changed. 

\[P_r(x) = \int P_1(g) P_2(r-gt) dg \quad \text{(conclusion)}\]

\[\text{Let } I_r(t) = \int \left[ \int P_1(g) P_2(r-gt) dg \right] \ln \left[ \int P_1(g) P_2(r-gt) dg\right] dr\]

---

\[P_r(r) = \int P_1(g) P_2(r-g) dg\]

\[\Rightarrow dt = 0 \quad P_r(0) = \int P_1(g) P_2(r) dg = \frac{P_2(r)}{2}\]

\[r - g + j \cdot v\]

\[\rightarrow r \quad j \cdot g + j \cdot v\]

\[P_r(x) = \int P_1(g) P_2(r-g) dg\]

Then \(x > x-1\) 

\[\Rightarrow \text{lim}_{x \to \infty} f(x) = f\]

\[\rho_r = \frac{1}{2\pi} \int P_1(g) P_2(r-g) dg\]

<|/det|>
\[\Rightarrow I_r = \int P_1(g) P_2(r-g) dg\]

\[
\begin{align*}
\Rightarrow I_r &= \int P_r \ln P_r \, dr \\
&= -\int \left[ P_1(g) P_2(r-g) \right] \ln \left[ P_1(g) P_2(r-g) \right] \, dr \\
&= -\int \left[ P_1(g) P_2(r-g)\right] \ln \left[ P_1(g) P_2(r-g) \righ
\end{align*}
\]

\[I(0) = -\int \left[ P_1(g) P_2(r) \ln P_2(r) \right] \, dr \, dg\]

---

Now the function \(P_2(r-gt)\) has the property 

\[ \int_{a}^{b} P_2(r-gt) \, dr = 1 \quad (\text{all } g, t) \]

\[ \begin{aligned} \text{and } \int_{-\infty}^{\infty} P_2(r-gt) \, dg \\ \text{let } \omega = r-gt \\ d\omega = -tdg \quad (\text{const}) \\ \omega \to \int_{-\infty}^{\infty} \frac{d\omega}{t} = \frac{d\omega}{t} \\ \text{thus } \int_{-\infty}^{\infty} P_2(\omega) \, d\omega \\ = \frac{1}{t} \int_{-\infty}^{\infty} P_2(\omega) \, d\omega \\ = \infty \quad \text{and } \text{thus } \text{that } \text{the} \end{aligned} \]

So we have \(\int_{-\infty}^{\infty} P_2(r-gt) \, dr = 1\) all \(g, t\)

\(\int_{-\infty}^{\infty} P_2(r-gt) \, dg = \frac{1}{t}\)

\(\Rightarrow \int_{-\infty}^{\infty} P_2(r-gt) \, dg = 1\) 

Now \(P_r = \int_{-\infty}^{\infty} P_2(r-gt) P_1(g) \, dg\) (all \(t=1\))

\[ \Rightarrow \int_{-\infty}^{\infty} P_2(r-gt) P_1(g) dg \]

---

\[ \text{则 } P_i' = \sum_j a_{ij} P_j \]

\[ \Rightarrow \sum_i P_i' \ln P_i' = \sum_i \left( \sum_j a_{ij} P_j \right) \ln \left( \sum_j a_{ij} P_j \right) \]

\[ = \sum_{ij} a_{ij} P_j \ln \left( \sum_j a_{ij} P_j \right) \]

\[ = \sum_j P_j \sum_i a_{ij} \ln \sum_j a_{ij} P_j \]

---

\[= \alpha \int \left( \ln p + \ln \alpha \right) dx + \beta \int g \left[ \ln g + \ln \beta \right] dx\]

\[= \alpha \left( p \ln p \right) + \alpha \ln \alpha + \beta \left( g \ln g \right) + \beta \ln \beta\]

Now we have that if \(F(p) = \int p \ln p \, dx\) and \(\alpha\) and \(\beta\) are constants \(\geq 0\)

\[F(p + \beta Q) \geq \alpha F(p) + \beta F(g) + \alpha \ln \alpha + \beta \ln \beta\]

**Notation:** For every \(\alpha_i \geq 0\) \(\sum \alpha_i = K\)

\(\Rightarrow\) **Maximum** \(\sum_i F(\alpha_i)\) when \(\alpha_i = x_j\) all \(j\).

**Definition** suppose \(\alpha\) **definitive**

\[P_1 \leq P_2\]

\[\text{then } 2\left(\frac{1}{2}P_1 + \frac{1}{2}P_2\right) \ln\left(\frac{1}{2}P_1 + \frac{1}{2}P_1\right) \geq P_1 \ln P_1 + P_2 \ln P_2\]

---

\[ \sum_{i} \left( \sum_{j} a_{ij} p_j \right) \ln \left( \sum_{j} a_{ij} p_j \right) \leq \sum_{j} p_j \ln p_j \]