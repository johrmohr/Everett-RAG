# Everett Notes -- Transformations on probability distributions circa 1955.pdf

Transformation : 
given 
\(P(x, y, z)\) 

Fed 

\[ \begin{aligned} \text{Let } u &= u(x, y, z) \\ v &= v(x, y, z) \\ w &= w(x, y, z) \end{aligned} \]

\[ P(x, y, z) = P(x, y, z) J \left( \frac{x, y, z}{u, v, w} \right) \]

\[ \begin{aligned} \text{Then } P(x, y, w) &= P(x, y, z) J \left( \frac{x, y, z}{x, y, w} \right) \\ \Rightarrow I' &= \int P(x, y, w) \ln P(x, y, z) J \left( \frac{x, y, z}{uv, w} \right) dudvdw \\ &= \int P(x, y, w) \ln P(x, y, z) \left( \frac{x, y, z}{uv, w} \right) dvdw \\ &= \int P(x, y, z) \left( \frac{x, y, z}{uv} \right) \ln P(x, y, z) dvdw \\ &\quad + \int P(x, y, w) \ln J \left( \frac{x, y, z}{uv, w} \right) \frac{x, y, z}{uv, w} dvdw \\ &= \int P(x, y, z) \ln P(x, y, z) \left( \frac{x, y, w}{uv, w} \right) dvdw + \int P(x, y, z) \ln J \left( \frac{x, y, z}{uv, w}  \right) dvdw \end{aligned} \]

\[ I'' = I + \exp \left\{ \ln J \left( \frac{x, y, z}{uv, w} \middle| \right) \right\} \]

---

Singular Variate Changel 

\[
\begin{align*}
U &= U(x) & -1 \\
y &= y & \overline{U} = \begin{bmatrix}
\frac{\partial U}{\partial x} & \frac{\partial y}{\partial x} & \frac{\partial z}{\partial x} \\
\frac{\partial u}{\partial x} & \frac{\partial y}{\partial x} & \frac{\partial u}{\partial x} \\
\frac{\partial u}{\partial y} & \frac{\partial y}{\partial y} & \frac{\partial u}{\partial y} \\
\frac{\partial u}{\partial z} & \frac{\partial y}{\partial z} & \frac{\partial u}{\partial z} \\
\frac{\partial u}{\partial z} & \frac{\partial z}{\partial z} & \frac{\partial u}{\partial z}
\end{bmatrix} &= \begin{bmatrix}
\frac{\partial U}{\partial x} & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} \\
&= \frac{\partial U}{\partial x}
\end{align*}
\]

\[
\Rightarrow \overline{U} = \frac{du}{du}
\]

\[
\Rightarrow P(u, y, z) = \frac{dx}{du} P(x, y, z)
\]

\[
\text{Proof: } \int P'(u, y, z) du = \int \left( \frac{du}{du} \right) P(x, y, z) du = P(x, y)
\]

\[
\Rightarrow I_{Uyz} = I_{XYZ} + \exp\{\ln \frac{dx}{du}\} \\
\text{Similarly } I_{Uyx} = I_{XYZ} + \exp \ln \frac{dx}{du}
\]

\[
\Rightarrow C_{U;YZ} = I_{UYZ} - I_U - I_{YZ}
\]

\[
= I_{XYZ} + \exp \ln \frac{\partial}{\partial u} - I_X - \exp \ln \overline{U} - I_{YZ} \\
= C_{X;YZ}!
\]

