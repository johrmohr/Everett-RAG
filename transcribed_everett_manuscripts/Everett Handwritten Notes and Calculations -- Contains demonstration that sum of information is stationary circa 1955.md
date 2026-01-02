# Everett Handwritten Notes and Calculations -- Contains demonstration that sum of information is stationary circa 1955.pdf

Contain exponential distribution. Sum of information
DS Stationary, normal distribution's with
respect to wave function, variations!
(begin pg 14) 

\[I_{nT} = - \ln \nabla - \ln \sqrt{2\pi e} \Rightarrow h_T = -I_x - h_{2\pi e}\]

Incentivity Prime restriction to Normal distribution:
since \(T_x T_p \ge \frac{h_2}{2}\) (for normal) (power density
\(T_x + T_p = \frac{h_2}{2}\) 

\[\Rightarrow \ln T_x + \ln T_p = \ln \frac{h_2}{2}\]

\[\Rightarrow -I_x - \ln \sqrt{2\pi e} - I_p - \ln \sqrt{2\pi e} = \ln \frac{h_2}{2}\]

\[\Rightarrow I_x + I_p = -\ln \sqrt{2\pi e} - \ln \sqrt{2\pi e} - \ln \frac{h_2}{2}\]

\[= -\ln 2\pi e - \ln \frac{h_2}{2}\]

\[= -\ln \left(\frac{1}{\pi e \hbar}\right)\]

\[I_x + I_p = \ln \left(\frac{1}{\pi e \hbar}\right)\]

---

Conjecture : \(I_x + I_p \leq \ln\left(\frac{1}{\text{rech}}\right)\) for all distributions.
(applicable, since holds for all normal distributions, no matter what variance.) 

(all wave functions) 

May need section representation 

\[ \Phi(p) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-ipx} \psi(x) dx \Rightarrow \Phi^*(p) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \psi^*(x) e^{ipx} dx \]

\[ \Phi^*(p) = \frac{1}{\sqrt{2\pi}} \left[ \int_{-\infty}^{\infty} e^{-ipx} \psi^*(x) dx \int_{-\infty}^{\infty} \psi^*(x) e^{ipx} dx + \int_{-\infty}^{\infty} \psi^*(x) e^{ipx} dx - \int_{-\infty}^{\infty} \psi^*(x) e^{ipx} dx = 0 \right] \]

---

\[ \begin{aligned} \mathcal{L} \phi &= a e^{i b} \\ \mathcal{L} \phi^* &= a e^{-i b} \\ \mathcal{L} \phi^2 &= a^2 e^{i 2 b} \\ \mathcal{L} \phi^2 + \mathcal{L} \phi^*^2 &= a^2 \left[ e^{i 2 b} + e^{-i 2 b} \right] \end{aligned} \]

\[ \mathcal{L} \phi^2 + \mathcal{L} \phi^*^2 = a^2 \left[ e^{i 2 b} + e^{-i 2b} \right] \]

\[ \begin{aligned} \mathcal{L} \phi^2 + \mathcal{L} \phi^*^2 &= 2 a^2 \left( \cos 2 b \right) \\ &= 2 a^2 \cos 2 b \end{aligned} \]

\[ \mathcal{L} \phi^2 + \mathcal{L} \phi^2 \leq 2 a^2 \phi \]

\[ \begin{aligned} \mathcal{L} \phi^2 + \mathcal L \phi^*^2 &= \text{real} \{\phi\} \\ &= \frac{1}{2} (\phi - \phi^*) = \text{imag} \{\phi\} \end{aligned} \]

\[ \begin{aligned} \mathcal{L} \phi + \mathcal{L} \phi^* &= \frac{1}{\sqrt{2\pi}} \left[ \int_{-\infty}^{\infty} e^{-i p x} \psi(x) dx + \int_{-\infty}^{\infty} e^{+i p x} \psi^*(x) dx \right] \\ &= \frac{1}{\sqrt{2\pi}} \left[ \int_{-\infty}^{\infin} e^{-i p x} \psi(x) dx + \int_{-\infin}^{\infin} e^{+i p x} \psi^*(x) dx \right] \\ &= 2 \text{real} \left[ e^{i p x} \psi(x) \right] \end{aligned} \]

---

\[ \text{so real } \int_{-\infty}^{\infty} \varphi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \text{real } \{ e^{i\frac{\pi x}{a}} \psi(x) \} dx = R(p) \]

\[ \text{imag } \int_{-\infty}^{\infty} \varphi(x) = \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} \text{imag } \{ e^{i\frac{\pi x}{a}} \psi(x) \} dx \quad = I(p) \]

\[ \begin{aligned} A^2(p) &= A_{\text{imp}}^2 = R^2 + I^2 \\ \Rightarrow A^2 \ln A^2 &= (R^2 + I^2) \ln (R^2 + I^2) \end{aligned} \]

\[ \text{Want } A^2 \ln A^2 \le \text{Something} \]

\[ \text{40. That } I(p) = \int A^2 \ln A^2 dp \le \text{Something} \]

