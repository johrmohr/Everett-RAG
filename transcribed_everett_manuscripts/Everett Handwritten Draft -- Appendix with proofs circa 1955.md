# Everett Handwritten Draft -- Appendix with proofs circa 1955.pdf

On this section we supply the proofs of several assertions made earlier. 

**Proof of Theorem 1:** \(\left( [x, y, \ldots, z] > 0 \text{ unless independent} \right)\) 

**Abbreviate** \(P(x; y; z; \ldots; z_k)\) by \(P_{i, j, \ldots, k}\) and let 

\[A.1. \quad Q_{ij \ldots k} = \begin{cases} P_{i, j, \ldots, k} & \text{if } P_{i, j, \ldots, k} > 0 \\ \frac{P_{i, j, \ldots, k}}{P_{i, j, \ldots, k}} & \text{if } P_{i, j, \ldots, k} = 0 \\ 1 & \text{if } P_{i, j, \ldots, k} = 0 \end{cases}\]

to that 

\[(A.2) \quad P_{ij \ldots k} = Q_{ij \ldots k} P_{i, j, \ldots, k} P_{k}\]

then 

\[(A.3) \quad \{x, y, \ldots, z\} = \exp \left[ \ln \frac{P_{i, j, \ldots, k}}{P_{i, j, k}} \right] = \exp \left[ \ln Q_{ij \ldots k} \right] = \sum_{j, \ldots, k} P_{i, j, \ldots, k} Q_{ij \ldots k} \ln Q_{ij \ldots k}\]

making use of the inequality 

\[(A.4) \quad x \ln x > x - 1 \quad (\text{except } x = 1) \quad (x > 0)\]

which is easily established by calculating the minimum of \(x \ln x - (x - 1)\) we have 

\[(A.5) \quad P_{i, j, \ldots, k} P_{i, j, \ldots, k} h Q_{ij \ldots k} > \sum_{j, \ldots, k} P_{i, j, \ldots, j} (Q_{ij \ldots k} - 1) \quad (\text{unless } Q_{ij \ldots k} = 0)\]

and hence the sum 

\[(A.6) \quad \sum_{ij, k} P_{i, j, \ldots, k} Q_{ij, \ldots, k} h Q_{ij, \ldots, k} > \sum_{ij, k} P_{i, j, \ldots, k} Q_{\ldots, k} - \sum_{ij, k} P_{i, j, \ldots, k} \quad (\text{unless } Q_{ij, \ldots, k} = 0)\]

---

\[ \sum_{i,j,k} P_{ij} P_k Q_{jk} = \sum_{j,k} P_{ij} = 1 \quad \text{and} \quad \sum_{i,j,k} P_{ij} P_k = 1 \]

so that the right side of (1.3) vanishes. But the left side is, by (1.3)
\(\{X,Y,Z\}\) and the condition that all the \(Q_{ij,k} = 1\) is precisely
the independence condition (II - ) so we have proved that 

\[ (11) \quad \{X,Y,Z\} > 0 \quad (\text{unless } X,Y,Z \text{ mutually independent}) \]

We now wish to establish some basic inequalities
based upon the fact that the function \(k\) has is a convex
function : 

\[ \text{Lemma 1:} \quad k \ge 0, \quad P_i \ge 0, \quad \sum_i P_i = 1 \]

\[ \Rightarrow \left( \sum_i P_i k_i \right) \ln \left( \sum_i P_i k_i \right) \le \sum_i P_i k_i \ln k_i \]

(This property is actually the definition of a convex function)
but follows from the fact that
\(\frac{d^2}{dx^2} (k \ln k) = \frac{1}{x} > 0\) (since \(x > 0\))
which is the elementary notion of convexity.) There is an
immediate corollary for this continuous case : 

\[ \text{Corollary 1} \quad \begin{aligned} & g(x) \ge 0, \quad f(x) \ge 0, \quad \int g(x) dx = 1 \\ \Rightarrow & \left( \int g(x) g(x) dx \right) \ln \left( \int g(x) g(x) dx \right) \le \int g(x) g(x) \ln g(x) dx \end{aligned} \]

---

We now derive a more general and very useful inequality from
Lemma 4: 

\[
\frac{\text{Lemma 2:} a_i \geq 0, b_i \geq 0 \quad \text{(auli)}}{\Rightarrow \left( \sum_i b_i \right) \ln \left( \frac{\sum_i b_i}{\sum_i a_i} \right) \leq \sum_i b_i \ln \frac{b_i}{a_i}}
\]

Proof: Let \(p_i = \frac{a_i}{\sum a_i}\), so that \(p_i \geq 0\) and \(\sum p_i = 1\). 

Then, by lemma 1: 

\[
(2.1) \quad \left[ \sum_i p_i \left( \frac{b_i}{a_i} \right) \right] \ln \left[ \sum_i p_i \left( \frac{b_i}{a_i}  \right) \right] \leq \sum_i p_i \left( \frac{b_i}{a_i} \right)  \ln \left( \frac{b_i}{a_i} \right)
\]

suitability for \(p_i\): 

\[
(2.2) \quad \left( \sum_i \frac{a_i}{\sum a_i} \frac{b_i}{a_i} \right) \ln \left( \sum_i \frac{a_i}{\sum a_i} \frac{b_i}{\sum a_i} \right) \leq \sum_i \frac{a_i}{\sum a_i} \frac{b_i}{\sum a} \ln \frac{b_i}{a_i}
\]

\[
(2.3) \quad \left( \sum_i b_i \right) \ln \left( \frac{\Sigma b_i}{\Sigma a_i} \right) \leq \sum_i b_i \ln \frac{b_i}{\Sigma a_i} \quad \text{QED.}
\]

