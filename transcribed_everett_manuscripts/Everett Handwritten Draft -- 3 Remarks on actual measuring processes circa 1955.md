# Everett Handwritten Draft -- 3 Remarks on actual measuring processes circa 1955.pdf

## §3. Remarks on actual measuring process: 

In the we discussed abstract measuring process, where we considered the measurement to be simply a direct coupling between two systems, the object system and the apparatus observer. In actuality, for microscopic measurements, there is a whole chain of intervening systems linking the object system to the observer, individual atoms mean that each link becomes correlated with its predecessor, which results in an amplification of effects from the microscopic object system to a macroscopic apparatus, and then to the observer. 

The actual amplification of microscopic effects to macroscopic effects depends upon the ability of the state of the state of an microscopic system (particle, for example) to become correlated with the state of a very large number of the microscopic systems which we shall call the detection system, or detector (such as the gas atom of a given count, or the water molecule of a cloud chamber). This is accomplished by arranging the conditions so that the state of the individual systems of the detector are metastable, and further that the falling of one system from the metastable state is sufficient to reduce others, so that a chain reaction is induced from one of the states to all of them (in a large number of them). This is the case, for example, in a Cesium counter, where the gas atoms are metastable against ionization, and when the products of the ionization of one atom cause further ionization in a cascade process. Similar considerations hold for cloud chambers and photographic films.

---

a) \(\sum x_i \ln \left(\frac{\sum x_i}{\sum a_i}\right) \leq \sum x_i \ln \frac{x_i}{a_i}\)

b) \(\int f(x) dx \ln \left(\frac{f(x)}{g(x)}\right) \leq \int f(x) \ln \frac{f(x)}{g(x)} dx\)

\[
= \int f(x) \ln f(x) - \int f(x) \ln g(x) dx
\]

\[\sum_{i} T_{ij} P_i\]

\[\Rightarrow \left(\sum_{i} T_{ij} P_i\right) \ln \left(\frac{\sum_{i} T_{ij} P_i}{\sum_{i} T_{ij}}\right) \leq \sum_{i} T_{ij} P_i \ln \frac{\sum_{i} T_{ij} P_i}{\sum_{i} T_{i}}\]

\[\Rightarrow \left(\sum_{i} T_{ij} P_i\right) \ln\left(\sum_{i} T_{ij} P_i\right) \leq \sum_{i} T_{ij} P_i \ln P_i + \left(\sum_{i} T_{ij} P_i\right) \ln\left(\frac{\sum_{i} T_{ij} P_i}{\sum_{i} T}\right)\]

\[\Rightarrow \sum_{j} \left(\sum_{i} T_{ij} P_i\right) \ln\left(\left(\sum_{i} T_{ij} P_i\right)\right) \leq \sum_{i} \left(\sum_{j} T_{ij} P_i\right) \ln P_i + \sum_{j} \left(\sum_{i} T_{ij} P_i\right)\ln\left(\frac{\sum_{i} T_{ij} P_i}{\sum_{i}} \right)\]

---

It is also interesting, on a wide range, to give
an example of the usefulness of the more general definition
of relativistic information. Suppose that we have a stationary
stochastic process with a finite number of states \(S_j\), and
that the process occurs at distinct times \(t_1, t_2, \ldots\)
at which time the transition probability from the state
\(S_j\) to the state \(S_j\) is \(T_{ij}\). The probabilities \(T_{ij}\) then form
what is called a stochastic matrix, i.e. the elements are
between 0 and 1 and \(\sum_j T_{ij} = 1\). Of any time
\(t\) the probability distribution over the states is \(\sum_j T_{ij}\) then
at the next time it will be \(P_{ij} = \sum_i P_{ij}^t\). \(T_{ij}\).

On the special case where the matrix is doubly-
stochastic, which means that \(\sum_j T_{ij}\) are well and \(\sum_j T_{ij}\) equal
unity, and which amounts to a principle of detailed
balancing holding, it is known that the entropy of
a probability distribution over the states, defined as
\(H = -\sum_i p_i \ln p_i\), is a monotonic increasing function
of time (See Rev. mod. Phys. 13). The entropy is,
known, simply the negative of the information relative
to the uniform measure.

