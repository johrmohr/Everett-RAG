# Everett Draft -- 2 Information and Correlation in Quantum Mechanics circa 1956.pdf

We shall begin by defining the information of an operator \(A\) in a state \(\Psi\). 

We shall be interested in 

We wish to be able to discuss information and correlation formulations \(A, B, \ldots\) with respect to a state function \(\Psi\) and these quantities are to be computed from the eigenvalues of the projection of \(\Psi\) upon the eigenstates of the operators, regarded as probability distributions over the eigenvalues, through the formulae of the preceding chapter. We have already seen ( ) that a state \(\Psi\) and an orthonormal basis \(\{|e_i\rangle\}\) leads to a \(p\)-square amplitude distribution of \(\Psi\) on the set \(\{|e_i\rangle\}\): 

\[(2.1) \quad P_i = |\langle e_i | \Psi \rangle|^2 = \langle [e_i] | \Psi \rangle \Psi \]

so that we can define the information of the basis \(\{|e_i\rangle\}\) for the state \(\Psi\), \(I_{\{e_i\}}(\Psi)\), to be simply the information of this distribution relative to the uniform measure: 

\[(2.2) \quad I_{\{e_i\}}(\Psi) = \sum_i p_i \ln p_i = \sum_i |\langle e_i | \Psi \rangle|^2 \ln |\langle e_i | \Psi \rangle|^2\]

We will define the information of an operator \(A\), for state \(\Psi\), \(I_A(\Psi)\), to be the information in the probability square amplitude distribution over its eigenvalues, the information of the probability distribution over the results of a determination of \(A\) which is presented in the probability interpretation. For a non-orthogonal operator \(A\) this distribution is the same as the distribution (2.1).

---

our the eigenstate \(\psi\) but because the information is
dependent only on the distribution over a numerical
value, it is the same as the information of the
distribution over eigenvalues of \(A\) in precisely the
information of the eigenbasis of \(A\), \(\mathcal{E}_0:3\) : Thus: 

\[(2,3) \quad I_A(\psi) = I_{\mathcal{E}_0:3}(\psi) = \sum_i \langle \psi_i | \psi \rangle \ln \langle \psi_i | \psi \rangle \quad (\text{analog})\]

We see that for fixed \(\psi\), the information of all non-eigenstate
operators having the same set of eigenstates is the same. 

In the case of degenerate operators it will
be convenient to take a definition of information, the
information of the square complete distribution over
the eigenvalues relative to the information measure
which consists of the multiplicity of the eigenvalues,
rather than the uniform measure. The definition
preserves the class of uniform measure over the
eigenstates, in distinction to the eigenvalues. 