**Integrity #117** Hardy Gold: 

\[ \frac{x \ln \left( \frac{x}{a} \right) + y \ln \left( \frac{y}{b} \right)}{a + b} > \frac{(x+y) \ln \left( \frac{x+y}{a+b} \right)}{a+b} \]

\[ \text{unless } \frac{x}{a} = \frac{y}{b} \]

\[ \text{let } a+b=1 \]

\[ \Rightarrow (R^2 + I^2) \ln(R^2 + I^2) < R^2 \ln \frac{R^2}{a} + I^2 \ln \frac{I^2}{b} \quad (\text{all } a, b \ge 0 \text{ and } a+b=1) \]

---

\[ \Rightarrow I(p) \leq \int R^2 \ln \frac{R^2}{a} dP + \int I^2 \ln I^2 dp \]

\[ = \int R^2 \ln R^2 + \int I^2 \ln I^2 - \int R^2 \ln a \frac{dI}{I} - \int I^2 \ln b dp \]

\[ = -\ln a \int R^2 dp - \ln b \int I^2 dp \]

\[ \text{(in case } a = b = \frac{1}{2} \text{)} \]

\[ \text{guin. } -\ln(1) \int R^2 + I^2 dp \]

\[ = \int \text{perp} dp \]

\[ = - \ln(\frac{1}{2}) \]

\[ = -\ln(a) \]

\[ \text{now, also } \int \ln(b) dx \int \ln(a) dx \cong \int f^2(x) dx \]

\[ (R^2 + I^2)^2 \leq (R + I)^2 \]

\[ \text{Wants to show: } I(p) \leq \ln\left(\frac{I}{I + K}\right) - I_x \]

\[ \Rightarrow \int \frac{dp}{p^2} \phi(p) \ln p dp \leq \ln\left(\frac{I}{I + K}\right) - \int \psi(p) \ln p dp \]

\[ \text{or } \int \frac{dp}{p^2} \phi(p) \ln p dp + \int \psi(p) \ln p dp \leq \ln\left(\frac{I}{I + K}\middle) \right) \]

---

\[ \mathcal{P}(p) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{ipx}{\hbar}} \psi(p) dx \]
\[ \psi(x) = \frac{1}{\sqrt{2\pi}} \int_{0}^{\infty} e^{\frac{ipx}{\hbar}} \phi(p) dp \]

\[ I(p) = \left[ \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-\frac{ipx}{\hbar}} \psi(x) dx \int_{-\infty}^{\infty} e^{\frac{ipx}{\hbar}} \psi^*(x) dx \right] \]
\[ \ln \left[ \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{\frac{-ipx}{\hbar}} \psi(x) dx \right] \int_{-\infty}^{\infty} e^{\frac{ipx}{\hbar}} \psi^*(-x) dx \]

\[ \mathcal{A} \mathcal{A}^* \supset \mathcal{A} \mathcal{A}^* \supset \mathcal{A} \mathcal{B} \]

\[ \mathcal{S}(\phi(p)) = \int_{-\infty}^{\infty} e^{\frac{ipx}{\hbar}} \psi(x) dx - \int_{-\infty}^{\infty} e^{-\frac{ipx}{\hbar}} \psi(x)dx \]

\[ \begin{aligned} \mathcal{S}(\phi(p)) &= \int_{-\infty}^{\infty} e^{\frac{ipx}{\hbar}} \psi(x)dx \\ \mathcal{S}(\phi(p)) dp &= \int_{\mathcal{S}(\phi(p))} \phi(p) dp \\ &= \int_{\mathcal{S}(\phi(p))} \phi(p) dp \end{aligned} \]

\[ = \int \left( 1 + \ln \int e^{\frac{ipx}{\hbar}} \psi(x) dx \right) dx \]

---

\[ \begin{aligned} \mathcal{S}(\phi^*\phi) &= \phi^*\mathcal{S}\phi + \phi\mathcal{S}\phi^* \\ \text{thus} \quad \mathcal{S}(\phi^*) &= (\mathcal{S}\phi)^* \\ \Rightarrow \mathcal{S}(\phi^*\phi) &= \phi^*\mathcal{S}\phi + (\mathcal{S}\phi)^* \end{aligned} \]

\[ \text{now} \quad \mathcal{S}\phi = \int_{-\infty}^{\infty} e^{-i\phi x} \mathcal{S}P(x) dx \]

\[ \text{and} \quad \mathcal{S}(\rho_{\text{ln}P}) = \mathcal{S}P + \text{ln}P \mathcal{S}P = (1+\text{ln}P)\mathcal{S}P \]

\[ \begin{aligned} \Rightarrow \mathcal{S}(\phi^*\phi \ln \rho \phi^*\phi) &= (1+\text{ln}\phi^*\phi) \mathcal{S}(\phi^*\phi) \\ &= (1+\text{ln}\phi^*\phi + \text{ln}\phi)(\phi^*\mathcal{S}\phi + \phi(\mathcal{S}\phi)^*) \end{aligned} \]

