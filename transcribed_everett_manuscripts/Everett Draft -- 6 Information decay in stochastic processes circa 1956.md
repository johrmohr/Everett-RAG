# Everett Draft -- 6 Information decay in stochastic processes circa 1956.pdf

## Example: 

## §6 Information Decay in Stochastic Processes 

Trial 1 

As an illustrative example we shall now apply the general definition of relative information to stochastic processes. \(^8\) Supposed that we a stationary stochastic process with a finite number of states \(S_j\) and that this process occurs at discrete (binary) time \(t_1, \ldots, t_n\), at which time the transition probability from the state \(S_j\) to the state \(S_j\) is \(T_{ij}\). The probabilities \(T_{ij}\) then form what is called a stochastic matrix, i.e. the elements are between 0 and 1 and \(\sum T_{ij} = 1\) for all \(i, j\). If at any time \(k\) the probability distribution over the states is \([P_k^S]\), then at the next time the probabilities will be \(P_k^{k+1} = \sum P_k^S T_{ij}\). 

On this special case when the matrix is doubly-stochastic, which means that \(\sum T_{ij}\) are well as \(\sum T_{ij}\) equals unity, and which amounts to a principal of detailed balancing holding, it is known that the entropy of a probability distribution over the states defined as \(H = -\sum P_k \ln P_k\) is a monotone (strictly) function of the time? This entropy is, however, simply the negative of the information relative to the uniform measure. 

Once we extend this result to more general stochastic processes only if one uses the more general definition of relative information. For an arbitrary (stationary) process the choice of an information measure which is stationary, i.e. for which 

\[a_j = \sum_i a_i T_{ij} \quad \text{(allj)}\]

---

holds to the derived result. In this case the relative information 

\[I = \sum_i P_i \ln \frac{P_i}{a_i}\]

is a monotone decreasing function of time and contributes
a suitable basis for the definition of the entropy \(H = -I\).
\(\sum \text{pert} 2\) 

One can further develop the requirement that the stochastic process be stationary, and even allow that the state can be different at different times, there are different sets of states at each time \(\{\mathbf{S}_i^n\}\), so that the process is now given by a sequence of matrices \(T_{ij}^n\) representing transition prior, at this point state \(\mathbf{S}_i^n\) to state \(\mathbf{S}_i^{n+1}\). In this case probability distribution change accordingly to: 

If we then choose any time-dependent information measure which satisfies the relation 

\[a_{ij}^{n+1} = \sum_i \Phi_i^n T_{ij}^{n+1} \quad (ab j, n)\]

then the information of a probability distribution is monotone decreasing with time. All of these results are easily extended to the continuous case, and we see that the concept of relative information allows us to define entropy for quite general stochastic processes.

---

2nd 1 

1 

2nd 2 

An outline of examples illustrating the usefulness of the concept of relative information we shall consider highly stochastic processes. Note that this definition leads to the previous result for doubly-stochastic processes, since the uniform measure, \(A = 1\) (elli), is obviously stationary in this case.