By \(\mathcal{E}_0:3\) (from \(L\) to \(m_i\)) an a complete orthonormal
set of eigenstates for \(A'\), with distinct eigenvalues
\(A_i\) (degenerate with respect to \(j\)) then the multiplicity
of the \(i\)th eigenvalue is \(m_i\) and the information \(I_A(\psi)\)
is defined to be: 

\[(2,4) \quad I_A(\psi) = \sum_i \left( \sum_j \langle \psi_j | \psi \rangle \ln \frac{\langle \psi_j | \psi \rangle}{\langle \psi_i | \psi \rangle} \right) \quad (\text{analog})\]

← The uniforma of this distribution lies in the fact
that any operator \(A''\) which distinguishes further
between any of the degenerate states leads to a
refinement of the relationship, in the sense of Thm.9,
and consequently has equal or greater information.

---

A non-algebraic operator thus represents the minimal refinement and preference minimal information. 

Since we shall be primarily concerned with
expansions and congruent distributions over complete
orthonormal nets \(E^2\), rather than distributions over
eigenvalues, we shall restrict \(E^2\) to the compactly
operator "onto" onto \(E^2\), by which we mean
any non-algebraic Hilbertian operator whose
eigenstates on the net \(E^2\). 

It is convenient to introduce a new notation
for projection operators which are relevant for a
specified operator. Let \(A\) be an operator with
eigenfunctions \(f_j\) and eigenvalues \(\lambda_j\) (denote
with respect to \(E^2\)). Then define projection \(A_j\) on
projection on the eigenspace of different eigenvalues to be: 

\[A_j = \sum_{i=1}^{m_i} [\phi_j]_{i,j}\]

To each such projection there is associated a number \(m_i\)
the multiplicity of the degeneracy, which is the
dimension of the \(i\)-th eigenspace. For this notation
the distribution over eigenvalues \(P_j\) becomes simply: 

\[P(\lambda_i) = \sum_{j} \langle A_i \rangle \psi_j\]

and the information, given by (2.4), becomes: 

\[I_A = \sum_i \frac{\langle A_i \rangle \psi_i}{m_i} \sum_j \frac{\langle A_i \rangle \psi_j}{m_i}\]

---

Similarly, for a pair of operators \(A\) in \(S_1\) and \(S_2\) in a composite system with state \(\Psi^S\), the joint distribution over eigenvalues is: (Ignore prior \(A, B, \text{and } m_1, m_2\)) 

\[(2.9) \quad P_{ij} = P(A_i, \Psi^S) = \langle A_i, B_j \rangle \Psi^S\]

and the marginal is: 

\[(2.9) \quad P_i = \sum_j P_{ij} = \langle A_i, (B_j)^S \rangle \Psi^S = \langle A_i, I^S \rangle \Psi^S \\ P_j = \sum_i P_{ij} = \langle I^S B_j \rangle \Psi^S\]

The joint information is given by: 

\[(2.10) \quad I_{AB} = \sum_{ij} P_{ij} \ln \frac{P_{ij}}{m_i m_j} = \sum_{ij} \langle A_i B_j \rangle \Psi^S \ln \frac{\langle A_i B_j \rangle \Psi^S}{m_i m_j} \\ \text{where } \langle \rangle \text{ is the multinomial of the eigenvalues } A_i \text{ and } B_j.\]

and the marginal is given by: 

\[(2.11) \quad I_A = \sum_i \langle A_i I \rangle \Psi^S \ln \frac{\langle A_i I \rangle \Psi^S}{m_i} \quad I_B = \sum_j \langle B_j I \rangle \Psi^S \ln \frac{\langle B_j I \rangle \Psi^S}{m_j}\]

We then define the correlation \(\{A, B\}\) as: 

\[(2.12) \quad \{A, B\} = \sum_{ij} P_{ij} \ln \frac{P_{ij}}{P_i P_j} = \sum_{ij} \langle A_i B_j \rangle \Psi^s \ln \frac{\langle A_i B_j \rangle \Psi^s}{\langle A_i I \rangle \Psi^s \langle B_j I \rangle \Psi^s}\]

and note that the expression does not involve the multiplications, as the information terms - which imply reflects the nullp, of correlation, on info measured. These expressions of course generate trivially to distribution over more than two variables. (Composite means of more than two variables.)

---

(1) 

(2) 

(3)

---

(2.16) \[ \left( \begin{array}{c} \xi \\ \eta \end{array} \right) \xi = \left( \begin{array}{c} N_{\xi} \\ \xi \end{array} \right) \left( \begin{array}{c} \phi_{e} \eta_{j} \gamma^{s} \end{array} \right) \phi_{e} \left( \begin{array}{c} N_{\xi} \\ \eta \end{array} \right) \left( \begin{array}{c} \phi_{m} \eta_{k} \gamma^{s} \end{array} \right) \phi_{m} \] 

\[= \sum_{e,m} \left( \phi_{e} \eta_{j} \gamma^{s} \right)^{*} \left( \phi_{m} \eta_{k} \gamma^{s} \right) \xi_{e,m} = \sum_{e} \left( \phi_{e} \eta_{j} \gamma^{s} * \phi_{m} \eta_{k} \gamma^{s} \right)\] 

\[= \mathcal{N}_{\xi} \mathcal{N}_{\eta} \mathcal{N}_{\gamma}^{s} \left( \phi_{e} \eta_{j} \gamma^{s} ^{*} \right) \left( \phi_{m} \eta_{k} \gamma^{s} \mathcal{N}_{\xi,m} \right) = \mathcal{N}_{\xi} \mathcal{N}_{\eta} \mathcal{N}_{\gamma}^{s}\]

---

We have we supposed \(P^S\) to be diagonal in this representation. We have thus constructed a canonical representation. (2.13). 

The density matrix \(P^S\) is also automatically diagonal,
by the choice of representation.
The choice of representation is a choice of basis in \(S\), which
corresponds to a choice of orthonormal wave functions: 

\[ 
\begin{aligned}
(\text{2.19}) \quad & \int_{S} \sum_{k} \left( \sum_{i} \left( \sum_{j} \left( \sum_{k} \left( \sum_{m} \left( \sum_{n} \left( \sum_{l} \left( \sum_{m} \left( \sum_{n} \left(\sum_{l} \left( \sum_{m} \left( \sum_{n}\right) \right) \right) \right) \right) \right) \right) \right. \right) \right) \right) \right) \right) \right) \left. \right) \right) \right) \right) \right) \right) \\
& = \sum_{k} a_{m}^{*} a_{n} \sum_{k} \delta_{kl} \delta_{km} \delta_{kn} = \sum_{k} a_{i}^{*} a_{j} \delta_{k} \delta_{kj} \\
& = a_{i}^{*} a_{j} \delta_{ij} = P_{i} S_{ij}
\end{aligned}
\]

