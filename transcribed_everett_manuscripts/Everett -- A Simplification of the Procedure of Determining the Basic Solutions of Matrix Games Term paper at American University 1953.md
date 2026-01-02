# Everett -- A Simplification of the Procedure of Determining the Basic Solutions of Matrix Games Term paper at American University 1953.pdf

A SIMPLIFICATION OF THE PROCEDURE OF DETERMINING
THE BASIC SOLUTIONS OF MATRIX GAMES 

- Hugh Everett, III

---

A SIMPLIFICATION OF THE PROCEDURE OF DETERMINING THE
BASIC SOLUTIONS OF MATRIX GAMES 

Hugh Everett, III 

It is the purpose of this paper to give a simplification of
the ifor solving matrix games by the use of Snow-Shapely kernels.¹ 

Snow and Shapely have shown that the set of all mixed strategies, \(\vec{X}, \vec{Y}\), which constitute the solutions to a game may be represented by a finite number of basic solutions which may be considered as pairs of vertices from two convex sets in the spaces of all mixed strategies for the two players. Each basic solution has associated with it one or more square submatrices of the whole game matrix, called the kernels of the solution, with the property that the solutions of this square submatrix are unique and simple, that is: 

\[ \vec{X} \cdot \vec{Y} = \vec{1} \cdot \vec{X} = \vec{v} \quad \text{for all } i, j \text{ in the submatrix.} \]

We wish to introduce now a simplified method for determining these simple solutions of a square matrix, provided that they exist. 

**Def. I:** Perpendicularity. Two \(n\)-dimensional vectors \(\vec{U}\) and \(\vec{V}\) are said to be perpendicular if and only if: 

\[ \vec{U} \cdot \vec{V} = 0 \]

**Def. II:** Extension of vector cross product. The cross product, \(\vec{V}\), of \(n\)-1 \(n\)-dimensional vectors, \(\vec{V}\), is the vector given by: 

\[ \vec{V} = \vec{V}^1 \times \vec{V}^2 \times \cdots \times \vec{V}^{n-1} = \begin{bmatrix} \vec{V}^1 \\ \vec{V}^1 \vec{V}^2 \\ \vdots \\ \vec{V}^1 \vec{V}^2 \cdots \vec{V}^n \end{bmatrix} = \begin{bmatrix} \vec{V}^1 \\ \vec{V}^2 \\ \vdots \\ \vec{V}^n \end{bmatrix} \]

Where the \(\vec{V}_i\) constitute the (orthogonal) basis.

---

THEOREM The unique (directionally) perpendicular to \(n-1\) \(n\) - dimensional vectors, if it exists, is given by the cross product of these vectors. 

Proof of perpendicularity: 

\[
\begin{align*}
\text{Let } \vec{v} &= \vec{v}_1 \times \vec{v}_2 \times \cdots \times \vec{v}_{n-1} \quad \text{then,} \\
\vec{v} \cdot \vec{v}_1 &= \vec{v}_1 \cdot \vec{v}_2 \cdot \vec{v}_3 \cdot \cdots \cdot \vec{v}_n \\
&= \begin{vmatrix}
\vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \\
1 & 1 & \cdots & 1 \\
\vdots & \vdots & \ddots & \vdots \\
1 & 1 & \cdots & 1
\end{vmatrix} \\
&= \begin{vmatrix}
\vec{v}_1 & \vec{v}_2 & 1 \\
1 & 1 & \cdots & 1 \\
\vdots & \vdots & \vdots & \vdots \\
1 & 1 & \cdots & 1
\end{vmatrix} = 0
\end{align*}
\]

Since now the first row of the determinant is repeated in the \(i\)th row for all \(i\). 

Proof of directional uniqueness: 

If \(\{\vec{v}\}\) constitutes a set of \(n-1\) linearly independent \(n\)-dimensional vectors, the system of linear equations 

\[
\begin{align*}
\vec{v}_1 \cdot \vec{v}_1 &= 0 \quad \text{for all } i, \text{ or} \\
v_1^1 + v_2^1 + \cdots + v_n^1 &= 0 \\
v_1^2 + v_2^2 + \cdots + v_n^2 &= 0 \\
\vdots \\
v_1^{n-1} + v_2^{n-1} + \cdots + v_n^{n-1} &= 0
\end{align*}
\]

has a unique solution for \(\forall i (i \neq 1)\) in terms of \(\vec{v}_1\), that is, there exist uniquely numbers \(\alpha, \beta, \ldots, \delta\), such that 

\[
\vec{v} = \vec{v}_1 (1, \alpha, \beta, \ldots, \delta)
\]

and the set of all solutions to the system of equations is therefore a set of parallel vectors \(\vec{v}\), characterized by
\(\vec{v} = \lambda (1, \alpha, \beta, \ldots, \delta)\) where \(\lambda\) is a scalar.
or \(\vec{v} = \lambda \vec{v}\) since \(\vec{v}\) is known to be a solution. 