\[ \begin{aligned} \Rightarrow \mathcal{S}(\phi^*\phi \phi \ln \rho \phi^*\phi) &= \int_{-\infty}^{\infty} (1+\text{ln} \int_{-\infty}^{\infty} e^{-i\phi x} \rho \phi^*\phi dx + \text{ln} \int_{-\infty}^{\infty} e^{-i\phi x} \phi^*\phi dx) \\ &\quad (\int_{-\infty}^{\infty} e^{-i\phi x} \rho \phi^*\phi) dx (\int_{-\infty}^{\infty} e^{-i\phi x} \phi^*\phi) dy + \int_{-\infty}^{\infty} e^{-i\phi x} \phi^*\phi dx (\int_{-\infty}^{\infty} e^{-i\phi x} \rho \phi^*\rho) dy) \end{aligned} \]

---

\[\begin{align*} \delta (\psi^*\psi_m\psi^*\psi) \\ &= (1 + \ln \psi^*\psi)\delta (\psi^*\psi) \\ &= (1 + \ln \psi^*\psi)(\psi^*\psi^*\psi + \psi^*\psi^*\psi) \\ \Rightarrow \delta I_1 &= \int \delta \psi^*\psi_m\psi^*\psi dx \\ &= \int (1 + \ln \psi^*\psi)(\psi^*\psi^*\psi^*\psi + \psi^*\psi^*\psi) dx \\ \Rightarrow \delta (I_1 + I_p) \\ &= \int \left[ 1 + \ln \left( e^{\frac{i p x}{\hbar}} \psi^*\psi \right) dx + \ln \left( e^{\frac{-i p x}{\hbar}} \psi^*\psi \right) dx \right] X \\ &\quad \int \left[ e^{\frac{i p x}{\hbar}} \psi^*\psi \right] dx \left[ e^{\frac{-i p x}{\hbar}} \psi^*\psi \right] dx \\ &\quad + \int (1 + \ln \psi^*\psi \ln \psi^*\psi)(\psi^*\psi^*\psi + \psi^2\psi) dx \\ &\quad \Rightarrow \delta \psi^* = 0 \quad \text{all} \delta \psi \end{align*}\]

---