where \(P_{i} = a_{i}^{*} a_{i}\) is the marginal distribution over \(\{S, S\}\). Similar computation shows that the elements of \(P^S\) are the same: 

\[ (\text{2.18}) \quad \int_{S} \sum_{k} a_{m}^{*} a_{n} \delta_{kl} = P_{k} \delta_{kl} \]

Thus in the canonical representation, both density matrices
are diagonal and have the same elements \(P_{k}\) which
give the marginal square amplitude distribution
and the ratio \([S]\) and \([S]\) form the basis of the
representation. 

Now any pair of operators \(A\) and \(B\) in \(S_2\)
which have as non- degenerate eigenfunctions the
pets \([S_2]\) and \([S_2]\) (i.e. operators which define the
canonical representation), are "perfectly" correlated
in the sense that there is a one-one correspondence
between their eigenvalues. The joint amplitude
distribution for eigenvalues \(\lambda_i\) of \(A\) and \(\lambda_j\) of \(B\) is: 

\[ (\text{2.19}) \quad P(\lambda_i, \text{and} \lambda_j) = P(S_i, \text{and} \lambda_j) = P_{ij} = a_{i}^{*} a_{j} S_{ij} = P_{i} S_{ij} \]

---

Therefore, the correlation between these sequences generates
\(\{A_i B_j\}^4\) is: 

\[(2, 20) \quad \{A_i B_j\}^4 = \sum_{i,j} P(\lambda_i = \lambda_j) \ln \frac{P(\lambda_i = \lambda_j)}{P(\lambda_i) P(\lambda_j)} = \sum_{i,j} P(\lambda_i = \lambda_j) \ln \left( \frac{P(\lambda_i = \lambda_j)}{P(\lambda_i) P(\lambda_i)} \right) = \sum_{i,j} P(\lambda_i = \lambda_j) \ln \sum_{i,j} P(\lambda_i = \lambda_j) \ln \frac{1}{P(\lambda_i) P(\lambda_j)} = \sum_{i,j} P(\Lambda_i = \Lambda_j) \ln \frac{1}{P(\Lambda_i) P(\Lambda_j)} = \sum_{i,j} P(\Lambda_i = \Lambda_j) \sum_{i,j} P(\Lambda_i = \Lambda_j) \ln \frac{P(\Lambda_i = \Lambda_j)}{P(\Lambda_i) P(\Lambda_j)} = \sum_{i,j} P(\lambda_i = \lambda_j) \sum_{i,j} P(\lambda_i = \lambda_j) \ln \frac{\frac{1}{P(\lambda_i) P(\lambda_j)}}{\frac{1}{P(\lambda_i) P(\lambda_j)}} = \sum_{i,j} P(\lambda_i = \lambda_j) \ln \int_{P(\lambda_i)}^{P(\lambda_j)} \frac{1}{P(\lambda_i) P(\lambda_j)} d\lambda_i d\lambda_j = \sum_{i,j} P(\lambda_i = \lambda_j) \ln \text{Tr} \int_{P(\lambda_i)}^{P(\lambda_j)} \frac{1}{1} d\lambda_i d\lambda_j = \sum_{i,j} P(\lambda_i = \Lambda_j) \ln \text{Tr} \int_{P(\lambda_i)}^{P(1)} \frac{1}{1} d\lambda_i d\lambda_j = \sum_{i} P(\lambda_i = \Lambda_j) \ln \text{Tr} \int_{\Lambda_i}^{P(\Lambda_j)} \frac{1}{1} d\lambda_i d\lambda_j = \sum_{j} P(\Lambda_i = \Lambda_j) \ln \text{Tr} \int_{\Lambda_i}^{1} \frac{1}{1} d\lambda_i d\lambda_j = \sum_{j} \text{Tr} \int_{\Lambda_i}^{1} \frac{1}{1 - \lambda_j} d\lambda_i d\lambda_j = \sum_{j} \text{Tr} \left( \int_{\Lambda_i}^{1} \frac{1}{1 - \lambda_j} \frac{1}{1 - \lambda_j} d\lambda_i d\lambda_j \right) = \sum_{j} \text{Tr} \left( \int_{\Lambda_i}^{\Lambda_j} \frac{1}{1 - \lambda_j} d\lambda_i d\lambda_j + \int_{\Lambda_j}^{\Lambda_i} \frac{1}{1 - \lambda_j} d\lambda_i d\lambda_j \cdot \frac{1}{1 - \lambda_j} d\lambda_i d\lambda_j \right).\] 

