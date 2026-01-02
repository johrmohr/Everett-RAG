# Everett -- Various game theory calculations.pdf

If you protest that anyway one player's netting gives the night answer, try the information-log game.

---

Erradien gami: 

Also, for \(P^2\) time \(V^4 = 1 + V^2\) 

\[ \text{weight} \frac{1 + V^2}{2 + V^2} \begin{pmatrix} 0 & 2 + V^2 \\ 1 + V^2 & 2 \end{pmatrix} = V^2 \Rightarrow \frac{(2 + V^2)(1 + V^2)}{3 + 2V^2} = V^2 \Rightarrow \frac{2 + 3V^2 + (V^2)^2}{3 + 2V^2} = V^2 \Rightarrow \frac{2 + V^2}{3 + 2V^2} = V^2 \]

\[ \text{atom} \quad \Gamma^1 \]

\[ V^2 = (V^2)^2 \]

<|det|>[[0, 0, 0, 0]]

---

\[
\begin{bmatrix}
\Gamma & \cdot x & \infty \\
& + & \beta \\
& & x \cdot \gamma
\end{bmatrix}
\begin{bmatrix}
0 & 1 + \Gamma_{\beta} \\
1 + \Gamma_{\beta} & 0 \\
1 + \Gamma_{\beta} & 1 + \Gamma_{\beta}
\end{bmatrix}
\]

Burner gone,
where \(\Gamma_{\beta} \Rightarrow \text{on next
page}\).
Now we don't restrict to
only single strategies \(\gamma\).

two consecutive move game 

<table><tr><td></td><td>1,1</td><td>1,2</td><td>2,1</td><td>2,2</td></tr><tr><td>\(\alpha, \beta\)</td><td>0</td><td>0</td><td>\(2 + \Gamma_{\alpha}\)</td><td>\(2 + \Gamma_{\alpha \beta}\)</td></tr><tr><td>\(\beta, \alpha\)</td><td>1</td><td>\(2 + \Gamma_{\alpha}\)</td><td>0</td><td>0</td></tr><tr><td>\(\beta, \beta\)</td><td>\(2 + \Gamma_{\alpha \beta}\)</td><td>1</td><td>0</td><td>0</td></tr><tr><td>\(\gamma, \beta\)</td><td>\(2 + \Gamma_{\alpha \beta}\)</td><td>1<td>1</td><td>\(2 + \Gamma_{\beta}\)</td></td></tr><tr><td>\(\gamma, \beta\)</td><td>\(2 + \Gamma_{\alpha}\)</td><td>1</td><td>\(2 + \Gamma_{\alpha \beta}\)</td><td>1</td></tr><tr><td>\(\gamma, \gamma\)</td><td>\(2 + \Gamma_{\alpha}\)</td><td>\(2 + \Gamma_{\alpha}\)</td><td>X</td><td>X</td></tr></table>

---

\[
\begin{align*}
& \sum_{x} \left( \begin{array}{cc} \delta & (1-\delta) \\ (i+V_{\alpha\beta}(\delta)) & 0 \\ (1+V_{\alpha\beta}(\delta)) & 1+V_{\alpha\beta}(\delta) \end{array} \right) \\
& \qquad \text{summe} \\
& V_{\alpha\beta}(\delta) = \max(\delta(1+V_{\alpha\beta}(\delta))+(1-\delta)(1+V_{\alpha\beta}(\delta)))
\end{align*}
\]

\[
\begin{align*}
V_{\gamma}(\delta) &= \max\left(\left[1-V_{\alpha\beta}(\delta)\right]\delta + (1-\delta)\left(1+i+V_{\alpha\beta}(\delta)\right)\right) \\
&= \delta\left(-\delta V_{\alpha\beta}(\delta)\right)\left(1\right) + V_{\alpha\beta}(\delta) - \delta\left(-\delta V_{\alpha\beta}(\delta)\right) \\
&= 1 - \delta\left[V_{\alpha\beta}(\delta) + V_{\alpha\beta}(\delta)\right] + V_{\alpha\beta}(\delta) \\
&= (1-\delta)V_{\alpha\beta}(\delta) + 1 - \delta V_{\alpha\beta}(\delta)
\end{align*}
\]

