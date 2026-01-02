# Everett Handwritten Notes on composite systems circa 1955.pdf

1) This section we assume system states to be
permitted by points in a Hilbert space.

Composite System:

We suppose that the system S under
consideration can be decomposed into two subsystems
S₁ and S₂. It N₁ be a complementary set of
total functions for S₁ and S₂ and for S₂. Then if
S is in the state ψ, ψ can be represented as a sum
of products of the n and ξ of the form:

\[
\psi = \sum_{i} a_{i} \eta_{i} N_{i}^{s_{2}} \xi_{i}^{s_{2}}
\]

(1)

---

Now, in this situation there does not exist anything like a state function for \(S_2\) alone, that is, there is no single \(Y_2\) such that for every operator \(A\) which operates on \(S_2\) alone \(\langle A \rangle_{Y_2} = \langle A \rangle_{Y_2}\). However, with respect to operators \(A\) on \(S_2\) only the system does behave like a certain mixture of states for \(S_2\) alone. 

(The distinction between a mixture of states and a pure state is that there are no interference phenomena between various states of a mixture, that is if we have a mixture of \(P_i\) weighted with \(P_i\) then the expectation of any operator \(A\) is \(\sum_i P_i \langle A \rangle_{P_i} = \sum_i P_i \langle \phi_i A \phi_i \rangle\) (note that a pure state \(\psi = \sum_i a_i \phi_i\) can not be considered as a mixture of the \(\phi_i\) with weights \(a_i^* a_i = P_i\) since \(\langle A \rangle_{\psi} = \left( \sum_i a_i^* \phi_i A \sum_i a_i \phi_i \right) = \sum_{i,j} a_i^* a_j \langle \phi_i A \phi_j \rangle\) in general.) 

(Emphasis that non-interference of mixtures of combined system leads for operators on a subsystem, not total.)

---

In the following, we will use the
conventionally defined by a density matrix \(\rho\). 

It is convenient to represent each
mixture by a density matrix \(\rho\). If the
mixture consists of the states \(\psi_j\) weighted by \(\rho_j\)
and if we are working in the approximation of the
set \(\{\phi_i\}\), and \(\psi_j = \sum a_{ij} \phi_i\), then 

we define the elements of the density matrix \(\rho\) to be: 

\[ (2) \quad \rho_{k \ell}^{(M)} = \sum_j P_j a_{j \ell}^* a_k^j \]

Now, if \(A\) is any operator, we calculate its expectation
for the mixture \(M\): 

\[ \begin{aligned} \langle A \rangle_M &= \sum_j P_j \langle A \rangle_{\psi_j} = \sum_j P_j \left( \psi_j A \psi_j \right) \\ &= \sum_j P_j \left( \sum_i a_{ij}^* \phi_i A \sum_k a_{kj}^* \phi_k \right) \\ &= \sum_{j \ell} P_j a_{j \ell}^* a_{j \ell} \left( \phi_{j \ell} A \phi_{\ell} \right) \\ &= \sum_{j \ell} \left( \sum_i P_j a_{j \ell}^* a_{j \ell} \right) \left( \phi_{j \ell} A \phi_{\ell} \right) \end{aligned} \]

---

And we see that any mixture is obviously
represented by the density matrix, since the
expectation of any operators can be computed from it
by (3). Note also that \(S_{k}^{*} = S_{k}\) so that \(S_{k}\) is hermitian,
and \(Trace S = 1\). 

Returning now to our general system \(S\) with
state (1): 

\[
\gamma_S = \sum_{ij} a_{ij} n_i^{S_2} f_j^{S_2}
\]

we calculate the expectation of an arbitrary operator \(A\)
which operates on \(S_1\) alone: 

\[
\begin{align*}
\langle A \rangle_{\gamma_S} &= \left( \sum_{ij} a_{ij} n_i^{S_2} f_j^{s_2} A \sum_{lm} a_{lm} n_l^{s_2} f_m^{s_2} \right) \\
&= \sum_{ijlm} a_{ij}^* a_{lm} \left( n_i^{s_2} A n_j^{s_2} \right) \left( f_j^{s_2} f_m^{s_2} \right) \\
&\text{and because last factor equals } S_{ijlm} \\
&= \sum_{ij} a_{ij}^* a_{ij} \left( n_i^{s_2} A n_j^{s_2} f_j^{s_2} \right) \\
&= \sum_{ij} \left( \sum_{kl} a_{ij}^* a_{kl} \right) A_{ijkl} \\
&= Trace \left( \rho^S A \right)
\end{align*}
\]

\[
(4) \quad \text{where we define} \quad \int_{\gamma_S}^{S_1} = \sum_{ij} a_{ij}^* a_{ij}
\]

---

Similarly, the density matrix for \(S_2\) is: 

\[(5) \quad \int_{i \in K} S_2 = \sum_j a_{jk}^* a_{ji}\]

And we see that in general the systems \(S_1\) and \(S_2\) of \(S\) do not possess state functions, while they do possess density matrices. 

It is easily seen that \(S_1\) then is represented by the mixture \(\psi_j\) weighted by \(P_j\), where 

\[(c) \quad \psi_j = \frac{1}{\sqrt{P_j}} \sum_i a_{ij} \psi_i \quad \text{and} \quad P_j = \sum_i a_{ij}^* a_{ij}\]

When is a further significance to this mixture, namely, we can consider \(\psi_j\) to be a relative, conditional state function for \(S_1\), conditioned on \(S_2\) being in state \(F_2\). By this we mean that if we were to perform a measurement on \(S_2\), and discover it to be in state \(F_2\), then the expectation for \(A\) is no longer to be computed from the density matrix \(P\), but from the pure state \(\psi_j\). The reason for this is that the two systems \(S_1\) and \(S_2\) are correlated, so that the probability distributions for two operators, \(A\) on \(S_1\) and \(B\) on \(S_2\), are not necessarily independent, and knowledge of \(B\)'s value may affect the expectation of \(A\). (Moreover, non-interference to be emphasized.) In order to justify calling \(\psi_j\) the state function for \(S_1\) conditioned on \(S_2\) for \(S_2\) we let \(B\) be the operator whose eigenbasis are the set \(\{F_2\}\), with eigenvalues \(b_j\) and let \(\{\psi_j\}\) be the set of eigenfunctions of \(A\), with values \(a_{ij}\).

---

We then transform \(\mathcal{V}^5\) to the A,B representation: 

\[
\begin{align*}
(1) \quad \mathcal{V} &= \sum_{k,j} d_{kj} u_j^k \sum_{i} \mathcal{F}_i^5, \\
&\text{where } \mathcal{N}_i = \sum_k b_k^i u_k \quad \text{(note that } \sum_k b_k^i b_k^i = \sum_{ij} \mathcal{F}_i^5) \\
&\text{and } d_{kj} = \sum_i a_{ij} b_k^i.
\end{align*}
\]

Now, in this representation \(d_{kj}^* d_{kj}\) is the probability that A has the value \(a_{ij}\) and B has the value \(b_j\), that is, it is the joint distribution for A and B, so 

\[
\mathcal{P}(a_k, b_j) = d_{kj}^* d_{kj}
\]

Now the marginal \(\mathcal{P}(b_j)\):

\[
\begin{align*}
(2) \quad \mathcal{P}(b_j) &= \sum_k \mathcal{P}(a_k, b_j) = \sum_k d_{kj}^* d_{kj} = \sum_k \left( \sum_i a_{ij} b_k^i \right) \left( \sum_i a_{ij} b_k^i \right) \\
&= \sum_{i \in I} a_{ij}^* a_{ij} \left( \sum_k b_k^i b_k^i \right) = \sum_{i \in I} a_{ij}^* a_{ij}.
\end{align*}
\]

To that the conditional distribution is 

\[
(10) \quad \mathcal{P}(a_k | b_j) = \frac{\mathcal{P}(a_k, b_j)}{\mathcal{P}(b_j)} = \frac{d_{kj}^* d_{kj}}{\sum_i a_{ij} a_{ij}^*}
\]

---

so that the conditional Expectation of \(A_j\), \(Exp^{b_j}(a_j)\) in 

\[ (11) \quad \mathbb{E} \exp^{b_j}(A) = \sum_k P(a_k | b_j) a_k = \frac{1}{\sum_j a_j^* a_j^*} \sum_k d_{kj}^* d_{kj} a_k \]

Which is the central conditional expectation. We now compute the Expectation using \(\gamma\)-substitution in (6): 

\[ \begin{aligned} \langle A \rangle_{\gamma j} &= \left( \gamma_j^A A \gamma_j^A \right) = \left( \frac{1}{\gamma_j^A} \sum_i a_{ij} \gamma_i^A A \sum_{lm} a_{lm} \gamma_l^A \right) \\ &= \frac{1}{\gamma_j^A} \left( \sum_{ik} a_{ij} b_k^A a_k \right) A \sum_{lm} a_{lm} b_m^A U_{lm} \\ &= \frac{1}{\gamma_j^A} \left( \sum_{ik}^* d_{kj} a_{ij} \right) A \sum_{lm} d_{lmj} U_{lm} \\ &= \frac{1}{\sum_i a_{ij} a_{ij}^*} \sum_k d_{kj}^* d_{kj} a_k \end{aligned} \]

which is the same as (11) and we have justified the use of \(\gamma_j^A\) as the conditional total function.

---

We would like finally to commit upon the existence of
a limit of canonical correlation between \(S_1\) and \(S_2\) and
describe some of its properties. As was remarked earlier
a density matrix is hermitian, so that there is a representation
in which it is diagonal. In particular, if we decompose
\(S\) into \(S_1\) and \(S_2\) we can choose our representation in such a
manner that both \(P_1^S\) and \(P_2^S\) are diagonal; since the
bases \(B_1\) and \(S_2\) can be chosen independently. This means
that it is always possible to write the state function as a
single sum; 

\[ \psi^S = \sum_j b_j \phi_j^S \Theta_j^S \]

when the \(\phi_j^S\) and the \(\Theta_j^S\) constitute orthogonal state bases,
to see that this is the case, we change the basis \(S_1\) to \(S_2\)
to a basis \(\Theta_j^S\) where \(P_1^S\) is diagonal. Then if our
state function for \(S_1\) is: 

\[ \psi^S = \sum_{i,j} \alpha_{ij} N_i^S \Theta_j^S \]

which we can rewrite as: 

\[ \psi^S = \sum_j b_j \phi_j^S e_j^S \Theta_j^S \quad \text{where} \quad \phi_j^S = \frac{1}{b_j} \sum_i \alpha_{ij} N_i^S \]

according to this definition of the \(\phi_j^S\) they are already normalized
since they are simply the previously considered relative states, but
furthermore they are orthogonal.

---

\[P(a_i) = b_i^* b_i\]

\[P(u_j) = b_j b_j^*\]

\[\Rightarrow \{A, B\}_{4'} = \sum_{i,j} P(a_i, b_j) \ln \frac{P(a_i, b_0)}{P(a_i) P(b_j)}\]

\[= \sum_{i,j} b_i b_j^* S_{ij} \ln \frac{b_i b_j^* S_{ij}}{b_i b_j^* b_j b_j^*}\]

\[= \sum_j b_j b_j^* \ln \frac{1}{b_j b_j^*} = -\sum_j b_j b_j^* \ln b_j b_j^*\]

---

\[
(\phi_j^* \phi_k) = \left( \frac{1}{b_j} \sum_i x_{ij} n_i, \frac{1}{b_k} \sum_k x_{ik} n_k \right)
\]

\[
= \frac{1}{b_j b_k} \sum_{i,j} \alpha_{ij} \alpha_{ik} \int_{S_{ij}} = \frac{1}{b_j b_k} \sum_{i,j} \alpha_{ik} \alpha_{ij}
\]

= 0 if j ≠ k since the sum is just the
\(K_j\) component of \(P_S\) in the \(\Theta\) representation, which
we supposed to be diagonal, so we have shown that
there always exits a representation where \(Y\) takes
the form: 

\[
\mathcal{V}^S = \sum_j b_j \phi_j^{S_2} \Theta_j^{S_2}
\]

with \(\phi_3^2\) and \(\Theta_3^2\) complete orthon. sets. This means
that these exist operators \(A\) and \(B\) whose operators
with eigenstates to \(\phi_3^2\) and the \(\Theta_3^2\) whose spectra
are perfectly correlated. Since the point-probability
distribution over the values \(a_i\) and \(b_j\) corresponding to \(\phi_3^2\) and \(\Theta_3^2\)
(and a sum over nondegenerate) is \(P(a_i b_j) = b_j b_i^* \phi_{ij}\)

We calculate easily that: 

\[
I_A = I_B = \sum_j b_j b_i^* \ln b_j b_i^*
\]

\[
\text{and } \{A, B\} = -\sum_j b_j b_i^* \ln b_j b_i^*
\]

Since a perfectly correlated direct distribution
has correlation equal to minus either marginal information) 

We shall denote this quantity by \(C(S_1, S_2)_{Y^S}\)
and call it the canonical correlation of the subsystems
\(S_1\) and \(S_2\).

---

It is interesting to note that this
Correlation of these special operators \(A, B\) is: 

\[ \{A, B\} = \text{trace} \left( \rho^S \ln \rho^S \right) = \text{trace} \left( \rho^S \ln \rho^S^2 \right) \]

We have
that is the quantity (invariant) usually described
as the entropy of the relative likelihood \(p\). So we
see that this "entropy" is exactly matched by a
correlation information between two variables \(A, B\)
in the two systems. The central question, (now of our own
time) is one more special property to this
"conceptual" representation, namely that the marginal
information of \(A\) and \(B\) is maximal in the sense that
any other non-degenerate operator operator on \(S\) has
the information then that \(A\) is similarly for any operator
on \(S_2\). That is, every non degenerate operator operator
on \(S_2\) on \(S_1\) only has information between or
equal to \(C(S_1, S_2)\), the system correlation. 

To prove this statement we consider any other
operator \(A'\) on \(S_2\) with eigenfunction \(u_j\)
and transformation \(\psi\) to this new basis: let \(\phi_j = \sum_{i} c_{ij} u_i\) 

\[ \psi = \sum_{ij} \gamma_{ij} u_i \otimes j \quad \text{where} \quad \gamma_{ij} \neq b_j C_{ij} \]

then \(P(a_i', b_j) = \gamma_{ij}^* \gamma_{ij}\) 

\[ \Rightarrow P(a_i') = \sum_j \gamma_{ij}^* \gamma_{ij} = \sum_j b_j^* C_{ij} b_j C_{ij} \]

---

\[\Rightarrow p(a_{i}^{\prime}) = \sum_{j} b_{j}^{*} b_{j} C_{ij}^{*} C_{ij}\]

But since the \(C_{ij}\) is unitary, so that
\(\sum_{j} C_{ij}^{*} C_{ij} = 1\) and \(\sum_{i} C_{ij} C_{ij}^{*} = 1\) 

by our theorem (T- ) we have that 

\[I\{\sum_{j} b_{j}^{*} b_{j} C_{ij}^{*} C_{\bar{j}}\} \le I\{b_{i} b_{i}^{*}\} = \{S_{1}, S_{2}\}\]

Which again indicates the fundamental role of \(\{S_{1}, S_{2}\}\). 

Conjecture: In addition to the above maximal
marginal information properties of \(A, B\), they
are maximally correlated, that is, for an arbitrary
pair of non-degenerate operators, \(C\) and \(D\), \(S_{1}\) and \(S_{2}\)
\(\{C, D\} \le \{A, B\} = \{S_{1}, S_{2}\}\).