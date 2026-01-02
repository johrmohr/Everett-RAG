# Everett Draft -- III Quantum mechanics version 2 circa 1956.pdf

## II. Quantum Mechanics 

In this chapter we assume that state of a physical system are represented by points in a Hilbert space, and that for isolated system, the time dependence of the state is given by a linear wave equation. The first section deals with the representation of composite system states, density matrices, and the definition of relative states. In the second section the concept of information of a system is introduced, and its application to the measurement of signals. Section 3 deals with the question of approximate eigenfunctions (Eigenfunction norm), and the relationship with correlation. Section 4 illustrates the building of correlation in physical systems with an example of Vol. 1. 1. 1. 1. 1. 1. 1. 

§1. Composite System 

In this chapter we assume that state of a 

physical system are represented by points in a

---

To begin with: Consider with points \(\mathbf{V}\) in Hilbert space \(\mathcal{H}\), as well as linear operators \(A\). We define a functional
\(\langle A, \cdot \rangle\) called the expectation of \(A\) to \(k\). 

\[ \langle A, \cdot \rangle = \langle \psi, A \cdot \psi \rangle \]

A particular class of intrinsic will be projection operators, \(P_{\xi}\):
projections on \(\xi\), defined strongly. 

\[ P_{\xi} \cdot \psi = \langle \xi, \psi \rangle \cdot \psi \]

For a complete orthonormal set \(\{E_j\}\) we define
a distribution, the square amplitudes distribution. 

\[ P_{\xi} = \langle \psi_j, \psi_j \rangle^{\frac{1}{2}} \]

We shall often be interested in the square amplitudes distribution of an \(n\)-dimensional Hilbert space, which is given by
\(\mathcal{H}\) where the \(\xi_j\) are the eigenfunctions. 

For two Hilbert spaces \(\mathcal{H}_1\) and \(\mathcal{H}_2\), \(\mathcal{H}_1\) and \(\mathcal{H}_2\) are
consistent the product Hilbert space \(\mathcal{H}_1 \otimes \mathcal{H}_2\) (tensor
product) which is then to be the space of all possible
sums of products of points of \(\mathcal{H}_1\) and \(\mathcal{H}_2\). 

The elements of form \(\sum a_j \xi_j \otimes \eta_j\) where \(\xi_j \in \mathcal{H}_1\), \(\eta_j \in \mathcal{H}_2\)
are properly, one considers only finite sums, the
completes the resulting space tensor with additional space.
The scalar product in \(\mathcal{H}_1 \otimes \mathcal{H}_2\) is then taken
as: 

\[ \langle \xi_1, \xi_2 \rangle = \sum a_j^* b_j \langle \xi_1, \xi_2 \rangle \langle \eta_1, \eta_2 \rangle \]

---

In (1.3) the dependence of \(P_i\) on the choice of \(a_i \in \mathbb{Q}\) is
not true for \(P_i\) even the choices \(S_i\) is in agreement. The
\(P_i\) is the projection on \(S_i\) and \(I_i\) is the identity in \(S_i\)
then the marginal distribution \(R_i\) is given by : 

\[
\begin{align*}
(1.4) \quad P_i &= \langle P_i \rangle^s \mathcal{Y}^s \\
\text{and similarly} \\
(1.5) \quad P_i &= \langle I_i^s P_i \rangle \mathcal{Y}^s
\end{align*}
\]

In order to prove this relation we calculate from (1.4) : 

\[
\begin{align*}
(1.6) \quad \langle P_i I \rangle \mathcal{Y}^s &= \langle \mathcal{Y}^s P_i I \mathcal{Y}^s \rangle = \langle \mathcal{Y}^s P_i I^s \sum_{i,m} (\mathcal{Y}^s P_i \mathcal{Y}^s) P_i \rangle \\
&= \sum_{i,m} (\mathcal{Y}^s P_i \mathcal{Y}^s) (\mathcal{Y}^s P_i \mathcal{Y}^s) S_i P_i = \sum_{m} |(\mathcal{Y}^s P_i \mathcal{Y}^s)|^2 = P_i
\end{align*}
\]

