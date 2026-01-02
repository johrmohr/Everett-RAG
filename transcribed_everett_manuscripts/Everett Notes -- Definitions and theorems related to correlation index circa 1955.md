# Everett Notes -- Definitions and theorems related to correlation index circa 1955.pdf

most useful formula 

< 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

14 

15 

16 

17 

18 

19 

20 

21 

22 

23 

24 

25 

26 

27 

28 

29 

30 

31 

32 

33 

34 

35 

36 

37 

38 

39 

40 

41 

42 

43 

44 

45 

46 

47 

48 

49 

50 

51 

52 

53 

54 

55 

56 

57 

58 

59 

60 

61 

62 

63 

64 

65 

66 

67 

68 

69 

70 

71 

72 

73 

74 

75 

76 

77 

78 

79 

80 

81 

82 

83 

84 

85 

86 

87 

88 

89 

90 

91 

92 

93 

94 

95 

96 

97 

98 

99 

100 

101 

102 

103 

104 

105 

106 

107 

108 

109 

110 

111 

112 

113 

114 

115 

116 

117 

118 

119 

120 

121 

122 

123 

124 

125 

126 

127 

128 

129 

130 

131 

132 

133 

134 

135 

136 

137 

138 

139 

140 

141 

142 

143 

144 

145 

146 

147 

148 

149 

150 

151 

152 

153 

154 

155 

156 

157 

158 

159 

160 

161 

162 

163 

164 

165 

166 

167 

168 

169 

170 

171 

172 

173 

174 

175 

176 

177 

178 

179 

180 

181 

182 

183 

184 

185 

186 

187 

<tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td><td></td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td colspan="2"></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td><td></td><td></td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

---

Def: Partial Correlation 

\[I_{\alpha, \beta}^{(r, s)} = \sum_{\alpha, \beta} p_{\alpha, \beta}^{r, s} \ln p_{\alpha, \beta}^{r, s}\]

\[conventionalCorrelation \quad C_{\alpha, \beta}^{(u, v)} = I_{\alpha, \beta}^{(u, v)} - I_{\alpha, \beta}^{(u, v)} - I_{\alpha, \beta}^{(v, s)} - I_{\alpha, \beta}^{(v, s)}\]

\[allendsform \quad I_{\alpha, \beta}^{(r, s)} = \frac{1}{p_{\alpha, \beta}} \sum_{\alpha, \beta} p_{\alpha, \beta}^{r, s} p_{\alpha, \beta}^{r, s} \ln p_{\alpha, \alpha, \beta}^{r, s} - \ln p_{\alpha, \beta}^{r, s}\]

---

\[P_{\alpha \dots \beta} I_{\alpha \dots \beta}^{\alpha \dots \beta} = \sum_{\alpha \dots \beta} P_{\alpha \dots \beta \alpha \dots \beta} \ln P_{\alpha \dots \beta \alpha \dots \beta} - P_{\alpha \dots \beta} \ln P_{\alpha \dots \beta}\]

\[\sum_{\gamma \dots \delta} P_{\gamma \dots \delta} I_{\alpha \dots \beta}^{\gamma \dots \delta} = I_{\alpha \dots \beta \gamma \dots \delta} - I_{\gamma \dots \delta} \quad (not: NOT I_{\alpha \dots \beta})\]

\[\Rightarrow \sum_{\alpha \dots \beta} P_{\alpha \dots \beta} C_{\alpha \dots \beta \gamma \dots \delta}^{\alpha \dots \beta} = I_{\alpha \dots \beta \gamma \dots \delta \alpha \dots \beta} + I_{\alpha \dots \beta \gamma \dots \delta} - I_{\gamma \delta \alpha \dots \beta}\]

which is not \(C_{\alpha \dots \beta \gamma \dots \delta}\) 

