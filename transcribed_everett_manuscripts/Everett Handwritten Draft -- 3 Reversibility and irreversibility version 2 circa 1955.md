# Everett Handwritten Draft -- 3 Reversibility and irreversibility version 2 circa 1955.pdf

## §3. Reversibility and Invariability 

Let us return, for the moment, to the
probability interpretation of quantum mechanics
found on pages 1 as well as pages 2. Suppose
that we have a large number of identical systems
(ensemble), each of which is in a state \(\psi_i\) and that the \(i\)'th system
is in the state \(\psi_i\). Then for purpose of calculating
expectation values for generators over the ensemble,
the ensemble is represented by the mixture of
states \(\psi_i\) weighted with \(\frac{1}{N}\), where \(N\) is the number
of systems, for which the density operator is 

(3.1) 

\[P = \frac{1}{N} \sum_i [\psi_i]^2\]

where \([\psi_i]^2\) denotes the projection operator on \(\psi_i\). This
density operator in turn, is equivalent to a density
operator which is a sum of projections on orthogonal
states (the eigenstates of \(P\)): 

(3.2) 

\[P = \sum_i P_i [\psi_i] \quad (m_i, n_i) = \delta_{ij}, \quad \sum_i P_i = 1\]

So the only ensemble is always equivalent to a
mixture of orthogonal states, which representation
we shall henceforth assume. 

Suppose that a quantity \(A_i\) with (non- degenerate)
eigenstate \(\psi_i\) is measured in each system of
the ensemble. This measurement has the effect
of transforming each state \(N_i\) into the state \(\psi_i\)
with probability \(1/(\delta_{ij} N_i)^2\), i.e. it will transform
a "ensemble of systems in the state \(N_i\) into an
ensemble represented by the mixture whose density
operator is \(\sum_i ((\psi_i, n_i))^2 [\psi_i]\). Extending this result

---

to the case where the original ensemble is a mixture of the \(N_i\) weighted by \(P_i\) (3.2), we
find that the density operator \(P\) is transformed
by the measurement of \(A\) into the new density operator
\(P'\) : 

\[
\begin{align*}
P' &= \sum_i P_i \sum_j (m_j \phi_j)^2 [\phi_j] = \sum_j (\sum_i P_i (\phi_j (m_j \phi_j) m_j) [\phi_j]) \\
&= \sum_j (\phi_j) \sum_i P_i [m_j] \phi_j) [\phi_j] = \sum_j (\phi_j P_j [\phi_j]) [\phi_j]
\end{align*}
\]

This is the general law by which mixtures change
through Process 1. 