---

One can extend this result to the more general case of (simply) stochastic matrices only if one defines the entropy to be the negative of the information relative to the stationary state measure, instead of the uniform measure. The stationary distribution \(P_i^*\) is that which does not change with time (if possible, \(\sum_{j=1}^{n} P_{ij}^* = \binom{n}{j}\)) so that the general definition of entropy for such a process becomes:

\[
H = -\sum_{i} P_i \ln \frac{P_i}{P_i^*}
\]

---

Stella \(S_i^n\) \(T_i^n\) matrix \(a_i^n\) 

\(p_j^{n+1} = \sum_i p_i^n T_j^n\) additive \(a_j^{n+1} = \sum_i p_i^n T_j^n\) 

Then if \(I^n = \sum p_i^n \ln \left( \frac{p_i^n}{a_i^n} \right)\) 

Then \(I^{n+1} \le I^n\)

---

By specifying to stationary processes, where
\(T_{i,j}^{m} = T_{i,j}^{m} (m \in \mathbb{N})\) and the state remain
constant, the information measure becomes simply the
stationary measure, which satisfies 

\[a_j = \sum_i a_i T_{i,j}\]

(proportional to stationary pdf distribution). 

Finally, in the case of Daily Zip, median 

Better original form than Geman's successively.

---

We now introduce ideal observers into our scheme, by which we shall have in mind machines endowed with memory appropriate (environmental) and programming memory by which, in the mean of recording choice capable of registering past memory data and machine configuration. We suppose that the machine is so constructed that its present actions shall be determined by its current memory data, as well as by the contents of its memory, so that its actions can be dependent upon past memory data as well. Thus such a machine will be capable of performing a series of observations (measurements), and furthermore of deciding upon future experiments on the basis of past results. We note that if we combine current memory data to be immediately recorded in the memory, then the actions of the machine at a given instant can be regarded as a function of the memory contents only, and the state of the machine is completely characterized by its state of its memory. For such machines we are justified in using phrases such as "the machine has provided A," "the machine is aware of A," if the occurrence of A is represented in the memory, since the machine's future behavior will then be based upon the sequence of A. In fact, all of the customary language of subjective experience is quite applicable to such machines, and forms the most natural and useful mode of expression when dealing with the properties of such machines, as we will show to individuals who work with complex automata.

---

Suppose that we have such a machine which is arranged so as to make a long sequence of measurements upon identical quantum mechanical systems \(S_1, S_2, \ldots, S_n\), each of which has the same state function \(P_1 = \gamma_1 S_1, P_2 = \gamma_2 S_2, \ldots, P_n = \gamma_n S_n\). We suppose this machine is measuring the property \(A\), and that it is arranged that a measurement upon an eigenstate of \(A\) will definitely result in the recording of this corresponding eigenvalue \(k\) in the memory. Thus if the state \(V_i\) is an eigenstate of \(A\) then after \(n\) measurements have taken place this memory state of this machine will be characterized by the definite sequence \((M_1, M_2, \ldots, M_n)\) of \(n\) identical numbers \(a_i\), which represent the \(i\) th eigenvalue, and hence also the state of this machine will be characterized. 

By, on the other hand, \(V_i\) is not an eigenstate of \(A\), but a superposition \(V = \sum a_i P_i\), then according to which we said in the last section the result of the first measurement will be a superposition of total states, each of which the system is left in the state \(P_i\), and the memory definitely records the eigenvalue \(k_i\). We write the total state then, after this first measurement; 

\[V^T = \sum a_i P_i M_i (a_i)\]

However, after the first measurement, when the machine analyzes \(S\) have ceased to interact, each element of the superposition will therefore behave completely independently of the others, since each operates after the previous operation, so that for the next measurement each element of the superposition, \(M_i(a_i)\)

---

same notion in physical behavior of
will show like a definite and independently
existing machine of state \(M_1(u_i)\). Therefore, since
after the second measurement each machine state
\(M_2(u_i)\) will go into the superposition: 