\[
\text{Convolution } I_{UYZ}^t = I_{X'YZ}^t + I_{EXP}^t \{\ln \frac{dx}{du}\}
\]

---

\[
\begin{align*}
C_{UYZ} &= I_{UYZ} - I_{UY} - I_Z \\
&= I_{XYZ} + \exp \left( \frac{I_X - I_{X'}}{I_X} - \exp \left( \frac{I_X'}{I_X} \right) - I_Z \right) \\
&= C_{X'YZ}
\end{align*}
\]

More Generally 

\[
\{ \begin{array}{l} \tau \\ \forall V, WY, Z \end{array} \} = \begin{array}{c} \bullet \\ \bullet \end{array} \]

\[
I_{UVWYZ}^{\tau} - I_{UV}^{\tau} - I_{WY}^{\tau} - I_{Z}^{\tau}
\]

\[
= I_{X'VWYZ}^{\tau} + \exp \left( \frac{I_X' - I_{X'}}{I_X} - \exp \left( \frac{I_X}{I_X} \right) - I_{WY}^{\tau} - I_Z^{\tau} \right)
\]

\[
\{ \begin{array}{l} \tau \\ \forall V, \forall WY, Z \end{array} \} = \{ X'VWYZ, Z \}^{\tau}
\]

ie in the [ ] symbols any notion
variable may be replaced by any other
which is functionally dependent upon it.

In fact any Group (with comma)
can be replaced. 

General division theorem!

---

h-3.5 

Proof of position correlation invariance: 

Let joint distribution of particles \(y_1, y_2\) be 

\[P(\hat{y}_1, \hat{y}_2) = P(y_1, y_2 | \hat{y}_1, \hat{y}_2)\]

\[\Rightarrow \hat{y}_1 \hat{y}_2 = \hat{y}_1 \hat{y}_2 \quad \{\hat{y}_1, \hat{y}_2\} = \{\hat{y}_1 \hat{y}_2, \hat{y}_1 \hat{y}_2\}\]

\[= \{\hat{y}_1 \hat{y}_2 \hat{w}_1, \hat{y}_1 \hat{y}_2 \hat{w}_2\} \quad \text{by general invariance theorem.}\]

---

Some identities: 

\[
\text{Some } I_{uvwx} = I_{uv} + I_{wx} + \{uywx\}
\]

\[
\text{we have } \{uywx\} = I_{uvwx} - I_u - I_v - I_w - I_x
\]

\[
\text{let } I_{uvwx} = I_{uvw} + I_x + \{uywx\}
\]

\[
= I_{uv} + I_w + \{uyw\} + \{uvw\}x^2 + I_x
\]

\[
= I_u + I_v + I_w + I_x + \{uyw\} + \{uvw\}x^2 + \{uvw\}y
\]

\[
\text{Now } \{uywx, yz\} = \{uy\} + \{uyw\} + \{uvw\}x
\]

\[
\begin{align*}
& \{uy, wx, yz\} = I_{uvwx} - I_{uv} - I_{wx} - I_{yz} \\
& \{uy, wx, yz\} = I_{uvwx} - I_{uvw} - I_{wx} - I_{yz}
\end{align*}
\]

\[
\begin{align*}
& \text{Now } \{uy, wx, yz\} = \{uy\} + \{uyw\} + \{uvw\}x \\
& \text{introduces } \text{introduces} \text{introduces}
\end{align*}
\]

---

General Synthetic Rule 

\[
\begin{align*}
1) \quad \{\cdots \cup v \setminus w x \cdots \} \cdot \{\cdots \} &= \{\cdots \cup v \setminus w x \cdots \} \cdot \{\cdots + \{\cdots \cup v \setminus w x \cdots \} \\
&\quad \text{null for general of Gamma}
\end{align*}
\]

Give: 

General Commutation : 

\[
\{\cdots \cup v \setminus w x \cdots \} \cdot \{\cdots \} \\
= \{\cdots \cup v \setminus w x \cdots \} \cdot \{\cdots\} + \{\cdots \cup v \setminus w x \cdots \}
\]

\[
\begin{align*}
\{\cdots \cup v \setminus w x \cdots \} \cdot \{\cdots \}&= \{\cdots \cup v \setminus w x \cdots \} \cdot \{\{\cdots \cup v \setminus w x \cdots \} + \{\cup v \setminus w x \cdots \} \\
&= \{\cdots \cup v \setminus w x \cdots \} \cdot \{\{\cup v \setminus w x \cdots \} + \{\cup v \setminus w x\} \cdot \{\cup v \setminus w x \cdots \} \\
&= \{\cdots \cup \cup v \setminus w x \cdots \} \cdot \{\{\cup v \cdots \} + \{\cup v \setminus w x \cdots \} \cdot \{\cup v \setminus w x \cdots \} \\
&= \{\cdots v \setminus w x \cdots \} \cdot \{\{\cup v \setminus w \cdots \} + \{\cup v \setminus w x \cdots \} \cdot \{v \setminus w x \cdots \} \\
&= \{\cdots v \setminus w x \cdot \{\cup v \setminus w x \cdots \} \cdot \{\cup v \cdots \} \cdot \{\cup v \setminus w x \cdots \} \\
\end{align*}
\]

2) 

\[
\begin{align*}
3) \quad &= \{\cdots \cup v \setminus w x \cdots \} \cdot \{\cup v \setminus w \cdots \} \\
&= \{\cup v \setminus w x \cdots \} \cdot \{\cup v \cup w x \cdots \}
\end{align*}
\]

---

\[
\begin{align*}
\text{Now } \{v, wx\} - \{vwx\} &= \{vwx\} \\
&= I_x w x - I_x - I_x w x - I_x w x + I_x w + I_x \\
&= -I_x \\
&= \{v, wx\} + \{vwx\} - \{v, wx\} \\
&\neq \{vwx\} - \{v, wx\}
\end{align*}
\]

\[
\begin{align*}
\text{Therefore from 3 } \{v, wxywxyz\} - \{v, wxyyz\} \\
&= \{v, wxywxyz\} - \{v, wxyyz\} \\
\text{using 4 } \\
&= \{v, wxywxyz\} - \{wxyyz\} - \{v, wxywxyz\} + \{v, wxywxyz\} \\
&= \{v, wxywxyz\} - \{wxyyz\}
\end{align*}
\]

---

Therefore General Commutation rule 3 

\[
\begin{align*}
& \{\cdots, \underline{v} \underline{v} \underline{v} \underline{v} \underline{v} \underline{v}, \underline{v}, \underline{v}, \underline{v}, \underline{v}, \underline{v} \underline{v}, \underline{v}, \underline{v}, \underline{v} \underline{v} \underline{v}, \underline{v}, \underline{v} \underline{v} \underline{v} \underline{v}, \underline{v} \underline{v} \underline{v} \underline{v} \underline{v}\} \\
& = \{\underline{v} \underline{v} \underline{v} \underline{v} \underline{v} - \{\underline{v} \underline{v} \underline{v} \underline{v} \underline{w} \underline{w} \underline{w} \underline{w} \underline{w} \underline{v} \underline{v} \underline{v} \underline{v} \underline{w} \\
& \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \underline{w} \underline{w} \underline{w} \underline{w} \underline{w}\} \\
& = \{\underline{v} \underline{v} \underline{v} \overline{w} \underline{w} \underline{w} \underline{w} \underline{w} \overline{w} \underline{w} \underline{w} \underline{w} \underline{v} \overline{w} \underline{w} \underline{w} \underline{v} \underline{w} \underline{w} \underline{w} \underline{v} \underline{w} \overline{w} \underline{w} \underline{w} \underline{v} \underline{v} \overline{w} \underline{w} \underline{v} \underline{w} \underline{w} \overline{w} \underline{w} \underline{v} \underline{w} \underline{v} \underline{w} \underline{w} \underline{v} \underline{w} \underline{v} \overline{w} \underline{w} \underline{v} \underline{v} \underline{w} \underline{w} \underline{v} \underline{v} \underline{w} \overline{w} \underline{w} \underline{v} \underline{v} \underline{v} \overline{w} \underline{w} \\
& = \{\underline{v} \underline{v} \underline{v} \underline{w} \underline{w} - \{\underline{v} \underline{v} \underline{w} \underline{w} \underline{w} - \{\underline{v} \underline{v} - \{\underline{v} \underline{v} \underline{w} \underline{w} - \{\underline{w} \underline{w} \underline{w} \underline{w} - \{\underline{w} \underline{w} - \{\underline{w} \underline{w} \underline{v} \underline{w} - \{\underline{w} \underline{w} \underline{w} - \{\underline{w} \underline{v} \underline{w} \underline{w} - \{\underline{w} - \{\underline{w} \underline{w} \underline{w} - \underline{w} \underline{w} \underline{w} - \{\underline{w} \overline{w} \underline{w} \underline{w} - \{\underline{w} \underline{w}\} \\
& = \{\underline{v} \underline{v}, \underline{w} \underline{w} \underline{w} \underline{w} - \{\underline{v} - \{\underline{w} \underline{w} \underline{w} \underline{w} \underline{w} - \{\overline{w} \underline{w} \underline{w} \underline{w} \underline{w} - \{w\} \underline{w} \underline{w} \underline{w} \underline{w} - \{\{w\} \underline{w} \underline{w} \underline{w} \underline{w} - \{w\}
\end{align*}
\]

Proof: 

\[
\begin{align*}
& \{\cdots, \underline{v} \underline{w} \underline{w} \underline{w} \underline{w}, \underline{v}, \underline{v}, \underline{v}, \underline{v}, \underline{w}, \underline{w}, \underline{w}, \underline{w}, \underline{w}, \underline{v}, \underline{v}, \underline{v}, \underline{v} \underline{w}, \underline{v}, \underline{v}, \underline{v}, \underline{w}, \underline{v}, \underline{w}, \underline{w}, \underline{w}, \underline{v}, \underline{w}, \underline{w}, \underline{v}, \underline{w}, \underline{v}, \underline{w}, \underline{v}, \underline{v}, \underline{w}, \underline{w}, \underline{v}, \underline{v}, \underline{w}, \underline{v}, \underline{v}, \underline{v}, \underline{w} \underline{w}, \underline{w}, \underline{w}, \underline{w}, \underline{w} \underline{w}, \underline{w}, \underline{w}, \underline{v}, \underline{w} \underline{w}, \underline{w}, \underline{v}, \underline{w}, \underline{w} \underline{w}, \underline{w}, \underline{v}, \underline{v}, \underline{w} \underline{w}, \underline{v}, \underline{w}, \underline{w}, \underline{w} \underline{w}, \underline{v}, \underline{w}, \underline{v}, \underline{w} \underline{w}, \underline{v}, \underline{v}, \underline{w}, \underline{w} \underline{w}, \underline{v}, \underline{v}, \underline{v} \underline{w}, \underline{w}, \underline{w}, \underline{w}, \underline{v} \underline{w}, \underline{w}, \underline{w}, \underline{v}, \underline{v} \underline{w}, \underline{w}, \underline{v}, \underline{w}, \underline{v} \underline{w}, \underline{w}, \underline{v}, \underline{v}, \underline{v} \underline{w} \underline{w}, \underline{w}, \underline{w}, \underline{w} \underline{w} \underline{w}, \underline{w}, \underline{w}, \underline{v} \underline{w} \underline{w}, \underline{w}, \underline{v}, \underline{w} \underline{w} \underline{w}, \underline{w}, \underline{v}, \underline{v} \underline{w} \underline{w}, \underline{v}, \underline{w}, \underline{w} \underline{w} \underline{w}, \underline{v}, \underline{w}, \underline{v} \underline{w} \underline{w}, \underline{v}, \underline{v}, \underline{w} \underline{w} \underline{w}, \underline{v}, \underline{v} \underline{w} \underline{w} \underline{w}, \underline{v}, \underline{w} \underline{w} \underline{w} \underline{w}, \underline{v} \underline{w} \underline{w} \underline{w} \underline{w}
\end{align*}
\]

in fact, under this condition 

Another degenerate case: \(\{x, y\}\) 

\[
\begin{align*}
P^x(x, y) &= P^x(y) \delta(x - y) \\
P^x(y) &\text{conjugate } I^x_y
\end{align*}
\]

\[
\begin{align*}
& \{\cdots, \underline{w} \underline{w} \underline{w} \underline{w} \underline{w}, \underline{w}, \underline{w} \underline{w} \underline{w} \underline{w} \underline{w},
\end{align*}
\]

---

\[ \text{Data} \quad \{v, w, x\} = I_{uvwx} - I_u - I_{vw} - I_x \]

\[ = \int P(vw, wx) \ln P(vw) dvdwdx \]

\[ - \int P(vw, wx) \ln P(u) dvdwdx \]

\[ - \int P(vw, wx) \ln P(y, w) dvdwdx \]

\[ - \int P(vw, wx) \ln P(x) dvdwdx \]

\[ = \int P(vw, wx) \ln \frac{P(vw, x)}{P(u) P(y, w) P(x)} dvdwdx \]

\[ = \exp \{ \ln \frac{P(vw, wx)}{P(u) P(y, w) P(x)} \} \]

\[ \{v, w, x\}^{st} = \int_{P_{vwx}}^{P_{vwx}} \ln \frac{P_{vwx}^{st}}{P_{vwx}^{st}} \frac{dvdwdx}{P_{vwx}^{st}} \]

\[ = \exp \{ \ln \frac{P_{vwx}^{st}(vwx)}{P_{vwx}^{st}P_{vwx}^{st}} \} \]

\[ \text{Note:} \{v, w, x\}^{sw'} = \exp \{ \ln \frac{P_{vwx}^{sw'}(vwx)}{P_{vwx}^{sw'}P_{vwx}^{sw'}} \} \]

\[ \text{but } P_{vwx}^{sw'} = P_{vwx}^{sw'}(w'-w) \]

\[ P_{vwx}^{sw'} = P_{vwx}^{sw'} \delta(w'-w) \]

---

**Definir**

\[
\{v,vw,x\}^{sw'}=\exp\left\{\ln\frac{p^{sw'}(vx)\delta(wx)}{p^{sw'}(v)\delta(wx)p^{sw'}(v)p^{sw'}(x)}\right\}
\]

\[
= \exp\left\{\ln\frac{p^{sw'}(vx)\delta(vx)}{p^{sw'}(v)p^{sw'}(v)p^{sw'}(x)}\right\}
\]

\[
= \{y,yx\}^{sw'}
\]

Putting condition of variable
in bracket on its variable in bracket 

\[
\text{incard alone} = \{y, wx\}^{sw'} = \exp\left\{\ln\frac{p^{sw'}(vx)\delta(wx)}{p^{s'}(v)p^{sw'}(x)\delta(wx)}\right\}
\]

\[
= \{y,x\}^{sw'}
\]

\[
\text{now} \quad \text{would about } \{y,wx\}^{sw'} = \exp\left\{\ln\frac{p^{sw'}(vx)\frac{\delta(wx)}{p^{sw'}(v)\delta(wx)}}{p^{sw'}(v)\frac{\delta(wx)}{p^{sw'}(v)}}\right\}
\]

\[
\begin{align*}
\text{Therefore } C_{y,w}^{sw} &= 0 \quad \text{define} \\
&\text{is define } [u] = 0 \quad \text{(bracket of only one variable)} \\
&= [u, y] = I_{u,y} - I_{u} - I_{y} \\
&\text{for empty set define } I_{y} = 0 \quad \text{else } I_{y} = I_{u}
\end{align*}
\]

---

no define \(\{uv\} = 0\) (ie normal) 

\[
\begin{align*}
\text{then } \{u, v, w\} & \xrightarrow{su'} = \{u, v, x\} \\
\text{also } \{u, v, w\} & \xrightarrow{su'} = \{u, w\} \\
\text{but then } \{u, w\} & \xrightarrow{su'} = \{u\} \\
\text{almost } \{u, w\} & = \emptyset
\end{align*}
\]

\[
\begin{align*}
\{u, v, w\} & = \{u, v, w\} \xrightarrow{su} \{u, w\} + \{u, w\} \\
&= \{u, v, w\} + \{u, w\} + \{u, w\} \\
&= \{u, v, w, w\} + \{u, w\} + \{u, w\} \\
&= \{u v, w\} + \{u, w\} + \{u, w\} \\
&= \{v, w\} + \{u, w\} + \{u, w\} \\
&= \{v w\} + \{u, w\} + \{u, w\} \\
&= \{v, u\} + \{u, w\} + \{u, w\} \\
&= \{v, u, w\} + \{u, w\} + \{u, w\} \\
&= \{v u\} + \{u, w\} + \{u, w\} \\
&= \{v u\} \\
&= \{v, u\} \\
&= \{v, u\} \\
&= \{v, u\} \\
&= \{u, v\} \\
&= \{u, v\} \\
&= \{u, v\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{v\} \\
&= \{v\} \\
&= \{v\} \\
&= \{v\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{w\} \\
&= \{w\} \\
&= \{w\} \\
&= \{w\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{x\} \\
&= \{x\} \\
&= \{x\} \\
&= \{x\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{y\} \\
&= \{y\} \\
&= \{y\} \\
&= \{y\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{z\} \\
&= \{z\} \\
&= \{z\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{a\} \\
&= \{a\} \\
&= \{a\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{b\} \\
&= \{b\} \\
&= \{b\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{c\} \\
&= \{c\} \\
&= \{c\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{d\} \\
&= \{d\} \\
&= \{d\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{e\} \\
&= \{e\} \\
&= \{e\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{f\} \\
&= \{f\} \\
&= \{f\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{g\} \\
&= \{g\} \\
&= \{g\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{h\} \\
&= \{h\} \\
&= \{h\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{i\} \\
&= \{i\} \\
&= \{i\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{j\} \\
&= \{j\} \\
&= \{j\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{k\} \\
&= \{k\} \\
&= \{k\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{l\} \\
&= \{l\} \\
&= \{l\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{m\} \\
&= \{m\} \\
&= \{m\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{n\} \\
&= \{n\} \\
&= \{n\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{o\} \\
&= \{o\} \\
&= \{o\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{p\} \\
&= \{p\} \\
&= \{p\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{q\} \\
&= \{q\} \\
&= \{q\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{r\} \\
&= \{r\} \\
&= \{r\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{s\} \\
&= \{s\} \\
&= \{s\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{t\} \\
&= \{t\} \\
&= \{t\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{U\} \\
&= \{U\} \\
&= \{U\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{V\} \\
&= \{V\} \\
&= \{V\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{W\} \\
&= \{W\} \\
&= \{W\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{X\} \\
&= \{X\} \\
&= \{X\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{Y\} \\
&= \{Y\} \\
&= \{Y\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{Z\} \\
&= \{Z\} \\
&= \{Z\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{A\} \\
&= \{A\} \\
&= \{A\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{B\} \\
&= \{B\} \\
&= \{B\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{C\} \\
&= \{C\} \\
&= \{C\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{D\} \\
&= \{D\} \\
&= \{D\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{E\} \\
&= \{E\} \\
&= \{E\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{F\} \\
&= \{F\} \\
&= \{F\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{G\} \\
&= \{G\} \\
&= \{G\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{H\} \\
&= \{H\} \\
&= \{H\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{I\} \\
&= \{I\} \\
&= \{I\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{J\} \\
&= \{J\} \\
&= \{J\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{K\} \\
&= \{K\} \\
&= \{K\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{L\} \\
&= \{L\} \\
&= \{L\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{M\} \\
&= \{M\} \\
&= \{M\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{N\} \\
&= \{N\} \\
&= \{N\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{O\} \\
&= \{O\} \\
&= \{O\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{P\} \\
&= \{P\} \\
&= \{P\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{Q\} \\
&= \{Q\} \\
&= \{Q\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{R\} \\
&= \{R\} \\
&= \{R\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{S\} \\
&= \{S\} \\
&= \{S\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{T\} \\
&= \{T\} \\
&= \{T\} \\
&= \{u\} \\
&= \{u\} \\
&= \{u\} \\
&= \{

---

\[
\begin{array}{r@{\;}c@{\;}l}
\text{convolution} & \{x,y,z\} & = \{x,y,z\} \\
& = \{x,y,z\} - \{y,z\} & \\
& & \text{convolution} \\
& & \text{non-shift} \\
\end{array}
\]

Also as check of continuity of common transform
and shift of \(\{u\}\) = 0 

\[
\{u, v\} = \{u v\} + \{u\} v \quad \Rightarrow \quad \{u v\} = 0 \\
\text{and} \quad \text{shift of } \{u\} = 0
\]

functional transformation across a domain:
convolution \(X Y \to V W\) 

\[
\begin{align*}
\{ \dots, u, v, w, z, \dots \} &= \{ \dots, uvw, z, \dots \} + \{ vw, z \} \\
&= \{ \dots, uxy, z, \dots \} + \{ vw, z \} \\
&\quad + \{ vw, z \} \\
&= \{ \dots, uxy, z, z \dots \} + \{ y, z \} - \{ ux, y, z \} + \{ ux, y, z \} \\
&\quad - \{ w, z \} + \{ v, w \} - \{ v, w \} \\
&\quad - \{ w, z \} + \{ v, w \} + \{ v, w \} - \{ x, y \}
\end{align*}
\]

\[
\begin{align*}
L &= \{ u, y, z \} + \{ u, y, z \} + \{ u, y, z \} - \{ x, y, z \} \\
&= \{ \dots, ux, y, z \dots \} + \{ y, z \} + \{ u, y, z \} - \{ x, y \} \\
&= \{ \dots, ux, y, z \dots \} + \{\dots, y, z \} + \{ u, y, z \} - \{ x, u, y \}
\end{align*}
\]