However, even when no measurement are
taking place the states of an ensemble are changing
according to Process 2, so that after a time interval t
each state \(\psi\) will be transformed into a state
\(\psi' = U \psi\), where \(U\) is a unitary operator. This
natural motion has the consequence that each
mixture \(P = \sum_i P_i [m_i]\) is carried into the mixture
\(P' = \sum_i P_i [U m_i]\) after a time t. But for every state \(f_j\) 

\[
\begin{align*}
P' f &= \sum_i P_i [U_t m_i] f = \sum_i P_i (U_t m_i) f U_t m_i \\
&= U_t \sum_i P_i (m_i) U_t^{-1} f m_i = U_t \sum_i P_i [m_i] (U_t^{-1} f) \\
&= (U_t P U_t^{-1}) f
\end{align*}
\]

Therefore
\(P' = U_t P U_t^{-1}\)
which is a general law for the change of a mixture
according to Process 2.

---

We are nonintuitive in which on nature
quit from any mixtire to another by means of
these two processes, it is for any pair \(P, P'\), this
exist quantity. A which can be measured and
unitary (time dependent) operators \(U\) such that \(P\) can
be transformed into \(P'\) by suitable application
of Process 1 and 2. We shall see that this is not
always possible, and that Process 1 can cause
invariable changes in mixtures. 

For each mixture \(P\) we define a quantity \(I_P\): 

\[
I_P = \text{Trace} (P \ln P)
\]

This number, \(I_P\), has the character of information. If
\(P = \sum_i P_i [n_i]\), a mixture of orthogonal states \(n_i\)
weighted with \(P_i\), then \(I_P\) is simply the
information of the distribution \(P_i\) over the eigenstates
of \(P\) (relative to the uniform measure). (Trace(\(P \ln P\))
is a unitary invariant and is proportional to the negative
of the entropy of the mixture, as discussed in (3.6).) 

Process 2 therefore has the property that it
leaves \(I_P\) unchanged, because 

\[
\begin{align*}
I_P &= \text{Trace}(P' \ln P') = \text{Trace}(U_P U_P^{-1} \ln U_P U_P^{-1}) \\
&= \text{Trace}(U_P P \ln P U_P^{-1}) = \text{Trace}(P \ln P) = I_P
\end{align*}
\]

Process 1, on the other hand, can decrease \(I_P\)
but never increase it. Accordingly to (3.3):

---

\[
\begin{align*}
P' &= \sum_j \left( \phi_j, P \phi_j \right) \left[ \phi_j \right] = \sum_{ij} P_{ij} \left| (n_j, \phi_j) \right|^2 \left[ \phi_j \right] \\
&= \sum_j P_j' \left[ \phi_j \right]
\end{align*}
\]

where \(P_j' = \sum_{ij} P_{ij} T_{ij}\) and \(T_{ij} = |(n_j, \phi_j)|^2\) is a doubly-stochastic matrix. But \(I_p = \sum_j P_j' \ln P_j'\) and \(I_p = \sum_{ij} \ln P_j\) with the \(P_j'\) omitted by \(T_{ij}\) implies by the theorem of information divergence for stochastic processes (\(I = S \in \mathcal{S}\)) that: 

\[
I_p' \le I_p
\]

Moreover, it can easily be shown by a slight strengthening of the theorem of \(I = S\) that strict inequality must hold unless (for each \(i\) such that \(P_i > 0\)) \(T_{ij} = 1\) for one \(i\) and 0 for the rest (\(T_{ij} = \delta_{ik_j}\)). This means that \(|(n_j, \phi_j)|^2 = \delta_{ik_j}\), which implies that \(N_j = \phi_{ik_j}\) — which says that the original mixture was already a mixture of eigenfunctions of the measurement. 

Therefore, we have answered our question, and
it is not possible to get from any mixture
to another by means of process 1 and 2. There
is an essential irreversibility to process 1,
since it corresponds to a stochastic process,
which cannot be compensated by flows 2, which
irreversibly kills classical mechanics.

---

Our theory of pure course mechanics is indivisible
now retent, must give equivalent results on the
subjective level, since it leads to Proca 1. Thus, there
nearing process will appear to be irreversible to any
observers (even though the composite system including
the observer changes its state reversibly). 

There is another way of looking at this apparent
irreversibility within our theory which recognizes only
process 2. When an observer performs an observation
this result is a superposition, each element of which
describes an observer who has perceived a particular
value. From this line forward there is no interaction
between the separate elements of the superposition (which
describe the observer as having perceived different results)
since each element separately obeys the wave equation.
Each observer describes by a particular element of the
superposition behaves in the future completely independently
of any events in the remaining element and he can no
longer obtain any information whatsoever concerning these
other elements. (They are completely unobservable to him). 

The irreversibility of the measuring process is
is therefore, within our framework, simply a subjective
manifestation reflecting the fact that in observation
process the state of the observer is transformed into
a superposition of observer states, each element of which
describes an observer who is irreversibly acted upon from
the remaining elements. While it is conceivable that some
critical agency could reverse the total wave function, such
a change cannot be brought about by any observer which is
represented by a single element of a superposition, since he is
partially powerless to have any influence on any other element.

---

There are therefore fundamental facts the
involve that an observer can obtain about
the state of the universe. It is impossible for
any observer to observe the total state function of
any physical system, since the process of observation
itself leaves no state to the system or the observer,
but only a composite system state in which the
system of system states are intuitively defined
in the way with the observer state. As soon as the
observation is performed the composite state is split
into a superposition, for which each element describes
a different off-jet-system state and an observer
with (different) knowledge of it. Only the totality
of these observer states, with their diverse knowledge,
contains complete information about the
off-jet-system state—but this is no possible
communication between the observers described by
these separate states. Any single observer can therefore
pursue knowledge only of the relative state
function (relative to his state) which is in any case
all that is of any importance to him.
We conclude this section by commenting on another
question which might be raised concerning irreversible
processes: Do it necessary for the existence of measuring
which can be correlated to other systems
preparations to have functional processes which involve
systems of a large number of degrees of freedom? The
such thermodynamic irreversible processes
possible in the framework of pure wave mechanics
with a reversible wave equation, and if so does
this circumstance pose any difficulties for our treatment
of measuring processes?

---

place
In this first, it is certainly not necessary for chiropractic
precise, uniformly additional degrees of freedom
to be present before an introduction which constitutes
an apparatus to modify - system can take place.
The simplified measuring process of 11- 53,
which involves only a system of one coordinate and
an apparatus of one coordinate and no further degrees of
freedom, supplies the same example. 

In the question of whether such precise are
possible within reversible wave mechanics we answer
yes, in the same sense that they are present in
classical mechanics, where the microscopic equations
of motion are also reversible. This type of irreversibility,
which might be called macroscopic irreversibility,
arises from a failure to separate "macroscopically
incompressible" states into "two" microscopic
states. 5 It has a fundamentally different character
than the irreversibility of forces 1, which applies to
micro-states of well and is peculiar to quantum mechanics.
Macroscopic irreversible phenomena are common
to both classical and quantum mechanics, since they
arise from our incomplete information concerning a
system, not from any intrinsic behavior
of the system. 6 

Finally, even when such initial precise
are involved, they present no new difficulties for
the treatment of measuring and observation processes
given here. We inspired no restrictions on the
complexity or number of degrees of freedom of measuring
apparatus or observers, and if any of these precise are
present (such as heat reservoirs, etc.) then these systems

---

are to be simply included as part of the apparatus or structure.