\[
V_{\alpha\beta}(\delta) = \max\left(\delta(1+V_{\alpha\beta}(\delta))\cdot(1-\delta)V_{\alpha\beta}(\delta)+1-\delta V_{\alpha\beta}(\delta)\right)
\]

---

Assuming stationary behaviour strategies 

for \(P_1\) more 1
more 2
\[\begin{bmatrix}
\alpha \\
1 - \alpha
\end{bmatrix}\]

configurational 

for \(P_2\) more 0
more 1
\[\begin{bmatrix}
\Phi^1 & C^2 & C^3 \\
\beta & \gamma & 1 \\
1 - \beta & 1 - \gamma & 0
\end{bmatrix}\]

combine to more than
parameter 

fairly close than in
configuration 2 holds if \(\gamma =\) 

time probability:
matrix

STOP
C^1
C^2
C^3

\[
\beta\alpha + \gamma - \alpha - \beta + \gamma
\]

\[
= 1 - \alpha - \beta - 2\alpha
\]

\[
\begin{array}{c|ccc}
\text{STOP} & C^1 & C^2 & C^3 \\
\hline
C^1 & 1 & 0 & 0 \\
C^2 & \beta\alpha + (1-\alpha)(1-\beta)\alpha(1-\beta) & 0 & \beta(1-\alpha) \\
C^3 & \gamma(1-\alpha) & \gamma\alpha + (1-\gamma)(1-\alpha)\alpha(1-\gamma) & 0 \\
\end{array}
\]

if domination argument used (γ=0) reduces to 

\[
\begin{array}{c|ccc|c}
S & C^1 & C^2 & C^3 \\
\hline
C^1/ & 1 & 0 & 0 & 0 \\
C^2/ & \beta\alpha + (1-\beta)(1-\beta)\alpha(1-\beta) & 0 & \beta(1-2\beta) & 0 \\
C^3/ & 1-\alpha & \alpha & 0 & 0 \\
\end{array}
\]

to now \(C^3\)
completely equiv to \(C^2\)

---

and we get (omitting \(c_2\)) 

\[
\begin{align*}
S & \quad C^1 \quad C^3 \\
S & \quad \begin{pmatrix} 1 & 0 & 0 \\ \alpha x + (1-\alpha)(1-\beta) & \alpha(1-\beta) & \beta(1-\alpha) \end{pmatrix} \\
C^3 & \quad 0 \quad 1-\alpha \quad \alpha
\end{align*}
\]

\[
\begin{align*}
\exp(x) &= \sum_{k=1}^{m} Q^k \\
\exp(x) &= \sum_{k=1}^{m} Q^k
\end{align*}
\]

\[
\text{but } \frac{1}{(1-Q)^2} = 1
\]

\[
\begin{align*}
(1-Q)^{-1} \sum Q^n &= \frac{1}{1-Q} \\
(1-Q)^{-1} (Q + Q^2 + Q^3 + \dots) \\
&= \frac{1}{1-Q} - 1 + Q^2 - Q^3 + Q^4 - \dots \\
&= -1
\end{align*}
\]

\[
\begin{align*}
\sum Q^n &= (1-Q)^{-1} \sum Q^n \\
&= (1-Q) \left( Q + Q^2 + Q^3 + \dots \right)^3 \\
&= Q - Q^2 + Q^3 - Q^4 + \dots \\
&= Q
\end{align*}
\]

---

at that 

\[
Q = \begin{pmatrix} \alpha(1-\beta) & \beta(1-\alpha) \\ 1-\alpha & \alpha \end{pmatrix}
\]

\[
\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} (1-\alpha) & (1-\alpha)(1-\beta) & -\beta(1-\alpha) \\ (1-\alpha) & (1+\alpha) & 1-\alpha \end{pmatrix}
\]