\[ \sum_{\alpha \dots \beta} P_{\alpha \dots \beta} C_{\gamma \dots \beta \gamma \dots \delta}^{\alpha \dots \beta} = C_{\alpha \dots \beta \gamma \dots \delta \alpha \dots \beta} - C_{\gamma \dots \beta \gamma \dots \delta} - C_{\gamma \dots \beta \gamma \dots \delta} \]

\[ \text{Charnelle: } I_{\alpha \gamma \delta} = I_{\alpha} + I_{\beta} + I_{\gamma} + I_{\delta} + C_{\alpha \gamma \delta} + C_{\beta \gamma \delta} + C_{\gamma \delta} \]

\[ W_{\text{commutator}} = C_{\alpha \beta} - C_{\alpha \beta} = C_{\alpha \beta} - C_{\beta \gamma} \]

---

Expected cost: corr. 

\[
\Rightarrow \sum_{a, \nu} P_{a, \nu} C_{\alpha, \beta; \nu}^{\alpha, \nu} = C_{\alpha, \beta; \nu} + C_{\alpha, \beta; \nu} u_{\alpha, \nu} - C_{\alpha, \beta; \nu} u_{\alpha, \nu} - C_{j, \beta; \nu} u_{\alpha, \nu}
\]

Basic theorem for expected cost information 

\[
U \left( \sum_{a, \nu} P_{a, \nu} I_{\alpha, \beta}^{\alpha, \nu} \right) = I_{\alpha, \beta} + C_{\alpha, \beta; \nu} u_{\alpha, \nu}
\]

Example: Correlation of portion of proton + electron in 

hydrogen atom, confined to box 1 cm³, (gnd state) is: 

\[
V \left( \text{(electron position, proton position)} \approx 55 \text{ fine} \right) \quad (\text{force bite})
\]

Dependence of Information of continuous distribution on
scale: if \(P(x)\) is beta, \(I = \int P(x) dx\) 

and scale changed \(x = kx'\) 

\[
I' = I + \ln K
\]

(so that differences are invariant.) 

Correlation indices imply of scale!)

---

Conversion, Bins to Bits (Bins unit = 1 bit) 

\[1 \, \text{bin} = 1.44 \, \text{bits}\]

\[1 \, \text{bin} \times 10 \, \text{Information} = 2.30 \, \text{bits} = 3.31 \, \text{bits} \, (\text{big})\]

Useful Inequality: #1 \(k \ln x \geq x - 1\) for \(x \geq 0\) equal \(x = 1\) 

Time Derivative: \(\dot{I}_{\alpha, \beta, \gamma} = \sum_{\alpha, \beta, \gamma} \dot{P}_{\alpha, \beta, \gamma} \ln P_{\alpha, \beta, \gamma}\) 

\[\dot{C}_{\alpha, \beta, \gamma, S} = \sum_{\alpha, \beta, S} \dot{P}_{\alpha, \beta, S} \ln \left( \frac{P_{\alpha, \beta, S}}{P_{\alpha, \beta, S}} \right)\]

---

Proj operation : 

\[U_t = \Phi_t(\Phi_t) = P[\Phi_t]\]

dim : \(\Delta U_t U_t = U_t\) 

\(\Delta U_t\) is Hermitian 

\(\Delta \text{Proj}(\Phi_t / \tau) = (\Psi_t \Psi_t) = (\Psi_t \Psi_t)\) 

\(\Delta \frac{\partial}{\partial t} U_t = \frac{1}{i\hbar} [H, U_t]\) (due to time change of \(\Phi_t\), (only)) 

Non-perturbative time-dip :

\[\hat{P} = P \frac{d}{dt} \ln P\]

\[\Rightarrow \hat{P} \ln P = P \ln P \frac{d}{dt} \ln P = P \frac{d}{dt} \frac{1}{2} (\ln P)^2 \\ \text{on } \hat{f} = \text{Expt.} (\frac{d}{dt} \ln P)^2\]

For two density \(\rho\) \(\Delta T = \int \rho Q \left[ \frac{\ln P}{Q} - \frac{\ln Q}{P} \right] dx\) 

