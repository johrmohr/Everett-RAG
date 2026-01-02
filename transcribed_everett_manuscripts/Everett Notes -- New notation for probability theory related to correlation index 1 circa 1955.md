# Everett Notes -- New notation for probability theory related to correlation index 1 circa 1955.pdf

New Notation: 

random variables \(X, Y, Z\) et particuliers \(X \land Y \land Z\)
Distributions \(P(x), P(y), P(z)\) et \(P(x)\) 

General distribution \(P_0(x) + P_1(x)\) 

Random Variable Continuous Range et Densité \(\tilde{x}\) 

Probability distribution \(P(x) + \tilde{P}_0 = \text{Prob of } x\) 

\(\text{cond } P_0 P_1 \geq 0 \quad P(x) + \sum P_n = 1\)

---

**Organization, two numbers** \(I_X = \int P(x)h_P(x)dx\) (continuous into) 

\[I_X = \sum_i P_i h_i P_i \quad (départé info)\]

not both \(I + I'\) vanish if their ranges null. 

Joint distribution \(P(x, y)\), \(P(x, y_1)\), \(P(x, y_2)\), \(P(x, y_3)\)
(units of 4 functions, but 4 inputs) 

Conditional distribution \(P^X = \frac{P(x, y)}{P(x)}\) 

\[= \frac{P(x, y_1)}{P(x)} \cdot \frac{P(x, y_2)}{P(x)} \cdot \frac{P(x, y_3)}{P(x)}\]

---

- Development for continuous case only:
  a) Variables \(P_{XYZ...}\)

\[P_{XYZ...} = P(x, y, z, \dots)\]

\[P_{XY} = \iiint P_{XYZ...} \, dx \, dy \, dz = \iiint P(x, y, z) \, dx \, dy \, dz\]

\[\text{Conditional Prob } P_{XY}^3 = \frac{P(x, y, z)}{P(z)}\]

\[\text{Information} = \frac{I_{XYZ}}{I_{XYZ}} = \int_{XYZ}^{uv} \ln \frac{P_{XYZ}^{uv}}{P_{XYZ}^{uv}} \, dx \, dy \, dz\]

\[\text{Binary Correlation} = \frac{C_{UV:XYZ}^{tw}}{C_{UV:XYZ}^{tw}} = I_{UV:XYZ}^{tw} - I_{UV:XYZ}^{tw}\]

\[\text{Total Correlation matrix of aggregate } Y_{YZ:UV} = \frac{I_{YZ:UV}^{tw}}{I_{YZ:UV}^{tw}} - \left[ I_{X}^{tw} + I_{Y}^{tw} + I_{Z}^{tw} + I_{UV}^{tw} \right]\]

---

**bien notary diff :**

**generalities of X with its diff :**

\[P(x,y)=P(x)S(x,y)=P(x)S(x,y)\]

\[\Rightarrow I_{XX}=\iint P(x,y)\ln P(x,y)dxdy\]

\[=\int P(x)\ln P(x)S(0)dx\]

\[distrib\ I_{xx}=\sum _{ij}P_{ij}S_{ij}\ln P_{ij}S_{ij}=\sum _{i}P_{i}\ln P_{i}=I_{x}\]

\[\Rightarrow C_{XX}=I_{XX}-I_{X}-I_{X}=00\]

\[distrib\ :=\frac {P_{ij}\cdot P_{ij}S_{ij}}{C_{XX}}=\sum _{ij}\frac {P_{ij}S_{ij}\ln \frac {P_{ij}S_{ij}}{P_{i}P_{j}}}{P_{i}P_{j}}=\sum _{ij}\frac {P_{i}\ln \frac {P_{i}}{P_{i}P_{j}}}{P_{i}P_{j}}\]

\[for\ conditional\ diff:\ P_{X}^{X^{\prime }}=\frac {P(x)S(x^{\prime })}{P(x)}=\frac {-P_{i}\ln P_{i}}{S(x-x^{\prime })}=-I_{X}\]

\[C_{XX}=\frac {\infty }{\infty }\]

\[P(x,y)=P(y,x)\]

\[x_{0}\]

\[y_{0}\]

<|det|>[[0, 0, 0, 0]]

---

Depende case: 

\[
\text{conditions: } \frac{T}{UVV} = +\infty \quad (\text{unles } P(v) = \delta)
\]

