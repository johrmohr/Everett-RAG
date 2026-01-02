# Everett Draft -- 1 Composite Systems circa 1956.pdf

## §1. Composite systems 

This well known the of the state of a pair
of systems \(S_1\) and \(S_2\) are represented by points in
Hilbert space \(H_1\) and \(H_2\) respectively, then the
state of the composite system \(S_1 + S_2\) (the two systems \(S_1\) and \(S_2\) regarded as a single system) are represented exactly by
points of the tensor product \(H_1 \otimes H_2\). Thus if \(E_1, E_2\) is
a complete orthonormal set for \(H_1\) and \(H_2\) and \(S_1 \otimes H_2\) and \(S_2\) the
general state of \(S = S_1 \otimes S_2\) has the form:

\[
\psi^S = \sum_{i,j} a_{ij} S_i \otimes M_j \quad \text{where} \quad \sum_{i,j} a_{ij} \otimes M_j = 1
\]

This one
We shall call \(P_{ij} = a_{ij}^* a_{ij}\) the point dual square-
amplitude distribution of \(S\) over \(H_1 \otimes H_2\) and \(S_1 \otimes H_2\). On the
standard probabilistic interpretation \(a_{ij}^* a_{ij}\) represents the
joint probability for the state \(\psi^S\) with the
found in state \(E_1\) and \(S\) will be found in \(M_j\). Following
the probabilistic model we now derive some distributions
from a state \(\psi^S\). Let \(A\) be operator in \(S\) with
eigenfunctions \(\phi_1\) and eigenvalue \(\lambda_1\). The eigenfunction \(S_1\)
with eigenfunction \(\phi_2\), eigenvalue \(\lambda_2\). Then the
joint distribution of \(S\) over \(H_1 \otimes H_2\) and \(H_1 \otimes H_2\) is:

\[
P_{ij} = P(\phi_1 \otimes \phi_2) = |(\phi_1 \otimes \psi^S)|^2 = \frac{1}{2}
\]

The marginal distribution of \(S\) over \(H_1 \otimes H_2\) and of \(H_1 \otimes H_2\)
are:

\[
P_i = P(\phi_i) = \sum_j P_{ij} = \sum_j |(\phi_i \otimes \psi^S)|^2
\]

\[
P_j = P(\phi_j) = \sum_i P_{ij} = \sum_i |(\phi_i \otimes \psi^S)|^2
\]

---

\[ \text{relation } [\phi] = \text{party on } \phi = \phi(\{\phi_i\}) \]

This specification is in fact the expectation for the case in which no measurement itself (identifiable) is performed in the other subsystem. 