Information in Normal density Variance \(\Gamma^2\) :

\[\Gamma_{nV} = -h\nu \Gamma - h\nu \sqrt{2n\epsilon} = \frac{(h\nu \sqrt{2n\epsilon})^2}{h\nu \sqrt{2n\epsilon}} \sim 1.42 \quad (thin) \quad \Gamma_{nV} \sim h\nu \Gamma - 1.42 \quad (thin)\]

Zero information point for normal : \(\Gamma^2 = \frac{1}{2\pi\epsilon} \sim 0.585\) 

\[1 \quad \text{For Uniform : Uniform density over unit interval has Zero uniform. (tan a refl of uniform scale) (all info not to this.)}\]

Uniform of Uniform density : \(\Gamma = h\nu \frac{1}{a} = -h\nu a\)

---

Minimum Uniform Distribution's Inequality 

For distribution, constrained to interval uniform occurs for Uniform distribution, hence: 

\[
\begin{align*}
I &\ge - \ln a \quad \text{for every distribution which is non-zero only over interval of length a (in fact if nonzero one any set of measure } a, \text{ since invariant to chuyening)}
\end{align*}
\]

For distribution of Centralized Variance: (V²) 

\[
V \geq - \ln \left( \sqrt{2 \pi e} \right) = - \ln \sqrt{e} - \ln \sqrt{2 \pi e}
\]

(equality only for normal) 

(Original usage: uniform) 

Unit change of uniform, occurs when Distribution
realized to one e at of original length for
uniform distribution, or becomes one e-th of
original for Normal distribution ( \(\frac{1}{e} \approx 3.68\) )

---

Vague Theorem: Any equalizing operation on a
distinct increase \(H\), i.e 

\[
\begin{align*}
\text{if } P_i = \sum e_{ij} P_j \quad \text{where } \sum a_{ij} = \sum a_{ij} = 1 \\
\text{and } a_{ij} \ge 0 \\
\text{(strong selection)} \\
H' \ge H \quad \text{equality only for permutation!}
\end{align*}
\]

Shannon introduces Groth Entropy 

\[
H_2(g) = \sum_{i,j} P_{ij} \log P_{ij}(g)

\]

\[
P_i(g) = \frac{P_{ij}}{\sum_j P_{ij}}
\]

\[
\text{Show that } H(g, y) = H(a) + H_c(y) \quad \text{(inherently)}
\]

Check effect on
productivity 

\[
\text{is expected } H = \text{the Hofstadter system.}
\]

---

Averaging Process 

\[P'(y) = \int a(x, y) P(x) dx\]

with \(\int a(xy) dx = \int a(xy) dy = 1\) 

merges H (on some) 

try to prove

---

Important inequalities : 

\[
\begin{align*}
1) \quad C_{u \times \beta} \equiv C_{u \times \beta} \quad \text{(proof of (10) to (12))} \\
2) \quad C_{u \times \beta} \equiv C_{u \times \alpha} + C_{u \beta} - C_{u \beta} \quad \text{check these!}
\end{align*}
\]

\[
\begin{align*}
C_{u \times \beta} \equiv C_{u \times \alpha} + C_{\alpha \beta} - C_{\alpha \beta} \quad \text{OK} \\
x \quad y \quad z
\end{align*}
\]

Ideal formula: (Explicit by cond proof) 

\[
\sum_{\alpha \in \mathcal{A}} p_{\alpha} \ln p_{\alpha}^{\infty} = \sum_{\alpha} p_{\alpha} I_{\alpha}^{\infty} = I_{\alpha} + c_{\alpha \beta} p_{\alpha}
\]

Simple Conditional Formula: \(p_{\alpha}^{\gamma} = \sum_{\beta} p_{\alpha}^{\gamma} p_{\beta}^{\gamma}\) 

Resultant Relation for discrete density 

