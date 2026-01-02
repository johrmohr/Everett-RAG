# Hugh Everett Handwritten algorithm sketch.pdf

# Subroutine Sequence 

(time sequential control routine) 

(1) Concept manages chaining of resources forward and shadow values backward. Uses arrays indexed by time period \(k\) as well as \(i\) and \(j\) indices in optimizers. 

(2) Computation (Arrays) \(k = 1, k\) 

\[ \overline{X}(i, k) \quad \text{lower of activity in time period } k \quad (i = 1, n) \]

\[ \overline{\Delta \lambda}(j, k), \quad \overline{\Delta \lambda}(j, k) \quad \text{chordar value of } R_j \text{ at end of time period } k \quad \text{rental value and total incremental value of } R_j \text{ during time period } k \quad \overline{R}(j, k) \quad \text{Resource Constraint at start of time period } k \quad \overline{\Delta R}(j, k) \quad \text{Contribution to Resource in time period } k \]

(3)

---

PB (L, j, k) Payback Period Estimator
user estimate \(L=1\)
proven planning \(L=2\)
actual recruit \(L=3\) 

(3) Input Data 

<table><tr><td></td><td>T(k)</td><td>time at start of period k</td></tr><tr><td></td><td>d(j)</td><td>capital depreciation rate.</td></tr><tr><td></td><td>TAG(j)</td><td>Time loss or gestation period for capital generation</td></tr><tr><td colspan="2">(4) Propagation of Capital Constraints</td><td></td></tr><tr><td colspan="3">\(R(j, k) := f * \bar{R}(j, k-1) + \sum_{i=1}^{n} \Delta R(j, k) * \delta_{k, k}\)<br/>where \(f = \exp[(T(k-1) - T(k)) * d(j)]\)<br/>where \(\delta_{k, k} = 0\) implies</td></tr><tr><td colspan="3">\(T(k-1) \le t(k) + TAG(j) < T(k)\)</td></tr><tr><td colspan="3">then \(\delta_{k, k} = \exp[-\tau TAG(j) * d(j)]\)</td></tr><tr><td colspan="3">\(R_j^0 = \bar{R}(j, k)\)</td></tr><tr><td colspan="3">\(\Delta T = T(k+1) - T(k)\)</td></tr></table>

---

5. Propagation of Shadow Values 

Option 1 Reverse Propagation 

Optimal Propagation of Shadow Values 

\[f = \exp \left[ (T(k-1) - T(k)) * d(g) \right]\]

