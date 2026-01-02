# Everett Draft -- III Quantum mechanics of composite systems circa 1956.pdf

III. Quantum mechanics of composite systems 

Information of Quantum system 

In this section we shall assume that states of a physical system S are represented by points \(\psi\) in a Hilbert space. We shall be concerned with linear operators, A, and their expectation \(\langle A \rangle_{\psi}\) with respect to states functions \(\psi\) which are defined by the: 

\[ \langle A \rangle_{\psi} = \langle \psi, A \psi \rangle \]

where we shall be particularly interested in projection operators \(P_{\psi}\). We shall want to discuss information and correlation for operators \(A, B, \ldots\) with respect to a state function \(\psi\), which these quantities are to be computed from the square amplitudes of the projection of \(\psi\) onto the eigenstates of the operators \(A, B, \ldots\) regarded as probability distributions over the eigenvalues, through the formulae of the preceding chapter. For example, let \(A\) be an operator with a discrete, non-degenerate spectrum, and with eigenstates \(\psi\). Then we define the information about \(A\) with respect to the state function \(\psi\) by the 

\[ I_A(\psi) = \sum_i \langle P_{\psi} | A | \psi \rangle \ln \langle P_{\psi} | \psi \rangle \]

Note that we have used the uniform measure for the definition of information. Therefore, if we expand \(\psi\) in terms of the eigenstates of \(A\), \(\psi = \sum_i a_i \phi_i\), we have that: 

\[ I_A(\psi) = \sum_i a_i^* a_i \ln a_i^* a_i^* \]

---

Furthermore, this information is not so much a property of the operator A as a list of the complete orthonormal set which forms the eigenstates of A, i.e. it is the name for all non degenerate operators which have the same eigenstates (but possibly different eigenvalues) which reflect the independence of information of numerical values. 

In the case of degenerate operators it will be convenient to take the definition of the information as the information of the square amplitude distribution over the eigenvalues, relative to the information measure which consists of the multiplicity of the eigenvalues rather than the uniform measure over the eigenvalues, reflecting the choice of uniform measure over the eigenstates. Thus if \(F_{ij}\) (from 1 to \(m_i\)) are a complete orthonormal set of eigenstates for A, with distinct eigenvalues \(d_i\) (denote with respect to \(j\)) the multiplicity of this i-th eigenvalue is \(m_i\), and the information is defined: 

\[I_A(\psi) = \sum_i \left( \sum_j \left( P_{\psi} \right)_{ij} \ln \left( \frac{\left( \sum_j \left( P_{\psi} \right)_{ij} \psi \right)}{m_i} \right) \right)\]

The usefulness of this definition lies in the fact that any operator A which distinguishes further between any of the degenerate states leads to a refinement of the relative density in the range of them, and consequently, greater information. A non degenerate operator thus represents the maximal refinement of their possible maximum information.

---

This is the volume of a square dihedral space \(G\) 

definition of Scalar product for
compact dihedral space \((\delta, n_1, \delta_2, n_2) = (\delta, \delta_1, n_1, n_2)\)

\[\text{referral to von Neumann.}\]

\[\text{Theorem 7.5 is an extension of the Hilbert space of} \]

\[\text{products } n_1 \delta_1, n_2 \delta_2 \text{ which the scalar product is defined.}\]

\[(n_1, n_2) = (n_1, n_2) = (n_1, n_2)\]

\[(\delta, n_1, \delta_2, n_2) = (\delta, n_1, n_2)\]

