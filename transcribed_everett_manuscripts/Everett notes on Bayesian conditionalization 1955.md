# Everett notes on Bayesian conditionalization 1955.pdf

\[ \text{definite} \omega^2 = \frac{1}{2\pi^2} \]

Normal distribution = Leblache-Funktion 

\[ P(x) dx = \frac{\omega}{\sqrt{\pi}} e^{-\omega^2 (x-u)^2} dx \]

\[ = \frac{1}{\sqrt{\pi}} e^{-\omega^2 (x^2 - 2ux + u^2) + \ln \omega} dx \]

Canonical form : 

\[ N e^{-\left[ a^2 \omega^2 - 2bc \omega^2 + c^2 \omega^2 - d \ln \omega \right]} \frac{d \ln \omega}{d \ln \omega} \]

\(N = \text{Normalform}\) 

Bayesian Update to Canonical Form for observation \(X\) : 

\[ \begin{aligned} a^2 &= a^2 + x^2 \\ bc &= bc + x \\ c^2 &= c^2 + 1 \\ d &= d + 1 \end{aligned} \]

Marginal Distribution of \(\omega\) : (bound) 

\[ P(\omega) d\omega = N \frac{\sqrt{\pi}}{2c} \omega^{d-1} e^{-\omega^2 (a^2 - b^2)} d\omega \]

Variance of distribution of \(x\) : 

\[ P(x) dx = \frac{N}{\sqrt{c^2 + 1}} \int_0^\infty \omega^d e^{-\omega^2 \left[ x^2 + a^2 - \frac{(bc + x)^2}{c^2 + 1} \right]} d\omega \]

---

Expected Value of u: 

\[ \langle u \rangle = \frac{b}{c} \quad (=\sum x_i / \text{Nobs}) \]

Standard dev (fagina w) 

\[ \text{Var}(u) = \frac{1}{2\omega^2c^2} \]

\[ \text{SD}(u) = \frac{1}{\omega c \sqrt{2}} = \frac{\sqrt{2}}{c} = \frac{\sqrt{2}}{\sqrt{\text{Nobs}}} \]

u is normally distributed for any w 

Mode of Variance (nonprobable) 

\[ \omega^* = \frac{2}{2(a^2-b^2)} \]

\[ \sqrt{\omega^*} = \frac{a^2-b^2}{d-1} \]

PIT FUNCTION 

\[ \psi(d) = \frac{\sqrt{1.3.5... (2m-1)}}{2^{m+1} \sqrt{\pi}} \quad \text{D even} \]

\[ \frac{m!}{2} \quad \text{0 odd} \]

\[ \sqrt{\pi}/2 \quad \text{0=0} \]

\[ \frac{1}{2} \text{Even} \quad \text{0=1} \]

---

Canonical Normalizer : 

\[ \frac{1}{N} = \psi(d-1) \frac{\sqrt{\pi}}{3c} \left( \frac{d}{a^2-b^2} \right)^{-1} \frac{d}{2} \]

Standard Regularizer 

\[ \int_{0}^{\infty} x^d e^{-ax^2} dx = \psi(d) a^{-d+1} \int_{a}^{\infty} e^{-(ax-b)^2} dx = \frac{\sqrt{\pi}}{a} \]

Unconstrained x 

\[ X P(x) dx = \frac{2c}{\sqrt{\pi}} \frac{\psi(d)}{\psi(d-1)} \frac{(cx-b)^2}{(a^2-b^2)(c^2+d)} + 1 \int_0^{\infty} \frac{1}{(a^2-b^2)(c^2+d)} dx = \frac{b}{2} \]

Mean of w : 

\[ \langle w \rangle = \overline{w} = \frac{\psi(d)}{\psi(d-1)} \frac{1}{\sqrt{a^2-b^2}} \]

Variance of w : 

\[ \text{VAR}(w) = \frac{\psi(d+1) \psi(d-1)}{(a^2-b^2) \psi(d-1)^2} \]

\[ \text{Rate of change of w} = \frac{\psi(d+1) \psi(d-1)}{\psi(d)^2} \frac{1}{\sqrt{d}} = \frac{1}{\sqrt{2}} \]