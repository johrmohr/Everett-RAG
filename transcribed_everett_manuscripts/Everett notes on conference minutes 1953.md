# Everett notes on conference minutes 1953.pdf

Application of Accelerating Field  

Dr. Shoemaker presented some comparative calculations made by himself and Dr. Mosley on the power requirements of acceleration using (a) a traveling wave system (VCE- 1- 53) and (b) a conventional system using ferrite.  

He calculated the power requirements in the two cases as  

\[P = \frac{f}{T}\frac{C_{\mathrm{T}}}{N}\frac{V_{\mathrm{T}}^{2}}{\cos^{2}\theta} \quad f = \text{frequency of} \mathrm{R.F.}\] \[P = \frac{10^{9}}{T}\frac{V_{\mathrm{T}}^{2}}{2\pi^{2}f\mu 1\ln\frac{r_{1}}{r_{0}}\cos^{2}\theta} \quad V_{\mathrm{T}} = \text{voltage gain per revolution.}\]  

where both expressions were for non- resonant systems and so represented the stored energy supplied and thrown away in each cycle (through class B tubes) (a) was calculated on the basis of a large number of drift tubes (and not a conducting wall tube) to apply the voltage and so included no inherent resistive dissipation. The terms mean: \(C_{\mathrm{T}}\) - total capacity, \(N\) - number of wavelengths per machine period, \(\Theta\) - phase of particles with respect to the r.f. wave, 1 - the total length of ferrite, \(r_{0} r_{1}\) the internal and external radii of cylindrical ferrite blocks.  

If the following values were chosen:  

rise time = 0.2 soc , injection energy = 4 Mev, final energy = 10 Bev, \(\frac{V_{\mathrm{T}}}{\cos\theta} = 10^{5}\) volts, \(1 = 10\) meters, \(r_0 = 6\) cms. to keep \(B_{\mathrm{max}}\) for the ferrite = 500 gauss, \(\ln \frac{r_1}{r_0} = 1\) , \(f_{\mathrm{max}} = 10\) Mc/s, \(N = 10\) \(\mu_{\mathrm{max}} = 300\) ,

---

\[ \int \int \int \int \int \int \int \int \int \int \left( \int \int \int \int \int \int \int \int \int \right) \left( \int \int \int \int \int \int \int \int  \int \int \int \int \int \int \int \int \int \end{array} \right) \]

\[ = \int u^* u \left[ \frac{\partial u^*}{\partial u^*} + \frac{\partial u^*}{\partial u} + \frac{\partial u^*}{\partial u} \right] \ln \left( 1 + \frac{\partial u^*}{\partial u} + \frac{\partial u^*}{\mu u} \right) + \ln u^* u \]

\[ \int \int \int \int \int \int \int \left( \int u^* u \frac{\partial u^*}{\partial u} \right) \alpha \alpha = \frac{\partial}{\partial u} \]

\[ = \int u^* u \left[ \alpha^* + \alpha + \alpha^* \alpha \right] \ln \left( 1 + \alpha^* + \alpha + \alpha^* \alpha \right) \]

\[ + \int u^* u \left[ \alpha^* + \alpha + \alpha^* \right] \ln u^* u \]

\[ \therefore \lim_{\alpha \to 2} \frac{1}{1 + \alpha} = \]