We next calculate the conditional distribution \(P_i^s\) and \(P_i^s\) : 

\[
P_i^s = P(\mathcal{Y}_i \text{ conditional on } \mathcal{Y}_i) = \frac{P_i^s}{P_i} = \frac{\langle P_i P_0 \rangle \mathcal{Y}^s}{\langle I_i \mathcal{Y} \rangle \mathcal{Y}^s}
\]

\[
P_i^s = P(\mathcal{Y}_i \text{ conditionally on } \mathcal{Y}_i) = \frac{P_i^s}{P_i} \quad = \frac{\langle P_i P_0 \rangle \mathcal{Y}^s}{\langle P_i I \rangle \mathcal{Y}^s}
\]

---

Therefore, for each system, this is not
meaning for expectation of operators on one subsystem,
alone, since each expectation clearly depends upon
the state of the other subsystem. There is \(A \otimes B\)
in quantum in \(S_1\) and \(S_2\) for \(S_1\) and \(S_2\) respectively)
only \(A \otimes B\) has meaning in \(S_1 \otimes S_2\).

Suppose that \(S_1\) are input of \(A\) and \(S_2\) are input of \(B\) and that the state of the system of \(S_1 \otimes S_2\) is in the product on \(S_1 \otimes S_2\) 

\[ \langle P_{S_1} P_{S_2} \rangle = \langle \psi_{S_1 S_2} P_{S_1} P_{S_2} \rangle \psi_{S_1 S_2} \]

\[ \begin{align*} \langle P_{S_1} P_{S_2} \rangle &= \langle \psi_{S_1 S_2} P_{S_1} P_2 \rangle \psi_{S_1 S_2} \\ &= \left( \sum_{i,j} a_{ij} S_i \right) \sum_{m,n} P_{S_1} P_{S_2} \sum_{mn} \langle m \rangle \langle n \rangle \psi_{S_1 S_2} \\ &= \sum_{i,j,m,n} a_{ij}^* a_{mn} \langle S_i P_{S_1} P_{S_2} \rangle \langle n_j P_{S_1} P_{S_2} \rangle \langle m_j P_{S_1} P_{S_2} \rangle \langle n_m P_{S_1} P_{S_2} \rangle \\ &= \sum_{i,j,m,n} a_{ij}^* a_{mn} S_i S_{km} S_{jn} S_{en} \\ &= a_{k e} a_{k e} \end{align*} \]

above we see that the expectation of the product of the
project operators corresponds to the square amplitude
of the coif of the product \(\sum_{k} N_k\) in the expansion
of \(\psi_{S_1 S_2}\) in the \(S_1 S_2\) symmetric. 

which the interpretation that \(\hat{a}_{k e} \hat{a}_{k e}\) is a joint
distribution over all state \(S_1 N_1\) is the
probability that \(S_1\) and \(N_1\) will be in the
expectation of subsystem operators are dependent
on the state of the subsystem.

---