\[
\begin{align*}
\text{Suppose } \psi(x) &= \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2x^2}} \\
&= \psi(x) = \left(\frac{1}{\sqrt{x^2}} e^{-\frac{x^2}{4x^2}} e^{-\frac{x^2}{4x^2}} e^{-\frac{x}{4x^2}} e^{-\frac{x}{4x^2}} e^{-\frac{1}{4x^2}} e^{-\frac{1}{4x^2}} e^{-\left(\frac{1}{4x^2}\right)^2} e^{-\left(\frac{1}{4x^2}\right)^2} e^{-\frac{1}{4x^2}} e^{-\frac{1}{4x} e^{-\frac{1}{4x} e^{-\frac{1}{4x} e^{\frac{1}{4x} e^{\frac{1}{4x} e^{\frac{\frac{1}{4x} e^{\frac{1}{4x} e^{\frac{x}{4x} e^{\frac{x}{4x} e^{\frac{x}{4x}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\\]
\end{align*}
\]

\[ \text{Suppose } \psi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2x}} \]

\[
\begin{align*}
\text{then } \phi(p) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{i px} \left( \frac{1}{\sqrt{x^2}} e^{-\frac{x^2}{4x^4}} e^{-\frac{x^2}{4x^4}} e^{-\frac{x}{4x^2}} e^{-\frac{x}{4x^4}} e^{-\frac{1}{4x^2}} e^{-\frac{1}{4 x^2}} e^{-\left(\frac{1}{4x^2}\right)^2}\right) dx \\
&= \frac{1}{\sqrt{2\pi}} \left( \frac{1}{\sqrt{x^2}} e^{-\frac{x^2}{\sqrt{4x^2}}} e^{-\frac{x^2}{\sqrt{4x^2}}} e^{-\frac{x}{4x^2}} e^{-\frac{x}{4x^2} e^{-\frac{1}{4x^2}} e^{-\frac{1}{2x^2}} e^{-\left(\frac{1}{2x^2}\right)^2} e^{-\left(\frac{1}{2x^2}\right)^2} e^{-\frac{1}{2x^2} e^{-\left(\frac{1}{2x^2}\right)^2} \right)} dx \\
&= \frac{1}{\sqrt{2\pi}} \left( \frac{2}{\sqrt{x^2}} e^{-\frac{x^2}{\sqrt{4x^2}} e^{-\frac{x^2}{\sqrt{4x^2}}} e^{-\left(\frac{1}{2x^2}\right)^2} e^{-\sqrt{4x^2} e^{-\left(\frac{1}{2x^2}\right)^4} e^{-\left(\frac{1}{2x^2}\right)^2} e^{\left(\frac{1}{2x^2}\right)^2} e^{-\left(\sqrt{4x^2}\right)^2} e^{-\left(\frac{1}{2x^4}\right)^2} e^{-\left(\frac{1}{2x^2}\right) e^{-\left(\frac{1}{2x^2}\right)^2} e^{-\pi^2} e^{-\left(\frac{1}{2x^2}\right)^2}} \right) dx \\
&= \frac{1}{\sqrt{2\pi}} \left( \left( \frac{2}{\sqrt{x^2}} e^{-\frac{x^2}{4x^2}} e^{\left(\frac{1}{2x^2}\right)^2} e^{-\frac{2}{\sqrt{4x^2}} e^{-\left(\frac{1}{2x^2}\right)^4} e^{-\frac{1}{4x^2} e^{-\left(\frac{1}{2x^2}\right)}} e^{-\left(\frac{1}{2x^2}\right)^2} e^{\pi^2} e^{-\left(\frac{1}{2x^2}\right)^4}} \right) dx \\
&= \frac{1}{\sqrt{2\pi}} \left(\frac{2}{\sqrt{x^2}} e^{-\frac{x^2}{4x^4}} e^{\left(\frac{1}{2x^2}\right)^2} e^{\left(\pi^2\right)} e^{-\left(\frac{1}{2x^2}\right)^4} e^{-\pi^2} e^{-\left(\frac{1}{2x^2} e^{-\left(\frac{1}{2x}\right)^2} e^{-\left(\frac{1}{2x^2}\right)} e^{-\left(\frac{1}{2x^2}\right)^2} e^{\frac{1}{2x^2} e^{-\left(\frac{1}{2x} e^{-\left(\frac{1}{2x^2}\right)^2} e^{-(\frac{1}{2x^2})} e^{-\left(\frac{1}{2x^2}\right)^2} e^{(\frac{1}{2x^2})} e^{-\left(\frac{1}{4x^2}\right)^2} e^{-(\frac{1}{2x^2} e^{-\left(\frac{1}{2 x^2}\right)^2} e^{-(\frac{1}{2x^2})}} e^{-\left(\frac{1}{2x^2}\right)^2} e^{2\pi^2} e^{-\left(\frac{1}{2x^2}\right)^2 e^{-\left(\frac{1}{2x^2}\right)^2} e^{4\pi^2} e^{-\left(\frac{1}{2x^2}\right)^4 e^{-\left(\frac{1}{2x^2}\right)^2} e^{8\pi^2} e^{-\left(\frac{1}{2x^2}\right)^6 e^{-\left(\frac{1}{2x^2}\right)^8 e^{-\left(\frac{1}{2x^2}\right)^8 e^{-\left(2\pi^2\right)}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\]
\]

---

\[\phi (\rho) = \kappa e^{-\frac{\rho^{2}\nabla_{x}^{2}}{\hbar^{2}}}\]

\[\Rightarrow \phi^{*}\phi (\rho) = \kappa^{2}e^{-\frac{2\nabla_{x}^{2}}{\hbar^{2}}\rho^{2}} \quad \text{Varimax}\]

\[S_{\phi^{*}\phi} = \kappa^{2}\int e^{-\frac{2\nabla_{x}^{2}}{\hbar^{2}}\rho^{2}}\rho^{2} = \frac{\sqrt{\pi}}{\hbar} \quad \rho^{2} = \frac{\hbar^{2}}{4\nabla_{x}^{2}}\]

\[\frac{\sqrt{\pi}}{\hbar}\frac{\hbar^{2}}{2\nabla_{x}^{2}} = \frac{\sqrt{\pi}}{\hbar}\frac{\hbar^{2}}{2\nabla_{y}^{2}} = \frac{\sqrt{\pi}}{\hbar}\frac{\hbar^{2}}{4\nabla_{x}^{2}} = \frac{\sqrt{\pi}}{\hbar}\frac{1}{2\nabla_{x}^{2}} = \frac{\sqrt{\pi}}{\hbar}\sqrt{\frac{\hbar^{2}}{4\nabla_{x}^{2}}}\]

\[\Rightarrow \kappa^{2} = \left(\frac{2\nabla_{x}^{2}}{\hbar^{2}}\right)^{1/2}\]

\[\Rightarrow \phi (\rho) = \frac{1}{\sqrt{\pi}\sqrt{\rho}}\frac{\text{求}\nabla_{x}}{\text{求}\hbar}\]

\[= \frac{2\nabla_{x}^{2}}{\sqrt{\pi}\hbar^{2}} \quad \frac{1}{2}\]

\[\Rightarrow \phi (\rho) = \left(\frac{2\nabla_{x}^{2}}{\hbar^{2}}\frac{1}{4} - \frac{\rho^{2}\nabla_{x}^{2}}{\hbar^{2}}\right) = \phi^{*}(\rho)\]

---

\[ \begin{aligned} \delta(\Gamma_p) &= \int \delta \phi \phi \delta \phi \ln \phi \delta \phi \delta \phi d\rho \\ &= \int \delta \phi \phi \ln \phi \delta \phi d\rho \end{aligned} \]

\[ \delta(\phi \phi \ln \phi \delta \phi) \]

\[ = \delta \phi \delta \phi + \ln \phi \delta \phi \delta \phi \delta \phi \]

\[ \text{not} \quad \phi \delta \phi = \left( \frac{2 \nabla_x^2}{\pi \hbar^2} \right)^{\frac{1}{2}} e^{-\frac{2 \nabla_x^2}{\hbar^2} \frac{p^2}{\hbar^2}} \]

\[ (1 + \ln \phi \delta \phi) = (1 + \frac{2 \nabla_x^2 p^2}{\hbar^2} + \frac{1}{2} \frac{\partial \nabla_x^2}{\partial t} \frac{2 \nabla_x^2}{\pi \hbar^2}) \]

\[ \Rightarrow \delta \int \Gamma_p = \int \left( 1 + \frac{1}{2} \ln \frac{2 \nabla_x^2}{\pi \hbar^2} - \frac{2 \nabla_x^2 p^2}{\hbar^2} \right) \delta \phi \delta \phi d\rho \]

\[ \text{but} \quad \int \delta \phi \phi d\rho = 0 \]

\[ \Rightarrow \delta \Gamma_p = \int_{-\infty}^{0} - \frac{2 \nabla_x^2 p^2}{\pi \hbar^2} \delta \left( \phi \delta \phi \right) d\rho \]

---

\[ \text{also } \int I_x = \int \left( \int \psi^* \psi \ln \psi \psi \right) d\tau \]

\[ = \int \left( 1 + \ln \psi^* \psi \right) \delta(\psi^* \psi) d\tau \]

\[ \text{now } \psi^* \psi = \frac{1}{\sqrt{2\pi} \sqrt{\tau}} e^{-\frac{\tau}{2\sqrt{\tau}^2}} \]

\[ \Rightarrow \left( 1 + \ln \psi^* \psi \right) = \left( 1 + \ln \left( \frac{1}{\sqrt{2\pi} \sqrt{\tau}} \right) - \frac{\tau}{2\sqrt{\tau}^2} \right) \]

\[ \Rightarrow \delta I_x = \int \left( 1 + \ln \left( \frac{1}{\sqrt{2 \pi} \sqrt{\tau}} \right) - \frac{\tau^2}{2 \sqrt{\tau}^2} \right) \delta(\psi^* \psi) d\tau \]

\[ \text{from Newton } \left( \text{ic} \int \delta \psi^* \psi = 0 \right) \]

\[ \Rightarrow \delta I_x = \int_{-\infty}^{\infty} \frac{-\tau^2}{2\sqrt{\tau}^2} \delta(\psi^* \psi) d\tau \]

\[ 2 \left( \frac{1}{2 \sqrt{\tau}} \right)^{\frac{1}{2}} e^{-\frac{\tau^2}{2 \sqrt{\tau}^2}} \delta(\psi^* \psi) d\tau \]

---

\[ \text{Now assuming } \phi(p) = k_1 \int_{-\infty}^{\infty} e^{-k_2 px} \psi(x) dx \]

\[ \Rightarrow \delta \phi(p) = k_1 \int_{-\infty}^{\infty} e^{-k_1 px} \delta \psi(x) dx \]

\[ \text{and } \delta \phi^2(p) = \delta \phi^2(p) = 2 \delta \phi(p) \delta \phi(p) \]

\[ = 2 \delta \phi(p) k_1 \int_{-\infty}^{\infty} e^{-k_1 px} \delta^2 \psi(x) dx \]

\[ \Rightarrow \delta \bar{L}_p = \left( \frac{1}{\pi} \int_{-\infty}^{\infty} \left( \frac{2 \bar{\tau}_x^2}{\pi \hbar^2} \right)^{\frac{1}{4}} \frac{p^2 \bar{\tau}_x^2}{\hbar^2} \right) k_1 \int_{-\infty}^{\infty} e^{-k_1 px} \bar{\psi}(x) dx \]

\[ \delta I_p = \left( \frac{4 \bar{\tau}_x^2 p^2}{\hbar^2} \frac{2 \bar{\tau}_x^2}{\pi \hbar^2} e^{-\frac{p^2 \bar{\tau}_x^2}{\hbar^2}} \right)^{\frac{1}{4}} \frac{p^2 \bar{\tau}_y^2}{\hbar^2} k_1 \int_{-\infty}^{\infty} e^{-k_1 px} \bar{ \psi}(x) dx \]

---

\[
\begin{align*}
e^{-\frac{p^2 \pi^2}{4 \pi^2}} - k_2 p x \\
a^2 = \frac{\pi^2}{4 \pi^2} \\
e^{-\frac{k_2 x^2}{4 \pi^2}} \\
e^{-\frac{\pi^2}{4 \pi^2}} \\
e^{-\frac{k_2 x^2}{4 \pi^2}} \\
e^{\frac{\pi^2}{4 \pi^2}} \\
e^{-\frac{k_2 \pi^2}{4 \pi^2}} \\
e^{-\frac{\pi^2}{4\pi^2}} \\
e^{-\frac{k_2 \pi^2}{4 \pi^3}} \\
e^{-\frac{\pi^2}{4 \pi^2}} \\
e^{-\pi^2} \\
e^{-\frac{k_2 \pi^2}{4 \pi^2}} \\
a = -\frac{4 \pi^2 p^2}{k_2^2} \left( \frac{2 \pi^2}{k_2^2} \right)^{\frac{1}{2}} \\
= \\
\delta I_p = -\frac{k_4}{4 \pi^2} \frac{4 \pi^2 p^2}{k_2^2} \left(\frac{2 \pi^2}{k_2^2}\right)^{\frac{1}{2}} \left(\frac{1}{k_2^2}\right)^{\frac{1}{2}} \\
x \int e^{\frac{k_2 x^2}{4 \pi^2}} \delta \psi(x) dx \\
\text{with} \quad \delta I_x = -\frac{x^2}{2 \pi^2} \left(\frac{1}{k_2^2 \pi^2}\right)^{\frac{1}{2}} e^{-\frac{x^2}{4 \pi^2}} \delta \psi(x) dx
\end{align*}
\]

---

More careful Treatment: 

\[
\text{maximum eigenvalues (radians)} \quad Q_k(r) = \mathcal{D} (2\pi)^{-\frac{1}{2}} e^{i k x}
\]

\[
\phi(k) = \int_{2\pi}^{+\infty} e^{-ikx} f(x) dx
\]

\[
\text{let } P = kx
\]

\[
2dp = 2kdx
\]

\[
\phi(p) = \left(\frac{1}{2\pi k}\right)^{\frac{1}{2}} \int_{-\infty}^{+\infty} e^{ikx} f(x) dx
\]

---

Maybe easier to work with K directly 

\[ \Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-ikx} \psi(x) dx \]

Now Assume \(\psi(x) = \left(\frac{1}{2\pi T_x^2}\right)^{\frac{1}{4}} e^{-\frac{x^2}{4T_x^2}}\) (Normal)

Then, by ① 

\[ \Phi(k) = \frac{1}{\sqrt{2\pi}} (\int_{-\infty}^{\infty} e^{-\frac{x^2}{4T_x^2} + ikx} dx) \times \left(\frac{1}{2\pi T_x^2}\right)^{\frac{1}{\sqrt{4}}} \]

\[ = \left(\frac{1}{4\pi^2 2\pi T_x^2}\right)^{\frac{1}{\sqrt{4}}} \left(4\pi T_x^2\right)^{\frac{1}{2}} e^{-\frac{k^2}{4T_x^2}} \]

\[ = \left(\frac{16\pi^2 T_x^4}{8\pi^3 T_x^2}\right)^{\frac{1}{\sqrt{4}}} e^{-\frac{k^2 T_x^2}{4}} \]

\[ = k^2 T_x^2 \]

---

\[ \text{but since } \phi(n) = \int_{-\infty}^{\infty} (2\pi)^{-\frac{1}{2}} \int_{-\infty}^{\infty} e^{-ikx} \psi(x) dx \]

\[ \text{we get } \delta \phi(n) = (2\pi)^{-\frac{1}{2}} \int_{-\infty}^{\infty} e^{ikx} \delta \psi(x) dx \]

\[ \begin{aligned} \text{moving, } \phi(n) &= \left( \frac{2\pi}{T} \right)^{-\frac{1}{2}} \frac{1}{\pi} e^{-2k \frac{\pi^2}{T} x} \\ \phi^*(n) &= \left( \frac{2\pi}{T} \right)^{\frac{1}{2}} \frac{1}{\pi} e^{-2k \frac{2\pi^2}{T} x} \end{aligned} \]

\[ \text{orbiting} \quad \text{③} \quad \text{②} \quad \text{①} \quad \text{②} \quad \text{③} \]

\[ \delta I = \int_{-\infty}^{\infty} \left[ 1 + \frac{1}{2} \ln \left( \frac{2\pi}{T} \right) - 2k \frac{2\pi^2}{T} \right] dx \]

\[ \text{but now restrict the } \delta \psi \text{ to those which preserve continuity,} \quad \Rightarrow \int \delta \psi^* \psi = \int \delta (\psi^* \psi) dx = 0 \]

---

we get 

\[ \mathcal{S}I_k = \int_{-\infty}^{\infty} \left[ 1 + \frac{1}{2} \ln\left(\frac{2V_k^2}{\pi}\right) - 2k^2V_k^2 \right] \mathcal{S}\phi^*\phi \, dk \]

\[ = -\int_{-\infty}^{\infty} 2k^2V_k^2 \mathcal{S}(\phi^*\phi) \, dk \]

\[ = -\int_{0}^{\infty} 2k^2V_k^2 2\phi \mathcal{S}\phi \, dk \]

**result ③ ad ⑥** 

\[ = -\int_{-\infty}^{\infty} \frac{2k^2V_k^2}{2} \mathcal{S}\left(\frac{2V_k^2}{\pi}\right)^{\frac{1}{4}} e^{-\frac{k^2V_k^2}{2}} \left(\frac{2\pi}{2\pi}\right)^{-\frac{1}{2}} e^{-\frac{ikx}{2}} \mathcal{S}V(x) \, dx \]

\[ = -4V_k^2 \left(\frac{2V_k^2}{\pi}\right)^{\frac{1}{4}}\left(\frac{2\pi}{2\pi}\right)^{-\frac{1}{2}} \int_{-\infty}^{\infty} k^2 e^{-\frac{k^2V_k^2}{2}} e^{-\frac{ikx}{2}} \mathcal{S}V(x) dx \]

\[ = -\left(\frac{4^4V_k^8}{\pi} \frac{2V_k^2}{4\pi^2}\right)^{\frac{1}{4}} \int_{-\infty}^{\infty} k^2 e^{-\frac{k^2V_k^{2}}{2}} e^{-\frac{ikx}{2}} \mathcal{S}V(x) dx = \]

---

\[ \text{thus out for Evaluation of} \int_{-\infty}^{\infty} x^2 e^{-a^2 x^2 - bx} dx \]

\[ \begin{aligned} y &= axd \quad x = \frac{y-d}{a} \\ y^2 &= a^2 x^2 \\ x^2 &= \left( \frac{y-d}{a} \right)^2 \\ &= \frac{a^2}{c^2} \left( y^2 - 2dy + d^2 \right) \end{aligned} \]

\[ a^2 x^2 + bx \quad (ax+d)^2 = a^2 x^2 + 2adx + d^2 \]

\[ \begin{aligned} &= a^2 x^2 + 2adx + d^2 - d^2 \\ &= (ax+d)^2 - d^2 \\ &= \left( \frac{ax+\frac{b}{2a}}{2a} \right)^2 - \frac{b^2}{4a^2} \\ &\text{so let } y = \left( \frac{ax+\frac{b}{2a}}{2a} \right) \\ &\text{and } dy = adx \end{aligned} \]

\[ \int y^2 e^{-\left[ ax^2 + bx \right]} dx = \int x^2 e^{-\left[ y^2 \right]} + \frac{b^2}{4a^2} dy \]

\[ = e^{\frac{b^2}{4a^2}} \int x^2 e^{-\frac{y^2}{2}} dx \]

\[ = e^{d^2} \int x^2 e^{-\frac{y^2}{2}} dx \]

---

\[y = ax + d\]

\[\Rightarrow x^2 = \frac{1}{a^2} (y^2 - 2dy + d^2)\]

\[and \quad dx = \frac{dy}{a}\]

\[\Rightarrow e^{d^2} \int_{-\infty}^{\infty} x^2 e^{-y^2} dx = e^{d^2} \int_{-\infty}^{\infty} \left( \frac{1}{a^3} (y^2 - 2dy + d^2) e^{-y^2} \right) dy\]

\[= \frac{e^{d^2}}{a^3} \int_{-\infty}^{\infty} \left( y^2 e^{-y^2} dy - 2d \int_{-\infty}^{\infty} y e^{-y^2} dy \right) \frac{1}{2\sqrt{\pi}} + d^2 \int_{-\infty}^{\infty} e^{-y^2} dy\]

\[= \frac{e^{d^2}}{a^3} \left[ \frac{1}{2}\sqrt{\pi} + d^2\sqrt{\pi} \right] \sqrt{\frac{1}{\pi}} \\ = \frac{e}{a^3} \frac{b^2}{4a^2} \sqrt{\pi} \left( \frac{1}{2} + \frac{b^2}{4a^2} \right) \\ = \int_{-\infty}^{\infty} x^2 e^{-bx} dx\]

---

from (3) 

so that
\[\int_{-\infty}^{\infty} k^2 e^{-k^2 T_x^2 - ikx} dk\]

\[a^2 = T_x^2 \quad b = ix \quad \frac{b^2}{4a^2} = \frac{-x^2}{4T_x^2}\]

\[= \sqrt{2\pi} \left( \frac{1}{2} \pm \frac{x^2}{4T_x^2} \right) \frac{1}{T_x^3} e^{-\frac{x^2}{4T_x^2}}\]

So that from (3)
\[\int_{-\infty}^{\infty} \frac{1}{4} \left( \frac{4^4}{4\pi^3} \frac{T_x^8}{T_x^2} \frac{T_x^2}{T_x^2} \right)^{1/4} \left( \frac{\sqrt{4}}{T_x^{12}} \right)^{1/4} \left( \frac{1}{2} \frac{-x^2}{4T_x^2} \right)^{1/4} e^{-\frac{x^2}{4T_x^2}} dk\]

\[\int_{-\infty}^{\infty} \frac{1}{k} = -\left( \frac{2}{\pi T_x^2} \right)^{1/4} \int_{-\infty}^{\infty} S(k) \left( \frac{1}{2} \frac{-x^2}{4T_{x^2}} \right)^{1/4} e^{-\frac{x^2}{4T_{x^2}}} dk\]

(9) imp!

---

Now to Evaluate \(\delta I_x\) 

\[\delta I_x = \int \left( \psi^* \psi \right) \exp \left( \psi^* \psi \right) dx\]

\[\Rightarrow \int \left[ 1 + \ln \psi^* \psi \right] \delta \psi^* \psi dx\]

\[\text{but } \psi = \left( \frac{1}{2\pi\sqrt{x}} \right)^{\frac{1}{4}} e^{-\frac{x^2}{4\sqrt{x}}^2}\]

\[\Rightarrow \psi^* \psi = \left( \frac{1}{2\pi\sqrt{x}} \right)^{\tfrac{1}{2}} e^{-\frac{x^2}{2\sqrt{x}}^2}\]

\[\ln \psi^* \psi = \frac{1}{2} \ln \left( \frac{1}{2\pi\sqrt{x}} \right) - \frac{x^2}{2\sqrt{x}}^2\]

\[\Rightarrow \delta I_x = \int_{-\infty}^{\infty} \left[ 1 + \frac{1}{2} \ln \left( \frac{1}{2\pi \sqrt{x}} \right) - \frac{x^2}{2\sqrt{x}}^2 \right] \delta \left( \psi^* \psi \right) dx\]

\[\text{again since } \delta \left( \psi^* \psi \right) dx = 0 \text{ thus vanish}\]

\[\text{and } \delta I_x = -\int_{-\infty}^{\infty} \frac{x^2}{2\sqrt{x}} \delta \left( \psi^* \psi \right) dx\]

\[\int_{-\infty}^{\infty} \frac{x^2}{2\sqrt{x}} \left( \frac{1}{2\pi\sqrt{x}} \right)^{\frac{1}4} e^{-\frac{x^2}{4\sqrt{x}}^2} \delta \left( \psi(x) \right) dx\]

---

\[ \delta(I_k + I_x) = \delta I_k + \delta I_x \]

\[ = -\frac{1}{2\pi V_x^2} \int_{-\infty}^{\infty} \left( \frac{2}{4\pi V_x^2} \right)^{\frac{1}{4}} \left( \int_{-\infty}^{\infty} \delta(x) e^{-\frac{x^2}{4V_x^2}} \left( \frac{1}{2} - \frac{x^2}{4V_x^2} \right) dx \right) \]

\[ = -\int_{-\infty}^{\infty} \frac{x^2}{4\pi V_x^2} \left( \frac{1}{2\pi V_x^2} \right)^{\frac{1}{4}} e^{-\frac{x^2}{4V_x^2}} \delta(x) dx \]

\[ = -\frac{1}{2\pi V_x^2} \int_{0}^{\infty} \left( \frac{1}{2\pi V_x^2} \right)^{\tfrac{1}{4}} \left( \int_{-\infty}^{\infty} \delta(x) \frac{x^2}{4V_x^2} \left( x - \frac{x^2}{V_x^2} \right) dx \right) \]

\[ = -\frac{1}{2\pi V_x^2} \int_0^\infty \left( \frac{1}{2\pi V_x^2} \right)^{\frac{\frac{1}{4}}{4}} \left( \int_{-\infty}^{\infty} \delta(x) e^{-\frac{\frac{x^2}{4}}{4V_x^2}} \left( \frac{x^2}{V_x^2} \right) dx \right) \quad (2) \]

\[ \Rightarrow \delta(I_k + I_x) = -\frac{1}{2\pi V_x^2} \int_{-\infty}^{\infty}\left( \frac{1}{2\pi V_x^2} \right)^{\frac{14}{4}} \left( \int_{-\infty}^{\infty} \delta(x) e^{-\left( \frac{x^2}{4V_x^2} \right)} (2) dx \right) \]

\[ \lim_{x \to \infty} \delta(x) = \delta(x) = \lim_{x \to \infty} \delta(x) = \delta(x) = 0 \]

---

And we have proved that the
Sum of the information is stationary
for the normal distribution. 

which
labore to support that the inequality 

\[I_x + I_p \le (without it is for normal)\]

May hold generally.

---

\[\nabla_{k}\nabla_{x}=\frac{1}{2}\]

\[I_{n\pi }=-ln\sqrt {2\pi e}\]

\[\Rightarrow ln\nabla _{k}+ln\nabla _{2}=ln\frac {1}{2}\]

\[-I_{k}-ln\sqrt {2\pi e}-I_{x}-ln\sqrt {2\pi e}=ln\frac {1}{2}\]

\[\Rightarrow \left|I_{k}+I_{x}=-ln(\frac {2\pi e}{r})\right|\]

\[\Rightarrow \left|I_{k}+I_{x}=-ln(\pi e)=ln\frac {1}{\pi e}\right|\]

---

Conjecture is that \(I_k + I_x \le - \ln(\pi e)\) 

where \(\phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-ikx} \psi(t) dt\) 

The necessary condition that \(I_k + I_x\) has a
Stationary value here is satisfied by 

\(\psi(x)\) of form \(\psi = \frac{1}{2} e^{-\frac{x^2}{k_2}}\) (normal) 

leading to \(\psi\) of some form 

and being Stationary with respect to 

Variation \(S\psi\) such that \(\int S\psi \psi = 0\) (normalization
(might however be a minimum and not a maximum.) 

is maybe \(I_k + I_p \ge - \ln(\pi e)\) always!