COROLLARY The cross product of \(n-1\) \(n\)-dimensional vectors,
if it is not 0, is the unique perpendicular to these vectors.
Proof: If the cross product is not zero, then the vectors of
its defining determinant are not linearly dependent, hence a
unique perp. exists and must be given by the cross product.

---

We are now in a position to determine the unique, simple solution (if it exists) of a square matrix. Denote by \((a_{ij})\) the square matrix, with \(i, j\) from one to \(r\). By definition a simple solution is an \(\bar{X}\) and a \(\bar{Y}\) and a \(\bar{v}\) such that: 

\[ \bar{X} \cdot \bar{I} = 1 \quad \bar{Y} \cdot \bar{I} = 1 \quad \text{and} \]

\[ (1) \quad \begin{cases} \bar{X} \cdot \bar{d} = v \text{ for all } j \\ \bar{Y} \cdot \bar{d} = v \text{ for all } k \end{cases} \]

where \(\bar{d}_i = (a_{i1}, a_{i2}, \ldots, a_{ir})\) (the \(i\)th row vector) 

\[ \bar{d}_j = (a_{1j}, a_{2j}, \ldots, a_{rj}) \quad (\text{the } j\text{th column vector}) \]

now, forming difference vectors: 

\[ \bar{d}_j = \bar{d}_j - \bar{d}_{j+1} \quad , \quad \bar{d}_i = \bar{d}_i - \bar{d}_{i+1} \]

we have, from (1): 

\[ (\bar{X} \cdot \bar{d}) - (\bar{X} \cdot \bar{d}_{i+1}) = v - v = 0 \]

\[ (2) \quad \text{or} \quad \bar{X} \cdot (\bar{d}_i - \bar{d}_{i+1}) = \bar{X} \cdot \bar{d}_i = 0 \quad \text{for all } j \]

\[ \text{and} \quad (\bar{Y} \cdot \bar{d}_i) - (\bar{Y} \cdot \bar{d}_{i+1}) = v - v = 0 \quad \text{for all } j \]

\[ (3) \quad \text{or} \quad \bar{Y} \cdot (\bar{d}_i - \bar{d}_{i+1}) = \overline{Y} \cdot \bar{d}_i = 0 \quad \text{for all } i \]

but (2) and (3) are precisely the perpendicularity conditions, so that we may find vectors parallel to \(\bar{X}\) and to \(\bar{Y}\), denoted by \(\bar{X}\) and \(\bar{Y}\), by taking the cross products of the \(\bar{d}_j\) and \(\bar{d}_i\) respectively: 

\[ \bar{X} \cdot \bar{r} = \sum_{j=1}^{r-1} \bar{d}_j \cdot \bar{d}_j = \sum_{j=1}^{r-1} (\bar{d}_j - \bar{d}_{j+1}) \]

\[ (4) \quad \bar{Y} = \sum_{i=1}^{r-1} \bar{d}_i \quad \bar{d}_i = \sum_{i=1}^{r-1} (\bar{d}_i - \bar{d}_{i+1}) \]

Now, to find \(\bar{X}\) and \(\bar{Y}\), which are parallel to these vectors, we simply normalize them so that their components sum to one: 

\[ \bar{X} = \frac{\bar{X}}{\bar{X} \cdot \bar{Y}} \quad \bar{Y} = \frac{\bar{Y}}{\bar{Y} \cdot \bar{X}} \quad (5) \]

If \(\bar{X}\) and \(\bar{Y}\) exist, by virtue of the corollary, they are the unique solutions, and the value of the game is given by: 

\[ (6) \quad v = \bar{X} \cdot \bar{d}_j = \bar{Y} \cdot \bar{d}_i \quad \text{for any } i, j. \]

---

GEOMETRIC INTERPRETATION. If an rxx square submatrix of a game is a kernel, then the game convex of the subgame consists of r vertices which determine an r- l dimensional flat in r- space. If this is a kernel, hence having a unique basic solution, the "corner"must pin the separating hyperplane uniquely, and the separating hyperplane must be the hyperplane of the flat. If this is the case, the (unique) optimal strategy for player 1 is a vector (sum one) perpendicular to this hyperplane, and therefore having the direction of the cross product of r- l vectors in the flat. These vectors are conveniently determined by taking r- l differences of the vertices, which is exactly what has been done in the preceding solution. The same argument holds for player 2.  

The formulae given by Snow and Shapely for testing square submatrices may therefore be replaced by formulae (4) (5) and (6). The remainder of the procedure for the solution of all matrix games is then exactly as given by Snow and Shapely.  

The advantage of this method of computing the solution of an rxx square submatrix is that it requires the computation of only 2r determinants of order r- l, while the previous method requires the computation of \(r^2\) determinants of the same order, all other calculations being approximately equal. This is a considerable saving, especially for large r.