<|det|>[[500, 0, 999

---

In the future we will be primarily concerned with expansions and consequent distributions over complete orthonormal sets \(S_1, S_2, \ldots\) and when we refer to "the corresponding operator" for the set \(S_1, S_2, \ldots\) we mean any non-degenerate operator where eigenstates are the set \(S_1, S_2, \ldots\) . 

## §2 Componit Systems - decomposition relation state 

Suppose that a system \(S\), with state function \(Y_S\), can be decomposed into two subsystems \(S_1\) and \(S_2\). Let \(\{N_i^{S_1}\}\) be a complete orthonormal set of state functions for \(S_1\) and \(\{E_i^{S_2}\}\) such a set for \(S_2\). Then the state function \(Y_S\) can always be represented as a sum of products of the \(N_i^{S_1}\) and \(E_i^{S_2}\) of the form: 

\[(6.1) \quad Y_S = \sum_{i,j} a_{ij} N_i^{S_1} E_j^{S_2}\]

In this situation there does not, in general, exist anything like a state function for \(S_2\) alone. That is, this is no single \(Y_S\) such that for any operator \(A\), which operates on \(S_2\) alone, \(\langle A Y_S \rangle = \langle A Y_S \rangle\). However, with respect to such operators on \(S_2\) alone, the system has no choice like a certain mixture of states for \(S_2\) alone. The distinction between a mixture of states \(Y\) and a weight \(a_i\) and a pure state \(Y\) which is a superposition \(Y = \sum a_i Y_i\) is that there are no interference phenomena between the various states of a mixture. The expectation of an operator \(A\) for the mixture is

---

\[ \langle A \rangle_M = \sum_i P_i \langle A \rangle_{\phi_i} = \sum_i P_i (\phi_j A \phi_i) \]

while the expectation for the pure state \(\psi_M\) is: 

\[ \langle A \rangle_{\psi} = \left( \sum_i a_i \phi_j A \sum_j a_j^* \phi_i \right) = \sum_{ij} a_i a_j^* (\phi_j A \phi_i) \]

which not the name as the mixture with weights
\(P_i = a_i a_j^*\) due to the premise of the interference terms (\(\phi_j A \phi_i\)) for \(j \neq i\). 

It is convenient to represent such mixtures by a density matrix \(\rho\). If the mixture \(M\) consists of the states \(\psi_j\), weighted by \(P_j\), and if we are working in the representation of the operator where eigenstates are the complex set \(\{\phi_j\}\) where \(\psi_j = \sum_i a_i^* \phi_i\), then we define the elements of the density matrix for the mixture, \(\rho^M\), to be: 

\[ \rho^M = \sum_j P_j a_j^* a_j \]

If \(A\) is any operator, we calculate its expectation for the mixture \(M\): 

\[ \begin{aligned} \langle A \rangle_M &= \sum_j P_j (\psi_j A \psi_j) = \sum_j P_j \left[ \sum_{i \in e} a_i^* a_j^* (\phi_j A \phi_i) \right] \\ &= \sum_{ij} \left( \sum_j P_j a_i^* a_j^* a_i \right) (\phi_j A \phi_i) = \sum_{ij} \rho^M_{ij} A_{ij} \\ &= \text{Trace}(\rho A) \end{aligned} \quad (A_{ij} \equiv (\phi_j A \phi_i)) \]

---

and we see that any mixture \(M\) is adjointly
represented by the density matrix \(P^M\). Note also
that \(P^*_{k} = P_{k}\) so that \(P_{k}\) is hermitian. 

Returning now to our output system \(S_j\),
decomposed according to (2.1), we calculate the
expectation of an arbitrary operator \(A\) which
operates on \(S_j\) only: 

\[
\begin{align*}
(A)_{ij}^S &= \left( \sum_j a_{ij}^* n_{ij}^{S_2} A \sum_{k,m} a_{km} n_{km}^{S_2} \right) \\
&= \sum_{ij,km} a_{ij}^* a_{km} (n_{ij}^{S_2} A n_{km}^{S_2}) \left( \sum_{j} n_{jm}^{S_2} \right) \\
&= \sum_{i} \left( \sum_j a_{ij}^* a_{ij} \right) A_{i,j} e \\
&= \text{Trace} \left( P^S A \right)
\end{align*}
\]

where we have defined \(P^S\) for the \(\{n_{ij}^S\}\) representation to be: 

\[
\rho_{ki}^{S_1} = \sum_j a_{kj}^* a_{ij}
\]

Similarly, the density matrix for \(S_2\) in the \(\{S_1, S_2\}\) representation is 

\[
\rho_{ik}^{S_2} = \sum_j a_{jk}^* a_{ji}
\]

and we see that in general while the subsystems
\(S_1\) and \(S_2\) do not possess state functions, they do
possess density matrices.

---

Furthermore, it is easily seen, \(S_1\) is then
represented by the non-interfering mixture of states \(V^0\)
weighted by \(S_j\), where 

\[ \frac{V^0}{S_1} = \frac{1}{P_1} \sum a_{ij} N_i \quad \text{and} \quad P_1 = \sum a_{ij}^* a_{ij} \]

There is a further significance to this mixture, in
that we can combine each \(V^0\) to be a relative or
conditional state function for \(S_1\), conditioned upon
the state \(S_2\) for \(S_3\). In actuality, the state \(V^0\)
determines a joint amplitude distribution for the
eigenvalues of an operator \(A\) on \(S_1\) and \(B\) on \(S_2\), i.e. the
distribution for \(A\) and \(B\) are not independent in
general, so that expectation of operators in \(S_1\)
will, in general, depend upon the value of \(B\) in \(S_2\). This
means that the relative function \(V^0\) is to be used
for the calculation of conditional expectation of any
operator on \(S_1\), conditioned upon \(B\) having the
value which is its eigenvalue for the state \(S_2\). The
two systems \(S_1\) and \(S_2\) are correlated, and the previous
expectation of subsystem operators calculated
from the density matrices, compared simply to
marginal expectations. Of will have performed a
measurement on \(S_2\), and observed it to be in state
\(S_3\), then we no longer calculate expectation for
\(S_2\) from \(P_2\), but from the pure state \(V^0\). 

In order to justify calling \(V^0\) (2.9) the
relative state function for \(S_1\), conditioned upon \(S_2\) lying
in state \(S_3\), we let \(B\) be an operator correspondingly
to the set \(\{S_3, S_2\}\) with distinct eigenvalues \(b_3\) and
let \(A\) be any operator on \(S_1\) with eigenstate \(S_1\) and values \(a_1\).

---

we then transform \(\mathcal{V}_5\) to \(A, B\) representation: 

\[
\begin{align*}
\mathcal{V}_5 &= \sum_{k,j} d_{kj} u_k^{5} \xi_j \xi_j^2 \\
\text{where } M_j &= \sum_k c_k^i u_k \\
\text{and } d_{kj} &= \sum_i a_{ij} c_k^i
\end{align*}
\quad (\Rightarrow \sum_k c_k^i c_k^j = \delta_{ij})
\]

Now in this representation \(d_{kj}^* d_{kj}\) represents the
joint square amplitude distribution over the values \(b_j\) and \(a_k\)
so that: 

\[
P(a_k, b_j) = d_{kj}^* d_{kj}
\]

and the marginal \(P(b_j)\) is: 

\[
\begin{align*}
P(b_j) &= \sum_k P(a_k, b_j) = \sum_k d_{kj}^* d_{kj} = \sum_k \left( \sum_i a_{ij} c_k^i \right)^* \left( \sum_i a_{ij} c_k^j \right) \\
&= \sum_i a_{ij}^* a_{ij} \left( \sum_k c_k^i c_k^j \right) = \sum_i a_{ij}^* a_{ij}
\end{align*}
\]

and hence the conditional distribution \(P^{b_j}(a_k)\) is: 

\[
P^{b_j}(a_k) = \frac{P(a_k, b_j)}{P(b_j)} = \frac{d_{kj}^* d_{kj}}{\sum_i a_{ij} d_{ij}^*}
\]

so that the conditional expectation of \(A_j\) is: 

\[
\langle A_j \rangle_{V_5}^{b_j} = \text{Exp}^{b_j}(a_k) = \sum_k a_k P^{b_j}(a_k) = \left( \frac{1}{\sum_i a_{ij} a_{ij}^*} \right) \sum_k d_{kj}^* d_{kj} a_k
\]

---

General definition of
Relative state function 

(0) 

0 

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

188 

189 

190 

191 

192 

193 

194 

195 

196 

197 

198 

199 

200 

201 

202 

203 

204 

205 

206 

207 

208 

209 

210 

211 

212 

213 

214 

215 

216 

217 

218 

219 

220 

221 

222 

223 

224 

225 

226 

227 

228 

229 

230 

231 

232 

233 

234 

235 

236 

237 

238 

239 

240 

241 

242 

243 

244 

245 

246 

247 

248 

249 

250 

251 

252 

253 

254 

255 

256 

257 

258 

259 

260 

261 

262 

263 

264 

265 

266 

267 

268 

269 

270 

271 

272 

273 

274 

275 

276 

277 

278 

279 

280 

281 

282 

283 

284 

285 

286 

287 

288 

289 

290 

291 

292 

293 

294 

295 

296 

297 

298 

299 

300 

301 

302 

303 

304 

305 

306 

307 

308 

309 

310 

311 

312 

313 

314 

315 

316 

317 

318 

319 

320 

321 

322 

323 

324 

325 

326 

327 

328 

329 

330 

331 

332 

333 

334 

335 

336 

337 

338 

339 

340 

341 

342 

343 

344 

345 

346 

347 

348 

349 

350 

351 

352 

353 

354 

355 

356 

357 

358 

359 

360 

361 

362 

363 

364 

365 

366 

367 

<tr>text<|/ref|>
368 

<tr>text<|/ref|>
369 

<tr>text<|/ref|>
370 

<tr>text<|/ref|>
371 

<tr>text<|/ref|>
372 

<tr>text<|/ref|>
373 

<tr>text<|/ref|>
374 

<tr>text<|/ref|>
375 

<tr>text<|/ref|>
376 

<tr>text<|/ref|>
377 

<tr>text<|/ref|>
378 

<tr>text<|/ref|>
379 

<tr>text<|/ref|>
380 

<tr>text<|/ref|>
381 

<tr>text<|/ref|>
382 

<tr>text<|/ref|>
383 

<tr>text<|/ref|>
384 

<tr>text<|/ref|>
385 

<tr>text</td><td>0.0</p> 

<|det|>[[0, 0, 0.0, 0.0</p> 

<|det|>[[0, 0, 0, 0.0</p> 

<|det|>[[0, 0.0, 0.0</p> 

<|det|>op</p> 

<|det|>[[0, 0.0, 0.1</p> 

<|ref|>text</p> 

<|ref|>text</p> 

<|ref|>text</p> 

</p> 

</p> 

</p> 

</p> 

</p>

---

we now compute the expectation acting \(\mathcal{W}_i^j\) as defined in (2.9): 

\[ (2.15) \quad \langle A \rangle_{\mathcal{W}_i^j} = \langle \psi_j A \psi_j \rangle = \left( \frac{1}{p_0} \sum_i a_{ij} N_i \right) A \frac{1}{p_0} \sum_i a_{ij} N_i \]

and using the relations 2.10 

\[ (2.16) \quad \langle A \rangle_{\mathcal{W}_i^j} = \frac{1}{p_0} \left( \sum_{i,k} a_{ij} c_{ik}^* u_k A \sum_{j,m} a_{ej} c_{jm}^* u_m \right) \\ = \frac{1}{p_0} \left( \sum_k d_{kj}^* u_k A \sum_j d_{mj} u_m \right) \\ = \frac{1}{p_0} \sum_{j,k} d_{kj}^* d_{mj} (u_k A u_m) = \frac{1}{2 a_{ij} a_{ij}} \sum_k d_{kj}^* d_{kj} a_k \]

which is the same as (2.14), and we have justified calling \(\mathcal{W}_i^j\) the conditional (or relative) state function for \(S_j\), conditioned upon \(S_j\) being in state \(S_j\). 

We have thus shown general a property of quantum states \(\mathcal{W}_i^j\) can be regarded as a superposition of states \(\mathcal{W}_i^j\) each of which contains a definite state \(S_j\) for \(S_j\) and all the corresponding definite states \(\mathcal{W}_i^j\) (i.e. relative to \(S_j\)). Furthermore, its state is an superposition with amplitudes \(\mathcal{F}_j\), so that \(\mathcal{W}_i^j = \sum_j \mathcal{F}_j \mathcal{W}_i^j\), thus implying to marginal expectations of any operators operating on a single subsystem, the system behaves like a non-interfering mixture of the \(\mathcal{W}_i^j\) with weights \(\mathcal{F}_j\). Furthermore, properties for the superposition are manifest in only for operators which operate on both sublevels simultaneously.

---

We now give a general definition of the relative state for \(S_1, Y_{n_1}\) for the state \(\psi^S_2\) for \(S_2\), when the total state is \(\psi^S\): 

\[ (2.16) \quad D\psi: \psi^S = N \sum_i \left( \phi_i^S \psi^S \psi^S \right) \phi_i^S \]

where \(\phi_i^S\) is any complete orthonormal set in \(S_1\) and \(N\) is a normalization constant. 

It should be noted first of all that \(\psi\) is unique, i.e. it does not depend upon the choice of the set \(\{S_i\}\). To prove this, choose another basis \(\{k_i\}\) with 

\[ \phi_i = \sum_j b_{ij} k_j, \quad \sum_j b_{ij}^* b_{ik} = \delta_{jk}, \quad \text{then} \]

\[ \begin{aligned} \sum_i \left( \phi_i \psi^S \psi^S \right) \phi_i &= \sum_i \left( \sum_j b_{ij} k_j \psi^S \psi^S \right) \left( \sum_k b_{ik} k_k \right) \\ &= \sum_{jk} \left( \sum_i b_{ij}^* b_{ik} \right) \left( \sum_j \psi^S \psi^S \right) k_k \\ &= \sum_k \left( \sum_j \psi^S \psi^S \right) k_k \end{aligned} \]

---

We now put this definition into correspondence with our previous result for \(N_j = \sum_{i,j} a_{ij} n_i^{s_2}\) for computing the relative state for \(S_2\) from the state \(S_1\) in \(S_2\). According to our definition 

\[
\begin{align*}
Y_j^{s_2} &= N_j \sum_i (n_i^{s_2})^{s_2} \Psi_j^{s_2} n_i^{s_2} \\
&= N_j \sum_i (n_i^{s_2})^{s_2} \sum_{j'} a_{ij'} n_i^{s_2} n_j^{s_2} n_i^{s_2} \\
&= N_j \sum_{i,j'} a_{ij'} \delta_{ij'} \delta_{j'} n_i^{s_2} = N_j \sum_{i,j'} a_{ij'} n_i^{s_2} \\
\end{align*}
\]

We further recall the total state is given by 

the superposition: 

\[
G.163) \quad Y^s = \sum_j \frac{1}{N_j} Y_j^{s_2} n_j^{s_2}
\]

Thus in general for any choice of a complete
orthonormal set \(\{S_j\}\) for one subsystem \(S_1 \in\)
complete system, it is the case that
consequently a set of relative states \(Y_j^{s_2}\) (not
necessarily orthogonal) 

This state of the complete system can be
represented by a superposition (2.163) each
element of which contains a definite state \(N_j^{s_2}\) for \(S_2\)
and a corresponding relative state \(Y_j^{s_2}\) for \(S_1\). (Note
however, that the \(Y_j^{s_2}\) are not necessarily orthogonal.

---

Furthurnore, for any operator which acts upon
5 alone, the expectation is the same as if the
superposition (2.163) is a non-interfering mixture,
as we have seen. This non-interfering mixture is
not, however, a complete description of the
composite system, since in the general case
of operators not restricted to 5, the interference
properties of the separate elements of the
superposition can be interpreted in terms of the
same superposition. As a final point, it may happen that
state for some state is zero by our definition
(and hence not really a state at all). We can then
if we choose, regard any state as the relative state,
but with zero amplitude only to the pairs
in the superposition (2.163).

---

We should like to complete this reaction by connecting
upon the existence of a fundamental system
correlation \(\{S_1, S_2\}\) between the two subsystems of \(S_1\)
and describing some of its properties. As was remarked
earlier a density matrix is hermitian, so that
there is a representation in which it is diagonal. In
particular, for the decomposition of \(S_1\) with state \(V_1\)
into \(S_1\) and \(S_2\), we can choose a representation in which
both \(P_1^S\) and \(P_2^S\) are diagonal, since the basis for
\(P_1^S\) and \(S_2\) can be chosen independently. Such a representation
will be called a canonical representation. This means that
it is always possible to represent the state \(V_1\) by
a single sum: 

(2.19) 

\[
\mathcal{W}^S = \sum_j b_j \phi_j^{S_2} \Theta_j^{S_2}
\]

where the \(\phi_j^{S_2}\) and \(\Theta_j^{S_2}\) methods orthonormal states
for \(S_1\) and \(S_2\) respectively. So we that this is the case
we first choose the basis \(\{S_1^S\}\) for a basis \(\{\Theta_j^{S_2}\}\).
where \(P_1^S\) is diagonal. Then if our state function \(V_1^S\)
is, in this representation: 

(2.18) 

\[
\mathcal{W}_S = \sum_{ij} \alpha_{ij} N_i^{S_2} \Theta_j^{S_2}
\]

we can rewrite it as 

(2.19) 

\[
\mathcal{W}_S = \sum_j b_j \phi_j^{S_2} \Theta_j^{s_2} \quad \text{where} \quad \phi_j^{S_2} = \frac{1}{b_j} \sum_i x_{ij} N_i^{S_2}
\]

\[
\text{and } b_j = \left( \sum_i \alpha_{ij}^* \alpha_{ij} \right)^{\frac{1}{2}}
\]

According to this definition of the \(\phi_j^{S_2}\) they are

---

already normalized, since they are simply the
previously considered relative states. Furthermore,
they are now orthogonal: 

\[
\begin{align*}
( \phi_j \phi_k ) &= \left( \frac{1}{b_j} \sum_i \alpha_{ij} \eta_i \right) \frac{1}{b_k} \sum_i \alpha_{ik} \eta_i \\
&= \frac{1}{b_j b_k} \sum_{ij} \alpha_{ij} \alpha_{ik} \sum_{i} \delta_{ij} = \frac{1}{b_j b_k} \sum_{i} \alpha_{ij} \alpha_{ik} \\
&= 0 \text{ if } j \neq k.
\end{align*}
\]

Since the sum is just the \(k_j\) component of
\(P^2\) in the \([\Theta_j]\) representation, which we have assumed
to be diagonal. We have therefore proved the existence
of a canonical representation (2.17). 

Now, any pair of non-diagonal operators
A on \(S_1\) and B on \(S_2\), which have or eigenfunctions that
\([\phi_j^S]\) and \([\Theta_j^S]\), are operators which define the
canonical representation, are "generally" correlated,
in the sense that there is a one-one correspondence
between their eigenvalues, i.e. the joint amplitudes
distribution for eigenvalues \(\{\alpha_i\}\) for A and B, for B
is: 

\[
P(a_i; b_j) = b_j^* b_j \delta_{ij}
\]

Moreover, since the marginals are \(P(a_i) = b_i b_i^*\), \(P(b_j) = b_j b_j^*\)
we calculate the correlation \(\{A, B\}_{Y^Y}\):

---

\[(2.22) \quad \langle A, B \rangle_{\gamma} = \sum_{ij} P(a_j, u_j) \ln \frac{P(a_i, u_i)}{P(a_i) P(u_i)}\]

\[= \sum_{ij} b_i b_i^* \delta_{ij} \ln \frac{b_i b_i^* \delta_{ij}}{b_i b_i^* b_j b_j^*}\]

\[= \sum_j b_j b_j^* \ln \frac{1}{\delta_j b_j^*} = -\sum_j b_j b_j^* \ln b_j b_j^*\]

we shall denote this quantity by \(\{\xi_1, \xi_2\}_{\gamma}\) and call it the canonical correlation of the subsystems \(\xi_1\) and \(\xi_2\) for the state \(\gamma\). It is the correlation between any pair of nondegenerate (\(A^2 B^2\)) operators which define the canonical representation. Furthermore, by (2.22) it is the negative of the marginal information of either of the operators: 

\[(2.23) \quad \{\xi_1, \xi_2\}_{\gamma} = -\Gamma_A(\gamma) = -\Gamma_B(\gamma) \quad (A, B \text{ non-ideal})\]

Furthermore, \(\Gamma_A\) is interesting to note, the canonical correlation is given by: (by 2.22) 

\[(2.24) \quad \{\xi_1, \xi_2\}_{\gamma} = \text{Trace} \left( P^2 h \right) P^2 = -\text{Trace} \left( P^2 h P^2 \right)\]

in the canonical representation when both density matrices are diagonal, \(\{\xi_1, \xi_2\} = \delta_{ij} b_i^* b_j\) and hence is given by (2.24) in general because the trace is invariant. However, the quantity \(\text{Trace}(P \ln P)\) is precisely the entropy of a mixture of states characterized by density matrix \(P\) (see Von Neumann) and we see that this entropy

---

of the mixture characteristic of a subsystem \(S_2\) for a state \(Y_2 = Y_{S_2}\) is exactly matched by a correlation information \(\{S_2, S_2^*\}\) which represents the correlation between the canonical variables \(A\) and \(B\) in the two systems. Similarly, for local Markov me 

There is a further special property of the operators \(A\) and \(B\) which define the canonical representation, namely, that the marginal information of \(A\) and of \(B\) is minimal in the sense that any other operator operating on \(S_2\) alone has marginal information less than or equal to that of \(A\), and similarly for any operator on \(S_2^*\). By (2.23) this implies the result that any operator \(C\) which operates either only on \(S_2\) or only on \(S_2^*\) satisfies: 

\[(2.25) \quad I_C(Y_2) \le -\{S_1, S_2^*\}_{W_S} \quad (\text{on } S_2 \text{ on } S_2^* \text{ alone}) \]

To prove this statement we consider an operator \(A'\) for \(S_2\), with eigenfunction \(2^{S_2}\) and transform \(Y_2\) from the canonical representation (2.19) to the representation in terms of the acts \(\{2^{S_2}\}\) and \(\{O_2^{S_2}\}\), so that if \(O_2 = \sum_i C_{ij} Y_i^{S_2}\), then in this representation we will have: 

\[(2.26) \quad Y_2 = \sum_{ij} \gamma_{ij} Y_i^{S_2} O_2^{S_2} \quad \text{where } \gamma_{ij} = b_{ij} C_{ij} \quad \text{then} \]

\[(2.27) \quad P(a_i^*, b_j) = \gamma_{ij}^* Y_{ij} \quad \text{and} \quad P(a_i^*) = \sum_j \gamma_{ij}^* Y_{ij} = \sum_j b_{ij}^* b_j C_{ij}^* C_{ij} \quad (2.28)\]

---

A1.5: high correlation between A, B
⇒ in B representation, A means small high inf
density (mean eigenfunctions with high inf)
on continuous with low A-C content.
B, C mean marginal density.

---

But \(C_{ij}\) is unitary, so that \(\sum C_{ij}^* C_{ij} = 1\) and \(\sum C_{ij}^* C_{ij} = 1\), so that \(T_{ij} = C_{ij} C_{ij}^*\) is clearly stochastic and by Theorem (1) of the appendix: 

\[ (2.29) \quad \sum_i \left( \sum_j T_{ij} b_i b_j^* \right) \ln \left( \sum_j T_{ij} b_i^* b_j \right) \le \sum_i b_i^* b_i \ln b_i b_i^* \]

but the left-hand is simply \(I_A(\psi_5)\), while the right-hand is the function of the canonical operator \(A\), and we have proved 

\[ (2.30) \quad I_A(\psi_5) \le I_A(\psi_5') \quad \text{where } A \text{ is canonical for } S_5 \text{ and } A' \text{ is an eigenoperator on } S_5. \]

This result is immediately extended to the code where \(A'\) is degenerate, since as a consequence of our definition of information for a degenerate operator (1.1) its information is still less than one which removes the degeneracy, and we have verified the general validity of (2.25). 

We should like to conclude this section by conjecturing that in addition to the maximal marginal information properties of operators \(A, B\) which define the canonical representation, they are maximally correlated, by which we mean that for any pair of operators \(C_1\) and \(D_1\) on \(S_1\) and \(D_2\): 

\[ (2.31) \quad \text{Gigiciture: } \{S, D\}_{4,5} \le \{A, B\}_{4,5} = \{S_1, S_2\}_{4,5}. \]

---

64. calculation of equivalent resistance 

Maybe it's like a line segment on a real picture.