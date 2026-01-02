# Everett Handwritten Notes and Calculations -- Relative wave functions circa 1955.pdf

Relative Wave functions: 

\[ \psi \psi(x,y) = \sum a_{ij} \phi_i(x) \phi_j(y) \]

\[ \text{thin } \psi^3(x) = \sum_i a_{ij} \phi_i(x) \]

\[ \psi \psi(x,y) = \iint a(x,y) S(x-x') S(y-y') dxdy \]

\[ \Rightarrow \psi^4(x) = \int a(x,y) S(x-x') dx \]

\[ \text{nowhere} \quad \text{ic if } \psi(x,y) = \frac{\psi(x,y)}{\sqrt{\psi(x,y)}} \]

\[ \text{then } \psi^{-r}(x) = N \psi_0(x) \psi(r-x) \]

\[ \int \psi_0^* \psi_0^* \psi_0^* \psi_0^*(r-x) dx = \int \psi_{xr} dx = P_r \]

\[ \therefore \psi^{-r}(x) = \frac{1}{\sqrt{P_r}} \psi_0^*(x) \psi(r-x) \]

---

\[\begin{align*} \text{Now, if} \quad \psi_0(x) &= \alpha e^{-\frac{[A+iB]\frac{x^2}{2}}{2}} \quad \text{that,} \\ u(r) &= \beta e^{-\frac{r^2}{4r}} \end{align*}\] \[\Rightarrow \psi^{-1}(x) = \frac{1}{\sqrt{r}} \propto e^{-\frac{[A+iB]\frac{x^2}{2}}{2}} \beta e^{-\frac{(r-x)^2}{4r}}\] \[\Rightarrow \phi^{-1}(k) \quad \text{similarly to region around} \quad x = \frac{r}{2}\] \[\Rightarrow \phi^{-1}(k) \quad \text{they will sample, assume} \quad \text{region} \quad x = x_1 + x_2\] \[\text{then} \quad f_c(r) = 1 \quad \text{otherwise} \quad 0 \quad \text{otherwise}\] \[\text{then} \quad \psi^{-1}(x) = \frac{1}{\sqrt{r}} \propto \beta e^{-\frac{[A+iB]\frac{x^2}{2}}{2}} \quad r \quad \text{only} \quad \text{region} \quad r \le r_1 + r_2\] \[\Rightarrow \phi^{-1}(k) = \frac{r_1 + r_2}{r} e^{-\frac{[A+iB]\frac{x^2}{2}}{2}} \quad k\]

---

\[ \alpha = [A+iB] \quad \beta = iK \]

\[ a = \]

\[ \text{Bettin (cairin)} \]

\[ \text{for Wobat with Gaussian} \quad \int_{-\infty}^{\infty} e^{ikx} e^{-[A+iB]\frac{x^2}{2}} e^{-\frac{(x^2+x)^2}{4r^2}} dx \]

\[ = \int \exp \left[ i k x - \frac{A x^2}{2} - i \frac{B x^2}{2} - \frac{r^2}{4 r^2} \right] \frac{x^2}{4 r^2} \frac{x^2}{4 r^2} \frac{x^2}{4 r} \]

\[ = \int \exp \left[ -\frac{A}{2} - \frac{i B}{2} - \frac{1}{4 r^2} x^2 + \left[ i k + \frac{2 r'}{4 r^2} \right] x - \frac{r'^2}{4 r^2} \right] dx \]

\[ \text{for perfectly Gaussian} \quad \frac{b^2}{4a^2} \quad \text{when} \quad a^2 = \frac{A}{2} + \frac{i B}{2} + \frac{1}{4 r^2} \]

\[ b = \left( i k + \frac{2 r'}{2 \sqrt{r^2}} \right)^2 \]

\[ = -k^2 + \frac{i k r'}{\sqrt{r^2}} + \frac{r'^2}{4 r^2} A \]

---

\[
\vec{\phi}(t) = N \exp\left[-\frac{k^2 + i k r'}{\sqrt{r^2}} + \frac{r'^2}{4 \sqrt{r^4}}\right] \\
2A + 2iB + \frac{1}{4r^2}
\]

\[
\text{and } \vec{\phi}(t) = N \vec{r} \quad \text{match by complex conjugate} \quad 1)
\]

\[
\left[-\frac{k^2 + i k r'}{\sqrt{r^2}} + -\frac{r'^2}{4 \sqrt{r^4}}\right] \left[2A - 2iB + \frac{1}{\sqrt{r^2}}\right] \\
\left(2A + \frac{1}{\sqrt{r^2}}\right)^2 + (2B)^2
\]

\[
\text{now want } \exp(\text{exp}(t)) = \exp(-t^*) = \exp(\text{real} - t)
\]

\[
\text{Real part of exp} = 2A k^2 + \frac{2A r'^2}{4 \sqrt{r^4}} + \frac{2B k r'}{\sqrt{r^2}} - k^2 + \frac{r'^2}{4 \sqrt{r^4}} - 4
\]

\[
\begin{align*}
\text{real} &= \frac{8A k^2 \sqrt{r^2} + 2A r'^2 + 8B k r' - 4 \sqrt{r^2} k^2 + r'^2}{2 \left[ (2A + 1)^2 + (2B)^2 \right] 4 \sqrt{r^2}}
\end{align*}
\]

---

Now \(e^{-\frac{x^2}{2\sqrt{2}}} = \frac{x^2}{2\sqrt{2}}\) 

Conclus 

\[ \Rightarrow \text{cuff } x^2 \text{ attle } \frac{1}{2\sqrt{2}} \]

Therefore 

in \(\mathcal{D}(k)\) k' normal
cuff of \(k^2\) 

\[ \text{is } \frac{8A\sqrt{r}^2 - 4\sqrt{r}^2}{8\left(\left[2A+1\right]^2+(2B)^2\right)} \sqrt{r}^2 \]

\[ = \frac{8A - 4}{8\sqrt{4A^2 + 4A + 1 + 4B^2}} \]

\[ = \frac{(2A - 1)}{2\sqrt{(2A+1)^2+(2B)^2}} = \frac{1}{2\sqrt{k}(r^2)} \]

indep 

for \(r^1\) 

and of \(\sqrt{r}^2\) 

what? 

unreasonable, 

some arbitrarily precise notion
title parameters \(k, s, t\)

---

Gradient 

\[
\frac{\left[-k^2 + \frac{1}{4}kr'^2\right]}{\frac{1}{4}r^4} + \frac{r'^2}{4r^4} \sqrt{\left[2A - 2\sqrt{B} + \frac{1}{r'^2}\right]} \\
\frac{\left[2A + \frac{1}{4}r'^2\right]^2}{r} + (2B)^2
\]

Études pour
Paris 

\[
\frac{\text{net part only}}{\text{only of } k^2} = \frac{\sqrt{2A^2 - k^2\left[2A + \frac{1}{r'^2}\right]^2}}{2} \cdot 2 \\
\frac{\left[2A + \frac{1}{r'^2}\right]^2}{\left(2B\right)^2} + (2B)^2
\]

\(\phi(r')\) is Gaussian
(quadrature, but)

\[
V_{\text{avance}} = \frac{1}{\sqrt{2k^2}} = \frac{4\left[2A + \frac{1}{r'^2}\right]}{\left[2A + \frac{1}{r'^2}\right]^2 + (2B)^2}
\]

\[
\frac{\sqrt{r}^2}{k} = \frac{\left(2A + \frac{1}{r'^2}\right)^2 + (2B)^2}{4\left(2A + \frac{1}{r'^2}\right)}
\]

---

\[\frac{\gamma}{l_{2}} = Ne^{\frac{-\left[A_{1}+iB_{1}\right]}{2}\frac{x^{2}}{2}}\]

\[\frac{\gamma}{l_{2}} = Ne^{\frac{-\left[\overline {A}_{1}+i\overline {B}_{1}\right]}{2}\frac{x^{2}}{2}}u_{2}\left(\frac{r_{1}-xr}{r_{2}}\right)^{2}\]

(known to solve this by a
(trinomial general exponential 

Good name His input \(x^{2}\) 7m 

no
Apparatus
of mine
1st. to remain
stationary 

\[y_{t_{2}}=Ne^{\frac{iH(t_{2}-x)}{n}}e^{\frac{-\left[A_{1}+iB_{1}\right]x^{2}}{2}}u_{2}\left(\frac{r_{1}-xr}{2}\right)\]

then 

did mean 

\[\frac{\gamma}{l_{2}}=u_{2}\left(\frac{r_{2}-x}{2}\right)Ne^{\frac{iH(t_{2}-x)}{n}}e^{\frac{-\left[\overline {A}_{1}+i\overline {B}_{1}\righ t\right]x^{2}}{2}}u_{2}\left(\frac{r_{2}-x}{2}\right)\]

\[u_{2}^{4}u_{2}\left(\frac{r_{2}-x}{2}\right)\]
\[\text{and}\delta\]

---

\[ \frac{(r')^2}{\sqrt{r}} = \frac{(2A + \frac{1}{\sqrt{r}})^2 + (2B)^2}{4(2A + \frac{1}{\sqrt{r}})} \]

\[ (y \text{ obe} \text{ to } \infty \text{ as } \sqrt{r^2} \to 0 \quad \text{40.04} \text{ } \]

\[ I_{r_k} = I_r + I_k + \{R, k\} \]

\[ \{R, k\} = I_r I_k - I_k \]

\[ \begin{aligned} \Rightarrow I_{r_k} &= I_r + I_k + \exp\{I_r^k\} - I_k \\ &= I_r + \exp\{I_r^k\} \end{aligned} \]

\[ \begin{aligned} \gamma_k &= \gamma_0(x) u(r-x) \\ \Rightarrow P(x, r) &= P_1(x) P_2(r-x) \\ \Rightarrow P(r) &= \int P(x) P_2(r-x) dx \\ \Rightarrow P(r) &= \int \frac{A + B x^2}{e} \frac{(x^2)^2}{2!} e^{-\frac{(r-x)^2}{2 \Gamma r^2}} \\ &\quad \int \exp\left[-A x^2 - B x^3 - \frac{\Gamma x^2}{2 \Gamma r^2} + \frac{r x}{2 \Gamma r^2} - \frac{x^2}{2 \Gamma r^2}\right] dx \end{aligned} \]

---

\[P(r) = N \int e^{i p \left[ -A - i B - \frac{1}{2} \frac{2}{\sqrt{r^2}} x + \frac{r}{\sqrt{r^2}} x \right]} dx\]

\[P(r) = N \exp \left[ \frac{\beta^2}{4a^2} \right] = N \exp \left[ \frac{\beta^2}{4r^4} \right] = \exp \left[ \frac{A + i B}{A - i B} \right]\]

\[P_4(r) = N \left( e^{-Ax^2} \frac{(r-x)^2}{e} dx \right) = A\]

\[\Rightarrow \int \exp \left\{ -A \frac{1}{r^2} x^2 + \frac{r}{r^2} x \right\} dx\]

\[\Rightarrow \int \exp \left\{ -A \frac{1}{x^2} x^2 + \frac{r}{r^2} x \right\} \exp \left\{ -a^2 \right\} dx\]

\[P(r) = N e^{\frac{b^2}{4a^2}} = \frac{\left( \frac{r^2}{4r^4} \right)}{4 \left( A + \frac{1}{2r^2} \right)} e^{-\frac{r^2}{2r^2}}\]

---

\[P(r) \sim \exp \left(-\frac{r^2}{4 \nabla_r^4 (A + \frac{1}{2 \nabla_r^2})} - \frac{r^2}{2 \nabla_r^2}\right)\]

\[= \exp -r^2 \left[ \frac{1}{2 \nabla_r^2} + \frac{1}{4 \nabla_r^4 (A + \frac{1}{2 \nabla_r})} \right]\]

\[= \frac{1}{2 \nabla_r^2} + \frac{1}{8 \nabla_r^2 (A \nabla_r^2 + 1)} \quad \frac{11}{8 (A \nabla_r^2 + 1)} + \frac{1}{16 \nabla_r^2 (A \nabla_r^2 + 1)} \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \frac{8}{16 \nabla_r^2} + \frac{1}{16 \nabla_r^2} + \frac{1}{16 \nabla_r^4} + \frac{1}{16 \nabla_r^2} + \frac{1}{\frac{1}{2 \nabla_r^2} + \frac{1}{2 \nabla_r^2} + \frac{1}{2 \pi^2} + \frac{1}{2 \pi^2} + \frac{2 \pi^2}{2 \pi^2} + \frac{2 \pi^2}{2 \nabla_r^2} + \frac{2 \pi^2}{2 \nabla_r^2}} \quad \quad \quad \quad \quad \quad \quad \quad \quad \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text{where} \quad \frac{1}{2 \nabla_r^2} + \frac{1}{2} \nabla_r^2 + \frac{1}{2 \nabla_r^2} + \frac{1}{16 \nabla_r^2} \quad \quad \quad \quad \quad \quad \quad \quad \quad \boxed{\text{where} \quad \frac{1}{2 \nabla_r^2} + 1} \quad \quad \quad \quad \quad \quad \quad \quad \quad 1 \quad \quad \quad \quad \quad \quad \quad \quad \quad \begin{array}{c} \frac{1}{2 \nabla_r^2} + \frac{1}{2}\nabla_r^2 + \frac{1}{2 \nabla_r^2} + \boxed{\frac{1}{2 \nabla_r^2} + \frac{1}{2 \frac{1}{2 \nabla_r^2} + \frac{1}{2}} + \frac{1}{2 \nabla_r^2} + \frac{1}{4}} \quad \quad \quad \quad \quad \quad \quad \quad \quad 2 \nabla_r^2 + \frac{1}{2 \nabla_r^2} + 1 \quad \quad \quad \quad \quad \quad \quad \quad \boxed{2 \nabla_r^2 + \frac{1}{2 \nabla_r^2} \quad \quad \quad \quad \quad \quad \boxed{2 \nabla^2} + \frac{1}{2 \nabla_r^2} + \frac{\frac{1}{2 \nabla_r^2} + \frac{1}{2}} \quad \quad \quad \quad \quad \quad \quad \quad \boxed{(2 \nabla_r^2 + \frac{1}{2 \nabla_r^2} - \frac{1}{2 \nabla_r^2} + \frac{1}{2})} \quad \quad \quad \quad \quad \quad \quad \quad \quad (2 \nabla_r^2 + \frac{1}{2 \nabla_r^2} ) \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array} \quad \quad \quad \quad \quad \quad \quad \quad \quad

---

\[ \therefore P(r) = N \exp\left(-\frac{A}{2A\sqrt{r^2+1}}\right) \]

\[ \text{which} \rightarrow A \propto \sqrt{r} \rightarrow 0 \]

\[ \text{and} \rightarrow \frac{1}{2\sqrt{r^2}} \propto \sqrt{r} \rightarrow \infty \]

\[ \therefore 2\sqrt{r} = \frac{A}{2A\sqrt{r^2+1}} \]

\[ \sqrt{r} = \frac{A\sqrt{r^2+\frac{1}{2}}}{A} = \sqrt{\frac{r^2}{r} + \frac{1}{2A}} \]

\[ \Rightarrow r = \frac{-\ln\left(\sqrt{r^2+\frac{1}{2A}}\right)}{2} - \ln\sqrt{r} \]

\[ \text{while} \left\{ \begin{array}{l} \sqrt{r} \\ \text{etc.} \end{array} \right\} = -\frac{1}{2} \ln\left(\frac{(2A+\frac{1}{\sqrt{r}})^2+(2B)^2}{4(2A+\frac{1}{\sqrt{r}})^2}\right) - \ln\sqrt{r} \]

\[ \Rightarrow I_y + I_k = \frac{\sqrt{r^2+\frac{1}{2A}}}{2A+\frac{1}{2r^2}} = \frac{\sqrt{r^2+\frac{1}{2A}}}{4A^2+\frac{2A}{\sqrt{r}}} = \frac{\sqrt{r^4+\sqrt{r^2}}}{4A^2\sqrt{r^2+2A}} \]

---

\[I_{r,k} = -\frac{1}{2} \ln \left[ \frac{\left(2A + \frac{1}{r^2}\right)^2 + (2B)^2}{4 \left(2A + \frac{1}{r^2}\right)} \left(\frac{r^2 + 1}{r^2 + 2A}\right) - 4 \ln \frac{r}{r} \right]\]

\[ \alpha = 2A \quad \beta = \frac{1}{r^2} \quad \gamma = 4B^2 \]

\[I_{r,k} = -\frac{1}{2} \ln\left[\frac{\left(\alpha + \beta\right)^2 + \gamma}{4 \left(\alpha + \beta\right)}\right]\left[\frac{1}{\beta} + \frac{1}{\alpha}\right]\]

\[ \frac{\left[\left(\alpha + \beta\right)^2 + \gamma\right]}{4 \left(\alpha + \beta\right)} = \frac{1}{2} \ln\left[\frac{\left(\alpha + \beta\right) + \gamma}{4 \alpha \beta}\right] \]

\[ = \frac{1}{2} \ln \left[ \frac{\left(\alpha + \beta\right)^2 + \gamma}{4 \alpha \beta} \right] \]

\[ \frac{\partial I_{r,k}}{\partial \beta} = \frac{4 \alpha \beta \left[ 2 \left( \alpha + \beta \right) \right] + 4 \alpha \left[ \left( \alpha + \beta \right)^2 + \gamma \right]}{4 \alpha \beta} = 0 \]

\[ \Rightarrow \frac{\partial}{\partial \beta} \left[ 8 \alpha + 4 \alpha \right] + \beta \left[ 8 \alpha^2 + 8 \alpha^2 \right] + 4 \alpha^3 + 4 \alpha \gamma \]

---

\[ \beta = \sqrt{\alpha^2 + \gamma} \]

\[ \Rightarrow \sqrt{\frac{1}{2}} \beta = \sqrt{4A^2 + 4B^2} = 2\sqrt{A^2 + B^2} \]

\[ \therefore \frac{I}{I_{\text{optimal}}} = -\frac{1}{2} \ln \left( \frac{2A + \frac{I}{2\sqrt{A^2 + B^2}}}{2} \right) \]

\[ = \frac{-\frac{1}{2} \ln \left[ \frac{(\alpha + \beta)^2 + \gamma}{4\alpha\beta} \right]}{4\alpha\sqrt{\alpha^2 + \gamma}} = \frac{11}{4\alpha\sqrt{\alpha^2 + \gamma}} \]

\[ = \frac{\alpha^2 + 2\alpha\sqrt{\alpha^2 + \gamma} + \gamma}{4\alpha\sqrt{\alpha^2 + \gamma}} \]

\[ = \frac{\alpha^2 + \gamma}{4\alpha\sqrt{\alpha^2 + \gamma}} + \frac{1}{2} = \frac{\sqrt{\alpha^2 + \gamma}}{4\alpha} + \frac{1}{2} \]

\[ = \frac{1}{4}\sqrt{\frac{\alpha^2 + \gamma}{\alpha^2}} = \frac{1}{4}\sqrt{1 + \frac{\gamma}{\alpha^2}} + \frac{1}{2} \]

---

\[
\beta = \frac{-[\beta \alpha^2] + \sqrt{16 \alpha^2 - 4 \cdot 12 \alpha [4 \alpha^2 + 4 \alpha \beta]}}{24 \alpha}
\]

\[
\frac{\partial}{\partial \beta} = 4 \alpha \beta \left( 2 \left[ \alpha + \beta \right] \right) - 4 \alpha \left[ \left( \alpha + \beta \right)^2 + \gamma \right]
\]

\[
= \left( 8 \alpha^2 \beta + 8 \alpha \beta^2 \right) - \left( 4 \alpha \left[ \alpha^2 + 2 \alpha \beta + \beta^2 \right] + \gamma \right)
\]

\[
\Rightarrow \beta^2 \left[ 8 \alpha - 4 \alpha \right]
\]

\[
+ \beta \left[ 8 \alpha^2 - 8 \alpha^2 \right]
\]

\[
- 4 \alpha^3 - 4 \alpha \beta = 0
\]

\[
\Rightarrow 4 \alpha \left( \beta^2 - \alpha^2 - \beta \right) = 0
\]

\[
\Rightarrow \beta^2 = \alpha + \gamma
\]

\[
\Rightarrow \beta = \sqrt{\alpha^2 + \gamma}
\]

---

\[ \frac{1}{\gamma_k} = -\ln \left[ \frac{1}{4} \sqrt{1 + \frac{1B^2}{4A^2}} + \frac{1}{2} \right] \]

actually \(>-\ln \gamma_0\) for \(t=0\) when \(\theta=0\). 

By regarding appropriate moments as \((1-\lambda)[1+\lambda A] = \Omega\) 

\[ \therefore A \phi_i = a_i \phi_i \]

\[ \Rightarrow \Omega \phi_i = (1-\lambda) \phi_i + \lambda a_i \phi_i = (1-\lambda + \lambda a_i) \phi_i \]

\[ \begin{aligned} \Omega^2 \phi_i &= \Omega (1-\lambda + \lambda a_i) \phi_i \\ &= (1-\lambda + \lambda a_i)^2 \phi_i \\ &= \sqrt{(1-\lambda)^2 + 2(1-\lambda) \lambda a_i + \lambda^2 a_i^2} \phi_i. \end{aligned} \]

Eventually that momentum \(\Omega_2\) on \(\gamma_0\) results in \((1-\lambda)\psi + \lambda \phi_0\) with probability \((1-\gamma_0 \phi_0)^2\)