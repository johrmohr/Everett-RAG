# Everett Handwritten Fragment -- Proof of proposition on joint probabilities circa 1955.pdf

Proof: for short, write \(P(x_i, y_j) = P_{ij}\) 

\[ \text{Let } Q_{ij} = \frac{P_{ij}}{P_i P_j} \text{ so that } P_{ij} = Q_{ij} P_i P_j \]

\[ \text{then } [X, Y]^2 = \text{Exp}[\ln P_{ij} - \ln P_i - \ln P_j] \\ = \text{Exp}[\ln \frac{P_{ij}}{P_i P_j}] = \text{Exp}[\ln Q_{ij}] \\ = \sum_{ij} P_i P_j Q_{ij} \ln Q_{ij} \]

but making use of inequality then \(> 1 - x\) implies we have 

\[ \text{if } P_i P_j Q_{ij} \ln Q_{ij} > P_i P_j (1 - Q_{ij}) \text{ then } Q_{ij} = 1 \]

\[ = \sum_{ij} P_i P_j Q_{ij} \ln Q_{ij}, \quad > \sum_{ij} P_i P_j - \sum_{ij} P_i P_j = 0 \]

when for every \(ij\), \(P_i P_j = 0\) on \(Q_{ij} = 0\) on 1
\(\Rightarrow P_{ij} = 0\) on \(Q_{ij} = 1\)

\[ \Rightarrow P_{ij} = P_i P_j \quad \text{and} \quad P_{ij} \]

\(\therefore \{X, Y\} > 0\) unless \(X, Y\) index, GED