We shall denote this quantity by \(\{S_1, S_2, S_3, S_4\}\) and call it the canonical correlation of the subsystems \(S_1\) and \(S_2\) for the system state \(\Psi^S\). It is the correlation between any pair of nondegenerate subsystem operators which define the canonical representation. We note that in this representation, where the density matrix are diagonal \((6, 15)\) and \((6, 18)\), the canonical correlation is given by: 

\[(2, 21) \quad \{S_1, S_2, S_3, S_4\}^4 = -\sum_{i,j} P(\lambda_i = \lambda_j) P(\lambda_i = \lambda_j) = -\text{Trace} \left( P^S \ln P^S \right) = \text{Trace} \left( P^S \ln P^S \right) = -\text{Tr} \left( P^S \ln P^S \right).\] 

But the trace is invariant, so that (2.21) holds
given all nonpolnarly of the representation, and
we have therefore established the uniqueness of \(\{S_1, S_2, S_3, S_4\}^4\).
It is also interesting to note that this quantity
- Trace \((P^S \ln P^S)\) is just (part from a factor of Boltzmann's constant) 
just the entropy of a mixture of states characterized
by the density matrix \(P^S\). Therefore the entropy of this
mixture characteristic of a subsystem \(S_1\) for this
\(\Psi^S = \Psi^{S_1, S_2, S_3, S_4}\) is exactly matched by a correlation
information \(\{S_1, S_2, S_3, S_4\}\) which represents the correlation
between any pair of systems \(A, B\) which defines the
canonical representation. The situation is thus
quite similar to that of classical mechanics.

---

And so on, properly of the canonical map, so that 

Any operators \(A, B\) defining a canonical representation
have maximum marginal information (\(I_A \ge I_A\) all \(A \ge B\)) 

\(I_B \le I_B\) all \(B \le B\). The canonical map is (2.13), with
distributivity 

\(f_1, f_2\) sign of \(f_1 B\) map, and \(A, B\) any non-degenerate operators with eigenfunctions \(\{f_k\}, \{g_k\}\) 

where \(f = \sum c_{ik} f_k, g = \sum d_{ij} g_j\), then \(f^*\) in \(f\) only in \(i\). 

\[ (2.23) \quad \psi^* = \sum_{i,k} a_i c_{ik} d_{ij} g_j = \sum_{i,k} \left( \sum_{j} a_i c_{ik} d_{ij} \right) g_j g_j \]

and the joint singularities distribution for \(d_j, g_j\) is: 

\[ (2.27) \quad P_{k,e} = \left\| \left( \sum_i a_i c_{ik} d_{ij} \right) \right\|^2 = \sum_{j,m} a_i^* a_m c_{ik}^* c_{mk} d_{ij}^* d_{jm} e \]

which is marginalise: 

\[ (2.24) \quad P_t = \sum_k P_{k,e} = \sum_{j,m} a_i^* a_m c_{ik}^* c_{m,k} \sum_{e} d_{ij}^* d_{jm} e \]

\[ = \sum_{j,m} a_i^* a_m c_{ik}^* c_{mj} \delta_{jm} = \sum_i a_i^* a_i C_{ik}^* C_{ik} \]

and similarly 

\[ (2.25) \quad P_e = \sum_k P_{k,e} = \sum_i a_i^* a_i d_i^+ d_{ij} e \]

Then the corresponding marginal information \(I_A\) is: 

\[ (2.26) \quad I_A = \sum_k P_k \ln P_k = \sum_k \left( \sum_i a_i^* a_i c_{ik}^* c_{ik} \right) \ln \left( \sum_i a_i^* a_i c_{ik}^* c_{ik}^* \right) \]

\[ = \sum_k \left( \sum_i a_i^* a_i T_{ik} \right) \ln \left( \sum_i a_i^* a_i T_{ik} \right) \]

where \(T_{ik} = C_{ik}^* C_{ik}\) is doubly-tractable (\(\sum_i T_{ik} = \sum_i T_{ik} = 1\)).

---

\[
\begin{align*}
I_A &= \sum_k \left( \sum_i a_i^* a_i T_{ik} \right) \ln \left( \sum_i a_i^* a_i T_{ik} \right) \\
&\le \sum_i a_i^* a_i \ln a_i^* a_i = I_A
\end{align*}
\]

and we have proved that \(A\) has marginal marginal
information. Identical proof holds also for \(B\). 

While this result was proved only for non-
eigenvalue operators \(A\), its universality extends
to the generators case, since as a consequence
of our definition of the generator operator (2.4)
its information is still less than that of an
operator which removes the degeneracy. We have
thus proved: 

\[
\text{Thm: } I_A \neq I_A^{(y^s)}
\]

where \(A\) is any non-eigenvalue operator defining
conicality, and \(A\) is any operator (discrete spectrum). 

We should like to conclude the discussion of
the canonical representation by conjecturing that
in addition to the maximum marginal information
properties of \(A^s\), with definite representation
they also maximally correlated; by which
we mean that for any pair of operators \(C\) on \(S_2\),
\(D\) in \(S_2\): 

\[

---

a final topic for this section we point out that
the distribution is
We can see that the uncertainty
principle, can probably be proved in a stronger form
in terms of information. The usual form of this
principle is phrased in terms of variances, namely: 

\[ \nabla_x^2 \nabla_k^2 \geq \frac{1}{4} \quad \text{for all } \Psi(x) \]

where
\[ \nabla_x^2 = \frac{\partial^2}{\partial x^2} \left( \sum_{i=1}^n x_i^2 \right) \]

and
\[ \nabla_k^2 = \frac{\partial^2}{\partial k^2} \left( \sum_{i=1}^n k_i^2 \right) \]

(see the variance of \(A\) in \(y = \left( A - \langle A \rangle \right)^2 \), \(y = \nabla_x^2\) 

The complicated information for the uncertainty principle is
that properties of the form, 

\[ (2.2) \]

\[ \nabla_x^2 \]

---

Although this inequality has not yet been proved with complete rigor, it is more probable by the circumstances that equality holds for \(P(x)\) of the form \(Y(x) = \left(\frac{1}{2n}\right)^n e^{-\frac{x^2}{4n^2}}\) , the so-called "minimum uncertainty" which give normal distributions, and that furthermore the first variation of \((I_1 + I_2)\) vanishes for such \(Y(x)\). (See App.) This, although due to the fact that the first variation of \((I_1 + I_2)\) vanishes for such \(Y(x)\), it is at least a stationary value. The principle (2.14) is stronger than (2.13), since it implies (2.13) but is not implied by both. To see that it implies (2.13) we use the well-known fact (early established by a variation calculation)

---

Three quantities are to be computed through the formulas of the previously-chosen form the square
amplitude of the coefficient of the exponent of the
terms of the coefficients of the operators. 

If the form of the coefficients of the operators depends
on the coefficients of the operators (zero)
the state goes to eigenstate. 

We can prove this more precisely by considering
a family of state operators called according to varying
information for an operator A. 

\[ A \left( y_1 + y_2 \right) = A y_1 + A y_2 = A y_1 + A y_2 \] 

\[ \text{The required change in the state operator is:} \] (normalized)
\[ \text{(with distance)} \] 

This ⇒ limit exists?

---

In order to the calculation of the equilibrium operators, given by (2.12), the above exists a unique quantity \(\{S_1, S_2\}\), the canonical correlation, which has some special properties and may be regarded as the fundamental correlation between the two equilibrium \(\xi_1\) and \(\xi_2\) of the composite system \(S\). 

2.4 

\[
\begin{align*}
\text{(2.14)} \quad & \int_{S_1} S_2 = \lambda_1 S_{ij} \\
\text{and let the } \xi_i \text{ be the relative rates in } S_i \\
\text{for the } n_i \text{ in } S_2 : \\
\xi = N_2 \sum_j \left( \beta_j n_j \gamma_j^S \right) \phi_j \quad \text{(only for } \xi_2 \text{)} \\
\text{Then } \quad \xi = N_2 \sum_j \left( \beta_j n_j \gamma_j^s \right) \phi_j \quad \text{(only for } \xi_2 \quad \text{)} \\
\end{align*}
\]

Thus, in the same that for all the different spectrum operators \(A\) on \(S_1\) and \(B\) on \(S_2\), \(T_A \le T_B\) and \(T_B \le T_B\). 

where 

\[
\begin{align*}
\nabla_x^2 &= \langle x^2 \rangle \psi - \langle x \rangle \psi^2 \\
\nabla_k^2 &= \langle i \frac{\partial}{\partial k} \rangle \psi - \langle i \frac{\partial}{\partial k} \rangle \psi^2 = \langle \frac{\partial}{\partial k} \rangle^2 \psi + \langle \frac{\partial}{\partial k} \rangle^2
\end{align*}
\]