\[
\begin{align*}
I_{\alpha} \equiv I_{\alpha \beta} \quad \text{//} \\
\text{all } C_{\alpha \beta} \supset I_{\alpha \beta} \equiv I_{\alpha} \equiv I_{\alpha \beta} \\
\Rightarrow -I_{\alpha} \equiv I_{\alpha} - I_{\alpha \beta} \equiv 0 \\
\text{or } I_{\alpha} \equiv I_{\alpha} - I_{\alpha} \equiv 0
\end{align*}
\]

Condition for Convex (see (25))

---

A Basic inequality (B1) 

\[
\begin{align*}
(\sum_{i} x_i) \ln \left( \frac{\sum_{i} x_i}{\sum_{i} x_i} \right) \le \sum_{i} x_i (x_i \ln x_i) \\
\text{for all } x_i \ge 0
\end{align*}
\]

Let Introduce \(Q_{\alpha, \beta, \omega}\) \(S\) 

\[
V_{\alpha, \beta, \omega} P_{\alpha, \beta, \omega} = Q_{\alpha, \beta, \omega} P_{\alpha, \beta, \omega} P_{\alpha, \beta, \omega}
\]

① all \(Q'\)'s \(\ge\) 0
(measure of height from independence.) 

② have property that any collection gives only one 

any Single Controllor is \(\sum_{i} p_i Q_{i\alpha} = 1\) 

③ \(C_{\alpha, \beta} = \sum_{i} p_i P_{\alpha, \beta} Q_{i\alpha} \ln Q_{i\alpha}\) 

④ General Controllor: 

\[
\sum_{j} p_{j} Q_{j\alpha} = Q_{j\alpha} \quad (\text{see } BIS \text{ and block})
\]

---

\[
\frac{\text{Conditional Prob.}}{\text{Prob.}} = \frac{P_{u|v}}{Q_{u|v}} = \frac{Q_{u|v} \cdot P_{u|v}}{Q_{u|v}} = Q_{u|v} \cdot \frac{P_{u|v}}{Q_{u|v}} = Q_{u|v} \frac{P_{u|v}}{Q_{u|v}} = Q_{u| v} \cdot \frac{P_{u|v}}{Q_{u|v}} = Q_{\alpha \beta} \cdot \frac{P_{u|v}}{Q_{u|v}} = Q \cdot \frac{P_{u|v}}{Q_{u|v}} = Q \frac{P_{u|v}}{Q_{u|v}} = Q \cdot \left( \frac{P_{u|v}}{Q_{u|v}} \right) = Q \cdot \left( \frac{P_{u|v}}{Q_{u| v}} \right) = Q \cdot \left( \frac{P_{u|v}}{P_{u|v}} \right) = Q \cdot \left( \frac{P_{v|v}}{P_{u|v}} \right) = Q \cdot \left( 1 - \frac{P_{u|v}}{P_{u|v}} \right) = Q
\]

\[
\text{when by definition} \quad Q_{\alpha \beta}^{u|v} = \frac{Q_{\alpha \beta|u|v}}{Q_{u|v}} \sqrt{(\frac{\beta - 1}{6})}
\]

\[
\text{note } Q_{\alpha} = 1 \text{ and } Q_{\alpha}^{u|v} \neq 1 \text{ necessarily}
\]

\[
\begin{align*}
u \dots y \\
\alpha \dots \beta &= \sum_{\alpha \le \beta} P_{\alpha \dots \beta} Q_{\alpha \dots \beta}^{u \dots y} \ln Q_{\alpha \dots \beta}^{u \dots y} + \sum_{\alpha \le \beta} Q_{\alpha \dots \beta}^{u \dots y} \ln P_{\alpha \dots \beta} + \dots + \sum_{\beta} Q_{\alpha \dots \beta}^{u \dots y} \ln P_{\beta} \\
C_{\alpha \dots \beta}^{u \dots y} &= \sum_{\alpha \le \beta} P_{\alpha \dots \beta} P_{\alpha \dots \beta} Q_{\alpha \dots \beta}^{ u \dots y} \ln \left( \frac{Q_{\alpha \dots \beta}^{u \dots y}}{Q_{\alpha \dots \beta}^{u \dots y}} \right) \\
&= \sum_{\alpha \le \beta} P_{\alpha \dots \beta} P_{\beta \dots \beta} Q_{\alpha \dots \beta}^{u \dots y} \left( \frac{Q_{\alpha \dots \beta}^{u \dots y}}{Q_{u \dots \beta}^{u \dots y}} \right)
\end{align*}
\]

\[
\text{Equality: } C_{\alpha \beta} \equiv \sum_{\alpha \le \beta} P_{\alpha \beta} Q_{\alpha \beta}^{u \dots y} \ln Q_{\alpha \beta}^{u \dots y} \quad (B-1)
\]

\[
\frac{\partial C_{\alpha \beta}}{\partial Q_{123}} = P_1 P_2 P_3 \left[ 1 + \ln Q_{12} \right] \quad (B-2)
\]

---

## Fourier Transform Relations: 

\[ \mathcal{D}(k) = \int_{-\infty}^{\infty} e^{-ikx} \psi(x) dx = \int_{-\infty}^{\infty} e^{ikx} \psi(-x) dx \]

\[ \mathcal{D}(-k) = \int_{-\infty}^{\infty} e^{ikx} \psi(x) dx = \int_{-\infty}^{\infty} e^{-ikx} \psi(-x) dx \]

\[ \mathcal{D}_{\text{even}} \rightarrow \mathcal{D}_{\text{even}} \quad \mathcal{D}_{\text{odd}} \rightarrow \mathcal{D}_{\text{odd}} \]

\[ \mathcal{D}_{\text{real}} \rightarrow \mathcal{D}^{(k)}(k) = \mathcal{D}(-k) \quad \text{(even)} \]

\[ \mathcal{D}_{\text{imag}} \rightarrow \mathcal{D}^{(k)}(k) = -\mathcal{D}(-k) \quad \text{(imaginary)} \]

**Theorem:** \(\mathcal{D}_{\text{real}} \rightarrow \mathcal{D}_{\text{real}}\) \(\Rightarrow\) \(\mathcal{D}_{\text{real}} \rightarrow \mathcal{D}_{\text{imag}}\) \(\Rightarrow\) Variation of \(I_x + I_k\) 

Vanishs for no phase factor (convolve part) 

to that in the of phase shifts delays it in this case. (end of C) 

Effect of expansion of scale: (on Fourier transform) 

\[ \text{let } \mathcal{U}_a(x) = \mathcal{J}_a \mathcal{Y}(ax) \quad \text{(a represents translation)} \]

\[ \Rightarrow \mathcal{I}_{ax} = \mathcal{I}_x + \ln a \]

\[ \Rightarrow \mathcal{I}_k^a = \mathcal{I}_k + \ln \frac{1}{a} \quad \text{where } \mathcal{I}_k = \int_0^\infty e^{-ikx} \mathcal{Y}(x) dx \]

\[ \Rightarrow \mathcal{I}_{ax} + \mathcal{I}_k^a = \mathcal{I}_x + \mathcal{I}_k = \text{const} \]

(undocumented change) 

\[ \text{Effect of translation: } \mathcal{Y}_a = \mathcal{Y}(x+a) \]

\[ \Rightarrow \mathcal{D}_a e^{-ikx} \mathcal{Y}(k) = e^{ikx} \mathcal{D}(k) \]

---

**Density:** \(g_n(x) \geq 0\). 

\[V \Rightarrow \int_{-\infty}^{\infty} \left( \sum_{n} g_n \right) h_n \left( \sum_{n} g_n \right) dx \leq \sum_{n} \int_{-\infty}^{\infty} g_n h_n g_n dx + \sum_{n} \int_{-\infty}^{\infty} g_n^2 dx\]

Section E