(2.2) \(\sum_j a_j M_1(u_i) M_2(u_j)\) (where we have omitted, for convenience, the superscripts to which are understood to be the corresponding eigenstates) 

this total state will be the double superposition: 

(2.3) \(\sum_{ij} a_i a_j M_1(u_i) M_2(u_j)\) 

and thus in general after \(n\) measurements the
total state will be the superposition 

(2.9) \(\sum_{ijk \dots k} a_i a_j \dots a_k M_1(u_i) M_2(u_j) \dots M_n(u_k)\)
so that we are confronted with a superposition between
of machines (called elements), each of which
remembers a distinct sequence of definite
eigenvalues, and relative to which the systems
are left in the corresponding eigenstates. Note that
we use the double superposition of machines,
rather than superposition of machine states, a
trivially which is justified by the completeness
that each element of the superposition behaves
like a definite and independently existing machine
with the corresponding state as numbered above.

---

So much for the qualitative interpretation. To establish quantitative results we must place a measure on the plane of elements of the final superposition, in order to make assertions about the two properties which will appear to hold for almost all observers (trajectories) and which shall hold for a certain fraction of them.
We choose for this measure the square amplitude of the coefficients of the superposition, a choice which is not as arbitrary as it appears, as will shall see subsequently.
This linear measure, measure as according to square amplitude, has equivalent to the product measure or individual sort of value in accord with results on part separate.

---

In the language of subjective experience, a typical machine of the superposition will have received an apparently random sequence of infinite results of the measurement. Furthermore, should the machine be arranged in advance to repeat some of the observations upon the same system, then each machine of the superposition will always record the same result for all subsequent measurements upon the same system, since the relative system state is then nondegenerate, so the first measurement. Thus it will appear to a typical machine that each initial measurement on a system caused the system to "jump" into an eigenstate in a random fashion, and therefore remain there. Thus to a typical machine of the superposition, the probabilities are certain of Poisson (2nd-order) appear to be valid. 

Furthermore, if we pick an element of the superposition (2.4) at random using for our probability distribution the square amplitudes of the superposition coefficients, then the probability that our choice will result in the machine with the particular memory sequence \(M_1(U_1), M_2(U_2), \ldots, M_n(U_n)\) is 

\[P(M_1(U_1), M_2(U_2), \ldots, M_n(U_1)) = (q_1 a_1^* q_1 a_1^*) (q_2 a_2^* q_2 a_2^*) \ldots (q_n a_n^* q_n a_n^*),\] 

which is completely equivalent to simply choosing each element in the memory sequence independently of whether it was with probability distribution \(q_1 a_1^*\), \(q_2 a_2^*\), \(\ldots\), \(q_n a_n^*\). We can therefore make use of some results of probability theory for random sequences. In particular, as the number \(n\) of measurements

---

(0.5) 

insert 

We should like also to indicate the continuity of allowing
several answers to measure a system's independantly, and then
"compare" it. We suppose two answers \(Q, P\) (not initially
intricately with each other) to perform separately a measurement
on \(Y = \sum a_i \phi_i\). Let \(\alpha\) make the first measurement, so that
afterwards we have the superposition: 

\[ \sum_i a_i M_i^*(u_i) \phi_i M_0^0 \]

We now allow \(Q\) to perform the same measurement on the
system. According to what was said in III, however, each
element of the superposition can be treated independently for
measurements on \(S_1\) alone (thus are no interference properties
between elements of the superposition for each measurement) so that,
since a state \(M_1^*(u_i) \phi_i M_0^0\) will result, after measurement
by \(Q\) in \(M_1^*(u_i) \phi_i M_0^0\) (because hypothesis \(Q\) causes \(M_1^*(u_i)\))
we see that the final superposition is: 

\[ \sum_i a_i \phi_i M_1^*(u_i) M_0^0 (u_i) \]

---