\[ \Delta I = \int u^* u \left[ 1 + \alpha^* + \alpha + \alpha^* \alpha \right] \ln \left[ 1 + \alpha^* + \alpha + \alpha^* \alpha \]

---

1 \(\Phi (k) = \alpha \int_{-\infty}^{\infty} e^{ikx} \gamma (k) dx\) 

for function \(u(s)\), 

\[I_s = \int_{-\infty}^{\infty} u^*(s) \ln u^*(s) ds\]

\[\Delta u'(s) = u(s) + \Delta u(s)\]

\[= u + s \quad u^* = u^* + s^*\]

\[\text{then } I_s' = \int (u^* s^*) (u + s) \ln (u^* s^*) (u + s) ds\]

\[= \int u^* u + u s^* s u^* + s^* s \left( \frac{\ln (u^* u + s u^* s u + s^* s)}{\ln (u^* u + s u^* s u + s^* s)} \right)\]

\[\Delta I = I_s' - I_s = \int u^* u \ln \left[ \frac{u^* u + s u^* s u^* + s^* s u^* u^*}{u^* u} \right] ds + \int (u^* s^* s u^* + s^* s) \ln (u^* u + s^* s) ds\]

\[= \int u^* u \ln \left( 1 + \frac{s}{u} + \frac{s^*}{u^*} + \frac{s^* s}{u^* u} \right) ds + \int (u^* s^* s u^* + s^* s) \ln \left( \frac{u^* u + s u^* s u + s^* s}{u^* u} \right) ds\]

---

\[
\begin{align*}
&= \int \left( m \left( 2 \ln \frac{4 \pi^2}{2 \pi} + \frac{\chi^2}{2 \pi^2} - 2 \right) e^{-\frac{\chi^2}{8 \pi^2}} \right. \\
&\qquad \left. + \frac{3}{\sqrt{2} \sqrt{2 \pi}} \left( \ln \frac{1}{2 \pi \sqrt{2}} - \frac{2^2}{2 \pi^2} \right) e^{-\frac{2^2}{2 \pi^2}} \right) \mathcal{N}(x) dx \\
&\qquad + C. C.
\end{align*}
\]

---

working out: 

\[ \Delta P = \int \rho \omega^* + \omega \rho^* + \omega^* \omega \]

---

\[
\begin{align*}
\Delta \int p \ln p d x &= \int \ln p d x \int \phi \omega^* + \omega \phi^* d x + \int \ln p d x \int \omega^* \omega d x + \frac{1}{2} \int \left( \frac{\partial}{\partial \phi} \omega^* + \frac{\partial}{\partial \omega} \phi^* \right)^2 d x \\
&\qquad \text{second order } \omega
\end{align*}
\]

Now assume Gaussian i.e. \(p(x) = ae^{-bx^2}\) (real)
\(p(x) = c e^{-dx^2}\)

\[
\Rightarrow \phi' \phi = c^2 e^{-2dx^2}
\]

\[
\begin{align*}
\Delta \int p \ln p d x &= \left[ \ln c^2 - 2dx^2 \right] \int c e^{-dx^2} \left( \omega^* + \omega \right) d x \\
&\qquad \text{first order} \\
&\qquad + \left[ \ln c^2 - 2dx^2 \right] \left[ \omega^* \omega d x + \frac{1}{2} \left( \omega^* + \omega \right)^2 d x \right] \\
&\qquad \text{second order} \\
&\qquad + \int \left[ \ln c^2 - 2dx^2 \right] \left( \omega^* \omega d x + \frac{1}{2} \left( \left( \omega^* + \omega \right)^2 - 2dx^2 \right) \right) d x \\
&\qquad \text{third order}
\end{align*}
\]

now 

\(U(x)\) is function of \(x\)
\(\Rightarrow \omega(x) = n \int e^{ikx} n(x) dx\)
\(\omega^* = n \int e^{-ikx} n(x) dx\)

---

\[
\begin{align*}
\int \phi^* \phi + \phi^* \phi \phi + \phi^* \phi \phi^* + \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \int \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \dots \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \cdots \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \ldots \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \ddots \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \vdots \phi^* \phi \phi^* \phi \phi^* \phi \phi^* \end{align*}
\]

\[
\begin{align*}
&=\int \phi^* \phi \ln \left[ \frac{\phi^* \phi + \phi^* \phi \phi^* + \phi^* \phi \phi \phi^* + \phi^* \phi \phi \phi^* \phi \phi^*}{\phi^* \phi} \right] dk \\
&\quad + \int \phi^* \phi \ln \left[ \frac{\phi^* \phi + 2 \phi^* \phi \phi^* + 2 \phi^* \phi \phi \phi^* + 2 \phi^* \phi \phi \phi^* \phi \phi^*}{\phi^* \pi} \right] \left[ \frac{\phi^* \phi + \phi^* \phi \phi^*}{\phi^* \pi} \right] dk \\
&= (1 + \frac{\phi \phi}{\phi^* \pi} + \frac{\phi \phi}{\phi^* \pi} + \frac{\phi \pi}{\phi^* \pi}) \frac{\phi \pi}{\phi^* \pi} \\
&\quad + \int \phi^* \phi \ln \left[ 1 + \frac{\phi \pi}{\phi^* \pi} \right] \left[ \frac{\phi \pi}{\phi^* \pi} \right] dk
\end{align*}
\]

\[
\Delta I_k = \int \phi^* \phi \ln \left[ 1 + \frac{\phi^* \phi}{\phi^* \pi} + \frac{\phi^* \phi}{\phi^* \pi} + \frac{\phi \pi}{\phi^* \phi} \right] + \int \left[ \phi^* \phi \ln \phi + \phi^* \phi \ln \phi \right] \left[ \frac{\phi^* \phi}{\phi^* \pi} + \frac{\phi^*}{\phi^* \pi} \right] dk
\]

---

First that Variation Vomite:
We have (1) that to find mean in \(c(t) = \Delta \phi(t) = m \int e^{ikx} \phi(x) dx\)
\[
V(x) = 2e^{-ikx^2} \int \phi(x) = Ce^{-ikx^2}
\]
\[
\Delta T_p = \int [\ln c^2 - 2dk^2] \int_0^2 ce^{-dk^2} (\omega^* + \omega) dk
\]
where \(\omega = m \int e^{ikx} \phi(x) dx\)
...
\[
\Delta T_k = \int [\ln c^2 - 2dk^2] [2ce^{-dk^2} \int_0^2 \frac{dk}{m \int e^{ikx} \phi(x) dx} + C. C.
\]
introducing integral
\Rightarrow \Delta T_k = \int \int [\ln c^2 - 2dk^2] [2ce^{-d^2} \frac{m e^{-ikx} \phi(x)}{dk} dx + C. C.
\)
\[
= \int f^+ \phi(x) dx + \int f^-
\]
\[
F = m \int \ln c^2 - 2dk^2 e^{-dk^2 + ikx} dk
\]
\[
J = \int 2dk^2 x \phi(x) e^{-dk^2 + ikx} dk + C. C.
\]

---

Evaluation of \(g\) 

need 

\[
\begin{align*}
\int_{-\infty}^{\infty} e^{-dK^2 + iKx} \, dK \\
\int_{-\infty}^{\infty} a = \sqrt{2} \quad b = -ix \\
\int_{-\infty}^{\infty} \sqrt{\frac{\pi}{d}} e^{-\frac{x^2}{4d}} \, d^2 = -x^2
\end{align*}
\]

\[
\begin{align*}
\int_{-\infty}^{\infty} \sqrt{K^2} e^{-dK^2 + iKx} \, dK \\
a = \sqrt{d} \quad b = -ix \\
\int_{-\infty}^{\infty} \frac{\sqrt{\pi}}{d^{3/2}} \left( \frac{1}{d} + \frac{x^2}{4d} \right) e^{-\frac{x^2}{4d}} \, d^2
\end{align*}
\]

\[
f = 2mc \ln c^2 \sqrt{\frac{\pi}{d}} e^{-\frac{x^2}{4d}}
\]

\[
g = -4dmc \frac{\sqrt{\pi}}{d^{3/2}} \left( \frac{2}{d} - \frac{x^2}{4d} \right) e^{-\frac{x^2}{2d}} \\
= -4mc \sqrt{\frac{\pi}{d}} \left( \frac{1}{d} - \frac{x^2}{4d} \right) e^{-\frac{2x^2}{4d}}
\]

\[
\text{and } f + g = \sqrt{\frac{\pi}{d}} e^{-\frac{x^2}{2d}} mc \left( 2\ln c^2 + \frac{x^2}{d} - 2 \right)
\]

\[
\Delta I_K = \int_{\text{first solid}}^\infty mc\sqrt{\frac{\pi}{d}} \left( 2\ln c^2 + \frac{x^2}{d} \right) e^{-\frac{x^2}{2d}} N(x) \, dx \\
\qquad + C, C.
\]

---

\[ \Delta I_x = \int [\ln a^2 - 2bx^2][2ae^{-bx^2}] N(x) dx + C. C. \]

\[
\begin{align*}
\Delta I_x + \Delta I_x &= \int_{-\infty}^{\infty} \left[ \left[ \ln c \frac{\sqrt{\pi}}{2} \left( 2 \ln c^2 + \frac{x^2}{2} - 2 \right) e^{-\frac{x^2}{2c}} \right] + \left[ \left( \ln a^2 - 2bx^2 \right) 2ae^{-\frac{bx^2}{2}} \right] \right] N(x) dx \\
&\quad + C. C. \\
b \text{ but } \psi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2c}} \quad \phi(k) = \frac{1}{\sqrt{2\pi}} e^{-\frac{k^2}{2c}} \\
\text{ and } \nabla_x \nabla_k = \frac{1}{2} \\
\text{ i.e } a = \frac{1}{\sqrt{2\pi}} \quad b = \frac{1}{2\sqrt{2\pi}} \\
C = \frac{1}{\sqrt{2\pi}} \quad d = \frac{1}{2\sqrt{2\pi}} = \frac{1}{2} \sqrt{2} \\
\text{ and } \nabla_x \nabla_k = \frac{1}{2} \quad \Rightarrow \nabla_k = \frac{1}{2\sqrt{2\pi}} \\
\text{ i.e } a = \frac{1}{\sqrt{2\pi}} \qquad b = \frac{1}{2\sqrt{2\pi}} \\
C = \frac{2}{\sqrt{2\pi}} \qquad d = \frac{1}{2\sqrt{2\pi}} = \frac{1}{4\sqrt{2}} = 2\sqrt{2} \\
\text{ and } \nabla_x \nabla_k = \frac{1}{\sqrt{2\pi}} \quad \Rightarrow \nabla_k = \frac{1}{2\sqrt{2\pi}} \quad \text{and} \quad \nabla_x \nabla_k = \frac{1}{2} \quad \Rightarrow \quad \nabla_k = \frac{1}{2\sqrt{2\pi}} \\
\text{ i. e. } a = \frac{1}{\sqrt{2\pi}} \qquad b = \frac{\sqrt{2\pi}}{2\sqrt{2\pi}} \qquad d = \frac{1}{2\sqrt{2\pi}} \qquad \Rightarrow \nabla_k = \frac{1}{2\sqrt{2\pi}} \qquad \text{and} \qquad \nabla_x \nabla_k = \frac{1}{2} \qquad \Rightarrow \nabla_k = \frac{1}{2\sqrt{2\pi}} \\
\text { and } \nabla_x \nabla_k = \frac{1}{2} \qquad \Rightarrow \quad \nabla_k = \frac{1}{2\sqrt{2\pi}} \qquad \text { and } \nabla_x \nabla_k = \frac{1}{2} \qquad
\end{align*}
\]

\[
\begin{align*}
\Delta I_x + \Delta I_x & = \int_{-\infty}^{\infty} \left[ \frac{\sqrt{\pi}}{2} \frac{\sqrt{\pi}}{2} \frac{\sqrt{\pi}}{2} \left( 2 \ln c^2 - 2 \right) e^{-\frac{x^2}{2c}} \right] N(x) dx \\
&\quad + \left[ \left( \ln \frac{1}{2\pi} \right)^2 - \frac{x^2}{2} \right] \frac{2}{\sqrt{2\pi}} e^{-\frac{x^2}{2c}} \int_{-\infty}^{\infty} N(x) dx \\
&\quad + C. C.
\end{align*}
\]

---

\[ \Delta(p \ln p) = (1 + \Delta p) \Delta p + \frac{1}{2} \Delta p^2 - \frac{1}{6} p^2 \Delta p^3 \quad \cdots \quad \text{④} \]

now it \(\Delta p\) such that \(S(p \Delta p) = 1 = S_p + \Delta p = 1 + \Delta p\)

\[ \therefore \int \Delta(p \ln p) = \int_{\Delta p} \Delta p + \Delta p \ln p + \frac{1}{2} \Delta p^2 - \frac{1}{\Delta p^2} \Delta p^3 \]

\[ \text{now } p = p^* \phi \quad \text{and } \phi \neq \phi + \Delta \phi \]

\[ \Rightarrow \phi^* = \phi^* + \phi(\Delta \phi)^* + \Delta \phi \phi^* + \Delta \phi(\Delta \phi)^* \]

\[ \Rightarrow \Delta \phi \phi^* = \Delta \phi \phi^* + \Delta \phi \phi^* + \Delta \phi \phi^* + \Delta \Delta \phi \phi^* \]

\[ \therefore \int \Delta(p \ln p) = \int_{-\infty}^{\infty} \left[ \Delta \phi \phi^* + \Delta \phi \phi^* + \Delta \psi \phi^* + \Delta \psi \psi^* \right] \ln \phi \phi^* \]

\[ \therefore \int \Delta(p \ln p) = \int_{-\Delta p}^{\Delta p} \left[ \Delta \phi \phi^* + \Delta \phi \phi^* \right] \ln \phi \phi^* \]

---

Another method 

\[f = x \ln x\]

\[\frac{\partial F}{\partial x} = \frac{x}{x} + \ln x = 1 + \ln x = f' = F'\]

\[\frac{dF}{dx^2} = \frac{1}{x} \cdot f'' \quad \frac{d^3}{dx^3} = -\frac{1}{x^2} = F''\]

\[Taylor series \quad f(x) = \sum_{0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n\]

\[\Rightarrow x \ln x = a \ln a + (1 + \ln a)(x-a) + \frac{1}{2a^2}(x-a)^2 + \frac{1}{2a^3}(x-a)^3\]

\[= a \ln a + \frac{1}{2a^2}(x-a)^2 + \frac{3}{2a^3}(x-a)^3\]

\[\Rightarrow \Delta (a \ln a)\]

\[= x \ln x - a \ln a\]

\[\Rightarrow \Delta a \ln a = (1 + \ln a) \Delta a + \frac{1}{2a} (\Delta a)^2 - \frac{1}{6a^3} (\Delta a)^3, \ldots\]

---

\[
e^{-\frac{1}{2}x^2} = e^{-\frac{1}{2}\sum_{n=1}^{\infty} \frac{x^n}{n!}} = \sum_{n=1}^{\infty} \frac{x^n}{n!} = \sum_{n=1}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{n=1}^{\infty} \frac{x^n}{n!}
\]

\[
I = \int_{-\infty}^{\infty} \phi(t) \ln \phi(t) dt + \int_{-\infty}^{\infty} \psi^*(t) \ln \psi^*(t) dt
\]

for which \(I\) stationary. 

\[
\gamma' = \gamma + \epsilon n
\]

\[
\begin{align*}
\phi(n) &= \frac{1}{(2\pi)^n} \int_{-\infty}^{\infty} e^{i n x} \psi^*(x) dx \\
&= \frac{1}{(2\pi)^n} \int_{-\infty}^{\infty} \left( e^{i n x} \psi(x) + \frac{1}{i n} \int_{0}^{\infty} e^{i n x} \epsilon \mathcal{T}(x) dx \right) dx \\
&= \phi(n) + \epsilon \mathcal{T}(n)
\end{align*}
\]

\[
\phi^*(k) = \frac{1}{(2\pi)^k} \int_{-\infty}^{\infty} e^{i k x} \psi^*(x) dx = \frac{1}{(2\pi)^k} \int_{-\infty}^{\infty} \left( e^{i k x} \psi(x) + \frac{1}{i k} \int_{0}^{\infty} e^{i k x} \epsilon \mathcal{T}(x) dx \right) dx
\]

---

\[
\begin{align*}
\frac{d^2 r}{dt^2} &= -\frac{dV}{dr} \cdot \frac{1}{r} \cdot \frac{d^2 r}{dt^2} = -\frac{dV}{r^2} \\
V &= \pm \int \left[ ar - bz + \frac{1}{2} c(r^2 - z^2) + drz + \frac{1}{3} e(r^2 - 3rz^2) - \frac{1}{3} f(3r^2 - z^2) \right. \\
&\qquad \left. + \frac{1}{4} h(r^4 - 6r^2z^2 + z^4) - q(r^2 - rz^2) \right]^2
\end{align*}
\]

up and a coder had been promised next week. The equation set up was: 

\[
\frac{d^2 r}{dt^2} = \pm \left| a_0 + a_1 r + b_1 z + a_2 (r^2 - z^2) + b_2 (2 r z) + a_3 (r^3 - 3 r z^2) + b_3 (z^3 - 3 z r^2) \right|
\]

where t is distance along the central equilibrium orbit and there was a similar equation for the z direction. The problem was to be coded so that each of the coefficients could be set constant, by-passed, or given small random deviations from an average value for the different sectors. Non-focusing guide sections could be accounted for separately. The integration was to be performed by the Runge-Kutt method. The maximum values of r and z were to be stored through a run and a run would be stopped if either r or z exceeded a predetermined value or after a predetermined number of revolutions. 

The tentative program was: 

(1) To find closed orbits 

(2) To study resonant blow-ups due to variations in n and the effect of the non-linear terms on these. 

(3) To study driving terms. 

(4) To find the effect of small non-linear terms randomly distributed among the sectors. 

(5) To test the cumulative effect of the guide sectors, where n = 0.
No account was to be taken of fringing fields in this calculation. He agreed that it would not complicate the calculation very much to include fifth-order non-linear terms if desired as they could be fed in as a separate block.

---

\[
I_T = \int_{-\infty}^{\infty} p(k) \ln p(k) dk + \int_{-\infty}^{\infty} p(k) \ln p(k) dk
\]

\[
I_k' = \int_{-\infty}^{\infty} [\phi(k) + 2E(\phi(k) + \phi^*(k)) + \epsilon^2 \gamma^2(k)] \ln[\phi(k) + 2E(\phi(k) + \phi^*(k)) + E(k)] dk
\]

\[
\delta F(k) = F' \delta x + \frac{F''}{2!} (\delta x)^2 \dots
\]

\[
\phi(k) = \int_{-\infty}^{\infty} e^{ikx} \psi(k) \, dk \qquad \phi'(k) = \psi'(k)
\]

\[
\delta \phi(k) = e^{ikx} \psi(k) \quad \delta \phi'(k) = \psi'(k) \\
\delta \int \phi(k) \, dk = \int \delta \phi(k) \, dk \\
\delta \int \phi(k) \, dk = \int \delta \phi(k + \delta k) \, dk
\]

\[
I' = \int \phi_{k0} + \phi_{k0}^* + \phi_{k0} \phi_{k0}^* + \phi_{k0} \phi_{k0} \phi_{k0}^* \ln \text{det } dk \\
I'' I
\]