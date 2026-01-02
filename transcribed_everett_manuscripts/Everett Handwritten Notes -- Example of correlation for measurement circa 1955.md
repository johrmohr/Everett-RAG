# Everett Handwritten Notes -- Example of correlation for measurement circa 1955.pdf

In order to illustrate the manner in which correlation builds up in a system, we consider a simplified measuring process introduced by von Neumann. Let \(g\) represent the system variable of interest and \(r\) the appropriate variable. Assume that they are initially independent so that the combined curve function is \(H = \phi(g)N(r)\) (where \(\phi(g)\) is the initial system average function) and \(N(r)\) is the statistical parameters function. Furthermore assume that the means are sufficiently large, so the time of measurement function(s) is small. That the kinetic portion of the energy may be neglected, so that during the time of measurement the distribution shall consist only of an interaction, which we shall take to be:

1. \(H_1 = -ik g \frac{\partial}{\partial r}\)

   Then according to the Schrödinger equation:

2. \(-\frac{\partial}{\partial t} \psi_t(g,r) = i \hbar g \frac{\partial}{\partial r} \psi_t(g,r)\)

   which has the general solution:

3. \(\psi_t(g,r) = f(g,r - gt)\)

   Since our initial wave function was \(\psi = \phi(g)N(r)\) we arrive at the final solution:

4. \(\psi_t(g,r) = \phi(g)N(r - gt)\)

---

or, translating into square amplitude (amplitude). 

\[P_t(g,r) = P_1(g) P_2(r-tg)\]

where \(P_1(g) = P^*(g) P(g)\), \(P_2(r) = N^*(r) N(r)\) 

and we note that for a fixed time, the distribution of \(r\) is translated by an amount depending upon the value of \(g\), which the marginal distribution of \(g\) is unchanged. We see that a correlation has been introduced between \(g\) and \(r\) by this interaction of \(r\) is instructive to see quantitatively how for the correlation there takes place. We note that: 

\[I_{QR}(t) = \int P_t(g,r) \ln P_t(g,r) dg dr = \int P_t(g)P_t(r-g) \ln P_t(g)P_t(r-g) dg dr \\
= \int \int P_t(g) P_2(\omega) \ln P_t(g) P_2(\omega) d\omega dg \\
= I_{QR}(0)\]

So that the information in the joint distribution does not change, furthermore, since the marginal distribution for \(g\) is unchanged, \(I_Q(t) = I_Q(0)\), and the only quantity which can change is the marginal information \(I_R(t)\) which is: 

\[I_R(t) = I \left\{ P_t(r) = \int_{-\infty}^{\infty} P_t(g) P_2(r-g) dg \right\}\]

using theorem (E-8-penile) this implies that 

\[I_R(t) \le I_Q(0) - \ln t\]

---

so that except for an additive constant for
initial information \(I_R\) tends to diminish at least
as fast as the time. This implies
that for the correlation : 

\[
\{Q, R\}_t^2 = I_R^{(t)} - I_R^{(t)} I_Q^{(t)} = I_{RQ}^{(t)} - I_Q^{(t)} - I_R^{(t)}
\]

but at \(t=0\) the distribution for \(RQ\) is independent
no that \(I_{RQ}^{(t)} = I_R^{(t)} + I_Q^{(t)}\), and substitution of
this relation together with \(8\) into \(7\) results in:

\[
\{Q, R\}_t^2 \equiv \frac{\Delta x}{I_R^{(t)}} \quad \text{(check this)}
\]

We notice that this maximum has the property
that it does not change the marginal system distribution
nor does the apparatus indicate any definite system
value. However, one can look at the combined
wave function as a superposition of states, continuity
definite \(g\) values, with correspondingly displaced
apparatus states \(i \in \mathcal{C}\) (see discussion in the section of relative \(W^5\)).

\[
\mathcal{H} = \int \phi(g') \delta(g - g') M(r - g' t) dg'
\]

which is a superposition of states \(\mathcal{H}_g = \delta(g - g') M(r - g' t)\)
in which the system has the definite eigenvalue \(g'\), and
which the apparatus is displaced from its original
position by an amount \(g' t\), superposed with amplitudes \(g'\).

---

Conversely, if we transform to the representation where
the apparatus is in a definite state, we write: 

\[ \Psi = \int \frac{1}{N_r} \xi_r(g) S(r-r') dr' \]

\[ \text{where } \xi_r(g) = N_r \varphi(g) N(r-gt), \quad \frac{1}{N_r} = \sqrt{\int \varphi(g) N(r-gt) dg} \]

where the functions \(\xi_r(g)\) are nearly eigenstates
for \(g = \frac{r'}{t'}\), i.e. as \(t \to \infty\), on the \(N(r)\) is sufficiently
peaked (near \(S(r)\)) then \(\xi_r(g)\) approaches \(S(g-\frac{r'}{t'})\).
Then the state of the combined system can be regarded
as a superposition of states each of which corresponds
to a definite apparatus value, \(r'\) and for which the
system state is nearly the eigenfunction correspondingly
to \(g = \frac{r'}{t'}\). In other words we are confronted with
a superposition of separate, each of which has
recorded the definite value, and relative to which
the system is left in an approximate eigenstate
of the measurement. The discontinuities "jump" into
on eigenstate is thus only a relative proportion
equivalent upon our method of decomposition of the
total wave function into the superposition and relative
to a particularly chosen apparatus variable. So far
as the completeness is concerned all elements of
the superposition exist simultaneously, and the
entire process was quite continuous. 

Extend similarly to General Observer, formally
on a measurement with memory.

---

remark upon the generality of the results. 

namely for any interaction
which yields eigenstates \(\phi_i\) 

\[ \Phi_i N \rightarrow u_i N^i \]

then results \(\langle \Phi_i \phi_j \rangle N\) 

\[ \text{into} \rightarrow \langle \Phi_i \phi_j \rangle N \]

That is, if any particular results are
to be expected when the system is in one
or another of a set of eigenstates \(\phi_i\). 

Then the result for system state \(\Phi_i \phi_j\)
will simply be the superposition of the special results
superposed with amplitudes \(a_i\). 

This is completely general, and depends
only upon the linearity of the corresponding
i.e. the superposition principle for whole functions
satisfying the wave equation. 

Then it follows that
for interaction in any quantum theory, field theory,
or other theory.

---

This in turn implies that any solution for which an observer will observe a definite system value when the system is in an eigenstate is such that if the system is not in an eigenstate the result of observation will be a superposition of observers who observe each particular system value, superposed with the system operators amplitudes. This is inapplicable conclusion of Quantum mechanical treatment of observing