\[
\begin{pmatrix} \frac{d-b}{c-a} & \frac{de}{c+d} \\ \frac{ab}{cd} & \frac{ad-bc}{c+d} \end{pmatrix} = \begin{bmatrix} 1-\alpha(1-\beta) & 1-\alpha & -\beta(1-\alpha) \\ 1-\alpha & 1-\alpha & 1-\alpha \end{bmatrix}
\]

\[
\begin{pmatrix} \frac{a}{c} \frac{b}{d} \end{pmatrix} = \begin{array}{c} \text{ad-bc} \\ \text{ad-bc} \end{array} \begin{pmatrix} \frac{d-b}{c-a} & \frac{de}{c+d} \end{pmatrix} = \begin{bmatrix} 1-\alpha(1+\beta) & 1-\alpha & -\beta(1+\beta) \\ 1-\alpha & 1-\alpha & 1-\alpha \end{bmatrix} \\
= \begin{bmatrix} 1-\alpha(1+\beta) & 1-\alpha & 1-\alpha \end{bmatrix} \begin{bmatrix} 1-\alpha & 1-\alpha & 1-\alpha \end{bmatrix} \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1-\alpha & 1-\alpha & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} 1-\alpha & 1-\alpha & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \begin{bmatrix} 1-\alpha & 1-\alpha & 0 \\ 0 \end{bmatrix} \begin{bmatrix} 1-\alpha & 1-\alpha \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \]

---

\[
\begin{align*}
\text{end} \quad (1-\alpha)^{-1}Q \tag{1}
\end{align*}
\]