\[\lambda(j, k) = f * \lambda(j, k+1) + \sum_{kk'} \Delta \lambda(j, kk') * \delta_{k, k'}\]

\[\text{where } \delta_{k, kk'} = 0 \text{ unless}\]

\[T(k) < T(kk) - T \lambda G(j) \leq T(k+1)\]

\[\text{then } \delta_{k, kk'} = \exp \left[ -T \lambda G(j) * d(g) \right]\]

\[\lambda_0^0 = \lambda(j, k)\]

Option 2 Current Heuristic (formal) 

\[\lambda_0(j, k) = \Delta \lambda R(j, k) * PB(2, j, k)\]

\[\lambda_0(j, k) = 0.0 \text{ for } j = l+1, m\]

Option 3 Retarded Heuristic (grand) 

\[\lambda_0(j, k) = \Delta \lambda R(j, -k) * PB(2, j, k-1)\]

\[\text{for } j = l, l\]

\[\lambda_0(j, k) = 0.0 \text{ if } j = l+1, m\]

---

(6) **Suggestion Mode of Operation** 

**For optimal solution** 

First Pass Option 3
Retarded Heuristic 

Second Pass Option 2
Current Heuristic 

Third Pass Option 1
Fourth etc 

**For Heuristic Solutions** 

(A) Retarded Heuristic
Stop with Option 3 

(B) Current Heuristic
Iterate Option 2
for convergence 

(7) **Use of PB(-,0,h)Arrays** \(g=1,2\) 

User Normally Specifies PB(1,0,k)
which f,1,s all PB(1,g,j,k)
May specify Specific PB(1,g,j,k)
to overwrite when desires

---

Program transfers data to
PB (2j, k) and may 

in later heuristics modify
this planings array 

Program Calculates for User the
actual Page back, based
on optimal shadow value
propagation and stores
in PB (3j, k) . Specifically 

\[PB(3j, k) = \lambda(g, k) / \Delta \lambda R(g, k)\]

---

Subroutine LOGRITHM 

(1) Concept called by time sequential control, converts from Log Utility to Quadratic and then calls QUADINT. 

(2) Input Data 

Same as QUADINT except:
Logarithmic Utility Parameters \(r_i, z_i, p, T\) instead of \(p_i, B_i, p\) plus ERROR 

Note: \(Utility = \Delta T \leftarrow \sum_i r_i \ln(x_i - z_i)\) f where \(f = e^{-pT}\) 

(3) Output Data 

Same as QUADINT

---

(4) Calculation of \(R_i, B_i, U_{i+1}, \text{Parameters for Delivry to QUADINT.}\) 

\[f = e^{-pt}\]

\[U_i = r_i \cdot \ln(x_i^0 - z_i) f = \omega_i\]

\[\frac{\partial U_i}{\partial x_i} = r_i \frac{f}{x_i^0 - z_i} = \omega_i\]

\[\frac{\partial^2 U}{\partial x_i^2} = r_i \frac{-f}{(x_i^0 - z_i)^2} = \omega_i^2\]

\[\tilde{U}_i = \omega_i + (x_i - x_i^0) \omega_i + (x_i - x_i^0)^2 \omega_i\]

\[\tilde{U}_i = \omega_i - x_i^0 \omega_i + x_i^0^2 \omega_i\]

\[+ x_i \omega_i^2 - 2 x_i x_i^0 \omega_i\]

\[+ x_i^2 \omega_i^2\]

\[\frac{s_0}{s} = \frac{k_i = \omega_i - x_i^0 \omega_i + x_i^2 \omega_i}{A_i = \omega_i - 2 x_i^0 \omega_i}\]

\[B_i = \omega_i^2\]

and 

\[\tilde{U}_i = k_i + A_i x_i + B_i x_i^2\]

---

(5) Iterative Operation 

1) with estimated \(x_i^0\)
   rule \(a_i, b_i\) for \(i=m+1, l\) 

2) call QUADINT to get
   optimum \(x_i, \lambda_j\) 

3) if for any \(x_i\) 

\[
\begin{align*}
\frac{x_i - x_i^0}{x_i^0 - z_i^0} & > \text{error} \quad \text{and} \quad x_i - z_i^0 \in \\
\text{then set } x_i^0 &= x_i \text{ for all } x_i \\
\text{and } G_0 &\text{ to } ① \text{ else } ④.
\end{align*}
\]

4) Return 

(6) Gradient of Observable Response
    level
    \(\Delta T\)
    for \(j = m+1, m\)
    \(\Delta t\)
    \(R_j = R_i \Delta t\)
    \(\Delta t\)
    \(b_i = b_i / \Delta t\)

---

Subroutine QUADINT
(the quadratic interface) 

(1) Input Data 

<table><tr><td>\(R_j^0\) (j = 1, m)</td><td>Resource constraints at beginnings of time period</td></tr><tr><td>\(\lambda_j^0\)</td><td>estimated resource shadow value and curvature at end of time period</td></tr><tr><td>\(X_i^0\)</td><td>estimated activity levels</td></tr><tr><td>ΔT</td><td>length of time period</td></tr></table>

(2) Output Data 

<table><tr><td>\(X_i\) (i = 1, n)</td><td>activity levels</td></tr><tr><td>ΔRj (j = 1, m)</td><td>net change in resource loads</td></tr><tr><td>Δλj (j = 1, m)</td><td>net change in shadow value</td></tr><tr><td>-ΔMj (j = 1, m)</td><td>contribution to curvature</td></tr></table>

---

(3) Preparation of Data for Quadratic 

\[
\begin{align*}
\text{consumption constraints } g &= 1, m \\
R_j &= R_j^0 / \Delta t \\
\lambda_j &= \lambda_j^0 \\
\mu_j &= \mu_j^0 * \Delta t
\end{align*}
\]

\[
\text{use constraints } g = 1, l.
\]

\[
R_{(m+j)} = R_j^0
\]

\[
\lambda_{m+j} = 0.0
\]

\[
\mu_{m+j} = 0.0
\]

\[
\begin{align*}
\text{Incorporate Shadow Values in Objective} \\
\text{ } j a_i = p_i + \sum_{j=1}^{m} \alpha_{ij} \lambda_j \\
\text{ } b_i = p_i + \sum_{j=1}^{m} \alpha_{ij} u_j
\end{align*}
\]

\[
\begin{align*}
\text{Initialize } X_i, \lambda_j \\
\lambda_j = 0 \quad \mu_j = 0 \quad X_i = 0
\end{align*}
\]

---

(4) Call on QUADRATIC Return New Values 

\[X_i = (i = 1, n)\]

\[\lambda_j = (j = 1, l)\]

(5) Calculation of Output Parameters 

\[\Delta R_j = \Delta T * \sum_i \alpha_{ij} x_i\]

now add "use" channel value \(\lambda_j + m\) to "consumption" value \(\lambda_j\) (corresponds to approximation in which use precedes consumption) 

\[for \quad j = 1, l \quad \lambda_j = \lambda_j + \lambda_m + g\]

correct for time interval 

\[\Delta \lambda_j = \lambda_j * \Delta T\]

---

Subroutine Quadratic 

(the basic quadratic program) 

(1) Input Data \(a_i, b_i, R_j\) 

\((a_i, b_i)\) Quadratic Value Parameters defined over direct & shadow values 

\[V = \sum_{i=1}^{n} a_i x_i^2 + b_i x_i^2\]

(R_j) Resource Constraints \(R_j\) -

\[R_j = j = 1, m \quad \text{Consumption constraint}\]

\[R_0 = j = m+1, m+l \quad \text{resource use : : :}\]

(2) User Supplied Constant Data \(\alpha_{ij}\) -

\[\sum_j \alpha_{ij} x_i \leq R_j\]

(3) Output Data \(x_i, \lambda_j\) -

\(x_i\) activity levels 

\(\lambda_j\) resource shadow values

---

art delvadii

---

Quadratic Programming 

(1) Partial Formulation 

\[ \text{Max} \sum_{x_i} H(x_i) \text{ where } H(x_i) = \sum_i a_i x_i - b_i x_i^2 \]

subject to linear constraints 

\[ \sum_i \alpha_{ij} x_i \leq R_j \quad \text{and} \quad x_i \geq 0 \]

(2) The nonconvexity introduced after variable \(y_j\) can sometimes lead
\[ \sum_i \alpha_{ij} x_i + y_j = R_j \]
\[ x_i \geq 0 \quad y_j \geq 0 \] 

(3) 

\[ \text{Now Form Lagrangian} \]
\[ \alpha \in L \text{ and } \alpha(x_i, y_j, \lambda_j) \]
\[ \alpha(x_i, y_j, \lambda_j) = H(x_i) - \sum_j \lambda_j (y_j + \sum_i a_{ij} x_i - R_j) \]
\[ \text{then find } \lambda_j \text{ such that for} \]
\[ \text{Max} \quad x_i y_j \alpha(x_i, y_j, \lambda_j) \text{ also satisfies constraints} \]
\[ \text{then optimum solution has been found.} \]

---

(4) Calculate Max Karpungin 

optimum per \(X_i, Y_j\) is minimum if \(Y_j\) 

and occurs when \(\frac{\partial}{\partial x_i} L(x_j, y_j, \lambda_j) = 0\) 

i.e. where 

\[a_i - 2b_i x_i - \sum_j \lambda_j \alpha_{ij} = 0\]

\[x_i = \frac{1}{2b_i} \left[ a_i - \sum_j \lambda_j \alpha_{ij} \right] \quad \text{and}\]

\[y_j = 0 \quad \text{if} \quad \lambda_j \geq 0\]

but if constants are to be used then 

\[\sum_i \alpha_{ij} x_i + y_j = R_j \quad \text{for all } j\]

(5) Transform into Simultaneous Equations 

\[\text{if } \lambda_j \text{ and } x_i \text{ can be found}\]

\[\text{such that } 2b_i x_i + \sum_j \lambda_j \alpha_{ij} = a_i\]

\[\text{and } y_j + \sum_i x_i \alpha_{ij} = R_j\]

Then Solution Has been found

---

6 Transformation to Linear Program 

Introduce dummy variables \(Z_i, M_j\)
where \(Z_i \geq 0\) and \(M_j \geq 0\) 

and rewrite equations to permit trivial
feasible solution \(x_i = 0 \land j = 0 \land y_i = 0 \land Z_i = a_i \land M_j = R_j\) 

\[2b_i x_i + \sum_j \lambda_j a_{ij} + Z_i = a_i\]

\[y_j + \sum_i x_i a_{ij} + M_j = R_j\]

now define linear objective function \(\Theta\) 

\[\sum_i Z_i + \sum_j M_j = \Theta\]

Vice linear program starts to 
find values of activities 

\[x_i, Z_i, \lambda_j, M_j \quad \text{which}\]

minimize \(\Theta\) subject to constraints 

\[a_i \quad \text{and} \quad R_j \quad \text{15 solution is found with } Z_i = 0 \quad M_j = 0 \quad \text{then original equations are solved}\]

Note: Linear Program deals with 

\[2(M+N) \quad \text{activities and} \quad M+N \quad \text{constraints}\]