build. \(m:\) (When referring to probabilities, independent variables will use phrases like "the probability that option \(i\) in state \(k\), which means that the probability that a maximum which has \(x\) as an eigenstate, will result in the eigenvalue of \(k_i\).)

it is then easily seen that if \(\{\xi_i\}\) and \(\{\eta_i\}\) form complete orthonormal bases in \(\mathcal{B}\) and \(\mathcal{B}_2\) respectively, that the set of products \(\{\xi_i \eta_i\}\) is a complete orthonormal set in \(\mathcal{B}_1 \otimes \mathcal{B}_2\). For any pair of operators \(A, B\) in \(\mathcal{B}_1\) and \(\mathcal{B}_2\), thus is a companion \(AB\) (direct product) in \(\mathcal{B}_1 \otimes \mathcal{B}_2\), which can be defined by its effect on the elements \(\xi_i \eta_i\) (\(\xi_i \in \mathcal{B}_1, \eta_i \in \mathcal{B}_2\)) of \(\mathcal{B}_1 \otimes \mathcal{B}_2\):

\[AB \xi_i \eta_i = (A \xi_i)(B \eta_i)\]

---

61 Composite Systems

It is well known that if the states of a pair of systems \(\Sigma_1\) and \(\Sigma_2\) are represented by points of Hilbert space for \(\text{ind}\mathcal{H}_2\), respectively, that the states of the composite system \(\Sigma_1 + \Sigma_2\) i.e. \(\Sigma_1 \Sigma_2\) and \(\Sigma_2\) regarded as a single system, are represented by points of the tensor product \(\mathcal{H}_1 \otimes \mathcal{H}_2\). Thus if \(\{\Sigma_i\}\) is a basis for \(\mathcal{H}_1\), \(\{\mathcal{H}_2\}\) for \(\mathcal{H}_2\), the general state of the composite system \(\Sigma_1 \Sigma_2\) is of the form:

\[
\mathcal{H} = \sum_{i,j} a_{ij} \{\Sigma_i \} \{\mathcal{H}_2\} \text{ where } \sum_{ij} a_{ij} a_{ij} = 1
\]

Accordingly to the standard probabilistic interpretation, \(\{\Sigma_i\}\) then is the probability that \(\mathcal{H}\) will be the state of the system \(\Sigma_1\) and \(\Sigma_2\) in \(\mathcal{H}_2\). The square amplitude distribution \(a_{ij} a_{ij}\) thus has the character \(\mathcal{H} = \text{joint distribution, Feller}\).

---

\[S = S_1 + S_2\]

We now introduce the concept of relative state. 

The relative state \(\psi_{rel}\) for the state \(\psi^S\) of \(S_2\) when the total state is \(\psi^S\) is: 

\[ \text{Def:} \quad \psi_{rel} = N \sum_{i=1}^{N} \left( \phi_i^S \psi_i^S \right) \phi_i^S \]

1. In case of two
fields in
the same
state 

\(S_1\) 

\(\psi^S\)

---

We note first that \(\mathcal{H}\) is unique, i.e. its dependence upon the choice of basis \(\{\mathcal{B}_i\}\) is only apparent. To prove this, choose another basis \(\{\mathcal{B}_i'\}\) with \(\mathcal{B}_i' = \sum_{j} b_{ij} \mathcal{B}_j\). Then 

\[\sum_i (b_i^* b_{ik} - \delta_{ik}) \mathcal{B}_j = 0\]

\[\sum_i (\sum_j (b_i^* b_{ik} \mathcal{B}_j) \mathcal{B}_j) = \sum_i (\sum_j b_{ij} \mathcal{B}_j \mathcal{B}_j) (\sum_k b_{ik} \mathcal{B}_k)\]

\[= \sum_{j,k} (\sum_i b_{ij} b_{ik} (\mathcal{B}_j \mathcal{B}_j) \mathcal{B}_k) = \sum_{j,k} \delta_{jk} (\mathcal{B}_j \mathcal{B}_j \mathcal{B}_j) \mathcal{B}_k\]

\[= \sum_k (\mathcal{B}_k \mathcal{B}_k \mathcal{B}_k) \mathcal{B}_k\]

and the normally added \(\sum_i (\mathcal{B}_i \mathcal{B}_i \mathcal{B}_i)\) is independent of the choice of the basis \(\{\mathcal{B}_i\}\) and is unique (it may, of course, be zero).

---

\[
\rho_{s} = \sum_{j} \delta(\phi_{0}, \psi_{s})(\psi_{s} \phi_{0}, \psi_{s})
\]

\[
\begin{align*}
\left\langle \rho_s I \right\rangle &= \left\langle \psi_s \rho_s I \psi_s \right\rangle \quad \text{since } \psi_s \phi_0 = \psi_s \\
&= \left\langle \psi_s \rho_s I \sum_{k \in \mathcal{K}} \left(\phi_0, \psi_s\right) \phi_0 \right\rangle \\
&= \sum_{k \in \mathcal{K}} \left(\phi_0, \psi_{s}\right) \left(\psi_{s} \rho_{k} \phi_{0}\right) \\
&= \sum_{k \in \mathcal{K}} \left(\phi_0, k \psi_{s}\right) \left(\psi_{s} \phi_{0}\right) \delta_{i k} \\
&= \sum_{j} \left(\phi_0, k \psi_{s}\right) \left(\psi_s \phi_{0}\right)
\end{align*}
\]

---

A

A of prequential D on S and S separating.

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

<|det|>[-1, 0, 999, 0]

---

\[
\begin{align*}
\text{Conditional} &= \langle \mathbf{A} \mathbf{p}_e \rangle \\
&= (\gamma^s \mathbf{A} \mathbf{p}_e \gamma^s) \\
&= (\gamma^s \mathbf{A} \mathbf{p}_e \sum_{\ell,m} (\phi_{\ell,m} \gamma^s) \phi_{\ell,m}^* \phi_{\ell,m}) \\
&= \sum_{\ell,m} (\phi_{\ell,m} \gamma^s) (\gamma^s \mathbf{A} \mathbf{p}_e) (\phi_{\ell,m} \phi_{\ell,m}^*) \\
&= \sum_{\ell,m} (\phi_{\ell,m} \gamma^s) \lambda_e \delta_{jm} (\gamma^s \phi_{\ell,m}^* \phi_{\ell,m}) \\
&= \langle \mathbf{A} \sum_{\ell} \lambda_e | (\phi_{\ell,m} \gamma^s) |^2 \rangle.
\end{align*}
\]

\[
\begin{align*}
\text{Cond} \quad \mathbb{E} \mathbf{p}^i \mathbf{A} &= \sum_{\ell} \mathbf{p}_i^j \lambda_e = \sum_{\ell} \frac{\mathbf{p}_i^j}{\mathbf{p}_s^j} \lambda_e \\
&= \frac{1}{\mathbf{p}_s^j} \sum_{\ell} \lambda_e | (\phi_{\ell,m} \gamma^j) |^2 \\
&= \frac{1}{\mathbf{p}_s^j} \sum_{\ell,m} (\phi_{\ell,m} \gamma^s) (\gamma^{s'} \phi_{\ell,m} \phi_{\ell,m}) \lambda_s \delta_{jm} \\
&= \frac{1}{\mathbf{p}_s^j} \sum_{\ell,m, \ell'} (\phi_{\ell,m} \gamma^s) (\gamma^{s'} \phi_{\mathrm{e}_j} \phi_{\mathrm{e}_j}) \\
&= \frac{1}{\mathbf{p}_s^j} (\gamma^s \mathbf{A} \mathbf{p}_e \sum_{\ell,m} \phi_{\ell,m} \gamma^s) \phi_{\ell,m}^* \\
&= \frac{1}{\mathbf{p}_s^j} (\gamma^s \mathrm{A} \mathbf{p}_e \gamma^s) = \frac{1}{\mathbf{p}_s^j} \langle \mathbf{A} \mathbf{p}_e \rangle = \frac{\langle \mathbf{A} \mathbf{p}_e \rangle}{\langle \mathbf{I} \mathbf{p}_e \rangle}.
\end{align*}
\]

---

\[ \text{Let } \langle AI \rangle = (\psi_j^s AI \psi_j^s) \]

\[ \psi_j^s \sum_{33} (\phi_0 \phi_j \psi^s) \phi_0 \phi_j \]

\[ \begin{aligned} & = \sum_{jj'} (\phi_0 \phi_j \psi^s) (\psi_j^s AI \phi_0 \phi_j) \\ & = \sum_{jj'} (\phi_0 \phi_j \psi^s) ((\psi_j^s \lambda_0 \phi_0) \\ & = \sum_{jj'} \lambda_0 (\phi_0 \phi_j \psi^s)^2 \end{aligned} \]

**Backwards:** 

\[ \begin{aligned} \text{Exp } A &= \sum_{jj'} \phi_j \lambda_i = \sum_{jj'} \lambda_0 (\phi_0 \phi_j \psi_j^s) (\psi_j^s \phi_0 \phi_j) \\ &= \sum_{jj'} (\phi_0 \phi_j \psi_j^s) (\psi_j^s \lambda_i \phi_0 \phi_j) \\ &= \sum_{jj'} (\phi_0\phi_j \psi_j^s) (\psi_j^s AI \phi_0 \phi_j) \\ &= (\psi_j^s AI \sum_{jj'} (\phi_0 \phi_j \psi_j^s) \phi_0 \phi_j) = (\psi_j^s AI \psi_j^s) \\ &= \langle AI \rangle \end{aligned} \]

---

Finally Get density matrix : 

\[
\begin{align*}
\langle A \rangle &= (\psi^s A \psi^s) \\
&= \left( \sum_{i,j} (\xi_i \eta_j) \psi^s \right) \sum_{i,j} \eta_j A \sum_{l,m} (\xi_l \eta_m \psi^s) \sum_{i,j} \eta_j \eta_m \\
&= \sum_{i,j,l,m} (\xi_i \eta_j \psi^s)^* (\xi_l \eta_m \psi^s) (\xi_l A \xi_l) (\eta_j \eta_m) \\
&= \sum_{i,j,l} \left( \sum_{j} (\xi_i \eta_j \psi^s)^* (\xi_l \eta_j \psi^s) (\xi_l A \xi_l) \right) \\
&= \sum_{i,j,l} \left[ \sum_{j} (\xi_i \eta_j \psi^s)^* (\xi_j \eta_j \psi^s) \right] (\xi_i A \xi_l) \\
&= T_{\text{race}} \rho A
\end{align*}
\]

\[
\text{where } A_{i,j} = (\xi_i A \xi_j) \\
\text{and } \rho_{\text{hermitian}} = \sum_j (\xi_i \eta_j \psi^s)^* (\xi_j \eta_j \phi^s)
\]

**Strategy** Almost: An initial important connection 

\[
\langle A \rangle = \sum_j \rho_j \langle \phi_j | A | \phi_j \rangle
\]

Leads to distribution between
hermitian and nonhermitian.

---

\[
v = \sum_{i} a_{i} \phi_{i} \psi_{i}
\]

\[
\langle A \rangle = \left( \sum_{i} a_{i} \phi_{i} \psi_{i} \right) A \sum_{j} a_{j} \phi_{j} \psi_{j}
\]
\[
= \sum_{i,j} a_{i}^{*} a_{j} \left( \phi_{i} A \phi_{j} \right) \left( \psi_{i} \psi_{j} \right)
\]

Work done by \(A\) on \(S\) is \(S\) 

\[
\begin{align*}
\langle A \rangle &= \left( \sum_{i} a_{i} \psi_{i} \right) A \sum_{j} a_{i} \phi_{j} \theta_{j} \\
&= \sum_{i} a_{i}^{*} a_{i} \left( \theta_{i} \theta_{i} \right) \left( \psi_{i} \psi_{i} \right) A \psi_{i} \theta_{i} \\
&= \sum_{j} a_{j}^{*} a_{j} \left( \psi_{i} \psi_{i} \right) A \psi_{\text{nel}} \\
&= \sum_{i} a_{i}^{*} a_{j} \left( A \right) \psi_{\text{nel}} \\
&= \sum_{j} p_{j} \left( A \right) \psi_{\text{nel}}
\end{align*}
\]

---

Start all over: 

\[
\frac{\text{Given } A, \text{ eigen } \phi_i \text{ in } S_1}{\text{and } \psi^s \text{ in } S_2} = \frac{\text{given } U_i}{\text{and } \psi^s}
\]

find S2 compl: 

\[
P_{ij} = P(\phi_i \text{ and } \theta_j) = |(\phi_i, \psi^s)|^2
\]

\[
\begin{align*}
\text{Marginal } P_i &= \sum_j P_{ij} = \sum_j |(\phi_i, \psi^s)|^2 = N_i^2 \\
\text{Conditional } P_{ij}^s &= \frac{P_{ij}}{P_i} = N_i^2 P_{ij}
\end{align*}
\]

\[
\text{Conditional } P_{ij}^s = \frac{P_{ij}}{P_i} = N_i^2 P_{ij}
\]

\[
\text{Conditional } \mathbb{E}[\exp_i] = \mathbb{E}[\lambda_i \phi_i^s] = \sum_i \lambda_i P_{ij}^s = \sum_i \lambda_i N_j^s P_{ij}^s \\
= \sum_i \lambda_i N_j^s |(\phi_i, \psi^s)|^2 \\
= \sum_i N_j^s |(\phi_i, \psi^s)|^2 (\phi_i A \phi_i)
\]

Marginal Exp: 

\[
\text{for } A = \sum_j P_{ij} \exp_i(A) = \sum_{ij} \lambda_i P_{ij} = \sum_{ij} |(\phi_i, \psi^s)|^2 (\phi_i A \phi_i) \\
= \sum_i \left( \sum_j |(\phi_i, \psi^s)|^2 \right) (\phi_i A \phi_i)
\]

---

\[\langle A\rangle \gamma_{n e l}^{\omega_{i}} = (\gamma_{n e l}^{\omega_{i}}A\gamma_{n e l}^{\omega_{i}})\] 

\[= (\sum_{i} (\phi_{i} \otimes j) \gamma_{n e l}^{\omega_{i}} A \sum_{m} (\phi_{i} \otimes j) \gamma_{m}^{\omega_{i}}) \phi_{n m}\]

\[= \sum_{i} (\phi_{i} \otimes j) \gamma_{n e l}^{s} (\phi_{i} \otimes j) \lambda_{m} S_{i m}\]

\[= \sum_{i} \lambda_{i} P_{i j}\]

But, \(N^2\) on the evaluated by computing \(\langle I \rangle \gamma_{n e l}\) 

\[= N^2 \sum_{i} P_{i j} = N^2 P_{j} = 1 \quad \text{that} \quad N^2 = \frac{1}{P_{j}} \text{ and}\]

\[\langle A\rangle \gamma_{n e l}^{\omega_{i}} = \frac{1}{P_{j}} \sum_{i} \lambda_{i} P_{i j} = \sum_{i} \lambda_{i} P_{i j}^{j} = \exp^{\omega_{i}} [A]\]

and we have proved that the conditional expectations are
given by the relative wave functions. (This of course includes
the conditional distributions themselves, since they can be
extended as expectations of very operators.)

---

To understand the significance of the relative shifts, we remark that for any pair of operators \(A, B\) on \(\mathbb{R}\) and \(S_2\) respectively, we have a joint distribution for the eigenfunctions. Let us now compute the conditional distributions for the eigenfunctions \(f_2\) of \(A\), conditioned upon eigenfunction \(\Theta_2\) of \(B_2\) for state \(\psi_2\). Write \(\psi_2\) in \(\otimes\) a representation: 

\[ \psi_2 = \sum_{ij} a_{ij} f_2 \Theta_j = \sum_{ij} (f_2 \Theta_j \psi_2) a_{ij} \Theta_j \]

we see that the joint square amplitudes of \(f_2\) and \(\Theta_j\) in 

\[ p_{ij} = \left| \left( f_2 \Theta_j \psi_2 \right) \right|^2 \]

---

**Summary:** State of composite system corresponds to joint distribution.

relative state corresponds to conditional distribution.

**Density matrix** **marginal** 

**A** 

<|/det|>
\(A_{0} = (S,A,Y)\) 

\(S\) 

\(\text {full in}\) 

and exp \(\text {exp}\) \(\text {exp}\) \(\text {exp}\) \(\text {exp}\) \(\text {exp}\)

\(\sum\) \(\text {exp}\) \(\text {exp}\) \(\text {exp}\) \(\text {exp} \text {exp}\) \(\text {exp}\) \(\text {exp}\) \(\text {exp}\) 

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=\"2\"></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan=\"2"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td rowspan=\"2\"></td><td rowspan=\"2\"></td><td></td><td></td><td></td><td></td><td></td><td rowspan=\"2\">None</td><td>None</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None </td><td>None</td><td>None</td><td>None</td></tr><tr><td></td><td></td><td></td><td>None</td><td>None</td><td>None</td><td>None</td><td></td><td></td><td></td><td rowspan=\"2\"></td><td></td><td></td><td rowspan=\"2\">None</td><td>None</td><td>None</td></tr><tr><td></td><td></td><td></td><td></td><td rowspan=\"2\"></td><td></td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td></td><td>None</td><td>None</td><td>None</td></tr><tr><td></td><td></td><td></td><td>/</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>None</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>None None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None None</td><td>None None</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>None</td><td>None None</td><td>None</td><td>None</td><td>None None</td><td>None</td><td>None</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=\"2\"></td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None None None</td><td>None</td><td>None</td><td>None</td></tr><tr><td></td><td></td><td></td><td> None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td></td><td> None</td><td>None</td><td>None</td><td>None</td><td>None</td></tr><tr><td></td><td></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td rowspan=\"2\"></td><td>None None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None </td><td>None None</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td rowspan=\"2\"></td><td></td><td></td><td></td><td></td><td>None</td><td>None</td><td>None</td><td></td><td>None</td><td>None</td><td></td><td>None</td><td>None</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>None</td><td>None</td><td>None</td><td></td><td>None None</td><td>None</td><td>None</td><td>None</td><td>None</td></tr><tr><td></td><td>None</td><td>None</td><td>None</td><td>None</td><td>None None</td><td>NoneNone</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td></tr><tr><td rowspan="2"></td><td></td><td></td><td></td><td></td><td>None</td><td>None</td><td>None</td><td rowspan=\"2\"></td><td>None</td><td>None</td><td>None</td><td></td><td>None</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>None</td><td>None</td><td></td><td></td><td></td><td></td><td></td><td></td><td>None</td><td>None</td><td rowspan=\"2\"></td><td>None</td><td></td><td>None</td></tr><tr><td></td><td></td><td></td><td></td><td rowspan=\"2"></td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td></table> 

Summary: State of composite system corresponds to joint distribution.

<|det|>[[0, 0,

---

\[Y = \sum_{i,j} a_{ij} N_i^S \xi_j^S\]

\[P_{[n_k]} P_{[s_l]} = \frac{P_{[n_k]}(n_i)}{P_{[s_l]}(n_i)} = \frac{\delta_{i,k} n_i}{\delta_{s_l} (n_i) \delta_{m_k} s_k}\]

\[\langle P_{[n_k]} P_{[s_l]} \rangle = \left( \sum_{i,j} a_{ij} N_i \xi_j \right) P_{[n_k]} P_{[s_l]} \frac{\sum_{i,j} a_{ij} n_i m_j}{\sum_{i,j} a_{ij} m_j}\]

\[= \sum_{i,j,k} a_{ij}^* a_{km} (n_i \xi_j) \left( P_{[n_k]} P_{[s_l]} \right) \left( P_{[s_l]} \xi_j \right)\]

\[= a_{ij}^* a_{km} (n_i \xi_j) \left( \sum_{j,m} \xi_j \right)\]

\[operators \quad A^S \quad A^S \quad have \quad in \quad products\]

\[\langle A^S A^S \rangle = \left( \gamma A^S A^S \gamma \right)\]

\[= \sum_{i,j} a_{ij}^* a_{mi} (n_i A^S n_i) \left( \text{when } \xi_j A^S \xi_j \right)\]