We remark at this point that this ambiguity exists when \(E[\phi, \phi_i, \gamma^2] = 0\) (we first have \(|\phi\rangle\) is uninterpreted for this representation, since it only shows states that are regarded as the relative state, for this term \(\gamma^2 \phi \phi\) will occur in (1,3) with coefficient zero. 

Josef 

L 

There does not, in general, exist anything like a state for one subsystem of a composite system. There's no subsystem do not possess states indistinguishable of the states of the remainder of a system, so that the subsystem states are correlated. One can arbitrarily choose a state for one subsystem, and add to the relative state for the other subsystem. Thus we can proceed with a fundamental relativity of states, implied by the formalism of composite systems. This meaning leads to the absolute state of a subsystem -- one can only add the state relative to a given state of the remainder of the system.

---

and the conditional distribution \(P_j^i\) and \(P_j^i\) are: 

\[(1.4) \quad P_j^i := P(\theta_i \text{ conditional on } \theta_0) = \frac{P_{ij}}{P_0}\]

\[P_i^i := P(\theta_i \text{ conditional on } \theta_1) = \frac{P_{i1}}{P_1}\]

We next define conditional expectation of an operator \(A\) on \(S_j\), conditioned on \(\theta_j\) in \(S_j\), \(E_{P_j} \Theta_j [A]\): 

\[(1.5) \quad E_{P_j} \Theta_j [A] = \sum_i \lambda_i P_i^i = \frac{1}{P_0} \sum_i \sum_j P_{ij} \lambda_i = \frac{1}{P_0} \sum_i \lambda_i (P_0 \Theta_j \mathbf{v}^j)^2 = \frac{1}{P_0} \sum_i \lambda_i (P_1 \Theta_j \mathbf{v}^j)^2 (P_1 A P_0)\]

And finally within the marginal expectation of \(A\) on \(S_j\): 

\[(1.6) \quad E_{P_j} [A] = \sum_i P_i \lambda_i = \sum_{ij} \lambda_i P_i = \sum_{ij} (P_0 \Theta_j \mathbf{v}^j)^2 (P_1 A P_0)\]

We shall now introduce projection operators to get more forms of the conditional and marginal quantities which will be directly used in the formulae of the formulae of the generalisation of the chosen basis. We let \([0_1]\) and \([0_2]\) be projections on \(P_1\) in \(S_1\) and \(P_2\) in \(S_2\) respectively, and let \(I_1^1\) and \(I_2^2\) be the identity operators in \(S_1\) and \(S_2\). 

We shall now introduce projection operators to get more forms of the conditional and marginal quantities which will be used in the formulae of the generalisation of the chosen basis. We let \([0_1]\) and [0_2] be projections on \(P_1\) in \(S_1\) and \(P_2\), respectively, and let \(I_1^1\) and \(I_2^2\) to the identity operators in \(S_1\) and \(S_2\). 

\[(1.7) \quad \mathbf{v} = \sum_{ij} (P_0 \Theta_j \mathbf{v}^j) P_0 \Theta_j \quad \text{for any correlation function}\]

\[< [0_1] [0_2] \mathbf{v}^2 = (\mathbf{v} [0_1] [0_2] \mathbf{v})^2 = (\sum_{klm} (P_0 \Theta_j \mathbf{v}^j) (P_0 \Theta_k \mathbf{v}^k) \sum_{mn} (P_0 \Theta_l \mathbf{v}^l) (P_0 \Theta_m \mathbf{v}^m))^2 = \sum_{klm} (P_0 \Theta_j \mathbf{v}^j) ((\sum_{mn} (P_0 \Theta_l \mathbf{v}^l) (P_m \mathbf{v}^m))^2) = P_{ij}\]

---

So that the joint distribution is given simply by \(\mathbb{P}(X, Y)\) .
For the marginal: 

\[
\begin{align*}
P_i &= \sum_j P_{ij} = \sum_j \langle \mathbb{E}[X] \mathbb{E}[Y] \rangle^{s} = \langle \mathbb{E}[X] \mathbb{E}[Y] \rangle^{s} \\
&= \langle \mathbb{E}[I^2] \rangle^{s}
\end{align*}
\]

and we see that the marginal distribution over the \(P_i\) is independent of the set \(\{\Theta_i\}\) chosen in \(S_2\). This has the consequence in the ordinary interpretation that the measurement expected outcome of measurement in one subsystem of a composite system is not influenced by the choice of quantity to be measured in the other subsystem, unless the outcome of a measurement in the other subsystem is performed in the other subsystem. This no measurement in \(S_2\) can affect the expected outcome of a more in \(S_2\), or long as the result of the measurement remains unknown. The one in quiet differs, however, if this result is shown, and we must turn to the conditional distributions and expectations in such a case. 

We now introduce the concept of relative
state function, which will play a central role in our
interpretation. Consider a composite system \(S_0 \cup S_1 \cup S_2\)
in state \(\gamma^S\). To every state \(I\) of \(S_2\) we associate
a state \(\gamma_{I^S}\) of \(S_1\) called the relative state in \(S_2\) for \(I\). 

\[
\begin{align*}
Df: \gamma_{I^S} &= N \sum_i \langle \Theta_i \gamma_{I^S} \rangle^{s} \Theta_i^{s} \\
&= \langle \Theta_i \gamma_{I^S} \rangle^{s} \text{ in any complete orthonormal state } S_1 \\
&\text{and } N_i \text{ a normalization constant.}
\end{align*}
\]

---

The first property of \(\mathcal{H}^n\) is its uniqueness, that is, its dependence upon the choice of the basis \(\{e_i\}\) is only apparent. To prove this, choose another basis \(\{e_j\}\) with \(e_j = \sum_k b_{jk} e_k\). Then \(\sum_k b_{jk}^* e_k = \delta_{jk}\), and: 

\[
\begin{align*}
\sum_k (\delta_k \eta, \psi^s) \phi_k &= \sum_k (\sum_j b_{jk} \eta, \psi^s) (\sum_k b_{jk} \phi_k) \\
&= \sum_{jk} (\sum_k b_{jk}^* b_{jk}) (\eta, \psi^s) \phi_k = \sum_{jk} \delta_{jk} (\eta, \psi^s) \phi_k \\
&= \sum_k (\delta_k \eta, \psi^s) \phi_k \tag{10}
\end{align*}
\]

The second property of the relative state \(\mathcal{H}(t)\) which justifies its name, is that it correctly gives the conditional expectations of all operators in \(S\), conditional to \(\Theta_j\) in \(S_z\). At first let \(A\) be an operator in \(S_z\) with operators \(B\). Then: 

\[
\begin{align*}
(A) \psi_{net} &= (\psi_{net}, A \psi_{net}) \\
&= (N \sum_i (\phi_i \psi_j^s) \phi_j A N \sum_m (\phi_m \phi_j^s) \psi_m^s) \phi_m \\
&= N^2 \sum_{ijm} (\phi_i \phi_j \psi^s)^* (\phi_m \phi_j \psi^s) \lambda_m S_{ijm} \\
&= N^2 \sum_i \lambda_i f_{ij}
\end{align*}
\]

At this point \(N^2\) can be conveniently evaluated by using (1.10) to compute \(\langle I \rangle \psi_{net} = N^2 \sum_i f_{ij} = N^2 f_j = 1\) so that \(N^2 = \frac{1}{f_j}\). 

\[
(N^2 = \frac{1}{f_j})
\]

---

Substitution of (1.11) in
Continuity the decomposition of (1.10) implies: 

\[(1.12) \quad \langle A \rangle \psi_0^0 = \frac{1}{P_0} \sum_i \lambda_i P_0 = \sum_i \lambda_i P_0^0 = \text{Exp} \Theta_i [A]\]

And we have proved that the conditional expectation
of operators are given by the relative state. (This
of course includes the conditional distributions themselves,
since they may be defined as expectations of projection
operators.) 

Another with little property of the relative state \(\psi_0^0\)
is that it depends only upon the single state \(\Theta_i\) in
\(S_j\) of the three elements of an orthogonal basis
in the orthogonal space to \(\Theta_i\). 

An important representation of a composite
system state \(\psi^S\) in terms of an orthonormal set \(\{\Theta_i\}\) in
and the state relative state \(\{\psi_0^0\}^S\) in: 

\[(1.13) \quad \psi^S = \sum_{ij} (\phi_i \Theta_j \psi^S) \phi_j = \sum_j \left[ \sum_i (\phi_i \Theta_j \psi^S) \phi_i \right] \Theta_j = \sum_j \frac{1}{N_j} \left[ N_j \sum_i (\phi_i \Theta_j \psi^S) \phi_i \right]\Theta_j = \sum_j \frac{1}{N_j} \psi_{\text{rel}}^0 \Theta_j, \quad \text{where } N_j \text{ is the number of } \psi^S \text{ in the system.}\]

Thus, for any orthonormal set in one subsystem, the
State of the composite system is a superposition of
elements coming of a state of the given set and its
relative state in the other subsystem. We notice further,
that a particular element \(\psi_0^0 \Theta_j\) is quite independent
of the choice of basis \(\{\Theta_i, \text{rel}_j\}\) for the orthogonal space of \(\Theta_j\)
since \(\psi_0^0\) depends only on \(\Theta_j\) and not on the other \(\Theta_i\)'s.

Small
2

---

Now that
Since we have found states which correctly give
conditional expectation, we might imagine as to whether
this ever yields values which give marginal expectation.
The answer to this question is no. Let us compute the
marginal expectation of A in S using representation (1.13):

\[
(1.19) \quad \text{EXP}[A] = \langle A \rangle \gamma^S = \left( \sum_j \frac{1}{N_j} \gamma_{\text{net}}^S \Theta_j A I \sum_k \frac{1}{N_k} \gamma_{\text{net}}^S \Theta_k \right)
\]

\[
= \sum_j \frac{1}{N_j N_k} \left( \gamma_{\text{net}}^S A \gamma_{\text{net}}^S \right) \otimes_j S_j
\]

\[
= \sum_j \frac{1}{N_j^2} \left( \gamma_{\text{net}}^S A \gamma_{\text{ne}}^S \right) = \sum_j P_j \langle A \rangle \gamma_{\text{net}}^S
\]

Now suppose that there exists a state in \( S_j \), which
correctly gives the marginal expectation (1.14) for all operators A
(i.e. \( \text{EXP}[A] = \langle A \rangle \gamma_j \)). One such operator in \( \gamma_j \), the
projection on \( \gamma_j \), for which \( \langle \gamma_j \rangle \gamma_j = 1 \). But, from
(1.14), \( \text{EXP}[\gamma_j] = \sum_j P_j \langle \gamma_j \rangle \gamma_j \) which is \( \leq 1 \)
unless \( P_j = 0 \) or \( \gamma_j \otimes_j \gamma_{\text{net}}^S = \gamma_{\text{net}}^S \) for all \( j \), which is not
generally true. Therefore, there exists no general
no state for S which correctly gives marginal expectation.

Even though this and no state describing marginal
expectation, there is a mixture of states, namely
the states \( \gamma_{\text{net}}^S \) weighted with \( P_j \) which yields the
desired expectation. This distinction between a mixture M,
of states \( \Theta_j \) weighted by \( P_j \), and a pure state \( \gamma_{\text{net}}^S \)
is superposition, \( \gamma = \sum_j P_j \Theta_j \) in that there are no
interference phenomena between the various states of
mixture. The expectation for a pure state \( \gamma_{\text{net}}^S \)
is \( \text{EXP}[A] = \sum_j P_j \langle A \rangle \Theta_j = \sum_j P_j (\Theta_j A \Theta_j) \), which
the expectation for the pure state \( \gamma_j \).

---

\[ \langle A \rangle \psi = \left( \sum_{i,j} a_i^* a_j A \sum_{i,j} a_i^* a_j \right) = \sum_{i,j} a_i^* a_j \left( \psi_i A \psi_j \right) \quad \text{which is not the norm as the mixture with weights } P_i = a_i^* a_i \]

due to the presence of the interference terms \((a_i^* A a_j)\) in \(\psi_i\).

It is convenient to represent nuclear mixtures
by a density matrix \(P\).

If the mixture omits of
the states \(\psi_i\) weighted by \(P_i\) and if we are working
in a basis consisting of the complete orthonormal set \(\{a_i^*\}\)

when \(\psi_i = \sum_{j} a_i^* a_j P_j\), then we define the element
of the density matrix for the mixture to be:

\[ (1.15) \quad P_{ke} = \sum_j P_j a_i^* a_k \quad a_i^* = (a_i^* \psi_j) \]

If A is any operator, with matrix \(P\). \(A_{ij} = (a_i^* A a_j)\) in the
chosen basis, then its expectation for the mixture is: 

\[ (1.16) \quad \mathbb{E}_{XP}[A] = \sum_j P_j (\psi_j A \psi_j) = \sum_j P_j \left[ \sum_{i,k} a_i^* a_k a_j^* (a_i A a_k) \right] = \sum_{i,j,k} ( \sum_j P_j a_i^* a_k a_j^* ) (a_i A a_k) = \sum_{i,j,k} P_{ik} A_{ij} \]

\[ = T_{race}(PA) \]

Therefore any mixture is adequately represented by a density mixture.
Note also that \(P_{ki} = P_{ek}\) is the Pii Hermitian. 

Let us now find the density matrix \(P^2\) and \(P^3\)
for the suboptimal \(S_1\) and \(S_2\) of a system \(S_1 S_2 S_1\) in state \(\psi^2\).
Further let us choose the orthonormal basis \(\{a_i^*\}_{i=1}^3\) in
\(S_1\) and \(S_2\) resp, and let \(A\) be an operator in \(S_1\), \(B\) an operator
in \(S_2\). Then:

---

\[(1.12) \quad \mathbb{E}[\rho[A]] = \langle A \rangle \psi^S = \left( \sum_{i,j} (\xi_i \eta_j \psi^S) \xi_i \eta_j A \sum_{i,j,m} (\xi_i \eta_j \psi^S) \xi_i \eta_j \right)\]

\[= \sum_{i,j,m} (\xi_i \eta_j \psi^S)^* (\xi_i \eta_m \psi^S) (\xi_j A \xi_i) (\eta_j \eta_m)\]

\[= \sum_{i,j} \left[ \sum_j (\xi_i \eta_j \psi^S)^* (\xi_i \eta_j \psi^S) \right] (\xi_j A \xi_i)\]

\[= Trace \left( \rho^S A \right)\]

where we have defined \(\rho^S\) in the \(\{\rho_i\}\) basis to be: 

\[\rho_{ei}^S = \sum_j (\xi_i \eta_j \psi^S)^* (\xi_i \xi_j \psi^S)\]

In similar fashion we find that \(\rho^S\) is in \(\{\eta_i\}\) basis: 

\[(1.19) \quad \rho_{mm}^S = \sum_i (\xi_i \eta_i \psi^S)^* (\xi_i \eta_i \psi^S)\]

It can be easily shown that here again the dependence of \(\rho^S\) upon the choice of basis \(\{\eta_i\}\) in \(S_2\) and of \(\rho^S\) upon \(\{\xi_i\}\) is only apparent. 

In summary, we have seen in this section that
a state of a composite system leads to joint distribution
probability which are generally not independent. Conditional
distribution and expectation are often from relativistic
nature; marginal distribution and expectation are given by
density matrices. 

There is, in general, no single state of a subsystem,
which is independent of the state of the other subsystem.
Subsystem do not possess states independently, only relations
between states of subsystems - i.e. they are correlated. One
can arbitrarily choose a state for one subsystem, and be led to
relative state for the other. There thus is a joint relativity of state

---

implied by the formalization of computer systems. This
meanings to each state of a subsystem one can
only ask the relative state of a given state of the subsystem.