\[
\begin{align*}
\text{un case } P(v) &= \delta(v - v') \quad P(UVV) = P(v, v') \delta(v - v') \\
&= P(u) \delta(v) \delta(v - v')
\end{align*}
\]

\[
\begin{align*}
& \int P(u) \delta(v) \delta(v - v') \ln P(u) \delta(v) \delta(v - v') \, du dv \\
&= \int P(u) \delta(v) \delta(v) \ln P(u) \delta(v) \delta(v) \, du dv \\
&= \int P(u) \delta(v) \delta(v) \left[ \ln P(u) \delta(v) \delta(v) \right] \, du dv \\
&= \int P(u) \delta(v) \delta(v) \delta(v) \ln P(u) \delta(v) \left[ \delta(v) \right] \, du dv \\
&= \int P(u) \delta(x) \delta(y) \ln P(u) \delta(y) \delta(x) \, du dv \\
&= \int P(u) \delta(x) \delta(y) \delta(x) \ln P(u) \delta(y) \delta(x) \, du dv \\
&= P(x, y) = \delta(x) \delta(y)
\end{align*}
\]

\[
C_{xy} = \int P(x, y) \ln \frac{\delta(x) \delta(y)}{\delta(x) \delta(y)} \, dx = 0
\]

really interesting, could define either
as 0 or +∞ 

\[
\text{direct} \quad I_{XUV} = p_{ijk} = p_{XUV} = p_{ij} s_{jk}
\]

\[
\Rightarrow I_{XUV} = \sum_{ijk} p_{ij} s_{jk} \ln p_{ij} s_{jk} \\
= \sum_{ij} p_{ij} \ln p_{ij} = I_{XV}
\]

---

\[ \mathcal{P}(x;x) \quad P_{ij} = P_i \delta_{ij} \]

\[ \Rightarrow I_{xx} = \sum_{ij} P_i \delta_{ij} \ln P_i \delta_{ij} \]

\[ = \sum_i P_i \ln P_i = I_x \]

\[ \Rightarrow C_{xx} = I_{xx} I_x I_x = -I_x \quad \text{!!} \]

**conventional**

\[ \mathcal{P} \xrightarrow{X_i} S_{ij} \]

\[ \begin{cases} I_{x_i} = \sum_i \delta_{ij} \ln S_{ij} \\ I_x = 0 \end{cases} \quad P_i = P_j \]

\[ \text{for discrete relations} \]

\[ \mathcal{P} \xrightarrow{X_i} S_{ij} \]

---

\[ \tilde{D}_{\text{igges}} = \tilde{I}_{uxx} \]

\[ P_{uxx} = P_{ij} \delta_{jk} \]

\[ \begin{aligned} \tilde{I}_{uxx} &= \sum_{ijk} P_{ij} \delta_{jk} \delta_{ik} P_{ij} \delta_{jk} \\ &= \sum_{ij} P_{ij} \delta_{ik} P_{ij} = \tilde{I}_{ux} \end{aligned} \]

\[ \begin{aligned} \tilde{I}_{uxx} &= \tilde{I}_{ux} \quad \text{donc} \\ \tilde{I}_{uxx} &= \tilde{I}_{uxx} - \tilde{I}_x \\ &= \tilde{I}_{uxx} - \tilde{I}_{ux} = \tilde{I}_x \end{aligned} \]

\[ \tilde{I}_{uxx} = \tilde{I}_{uxx} \quad \text{nonnal} \quad \tilde{I}_{uxx} = \tilde{I}_{uxx} \quad \text{supposé donc} \quad \tilde{I}_{uxx} \]

---

Check the continuity of \(\rho\) 

\[P(u,v,w) = P(u,v) \delta(v-w)\]

\[\Rightarrow I_{uvw} = \int P(u,v) \delta(v-w) \ln P(u,v) \delta(v-w) \, du dv\]

\[I_{uvv} = \infty \quad I_{uvv} = +I_{uv}\]

**bicontinuous of continuous + discrete**

\[S_0\]

\[t\]

\[\infty\]

\[0\]

---

Transformation 

given \(P(x, y)\) with \(C(x, y)\) 

what about \(C_{z, y}\) where \(z = f(x)\)?
\(x = g(z)\) 

\[
\begin{align*}
P(z, y) &= P(g(z), y) \frac{\partial P(g(z))}{\partial y} \\
P(g(z)) &= \int P(g(z), y) \frac{\partial P(g(z))}{\partial y} dy
\end{align*}
\]

\[
\int P(g(z), y) Dg(z) \ln \frac{P(g(z), y)}{P(g(z))} dy dz
\]

\[
\begin{align*}
w &= g(z) \\
&= \int P(\omega, y) D\omega \ln \frac{P(\omega, y)}{P(\omega) P(y)} dy d\omega
\end{align*}
\]

\[
\begin{align*}
\text{General Theorem:} \quad C_{z, y} &= C_{x, y} \\
\text{where} \quad z = f(x) \quad \text{and} \quad z = g(z)
\end{align*}
\]

Very important!
General formulation.
of combination.

---

One more 

\[C_{y;xx}\]

\[= I_{uxx} - I_{u} - I_{xx}\]

\[in \text{ derivate} = I_{ux} - I_{u} - I_{xx} = C_{y;x}\]

On continuo Core 

\[C_{y;xx} = \frac{P(u;x) \delta(x-x')}{P(x;x') = \delta(x-x') P(x)}\]

\[= \int \int P(u;x) \ln \frac{P(u;x) \delta(x-x')}{P(u) \delta(x-x') P(x)}\]

\[S_0 \text{ then } C_{y;xx} = C_{yx}\]

\[I_{uxx} = I_{xx}\]

---

Work out carefully section on transformation 

\[
\begin{array}{l@{\qquad}l}
\text{ie } \text{given } P(x,y,z) \\
\text{change} & u = u(x,y,z) \\
\text{transform to } P'(uvw) & v = v(x,y,z) \\
\text{and } w = w(x,y,z) \\
\end{array}
\]

\[
\text{culbout } I' = I + \text{Exp } \ln J
\]

Standard deviation of any one variable
changed \(\Rightarrow\) Correlation increased
in normal with dependent on its value. 

\[
\begin{pmatrix}
\alpha & 0 \\
0 & \beta
\end{pmatrix}
\]

\[
P(u,y,w) = P(x,y,z) J \left( \frac{x+y}{uvw} \right)
\]

\[
\text{Add} g = \int_{0}^{u} \int_{0}^{v} \frac{x+y}{uvw} dv dw
\]

\[
P'(u,v,w) du dw = P(x,y,z) du dy dz
\]