\[
\begin{align*}
& = \left[ \left( (1-\alpha)\alpha(1-\beta) + \beta(1-\alpha)(1-\alpha) \right) \right] \left[ (1-\alpha)(\beta)(1-\alpha) + \beta(1-\alpha) \right] \alpha \tag{1} \\
& \qquad \cdot (1-\alpha) \left[ \alpha(1-\beta) + \beta(1-\alpha) \right] \tag{1} \\
& \qquad \cdot (1-\alpha) \left[ (1-\alpha)(1-\beta) + (1-\alpha)(1-\alpha) \right] \left[ (1-\alpha)(\beta)(1-\alpha) \right] \tag{1} \\
& \qquad \cdot (2-\alpha)(1-\beta) + \beta \tag{1} \\
& \qquad \cdot (1-\alpha) \left[ (\alpha(1-\beta) + (1-\alpha)(1-\alpha)) \right] \left[ (1-\alpha)(\beta)(1-\alpha) + (\alpha(1-\beta) + \beta) \right] \tag{1} \\
& \qquad \cdot (1-\alpha)(\beta)(1-\alpha) + (\alpha(1-\beta)) \tag{1} \\
& \qquad \cdot (1-\alpha)(\beta)((1-\alpha) + \alpha(1-\beta)) \tag{1} \\
& \qquad \cdot (1-2\alpha + \alpha^2) \beta \tag{1} \\
& \qquad \cdot (1-2\alpha + \alpha) \beta \tag{1} \\
& \qquad \cdot (1-2\alpha) \beta \tag{1} \\
& \qquad \cdot (1-2\alpha)(1-\beta) \tag{1} \\
& \qquad \cdot (1-2\alpha)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-2\alpha)(1-2\alpha) \tag{1} \\
& \qquad \cdot (1-2\alpha)(1) \tag{1} \\
& \qquad \cdot (1-2\alpha)(1)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-1)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\alpha)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\beta)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\gamma)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\delta)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\epsilon)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\zeta)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\eta)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\kappa)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\lambda)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\mu)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\nu)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\xi)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\pi)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\sigma)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\tau)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\upsilon)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\phi)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\chi)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\psi)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\omega)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\rho)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\theta)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\iota)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\jmath)(1-\alpha) \tag{1} \\
& \qquad \cdot (1-\kapp

---

\[
\begin{array}{c}
\Gamma^2 \overset{\alpha}{\sim} \begin{pmatrix} 0 & 1+\Gamma^4 \\ 1+\Gamma^2 & 0 \end{pmatrix} \\
\Gamma^3 \overset{\alpha}{\sim} \begin{pmatrix} 1+\Gamma^2 & 0 \\ 1+\Gamma^3 & 1+\Gamma^2 \end{pmatrix} \\
\Gamma^4 \overset{\alpha}{\sim} \begin{pmatrix} 1+\Gamma^3 & 1+\Gamma^2 \end{pmatrix} \\
\end{array}
\]

\[
V_2 = \alpha(1-\beta)(1+V_2) + \beta(1-\alpha)(1+V_4) \quad V_3 = \alpha(1+V^3) + (1-\alpha)(1+V^2) \\
\quad \begin{cases}
V_4 = \alpha(1+V_3) + (1-\alpha)(1+V_2) \\
\quad = \alpha + \alpha V_3 + 1 - \alpha + V_2 - V_2 \alpha \\
\quad = 1 + V_2 - \alpha (V_3 + V_2)
\end{cases}
\]

\[
\begin{align*}
\alpha \text{ and } \alpha \\
\text{such that} \\
\alpha(1+V^2) &= (1-\alpha)(1+V^4) \\
\Rightarrow \alpha(1+V^2) + \alpha(1+V^4) &= 1+V^4 \\
\alpha(2+V^2+V^4) &= 1+V_4 \\
\Rightarrow \alpha &= \frac{1+V_4}{2+V_2+V_4}
\end{align*}
\]

This generalised by algebraically proving play, arbitrary strategy \((\alpha, 1-\alpha)\) on all rounds beginning to first.
(most play some strategy in all game elements of regular game, excluding initial move.)

---

\[
\begin{align*}
V_2 &= (\alpha - \alpha\beta)(1 + V_2) + (\beta - \alpha\beta)(1 + 1 + V_2 - \alpha)(V_3 - V_2) \\
&= \alpha + \alpha V_2 - \alpha\beta - \alpha\beta V_2 + 2\beta + \beta V_2 - \alpha\beta V_2 \\
&\qquad - 2\alpha\beta - \alpha\beta V_2 + \alpha^2\beta V_3 - \alpha^2\beta V_2
\end{align*}
\]

\[
\begin{align*}
V_2 &= \alpha \cdot +\alpha V_2 - 3\alpha\beta - 3\alpha\beta V_2 + 2\beta + \beta V_2 - \alpha\beta V3 \\
&\qquad + \alpha^2\beta V_3 - \alpha^2\beta V_2
\label{first}
\end{align*}
\]

\[
\begin{align*}
V_3 - \alpha V_3 &= \alpha + (1 - \alpha)(1 + V^2) \\
V_3 &= \frac{\alpha}{1 - \alpha} + 1 + V_2
\end{align*}
\]

As that 

\[
\begin{align*}
V_2 &= (\alpha + \alpha V_2 + 3\alpha\beta - 3\alpha\beta V_2 + 2\beta + \beta) \\
&\qquad + (-\alpha\beta + \alpha^2\beta) \left( \frac{\alpha}{1 - \alpha} + 1 + V_2 \right) - \alpha^2\beta V_2 \\
&\qquad - (\alpha\beta)(1 - \alpha) \\
&\qquad \left( \frac{\alpha^2\beta}{1 - \alpha} - \alpha\beta(1 - \alpha) - \alpha\beta(1 - \alpha) \right) V_2 - \alpha^2\beta V_2
\end{align*}
\]

---

\[
\begin{align*}
\alpha \left[ 1 - \alpha + 3\alpha \beta - \beta + \alpha \beta (1-\alpha) + \alpha \beta \right] V^2 &= \\
&= \alpha - 3\alpha \beta + 2\beta - \alpha^2 \beta - \alpha \beta + \alpha^2 \beta \\
&= \alpha - 4\alpha \beta + 2\beta
\end{align*}
\]

\[
V_2 = \frac{\alpha - 4\alpha\beta + 2\beta}{1 - \alpha + 4\alpha\beta - \beta}
\]

\[
\Rightarrow \frac{\alpha}{1-\alpha} = \frac{\alpha - 4\alpha + 2}{1 - \alpha + 4\alpha - 1}
\]

\[
\Rightarrow \frac{\alpha}{1-\alpha} = \frac{x+4\alpha+2}{3\alpha}
\]

\[
\Rightarrow \left(3\alpha\right)^2 = \left(5\alpha\right) + 2\left(5\alpha\right)^2
\]

\[
8\alpha^2 = 3\alpha + 2
\]

\[
8\alpha^2 - 3\alpha - 2 = 0
\]

\[
\alpha = \frac{3 \pm \sqrt{9 + 64}}{16} = \frac{3 \pm \sqrt{73}}{16}
\]

\[
\alpha = \frac{3 + \sqrt{73}}{16} = \frac{3 + \sqrt{73}}{13 - \sqrt{73}}
\]

---

\[
\begin{array}{r@{\;}c@{\;}l}
\frac{3+\sqrt{13}}{(13-\sqrt{13})(13+\sqrt{13})} & = & \frac{39+16\sqrt{13}+13}{169-73} \\
& & \frac{22}{96} \\
& & = \frac{28+4\sqrt{13}}{24} \\
\end{array}
\]

\[
\alpha = \frac{3+\sqrt{13}}{16}
\]

\[

\[V_{3} = \frac{\alpha}{i-\alpha} + 1 + V_{2}\]

\[
\begin{align*}
V_2 + 1 + V_2 &= 2V_2 + 1 \\
&= \frac{1+\sqrt{13}}{3} + \frac{3}{3} \\
&= \frac{10+\sqrt{13}}{3} = \frac{V_3}{3}
\end{align*}
\]

\[
\begin{align*}
V_4 &= V_3 = \frac{10+\sqrt{13}}{3} \\
&= \left| 1 + \frac{1+\sqrt{13}}{6} - \left( \frac{3+\sqrt{13}}{16} \right) \left( \frac{20+2\sqrt{13}}{6} - \frac{7+\sqrt{13}}{6} \right) \right| \\
&= \left| 1 + \frac{1+\sqrt{13}}{6} \right| - \left[ \frac{39+16\sqrt{13}+13}{6 \cdot 16} \right] \\
&= \left| 1 + \frac{1+\sqrt{13}}{6} + \frac{44+7}{12+16\sqrt{13}} \right| \\
&= \left| 1 + \frac{1+\sqrt{13}}{\sqrt{3}} \right|.
\end{align*}
\]

---

for parameter game 

\[V_2 = \frac{9 + \sqrt{73}}{6} = \frac{15.544004}{6} = \frac{2.590667}{7}\]

\[V_3 = V_4 = \frac{10 + \sqrt{73}}{3} = \frac{18.544004}{3} = \frac{6.181335}{5}\]

\[20 \text{ that } \frac{13}{6} \quad \frac{26 + 2\sqrt{73}}{6}\]

\[P^1 \quad \frac{13}{6} \quad \begin{pmatrix} 0 & \frac{26 + 2\sqrt{73}}{6} \\ \frac{26 + 2\sqrt{73}}{6} & \frac{13 + 2\sqrt{73}}{6} \end{pmatrix} \quad \frac{13 + \sqrt{73}}{3} \quad \frac{10 + \sqrt{73}}{3} = ?\]

\[Value = \left(\frac{13 + \sqrt{73}}{3}\right)^2 \div \frac{39 + 2\sqrt{73}}{6} \quad \text{normalized by} \quad \frac{39 + 2\sqrt{73}}{6}\]

\[= \left(7.181335\right)^2 \div \frac{13}{6} + 7.181335 \quad \frac{13}{6}\]

\[= \frac{5.15716}{7.348002} \neq \frac{5.51686}{5.51686}\]

Value of parameter game
Value of evading game cost 2.6