and for each (subsequently implemented) element of the superposition
the memory states of x and p agree, so that if they should
later interact with one another to compare results they would
always find that they were in agreement. This obviously also
holds if p should first compare with x and then measure
the system, since the interaction with x would suffice to
correlate p with x and hence to the system. In all such cases
the correlation of a system a with system b, which is taken as
correlated to c, results also in the correlation of a with c, no
the continuity of the wavepacket with respect to an arbitrary
number of observers is preserved by this correlations.

---

due to infinity we can assert that for each element of the superposition the memory sequence will satisfy all the requirements of a random sequence with individual independent probabilities \(d_i\) , except for a set of measure infinity to zero as \(n \to \infty\), when we have taken over basic measures for a superposition to be that given by the square amplitude of the coefficients. Thus, for each element of the superposition (except for any measure zero) all averages of functions over the memory sequence can be computed as expectations with respect to the probabilities" at \(d_i\). In other words, the usual statistical equations of quantum theory will appear to hold to almost all observables of a superposition. 

Summarizing our situation, we have described a process involving an ideal observer, a process which is entirely deterministic and continuous from an objective overall viewpoint (premised to satisfy a wave equation at all times) but whose result is a superposition of ideal observers, to almost all of which it appears that the discontinuities and probabilities appear to the usual form of quantum theory are valid. Thus we have seen how pure and mechanics, without any initial probability assertions, can lead to these notions on a subjective level, as appearances to observers. 

In this proof, the
second finding
proof would be
for
Bos. of being known in
a wide theory

---

Finally, indolence subjective supreme, it suffices to believe the contents of the memory. 

① 

If an observer is to perform a measurement of a quantity A
for a system S, say a specified interaction, then it is necessary
that each significant, E, of A shall produce a definite
result on the observer, which is different for each state of S.
Thus it is a requirement, if we are to be able to interpret
the interaction as a measurement of all that each possible
significant E shall change the state of its
observer from the original state O, to a definite
state O[E], which is different for each i and
which can be interpreted to describe an observer which
has observed that the state was E (possibly by only
knowing the eigenvalue.) (which can be interpreted as
describing that observer who perceives, who is aware

---

on memories. That the has obtained as a result of
his observation the information that the system was in the
states \(P_0\) . We shall pay particular attention to the
memory (considering device) where states we shall
write symbolically as \(\bigotimes_{i=1}^{n} A_i B_i \ldots \bigotimes_{i=1}^{n} C_i\) . \(\bigotimes_{i=1}^{n} A_i B_i \ldots \bigotimes_ {i=1}^{n} C_i\) as memory that the memory of a
state has recorded an event \(A_i\) , then \(B_i\) , then \(C_i\) , and
therefore the memory is blank. We shall thus
describe the complete state as an observer by
\[
\begin{array}{c}
Y_0 \\
[A, B, \ldots, C, 000]
\end{array}
\]
at my notes
The sub product indicating that this state observers
enobrers where memory state definitely violates
the necessary events \(A, B, \ldots, C\) . We can observe
the entity position, then with the previous that
they will be added on new experience are recorded
in the memory.

---

This form shows when initial state is \(W^0\) we require that the observation of property \(A\) where eigenfunction are \(\phi_j\) while in the case that the system is initially in fact in the perturbed eigenstate \(\phi_j\) definitely leads to the resulting observer state at the later time 

\[ \frac{W^0}{L \cdot S \phi_j} \]

where we have inserted the symbol \(L\) in the memory characterization. Instead for the situation that \(W^0\) is
we shall need to indicate the possible presence of some previous memory
(without loss of generality, we have assumed a a result
of the measurement the eigenvalue corresponding to \(\phi_j\) 

- The device is an observer who perceives, or
is now aware, that the system is in the state \(\phi_j\).
(e.g. is the position of a material needle is recorded
on a a mark on a strip of paper, this mark
depends upon the mixture, while depends upon
the value of A on the paper, and can therefore
through this correspondence be interpreted to mean that
the device remembers that the value is obtained
via the eigenvalue of \(\phi_j\) correctly to the mark, and hence
one can say that it remembers that the system was
found to be in the state \(\phi_j\). This, then, is the
meaning of our symbolic notation.
(we may think of the picture of relays, the if we wish,
or even configuration of brain cells.)