We also mention the analogous continuous case: 

\[
\text{Corr 2:} \quad f(x) \geq 0, g(x) \geq 0
\]

\[
\Rightarrow \int f(x) dx \ln \frac{\int g(x) dx}{\int g(x) dx} \leq \int f(x) \ln \frac{f(x)}{g(x)} dx
\]

---

We now prove the theorem (7- ) concerning
the behavior of correlation and relative information under refinement.
We suppose that the original (unrefined) distribution is \(P_{i,j,\ldots,k} = P_{i,j,\ldots,k}^{(0)}\), and that the refined distribution is \(P_{i,j,\ldots,k}^{(1)}\), so that
the value \(k_i\) has been reduced into a number of values \(k_i'\), and similar to 9-2,
then: 

\[(3.1) \quad P_{i,j,\ldots,k} = \sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(0)} \quad P_i = \sum_{i,j,\ldots,k} P_i^{(1)} \quad \text{etc.}\]

(3.2) \[[X,Y,\ldots,Z]' = \sum_{i,j,\ldots,k} \sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(1)} \ln \frac{P_{i,j,\ldots,k}^{(1)} \cdot P_{i,j,\ldots,k}^{(0)}}{P_i^{(1)} \cdot P_j^{(0)} \cdot P_k^{(0)}}\]

but by Lemma 2:
(3.3) \[(\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(1)} \cdot \ln \frac{P_{i,j,\ldots,k}^{(1)} \cdot P_{i,\ldots,k}^{(0)}}{(\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(0)} \cdot P_{i,\ldots,k}^{(0)})}) \leq \sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(1)} P_{i,\ldots,k}^{(0)}\]

and substitution of (3.3) into (3.2) imply that \(\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(1)} P_k^{(0)} = (2P_i^{(0)})(2P_j^{(0)}) \cdot (2P_k^{(0)})\) and
hence: 

\[(3.4) \quad \{X,Y,\ldots,Z\}' \geq \sum_{i,j,\ldots,k} (\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(1)} \times \ln \frac{(\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(0)})}{(\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(0)})^{2}}) \cdot (\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(0)}) \cdot (\sum_{i,j,\ldots,k} P_{i,j,\ldots,k}^{(1)}) \cdot (\sum_{i,j,\ldots,k} P_{i,j,\ldots, k}^{(0)}) \cdot (\sum_{i,j,\ldots,k} P_{i,j, \ldots, k}^{(1)}) \cdot (\sum_{i,j,\ldots,k} P_{i,j, \cdots, k}^{(0)}) \cdot (\sum_{i,j,\ldots,k} P_{k}^{(0)}) \cdot (\sum_{i,j,\ldots,k} P_{i,j}^{(0)}) \cdot (\sum_{i,j,\ldots,k} P_{i,j}^{(\infty)}) \cdot (\sum_{i,j,\ldots,k} P_{i,j}^{(\text{ref})}) \cdot (\sum_{i,j,\ldots,k} P_{i,j}^{(\text{sat})}) \cdot (\sum_{i,j,\ldots,k} P_{i,j}^{(\infty)})\]

---

It is now crucial the effect upon relative information: 

Suppose that \(Q_i^{(k)}, b_j^{(k)}, \ldots, C_k^{(k)}\) are the basic measures for \(P_{ij\ldots k}^{(k)}\) . Then the measure for \(P_{ij\ldots k}\) are 

\[
A := \sum_{i} Q_i^{(k)} b_j = \sum_{i} b_j^{(k)} \ldots, \quad \text{and the relative information} \quad A
\]

\[
(3.5) \quad \frac{I'}{X_{Y \cdot Z}} = \sum_{i,j,k} \sum_{a,b,c} P_{ij\ldots k}^{(a,b,c)} \ln \frac{P_{ij\ldots k}^{(a,b,c)} \cdot n_k}{Q_i^{(a,b,c)} \cdot C_k} \quad \text{and by exactly this same argument at before (lemma 2)}
\]

\[
(3.6) \quad \frac{I'}{X_{Y \cdot Z}} \geq \sum_{i,j,k} P_{ij\ldots k} \ln \frac{P_{ij\ldots k}}{a \cdot b \cdot c_k} = \frac{I}{X_{Y \cdot Z}}
\]

and represent more decrease relative information.

---

Just for fun: 

General Stochastic Process: (Continuous) 

\[ \mathbb{P}(X_t = x) = \int P(x') A(x', x) dx' \xrightarrow{\text{now}} \text{Negative} \]

\[ \text{where } A(x', x) = \int A(x', x') A(x, x) dx' \]

Stationary ⇒ \(P^*(x, \infty) = P^*(x, t+s)\) are s 

\[ \Rightarrow P^*(x) \]

\[ \Rightarrow \int P^*(x) A(x', x) dx' = P^*(x) \quad \text{(now)} \]

\[ \text{now, } I_t = \int P(x') A(x', x) dx' \]

\[ I^{t+4} = \int [P(x') A(x', x) dx'] e_n \frac{[S(x', x) A(x', x) dx']}{[P^*(x') A(x', x) dx']} \]

\[ \text{by Lemma 2 conclude} \]

\[ \begin{aligned} & \leq \int [S(x') A(x', x) e_n \frac{P(x') A(x', x) dx']}{[P^*(x') A(x', x) e_n \frac{P(x') A(x', x) dx'}{P^*(x') A(x', x) dx']} dx' \\ & = \int [S(x') A(x', x) dx'] P(x') e_n \frac{P(x') A(x', x) dx'}{P^*(x) A(x', x) dx'] dx' \\ & = I^t \end{aligned} \]